import streamlit as st

# ==========================================================
# CONFIGURACIÓN
# ==========================================================

st.set_page_config(
    page_title="AKS — Algorithmic Knowledge Standard",
    page_icon="💻",
    layout="centered"
)

# ==========================================================
# INFORMACIÓN DEL EXAMEN
# ==========================================================

preguntas = [
    {
        "numero": 1,
        "tema": "Secuenciación",
        "dificultad": "Fácil",
        "puntos": 1,
        "pregunta": "Una persona desea preparar una taza de té. ¿Cuál es el orden correcto?",
        "opciones": {
            "A": "Hervir agua → Colocar la bolsa de té → Servir el agua → Esperar 3 minutos",
            "B": "Colocar la bolsa → Hervir agua → Esperar → Servir",
            "C": "Servir el agua → Hervir → Bolsa → Esperar",
            "D": "Esperar → Hervir → Bolsa → Servir"
        },
        "respuesta": "A"
    },
    {
        "numero": 2,
        "tema": "Secuenciación",
        "dificultad": "Fácil",
        "puntos": 1,
        "pregunta": "En un cajero automático, ¿qué acción debe ocurrir primero?",
        "opciones": {
            "A": "Entregar el dinero",
            "B": "Verificar el saldo",
            "C": "Imprimir el recibo",
            "D": "Cerrar la sesión"
        },
        "respuesta": "A"
    },
    {
        "numero": 3,
        "tema": "Secuenciación",
        "dificultad": "Media",
        "puntos": 2,
        "pregunta": "Un algoritmo posee ocho instrucciones consecutivas. ¿Qué afirmación es correcta?",
        "opciones": {
            "A": "El usuario decide el orden.",
            "B": "Se ejecutan en el orden establecido, salvo que exista una condición.",
            "C": "Siempre se ejecutan simultáneamente.",
            "D": "Las últimas instrucciones ocurren primero."
        },
        "respuesta": "B"
    },
    {
        "numero": 4,
        "tema": "Condicionales",
        "dificultad": "Fácil",
        "puntos": 1,
        "pregunta": "Una puerta se abre únicamente cuando hay tarjeta válida y contraseña correcta. ¿Qué operador representa esa regla?",
        "opciones": {
            "A": "O",
            "B": "Y",
            "C": "NO",
            "D": "SI NO"
        },
        "respuesta": "B"
    },
    {
        "numero": 5,
        "tema": "Condicionales",
        "dificultad": "Media",
        "puntos": 2,
        "pregunta": "Un descuento se aplica si el cliente es estudiante o adulto mayor. ¿Qué operador lógico corresponde?",
        "opciones": {
            "A": "Y",
            "B": "O",
            "C": "NO",
            "D": "MIENTRAS"
        },
        "respuesta": "B"
    },
    {
        "numero": 6,
        "tema": "Condicionales",
        "dificultad": "Difícil",
        "puntos": 4,
        "pregunta": "Un ascensor funciona únicamente cuando: la puerta está cerrada, hay un piso seleccionado y no está en mantenimiento. ¿Cuál expresión representa correctamente la regla?",
        "opciones": {
            "A": "(Puerta cerrada Y Piso seleccionado) Y NO Mantenimiento",
            "B": "Puerta cerrada O Piso seleccionado",
            "C": "NO Puerta cerrada Y Piso",
            "D": "Piso seleccionado solamente"
        },
        "respuesta": "A"
    },
    {
        "numero": 7,
        "tema": "Iteración",
        "dificultad": "Fácil",
        "puntos": 1,
        "pregunta": "Un robot coloca 10 botellas en una caja. ¿Cuántas veces repite la acción de colocar una botella?",
        "opciones": {
            "A": "1",
            "B": "5",
            "C": "10",
            "D": "11"
        },
        "respuesta": "C"
    },
    {
        "numero": 8,
        "tema": "Iteración",
        "dificultad": "Media",
        "puntos": 2,
        "pregunta": "Una impresora imprime las páginas desde la 1 hasta la 25. ¿Cuántas iteraciones realiza?",
        "opciones": {
            "A": "24",
            "B": "25",
            "C": "26",
            "D": "50"
        },
        "respuesta": "B"
    },
    {
        "numero": 9,
        "tema": "Iteración",
        "dificultad": "Difícil",
        "puntos": 4,
        "pregunta": "Un algoritmo suma todos los números del 1 al 100. ¿Cuántas veces ejecuta la operación de suma?",
        "opciones": {
            "A": "50",
            "B": "99",
            "C": "100",
            "D": "101"
        },
        "respuesta": "C"
    },
    {
        "numero": 10,
        "tema": "Diseño de algoritmos",
        "dificultad": "Fácil",
        "puntos": 1,
        "pregunta": "Debes encontrar el libro más pesado entre cinco libros. ¿Cuál estrategia es correcta?",
        "opciones": {
            "A": "Comparar todos y conservar el más pesado encontrado.",
            "B": "Elegir uno al azar.",
            "C": "Ordenarlos por color.",
            "D": "Revisar únicamente el primero."
        },
        "respuesta": "A"
    },
    {
        "numero": 11,
        "tema": "Diseño de algoritmos",
        "dificultad": "Media",
        "puntos": 2,
        "pregunta": "Una biblioteca quiere organizar libros alfabéticamente. ¿Qué procedimiento es el más apropiado?",
        "opciones": {
            "A": "Comparar e intercambiar posiciones incorrectas.",
            "B": "Agruparlos por tamaño.",
            "C": "Ordenarlos por número de páginas.",
            "D": "Elegir posiciones al azar."
        },
        "respuesta": "A"
    },
    {
        "numero": 12,
        "tema": "Diseño de algoritmos",
        "dificultad": "Media",
        "puntos": 2,
        "pregunta": "Un supermercado necesita identificar el producto más barato de una lista. ¿Qué dato debe conservar mientras recorre todos los productos?",
        "opciones": {
            "A": "El precio máximo",
            "B": "El precio mínimo encontrado",
            "C": "El promedio de precios",
            "D": "El número de clientes"
        },
        "respuesta": "B"
    },
    {
        "numero": 13,
        "tema": "Diseño de algoritmos",
        "dificultad": "Difícil",
        "puntos": 4,
        "pregunta": "Deseas encontrar la temperatura máxima registrada durante una semana. ¿Cuál debe ser el primer paso del algoritmo?",
        "opciones": {
            "A": "Guardar como máxima la temperatura del primer día.",
            "B": "Calcular el promedio.",
            "C": "Ordenar todas las temperaturas.",
            "D": "Eliminar valores repetidos."
        },
        "respuesta": "A"
    },
    {
        "numero": 14,
        "tema": "Análisis y eficiencia",
        "dificultad": "Media",
        "puntos": 2,
        "pregunta": "Dos algoritmos buscan un nombre en una lista ordenada de 1.000 elementos. Algoritmo A: revisa desde el inicio. Algoritmo B: divide repetidamente la lista por la mitad. ¿Cuál suele requerir menos comparaciones?",
        "opciones": {
            "A": "Algoritmo A",
            "B": "Algoritmo B",
            "C": "Ambos requieren las mismas",
            "D": "Depende del alfabeto"
        },
        "respuesta": "B"
    },
    {
        "numero": 15,
        "tema": "Análisis y eficiencia",
        "dificultad": "Fácil",
        "puntos": 1,
        "pregunta": "¿Qué característica define mejor a un algoritmo eficiente?",
        "opciones": {
            "A": "Utiliza la mayor cantidad posible de pasos.",
            "B": "Resuelve correctamente el problema utilizando los recursos de forma razonable.",
            "C": "Siempre contiene muchas condiciones.",
            "D": "Debe repetirse indefinidamente."
        },
        "respuesta": "B"
    },

    # ======================================================
    # PREGUNTAS NUEVAS CON IMÁGENES (16-20)
    # ======================================================

    {
        "numero": 16,
        "tema": "Secuenciación",
        "dificultad": "Fácil",
        "puntos": 1,
        "imagen": "img/diagrama_16.png",
        "pregunta": "Observa el diagrama de flujo de un cajero automático. ¿Qué paso falta antes de 'Entregar dinero'?",
        "opciones": {
            "A": "Repetir el PIN",
            "B": "Verificar saldo disponible",
            "C": "Cerrar sesión",
            "D": "Reiniciar el cajero"
        },
        "respuesta": "B"
    },
    {
        "numero": 17,
        "tema": "Condicionales",
        "dificultad": "Media",
        "puntos": 2,
        "imagen": "img/diagrama_17.png",
        "pregunta": "Según el diagrama, si un cliente tiene 16 años y no lleva acompañante, ¿qué ocurre?",
        "opciones": {
            "A": "Entra sin restricción",
            "B": "No ingresa",
            "C": "Debe pagar una tarifa extra",
            "D": "El sistema pide su documento"
        },
        "respuesta": "B"
    },
    {
        "numero": 18,
        "tema": "Iteración",
        "dificultad": "Media",
        "puntos": 2,
        "imagen": "img/diagrama_18.png",
        "pregunta": "Observa el ciclo. Si la lista tiene 7 elementos, ¿cuántas veces se ejecuta el bloque 'Revisar elemento'?",
        "opciones": {
            "A": "6",
            "B": "7",
            "C": "8",
            "D": "Infinitas veces"
        },
        "respuesta": "B"
    },
    {
        "numero": 19,
        "tema": "Diseño de algoritmos",
        "dificultad": "Difícil",
        "puntos": 4,
        "imagen": "img/diagrama_19.png",
        "pregunta": "Este diagrama busca el número mayor en una lista, pero le falta un paso. ¿Cuál falta?",
        "opciones": {
            "A": "Actualizar máximo con el nuevo número",
            "B": "Reiniciar el contador",
            "C": "Eliminar el número anterior",
            "D": "Ordenar la lista completa"
        },
        "respuesta": "A"
    },
    {
        "numero": 20,
        "tema": "Análisis y eficiencia",
        "dificultad": "Difícil",
        "puntos": 4,
        "imagen": "img/diagrama_20.png",
        "pregunta": "Compara ambos algoritmos de búsqueda sobre una lista ordenada de 1.000 elementos. ¿Cuál afirmación es correcta?",
        "opciones": {
            "A": "La búsqueda lineal siempre es más rápida.",
            "B": "La búsqueda binaria requiere menos comparaciones en el peor caso.",
            "C": "Ambas requieren el mismo número de comparaciones.",
            "D": "La búsqueda binaria solo funciona con listas desordenadas."
        },
        "respuesta": "B"
    }
]

