import pandas as pd
import numpy as np
import streamlit as st

st.title("Netflix App")

sidebar = st.sidebar

sidebar.title("esta es la barra lateral")


st.header("Todos los filmes")

dataframe = pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/movies.csv",encoding = 'ISO-8859-1')

st.dataframe(dataframe) 
