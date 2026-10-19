import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt


st.title("Conjunto de datos de estadisticas de pokemon")
st.header("estadisticas")

dataframe = pd.read_csv("https://github.com/key-lgmz/ciencia-datos/blob/main/pokemon_complete_stats%20(2).csv")

st.dataframe(dataframe) 

st.sidebar.title("opciones")
 ##prueba

agree = st.sidebar.checkbox("visualizar estadisticas")
if agree:
    st.dataframe(dataframe)


agree = st.sidebar.checkbox("Recorrido por hora")

#if agree:
    #dataframe["started_at"] = pd.to_datetime(dataframe["started_at"])

    #fig, ax = plt.subplots()
    #ax.hist(
        #dataframe["started_at"].dt.hour.dropna(),
        #bins=24,
        #range=(0, 24)
    #)
    #ax.set_xlabel("Hora del día")
    #ax.set_xticks(range(24))
    #ax.set_xticklabels([f"{hora}:00" for hora in range(24)], rotation=45)
    #st.header("Recorrido por hora")
    #st.pyplot(fig)



agree = st.sidebar.checkbox("Mapa")

if agree:
    st.title("Mi pueblito natal")
    st.header("Corral de Piedra")

    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [40.71427, -74.00597],
        columns=["lat", "lon"]
    )

    st.map(map_data)


# Select a range of the fare and then display the dataset
optionals = st.sidebar.expander("Optional Configurations", True)
fare_min = optionals.slider(
 "Minimum Fare",
 min_value=(0),
 max_value=(23), 
 )

DATE_COLUMN = 'started_at'
DATA_URL = ("https://github.com/key-lgmz/ciencia-datos/blob/main/pokemon_complete_stats%20(2).csv")
def load_data(nrows) :
  data = pd.read_csv(DATA_URL, nrows=nrows)
  lowercase = lambda x: str(x).lower()
  data.rename(lowercase, axis='columns', inplace=True)
  data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
  return data
  data = load_data(10000)
  filtered_data = data[data[DATE_COLUMN] .dt.hour == hour_to_filter]



map_data = pd.DataFrame(
np.random.randn(100, 2) / [50,50] + [18.85639,-96.76306],
columns=['lat', 'lon'])

st.title("Keyra Mychell Luna Gomez")
