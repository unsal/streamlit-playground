import streamlit as st

import pandas as pd 
import numpy as np 

header = st.container()
body = st.container()

with header:
    st.header("Pandas Data Frame 1") # This is equal to: st.write("# Pandas Data Frame 1")

with body:
    np.random.seed(0)
    
    df = pd.DataFrame(
        np.random.rand(12,3),
        columns = ('Col1', 'Col2', 'Col3')
    )
    
    df['Name'] = pd.DataFrame(['Unsal','Emre','Burak','Filiz','Yurdanur','Seda','Unsal','Burak','Filiz','Unsal','Sakir','Emre'])
    df['Category'] = pd.DataFrame(['B','C','A','C','D','E','B','F','A','C','B','E'])
    
    st.subheader("Original Data Frame")
    st.write(df)
    
    # Group By
    st.subheader('Group By')
    df = df.groupby(['Name','Category']).first()
    st.write(df)
    
 
    
    
    
    
    
    
    
