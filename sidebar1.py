# importamos la libreria Streamlit
import streamlit as st 

# Crear el tituilo de la aplicacion web
st.title("Mi primera app con streamlit")

# Creamos el sidebar
sidebar = st.sidebar

#Agregamos un titulo y texto al sidebar
sidebar.title("esta es la barra lateral")

sidebar.write("aqui van los elementos de entrada")

#Agregamos headers ala seccion principal
st.header("informacion soibre el conjunto de datos")
st.header("descripcion de los datos")

#Agregamos texto ala seccion principal
st.write("este es un simple ejemplo de una app para predicir ,esta app predice mis datos")