# Puntaje máximo posible del examen (se calcula automáticamente,
# así que si agregas o quitas preguntas no hay que tocar nada más)
PUNTAJE_MAXIMO = sum(p["puntos"] for p in preguntas)


# ==========================================================
# FUNCIONES
# ==========================================================

def obtener_nivel(puntos, puntaje_maximo):
    """
    Clasifica al estudiante según la escala AKS,
    usando el porcentaje obtenido (no un número fijo de puntos),
    para que funcione sin importar cuántas preguntas tenga el examen.

    Retorna: (codigo_nivel, descripcion, mensaje, aprobado)
    """

    porcentaje = (puntos / puntaje_maximo) * 100

    if porcentaje <= 20:
        return (
            "AKS-1",
            "Nivel inicial",
            "El resultado indica que el estudiante aún presenta "
            "dificultades importantes en los fundamentos evaluados de algoritmia.",
            False
        )

    elif porcentaje <= 40:
        return (
            "AKS-2",
            "Nivel básico",
            "El resultado indica que el estudiante comprende algunos "
            "fundamentos de algoritmia, pero aún debe reforzar varios temas.",
            False
        )

    elif porcentaje <= 60:
        return (
            "AKS-3",
            "Nivel intermedio",
            "El resultado indica que el estudiante presenta un nivel "
            "intermedio y resuelve problemas de algoritmia de forma autónoma.",
            True
        )

    elif porcentaje <= 80:
        return (
            "AKS-4",
            "Nivel avanzado",
            "El resultado indica que el estudiante tiene un buen dominio "
            "del razonamiento algorítmico.",
            True
        )

    else:
        return (
            "AKS-5",
            "Nivel experto",
            "El resultado indica que el estudiante presenta un dominio "
            "avanzado de algoritmia.",
            True
        )


