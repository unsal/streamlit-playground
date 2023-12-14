import streamlit as st  # use on Terminal as: streamlit run yz_streamlit.py


header_container = st.container()


with header_container:
    # Use Markdown for Writing Web Text
    st.title("Text Input")
    text_input = st.text_input("Enter Your Name", "")
    st.write(text_input)
