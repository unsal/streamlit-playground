import streamlit as st  # use on Terminal as: streamlit run yz_streamlit.py
import time


header_container = st.container()
body_container = st.container()


with header_container:
    # Use Markdown for Writing Web Text
    st.title("Hello World :wave:")
    st.write("Welcome to Python Streamlit")

with body_container:
    progress_value = st.progress(0)
    for i in range(100):
        time.sleep(0.05)
        progress_value.progress(i + 1)

    st.success("Data loaded Successfully")
