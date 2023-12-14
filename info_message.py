import streamlit as st  # use on Terminal as: streamlit run yz_streamlit.py


header_container = st.container()

col1, col2, col3 = st.columns([1, 2, 1])


with header_container:
    # Use Markdown for Writing Web Text
    st.title("Info Message :wave:")


# Container is just for organizing code. It is optional
# Header Section
with header_container:
    # Use Markdown for Writing Web Text
    col1.success("success")
    col2.warning("warning")
    col3.error("error")
