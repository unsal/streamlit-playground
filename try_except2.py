import streamlit as st

container = st.container()

col1, col2 = st.columns(2)

    
with container:
    st.title("Exception 2")
    
with col1:
    number1 = st.number_input("Enter your age", value=0, step=1)

with col2:
    number2 = st.number_input("Lucky Number?", value=0, step=1)
    
try:
    percentage = number1/number2
    
    st.write(f"**Percantage** is {percentage}")
    
except ZeroDivisionError:
    st.error("Division by Zero Error!")
    