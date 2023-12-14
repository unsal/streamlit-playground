import streamlit as st  # use on Terminal as: streamlit run yz_streamlit.py


header_container = st.container()
column_container1 = st.container()
column_container2 = st.container()

col1, col2, col3 = st.columns([1, 2, 1])

col4, col5 = st.columns(2)


with header_container:
    # Use Markdown for Writing Web Text
    st.title("Hello Worlds :wave:")
    st.write("Welcome to Python Streamlit")

with column_container1:
    col1.text("This is Column1")
    col2.text("This is Column2")
    col3.text("This is Column3")

with column_container2:
    col4.text("This is Column4")
    col5.text("This is Column5")
