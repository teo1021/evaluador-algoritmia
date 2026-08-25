import streamlit as st
from sqlalchemy import create_engine, text
from datetime import datetime

DATABASE_URL = st.secrets["DATABASE_URL"]

engine = create_engine(
    DATABASE_URL.replace(
        "postgresql://",
        "postgresql+psycopg://",
        1
    ),
    pool_pre_ping=True
)

from datetime import datetime


def guardar_intento(
    correo,
    nombre,
    respuestas,
    puntos,
    correctas,
    puntaje_maximo,
    porcentaje,
    nivel,
    aprobado
):
    """
    Guarda un intento completo del cuestionario.

    - Crea el estudiante si no existe.
    - Crea un nuevo intento.
    - Guarda cada respuesta.
    """

    with engine.begin() as connection:

        # ==========================================
        # 1. BUSCAR ESTUDIANTE
        # ==========================================

        estudiante = connection.execute(
            text("""
                SELECT id
                FROM estudiantes
                WHERE correo_institucional = :correo
            """),
            {
                "correo": correo
            }
        ).fetchone()

        # ==========================================
        # 2. CREAR ESTUDIANTE SI NO EXISTE
        # ==========================================

        if estudiante is None:

            estudiante_id = connection.execute(
                text("""
                    INSERT INTO estudiantes (
                        correo_institucional,
                        nombre,
                        fecha_registro
                    )
                    VALUES (
                        :correo,
                        :nombre,
                        :fecha
                    )
                    RETURNING id
                """),
                {
                    "correo": correo,
                    "nombre": nombre,
                    "fecha": datetime.now()
                }
            ).scalar_one()

        else:

            estudiante_id = estudiante.id

        # ==========================================
        # 3. CREAR NUEVO INTENTO
        # ==========================================

        fecha_inicio = datetime.now()

        intento_id = connection.execute(
            text("""
                INSERT INTO intentos (
                    estudiante_id,
                    fecha_inicio,
                    puntaje_obtenido,
                    puntaje_maximo,
                    porcentaje,
                    respuestas_correctas,
                    nivel,
                    aprobado
                )
                VALUES (
                    :estudiante_id,
                    :fecha_inicio,
                    :puntaje_obtenido,
                    :puntaje_maximo,
                    :porcentaje,
                    :respuestas_correctas,
                    :nivel,
                    :aprobado
                )
                RETURNING id
            """),
            {
                "estudiante_id": estudiante_id,
                "fecha_inicio": fecha_inicio,
                "puntaje_obtenido": puntos,
                "puntaje_maximo": puntaje_maximo,
                "porcentaje": porcentaje,
                "respuestas_correctas": correctas,
                "nivel": nivel,
                "aprobado": aprobado
            }
        ).scalar_one()

        # ==========================================
        # 4. GUARDAR RESPUESTAS
        # ==========================================

        for respuesta in respuestas:

            connection.execute(
                text("""
                    INSERT INTO respuestas (
                        intento_id,
                        pregunta_id,
                        respuesta_seleccionada,
                        es_correcta,
                        puntos_obtenidos
                    )
                    VALUES (
                        :intento_id,
                        :pregunta_id,
                        :respuesta_seleccionada,
                        :es_correcta,
                        :puntos_obtenidos
                    )
                """),
                {
                    "intento_id": intento_id,
                    "pregunta_id": respuesta["pregunta_id"],
                    "respuesta_seleccionada": respuesta["respuesta"],
                    "es_correcta": respuesta["es_correcta"],
                    "puntos_obtenidos": respuesta["puntos"]
                }
            )

        # ==========================================
        # 5. FINALIZAR INTENTO
        # ==========================================

        connection.execute(
            text("""
                UPDATE intentos
                SET fecha_finalizacion = :fecha_finalizacion
                WHERE id = :intento_id
            """),
            {
                "fecha_finalizacion": datetime.now(),
                "intento_id": intento_id
            }
        )

    return intento_id