import streamlit as st

import pandas as pd 
import numpy as np 

header = st.container()
body = st.container()

with header:
    st.header("Pandas Data Frame") # This is equal to: st.write("# Pandas Data Frame 1")

with body:
   df1 = pd.DataFrame(data={'Name':['Unsal','Nevin','Merve','Gamze'], 'Score 1':[10,34,45,77]})
   df2 = pd.DataFrame(data={'Name':['Unsal','Nevin','Merve','Gamze'], 'Score 2':[66,78,95,23]})
   
   # Sources
   st.subheader('Sources')
   st.write(df1)
   st.write(df2)
   
   # Merged DF's
   st.subheader('Merged Data Frames')
   df1 = df1.merge(df2,how='inner',on='Name' )
   st.write(df1)
   
   
   
   
   
    
    
    
    
    
    
    
