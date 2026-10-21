import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt


st.title("Conjunto de datos de estadisticas de POKEMON")
st.header("Pokemon")

dataframe = pd.read_csv("https://raw.githubusercontent.com/key-lgmz/ciencia-datos/refs/heads/main/pokemon_complete_stats%20(2).csv")

st.dataframe(dataframe) 
st.sidebar.title("opciones")
 ##prueba

agree = st.sidebar.checkbox("mostrar estadisticas")
if agree:
    st.dataframe(dataframe) 

selected_color = st.sidebar.radio("selecciona pokemon",
dataframe['color'].unique())
st.write("Selected Embark Town:", selected_color)

# Select a range of the fare and then display the dataset
optionals = st.sidebar.expander("Optional Configurations", True)
fare_min = optionals.slider(
 "Minimum Fare",
 min_value=(0),
 max_value=(23), 
 )

st.sidebar.write("Seleccionar tipo")
type_1 = st.selectbox(" ",
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
])
filtrar_director = st.button("Filtrar")