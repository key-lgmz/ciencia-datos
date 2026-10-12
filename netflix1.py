import pandas as pd
import numpy as np
import streamlit as st

st.title("Netflix App")

st.header("Todos los filmes")

dataframe = pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/movies.csv",encoding = 'ISO-8859-1')

st.dataframe(dataframe) 

#prueba

st.set_page_config(
page_title="Netflix App",
layout="wide"
)

# Barra lateral
with st.sidebar:
 st.title("Filtros")

 mostrar_todos = st.checkbox("Mostrar todos los filmes")

 titulo = st.text_input("Título del filme:")

 buscar = st.button("Buscar filmes")

 st.write("Seleccionar Director")

 director = st.selectbox(
" ",
[
"Alan Metter",
"Tobe Hooper",
"Clint Eastwood",
"Tony Scott",
"James Cameron",
"Randall Wallace",
"Jim Henson",
"David Lynch",
"Howard Deutch",
"David Cronenberg"
]
)

 filtrar_director = st.button("Filtrar director")