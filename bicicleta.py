import pandas as pd
import numpy as np
import streamlit as st


st.title("Cicle Rides in NYC")

st.header("Raw Data")

dataframe = pd.read_csv("https://raw.githubusercontent.com/key-lgmz/ciencia-datos/refs/heads/main/citibike-tripdata.csv")

st.dataframe(dataframe) 

st.sidebar.title("opciones")
 ##prueba
st.header("Keyra Mychell Luna Gomez - Maria de Jesus Montalvo Lopez")
agree = st.sidebar.checkbox("show raw data")
if agree:
    st.dataframe(dataframe)



agree = st.sidebar.checkbox("Recorrido por hora")
if agree:
    st.dataframe(dataframe.started_at)

  # Select a range of the fare and then display the dataset
optionals = st.sidebar.expander("Optional Configurations", True)
fare_min = optionals.slider(
 "Minimum Fare",
 min_value=float(0),
 max_value=float(23)
 )

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
ax.hist(dataframe.started_at)
st.header("Recorrido")
st.pyplot(fig)

map_data = pd.DataFrame(
np.random.randn(100, 2) / [50,50] + [40.71427,-74.00597],
columns=['lat', 'lon'])

# Create the title for the web app
st.title("Mapas por recorridos")
st.header("NYC")

st.map(map_data)