def evaluar_respuestas(respuestas):
    """
    Evalúa todas las respuestas y calcula
    el puntaje total.
    """

    puntos = 0
    correctas = 0
    resultados = []

    for i, pregunta in enumerate(preguntas):

        respuesta_usuario = respuestas[i]

        respuesta_correcta = pregunta["respuesta"]

        valor = pregunta["puntos"]

        if respuesta_usuario == respuesta_correcta:

            puntos += valor
            correctas += 1

            resultados.append({
                "pregunta": pregunta["numero"],
                "tema": pregunta["tema"],
                "resultado": "Correcta",
                "puntos": valor
            })

        else:

            resultados.append({
                "pregunta": pregunta["numero"],
                "tema": pregunta["tema"],
                "resultado": "Incorrecta",
                "puntos": 0
            })

    return puntos, correctas, resultados


# ==========================================================
# INTERFAZ
# ==========================================================

st.title("AKS — Algorithmic Knowledge Standard")

st.write(
    "Este sistema analiza el desempeño del estudiante "
    f"mediante una prueba de {len(preguntas)} preguntas y utiliza la "
    "escala AKS para determinar su nivel."
)

st.info(
    "Puntuación: Fácil = 1 punto | "
    "Media = 2 puntos | Difícil = 4 puntos "
    f"| Puntaje máximo del examen: {PUNTAJE_MAXIMO} puntos"
)

