import streamlit as st 

st.set_page_config(
    page_title="Dashboard multi-página",
    layout="wide",
    initial_sidebar_state="expanded" # "collapsed"
)

#Definir las páginas
home_page = st.Page(
    "Paginas/home.py",
    title="Home",
    icon=":material/home:"
)

projects_page = st.Page(
    "Paginas/project_analysis.py",
    title="Análisis de proyectos",
    icon=":material/analytics:"
)

percentage_page = st.Page(
    "Paginas/percentage_analysis.py",
    title="Análisis de porcentajes",
    icon=":material/table_chart_view:"
)

mapa_page = st.Page(
    "Paginas/Mapa.py",
    title="Mapas",
    icon=":material/map_search:"
)

# Crear navegación con secciones
#pg = st.navigation([home_page,projects_page, percentage_page])
pg = st.navigation({
    "Inicio": [home_page],
    "Análisis": [projects_page, percentage_page],
    "Visualización": [mapa_page]
})

# Ejecutar la página seleccionada
pg.run()