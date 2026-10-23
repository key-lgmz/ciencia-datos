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

agree = st.sidebar.checkbox("Mapa")

if agree:
    st.title("Mi pueblo")
    st.header("CORRAL DE PIEDRA")

    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [18.85639, -96.76306],
        columns=["lat", "lon"]
    )

    st.map(map_data)

selected_color = st.sidebar.radio("color de pokemon",
dataframe['color'].unique())
st.write("Selected Embark Town:", selected_color)
filtered_dataframe = dataframe [
    dataframe["color"]==selected_color
]
st.dataframe(filtered_dataframe)

# Select a range of the fare and then display the dataset
optionals = st.sidebar.expander("Optional Configurations", True)
fare_min = optionals.slider(
 "Minimum Fare",
 min_value=(0),
 max_value=(23), 
 )
 

 
dataframe = pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv")
st.header("estadisticas") 

fig,ax = plt.subplots()
ax.hist(dataframe.fare)
st.header("speed")
st.pyplot(fig)

fig2, ax2 = plt.subplots()
y_pos = dataframe['class']
x_pos = dataframe['fare']
ax2.barh(y_pos, x_pos)
ax2.set_ylabel("attack")
ax2.set_xlabel("special_attack")
ax2.set_title('¿Cuanto pagaron las clases del Titanic')
st.header("Grafica de Barras del Titanic")
st.pyplot(fig2)

fig3, ax3 = plt.subplots()
ax3.scatter(dataframe.age, dataframe.fare)
ax3.set_xlabel("hp")
ax3.set_ylabel("defense")
st.header("Grafica fuerza")
st.pyplot(fig3)

name = st.sidebar.text_input("Buscar tu Pokemon")

st.title("Keyra Mychell Luna Gomez")
st.title("Matricula: zS26004561")
