import streamlit as st  # use on Terminal as: streamlit run yz_streamlit.py


header_container = st.container()


with header_container:
    # Use Markdown for Writing Web Text
    st.title("Hello World :wave:")
    st.write("Welcome to Python Streamlit Playground")
