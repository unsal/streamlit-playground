import streamlit as st  # use on Terminal as: streamlit run yz_streamlit.py


header_container = st.container()
sidebar_container = st.container()

col1, col2 = st.columns([1, 2])


with header_container:
    # Use Markdown for Writing Web Text
    st.title("Hello World :wave:")
    st.write("Welcome to Python Streamlit")


# Navigation Section
with sidebar_container:
    animal_type = st.sidebar.selectbox("What is your pet?", ("Cat", "Dog", "Hamster"))
    pet_color = st.sidebar.text_area(f"What color is your {animal_type}", max_chars=15)

    if pet_color:
        col1.text("Sidebar selection occured")
