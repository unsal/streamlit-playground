import streamlit as st

import pandas as pd 
import numpy as np 

header = st.container()
body = st.container()

with header:
    st.header("Pandas Data Frame 1") # This is equal to: st.write("# Pandas Data Frame 1")

with body:
    np.random.seed(0)
    
    df_original = pd.DataFrame(
        np.random.rand(4,3),
        columns = ('Col1', 'Col2', 'Col3')
    )
    
    st.subheader("Original Data Frame")
    st.write(df_original)
    
    # Mutated Cols
    st.subheader("Mutated Data Frame")
    df = df_original[['Col1','Col2']]
    st.write(df)
    
    
    # Filtered Data Frame
    st.subheader("Fitered Data Frame")
    df = df_original[df_original['Col1'] > 0.5]
    st.write(df)
    
    
    
    
    
    
    
