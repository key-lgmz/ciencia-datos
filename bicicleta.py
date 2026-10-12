import pandas as pd
import numpy as np
import streamlit as st

st.title("Cicle Rides in NYC")

st.header("Raw Data")

dataframe = pd.read_csv("https://raw.githubusercontent.com/key-lgmz/ciencia-datos/refs/heads/main/citibike-tripdata.csv")

st.dataframe(dataframe) 

with st.sidebar:
 st.title("opciones")
 ##prueba
 st.header("Dataset")
 agree = st.checkbox("show raw data")
 agree = st.checkbox("recorridos por hora")
 if agree:
    st.dataframe(dataframe)
    
###hora
#%%writefile uber_ny.py
#import pandas as pd
#import numpy as np
#import streamlit as st
#st.title('Uber pickups in NYC')
#DATE_COLUMN = 'date/time'
#DATA_URL = ('/content/uber_dataset.csv')
#@st.cache
#def load_data(nrows):
#data = pd.read_csv(DATA_URL, nrows=nrows)
#lowercase = lambda x: str(x).lower()
#data.rename(lowercase, axis='columns', inplace=True)
#data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#return data

#data_load_state = st.text('Loading data...')
#data = load_data(1000)
#data_load_state.text("Done! (using st.cache)")
# Some number in the range 0-23
#hour_to_filter = st.slider('hour', 0, 23, 17)
#filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
#st.subheader('Map of all pickups at %s:00' % hour_to_filter)
#st.map(filtered_data)