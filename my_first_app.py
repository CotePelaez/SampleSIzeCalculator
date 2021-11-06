import streamlit as st
import pandas as pd
import numpy as np

from PIL import Image

## Add a title of your app
st.title('Halina Skorulski Pelaez')

## ASdding some metrics

col1, col2, col3 = st.columns(3)
col1.metric("Edad", "9", "pronto 10")
col2.metric("Simpatica", "10", "con la edad más")
col3.metric("Astronauta", "8", "lo que ella quiera ser")


## selector of images

select_image = st.selectbox(
   "Momentos",
   ('picara', 'frio polaco', 'rome','cumple47', 'abuelos españoles', 'bruja',
    'family', 'volar: lo que mas me gusta', 'tios', 'abuelos polacos'))

if select_image == 'picara':
    img = Image.open("photos/ima1.png")
    st.image(img,width=500)
elif select_image == 'frio polaco':
    img = Image.open("photos/ima2.png")
    st.image(img,width=500)
elif select_image == 'rome':
    img = Image.open("photos/ima3.png")
    st.image(img,width=500)
elif select_image == 'cumple47':
    img = Image.open("photos/ima4.png")
    st.image(img,width=500)
elif select_image == 'abuelos españoles':
    img = Image.open("photos/ima5.png")
    st.image(img,width=500)
elif select_image == 'bruja':
    img = Image.open("photos/ima6.png")
    st.image(img,width=500)
elif select_image == 'family':
    img = Image.open("photos/ima7.png")
    st.image(img,width=500)
elif select_image == 'volar: lo que mas me gusta':
    img = Image.open("photos/ima8.png")
    st.image(img,width=500)
elif select_image == 'tios':
    img = Image.open("photos/ima9.png")
    st.image(img,width=500)
elif select_image == 'abuelos polacos':
    img = Image.open("photos/ima10.png")
    st.image(img,width=500)
else:
    st.write("seguiremos buscando buenas fotos...")
