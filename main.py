# Instalamos las librerías necesarias
pip install numpy streamlit pandas matplotlib seaborn sqlite st_aggrid

# Importamos las librerias necesarias

from git import Object
from numpy import int64
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
from st_aggrid import AgGrid

# Cargamos los datos
data = pd.read_csv('./data/titanic.csv', dtype={'Pclass' : int64})

female = data[data.Sex=='Female'].count()
male = data[data.Sex=='Male'].count()

# Barra lateral 
st.sidebar.subheader('Prácticas profesionalizantes II')
st.sidebar.caption('Ejemplo 1')

st.header('La tragedia del Titanic')

col1, col2 = st.columns(2)
col1.markdown('El __RMS__ __Titanic​__ fue un transatlántico británico, el mayor barco de pasajeros del mundo al finalizar su construcción, que naufragó en las aguas del océano Atlántico durante la noche del 14 y la madrugada del 15 de abril de 1912, mientras realizaba su viaje inaugural desde Southampton a Nueva York. En el hundimiento murieron 1496 personas de las 2208 que iban a bordo, lo que convierte a esta catástrofe en uno de los mayores naufragios de la historia ocurridos en tiempos de paz. ')
col2.image('https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/RMS_Titanic_3.jpg/800px-RMS_Titanic_3.jpg', caption='Imagen del Titanic al zarpar')

col1,col2 = st.columns(2)
col1.metric(label='Pasajeros', value='2787')
col2.metric(label='Tripulación', value='885')

st.subheader('Análisis de la composición de los pasajeros')

col1, col2 = st.columns(2)
col1.markdown('Distribución por __Edad__ y __Sexo__')
fig = plt.figure()
sns.histplot(x=data.Age, hue=data.Sex, multiple='stack', palette='mako')
col1.pyplot(fig)

col2.markdown('Distribución por __Clase__')
fig = plt.figure()
sns.histplot(x=data.Pclass, palette='Set2')
col2.pyplot(fig)

with st.expander('Abrir para ver el listado de los pasajeros'):
    AgGrid(data)


st.subheader('Análisis de la supervivencia')

tabla1 = pd.crosstab(data.Sex, data.Survived)
tabla2 = pd.crosstab(data.Pclass, data.Survived)


col1, col2, col3 = st.columns(3)
col1.markdown('Supervivencia por __Sexo__')
col1.table(tabla1*100/tabla1.sum(axis=0))

col2.markdown('Supervivencia por __Clase__')
col2.table(tabla2*100/tabla2.sum(axis=0))
col3.markdown('Supervivencia por __Edad__')

col1, col2, col3 = st.columns(3)
fig = plt.figure()
sns.histplot(x=data.Sex, hue=data.Survived, multiple='stack', palette='deep')
col1.pyplot(fig)
fig = plt.figure()
sns.histplot(x=data.Pclass, hue=data.Survived, multiple='stack', palette='deep')
col2.pyplot(fig)

fig = plt.figure()
sns.histplot(x=data.Age, hue=data.Survived, multiple='stack', palette='deep')
col3.pyplot(fig)
