import streamlit as st  # use on Terminal as: streamlit run yz_streamlit.py


header_container = st.container()


with header_container:
    # Use Markdown for Writing Web Text
    st.title("Slider")
    level = st.slider("Select Level", min_value=10, max_value=100, value=20, step=10)
    st.header(level)
