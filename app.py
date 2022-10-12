import streamlit as st
import pandas as pd 
import numpy as np 
import pickle as pkl

data=pd.read_csv("https://raw.githubusercontent.com/labeconometria/MLxE/main/proyectos1er/dataset_2.csv")
st.title('Proyecto 8') 
st.write('A partir de la siguiente base de datos se analiza si la persona clasificaría como un cliente existente o un cliente retirado')
st.dataframe(data)
st.subheader('Descripción de variables')

