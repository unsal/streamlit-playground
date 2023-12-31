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
        np.random.rand(4,3),
        columns = ('Col1', 'Col2', 'Col3')
    )
    
    st.subheader("Original Data Frame")
    st.write(df)
   
   # Sorted Data Frame
    st.subheader("Sorted Data Frame")
    df=df.sort_values(by='Col1', ascending=True)
    st.write(df)
   