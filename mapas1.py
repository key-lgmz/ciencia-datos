import pandas as pd
import numpy as np
import streamlit as st

map_data = pd.DataFrame(
np.random.randn(100, 2) / [50,50] + [18.855,-96.76056],
columns=['lat', 'lon'])

# Create the title for the web app
st.title("corral Map")
st.header("Using Streamlit and Mapbox")

st.map(map_data)