st.divider()

# ==========================================================
# DATOS DEL ESTUDIANTE
# ==========================================================

nombre = st.text_input(
    " Nombre del estudiante"
)

st.divider()

# ==========================================================
# FORMULARIO
# ==========================================================

respuestas_usuario = []

with st.form("examen_algoritmia"):

    for pregunta in preguntas:

        st.subheader(
            f"Pregunta {pregunta['numero']} "
            f"({pregunta['tema']})"
        )

        st.caption(
            f"Dificultad: {pregunta['dificultad']} "
            f"| Valor: {pregunta['puntos']} punto(s)"
        )

        st.write(
            pregunta["pregunta"]
        )

        # Si la pregunta tiene imagen asociada, se muestra aquí
        if pregunta.get("imagen"):
            st.image(
                pregunta["imagen"],
                caption=f"Figura – Pregunta {pregunta['numero']}",
                use_container_width=True
            )

        opciones = list(
            pregunta["opciones"].keys()
        )

        respuesta = st.radio(
            "Selecciona una respuesta:",
            opciones,
            index=None,
            format_func=lambda x, p=pregunta: (
                f"{x}. {p['opciones'][x]}"
            ),
            key=f"pregunta_{pregunta['numero']}"
        )

        respuestas_usuario.append(respuesta)

        st.divider()

    enviar = st.form_submit_button(
        "🔎 Evaluar conocimientos",
        use_container_width=True
    )


# ==========================================================
# RESULTADOS
# ==========================================================

