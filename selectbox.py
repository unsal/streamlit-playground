import streamlit as st  # use on Terminal as: streamlit run yz_streamlit.py


header_container = st.container()


with header_container:
    # Use Markdown for Writing Web Text
    st.title("Select Box")
    donation = st.selectbox(
        "How much to donate?", options=[100, 200, 300, 400, 500, "No Limit"], index=0
    )
    st.header(donation)
