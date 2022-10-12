import streamlit as st
import pandas as pd 
import numpy as np 
import pickle as pkl

data=pd.read_csv("https://raw.githubusercontent.com/labeconometria/MLxE/main/proyectos1er/dataset_2.csv")
st.title('Proyecto 8') 
st.write('A partir de la siguiente base de datos se analiza si la persona clasificaría como un cliente existente o un cliente retirado')
st.dataframe(data)
st.subheader('Descripción de variables')

col1,col2=st.columns(2)
with col1:
  st.write("""0 CLIENTNUM: "Número de cliente"  """)
  st.write(""" 1   Attrition_Flag: "Variable de actividad del cliente" """)
  st.write( """2   Customer_Age      """)                                                                                                                    
  st.write( """ 3   Gender          """)                                                                                                                      
  st.write( """ 4   Dependent_count  """)                                                                                                                     
  st.write( """ 5   Education_Level  """)    
  st.write( """ 6   Marital_Status: "Estado civil"   """)
  st.write( """ 7   Income_Category""") 
  st.write( """ 8   Card_Category    """)           
  st.write( """ 9   Months_on_book   """)                                                                                                                     
  st.write( """ 10  Total_Relationship_Count     """)                                                                                                         
  st.write( """ 11  Months_Inactive_12_mon """)                                                                                                          
  st.write( """ 12  Contacts_Count_12_mon  """)                                                                                                               
  st.write( """ 13  Credit_Limit          """)                                                                                                               
  st.write( """ 14  Total_Revolving_Bal """)                                                                                                                  
  st.write( """ 15  Avg_Open_To_Buy        """) 
  st.write( ""   "")
  st.write( ""   "")
  st.write( """ 16  Total_Amt_Chng_Q4_Q1    """)                                                                                                              
  st.write( ""   "")
  st.write( """ 17  Total_Trans_Amt   """) 
  st.write( ""   "")
  st.write( ""   "")
  st.write( """ 18  Total_Trans_Ct         """)                                                                                                               
  st.write( """ 19  Total_Ct_Chng_Q4_Q1  """)        
  st.write( ""   "")
  st.write( """ 20  Avg_Utilization_Ratio    """)                                                                                                             

 

  
with col2: 
  st.write("""Identificador único del cliente titular de la cuenta""")
  st.write(""" Si la cuenta está cerrada, entonces 1, si no 0 """) 
  st.write( """Edad del cliente en años""")
  st.write( """M=Hombre, F=Mujer """)
  st.write( """Número de personas a cargo  """) 
  st.write( """Nivel educativo del titular de la cuenta """)
  st.write( """ Casado, Soltero, Divorciado, Desconocido  """)
  st.write( """Ingresos anuales del titular de la cuenta   """) 
  st.write( """Tipo de tarjeta (Azul, Plata, Oro, Platino)  """) 
  st.write( """Duración de la relación con el banco en meses """)
  st.write( """Número total de productos en poder del cliente  """) 
  st.write( """Meses de inactividad en los últimos 12 meses """) 
  st.write( """Número de contactos en los últimos 12 meses   """)
  st.write( """Límite de crédito de la tarjeta de crédito """)
  st.write( """Saldo rotativo total de la tarjeta de crédito """) 
  st.write( """Línea de crédito abierta a la compra (media de los últimos 12 meses) """) 
  st.write( """Variación del importe de las transacciones (cuarto trimestre sobre primer trimestre) """)
  st.write( """Cantidad total de las transacciones (últimos 12 meses)   """)
  st.write( """Recuento de transacciones  """) 
  st.write( """Cambio en el recuento de transacciones (cuarto trimestre sobre primer trimestre) """) 
  st.write( """Índice de utilización promedio de la tarjeta """)
  
  
st.subheader(""" Graficas""")
st.write("A continuación se muestran nlos graficos relevantes para la descripción de variables")

st.image("./img/Img1.png")
st.caption('Participación por edad de las personas en el estudio')

st.image("./img/Img2.png")
st.caption('Participación por estado civil de las personas en el estudio')

st.image("./img/Img3.png")
st.caption('Participación por hombres y mujeres como clientes actios o inactivos en relación a su periodo en relacion al banco')
  
st.image("./img/Img4.png")
st.caption('Participación por categoria de ingreso de las personas en el estudio')

st.image("./img/Img5.png") 
st.caption('Participación por categoria de tarjeta de las personas en el estudio')


st.write("**En los siguientes graficos se muestra el comportamiento del modelo de clasificación**")

st.image("./img/Img6.png")  
st.caption('Matriz de confusion de la predicción del modelo')

st.image("./img/img7.png")
st.caption('Arbol de clasificación')

st.image("./img/img8.png")
st.caption('Insidencia de las variables en el modelo por barras')

st.image("./img/img9.png")
st.caption('Insidencia de las variables en el modelo: beeswarm')

st.image("./img/img10.png")
st.caption('Insidencia de las variables en el modelo: waterfall')


st.subheader("""Notebook """)
st.write("Acontinuación encontrará el link al notebook de entrenamiento del modelo")
st.write('https://github.com/ValeriaMendezC/Repositorio/blob/d014783430add3f37b81a4497141dbb6bfb70838/project8_final.ipynb')


st.markdown("""f
### **Captura de datos**

##### Ingrese los siguientes datos 

""")

nombre = st.text_input('Nombre completo')
Customer_Age =st.text_input('Edad')
Gender = st.text_input('Genero')

Gender = 1 if Gender == 'Masculino' else 0

dependent = st.text_input('Número de personas a cargo')
Education_Level = st.text_input('Nivel educativo')

Marital_Status = st.text_input('Estado civil')

Marital_Status = 1 if Marital_Status == 'Casado' else 0

Income_Category= st.text_input('Categoría de ingresos ')
card = st.text_input('Tipo de tarjeta')
Months_on_book = st.text_input('Duración de la relación con el banco')
Total_Relationship_Count = st.text_input('Número total de productos')
Months_Inactive_12_mon= st.text_input('Número de meses de inactividad')
cc = st.text_input('Número de contactos')
Credit_Limit = st.text_input('Límite de crédito')
Total_Revolving_Bal = st.text_input('Saldo rotativo total')
Avg_Open_To_Buy = st.text_input('Línea de crédito abierta a la compra (media de los últimos 12 meses)')
Total_Amt_Chng_Q4_Q1 = st.text_input('Variación del importe de las transacciones(cuarto trimestre sobre primer trimestre)')
Total_Trans_Amt = st.text_input('Cantidad total de las transacciones(12 meses)')
Total_Trans_Ct = st.text_input('Recuento de transacciones')
Total_Ct_Chng_Q4_Q1 = st.text_input('Cambio en el recuento de transacciones')
Avg_Utilization_Ratio =  st.text_input('Utilización promedio de la tarjeta')

