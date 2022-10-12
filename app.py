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
