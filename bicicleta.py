import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt


st.title("Cicle Rides in NYC")

st.header("Raw Data")

dataframe = pd.read_csv("https://raw.githubusercontent.com/key-lgmz/ciencia-datos/refs/heads/main/citibike-tripdata.csv")

st.dataframe(dataframe) 

with st.sidebar:
 st.title("opciones")
 ##prueba
 st.header("Dataset")
 agree = st.checkbox("show raw data")
 if agree:
  st.dataframe(dataframe)
 agree = st.checkbox("Recorrido por hora")
 if agree:
    st.dataframe(dataframe)

 DATE_COLUMN = 'date/time'
 DATA_URL = ("https://raw.githubusercontent.com/key-lgmz/ciencia-datos/refs/heads/main/citibike-tripdata.csv")
 
 def load_data(nrows) :
  data = pd.read_csv(DATA_URL, nrows=nrows)
  lowercase = lambda x: str(x).lower()
  data.rename(lowercase, axis='columns', inplace=True)
  data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
  return data
  data = load_data(10000)
  filtered_data = data[data[DATE_COLUMN] .dt.hour == hour_to_filter]

fig,ax = plt.subplots()
ax.hist(dataframe.rideable_type)
st.header("Recorrido")
st.pyplot(fig)

    
