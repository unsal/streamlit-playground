import streamlit as st  # use on Terminal as: streamlit run photo_taken.py
import time

header_container = st.container()
column_container = st.container()


if "photo" not in st.session_state:
    st.session_state["photo"] = "not done"


def change_photo_state():
    st.session_state["photo"] = "done"


# Container is just for organizing code. It is optional
# Header Section
with header_container:
    # Use Markdown for Writing Web Text
    st.title("Hello World :wave:")
    st.write("Welcome to Python Streamlit")

# Body Section
with column_container:
    st.write("---")
    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if st.session_state["photo"] == "done":
            st.header("Column 1")
        else:
            st.header("Column 1 - Photo Taken")

    with col2:
        st.header("Column 2")
        photo_taken = col2.camera_input("Take a Photo", on_change=change_photo_state)

        if st.session_state["photo"] == "done":
            col2.success("Photo Uploaded Successfully")

    with col3:
        if photo_taken:
            st.image(photo_taken)
        else:
            st.write("No Photo Taken")
