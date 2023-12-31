import streamlit as st

container = st.container()

col1, col2 = st.columns(2)

    
with container:
    st.title("Form 2")
    
with col1:
    age = st.number_input("Enter your age", value=0, step=1)

with col2:
    lucky_number = st.number_input("Lucky Number?", value=0, step=1)
    

    