if enviar:

    if nombre.strip() == "":

        st.error(
            " Debes ingresar el nombre del estudiante."
        )

    elif None in respuestas_usuario:

        faltantes = [
            preguntas[i]["numero"]
            for i, r in enumerate(respuestas_usuario)
            if r is None
        ]

        st.error(
            " Debes responder todas las preguntas antes de enviar. "
            f"Faltan: {', '.join(str(n) for n in faltantes)}"
        )

    else:

        puntos, correctas, resultados = evaluar_respuestas(
            respuestas_usuario
        )

        nivel, descripcion, conclusion, aprobado = obtener_nivel(
            puntos, PUNTAJE_MAXIMO
        )

        porcentaje = (
            puntos / PUNTAJE_MAXIMO
        ) * 100

        # ==============================================
        # RESULTADO GENERAL
        # ==============================================

        st.divider()

        st.header(" Resultado de la evaluación")

        st.success(
            f"Estudiante: {nombre}"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Correctas",
                f"{correctas}/{len(preguntas)}"
            )

        with col2:

            st.metric(
                "Puntaje",
                f"{puntos}/{PUNTAJE_MAXIMO}"
            )

        with col3:

            st.metric(
                "Porcentaje",
                f"{porcentaje:.1f}%"
            )

        # ==============================================
        # NIVEL AKS
        # ==============================================

        st.subheader(
            f"🎯 Nivel obtenido: {nivel}"
        )

        st.write(
            f"**Clasificación:** {descripcion}"
        )

        if aprobado:

            st.success(
                conclusion
            )

        else:

            st.error(
                conclusion
            )

        st.progress(
            puntos / PUNTAJE_MAXIMO
        )

        # ==============================================
        # DETALLE
        # ==============================================

        st.divider()

        st.subheader(
            " Detalle de resultados"
        )

        for resultado in resultados:

            numero = resultado["pregunta"]

            if resultado["resultado"] == "Correcta":

                st.write(
                    f"✅ Pregunta {numero}: "
                    f"Correcta (+{resultado['puntos']} puntos)"
                )

            else:

                st.write(
                    f"❌ Pregunta {numero}: "
                    f"Incorrecta (+0 puntos)"
                )

        # ==============================================
        # RESULTADO POR ÁREA
        # ==============================================

        st.divider()

        st.subheader(
            " Desempeño por área"
        )

        temas = {}

        for i, pregunta in enumerate(preguntas):

            tema = pregunta["tema"]

            if tema not in temas:

                temas[tema] = {
                    "obtenidos": 0,
                    "maximos": 0
                }

            temas[tema]["maximos"] += pregunta["puntos"]

            if respuestas_usuario[i] == pregunta["respuesta"]:

                temas[tema]["obtenidos"] += pregunta["puntos"]

        for tema, datos in temas.items():

            porcentaje_tema = (
                datos["obtenidos"] /
                datos["maximos"]
            ) * 100

            st.write(
                f"**{tema}:** "
                f"{datos['obtenidos']}/"
                f"{datos['maximos']} puntos "
                f"({porcentaje_tema:.1f}%)"
            )

            st.progress(
                porcentaje_tema / 100
            )

        # ==============================================
        # FORTALEZAS Y DEBILIDADES
        # ==============================================

        fortalezas = []
        debilidades = []

        for tema, datos in temas.items():

            porcentaje_tema = (
                datos["obtenidos"] /
                datos["maximos"]
            ) * 100

            if porcentaje_tema >= 70:

                fortalezas.append(tema)

            else:

                debilidades.append(tema)

        st.divider()

        col1, col2 = st.columns(2)

        with col1:

            st.subheader(" Fortalezas")

            if fortalezas:

                for tema in fortalezas:

                    st.write(
                        f"✅ {tema}"
                    )

            else:

                st.write(
                    "No se identificaron fortalezas "
                    "claras."
                )

        with col2:

            st.subheader(" Por mejorar")

            if debilidades:

                for tema in debilidades:

                    st.write(
                        f" {tema}"
                    )

            else:

                st.write(
                    "No se identificaron áreas "
                    "críticas."
                )

        # ==============================================
        # CONCLUSIÓN
        # ==============================================

        st.divider()

        st.subheader(
            " Conclusión"
        )

        st.write(
            f"El estudiante **{nombre}** obtuvo "
            f"**{puntos} de {PUNTAJE_MAXIMO} puntos**, equivalentes "
            f"al **{porcentaje:.1f}%** del puntaje máximo. "
            f"De acuerdo con la escala AKS, alcanzó "
            f"el nivel **{nivel} ({descripcion})**."
        )

        st.write(
            conclusion
        )
