# Source: Web Application Development with Streamlit Book

import streamlit as st
from PIL import Image

icon = Image.open('favicon.ico')

st.set_page_config(
    page_title='Hello World',
    page_icon = icon,
    layout = 'centered',
    initial_sidebar_state='auto',
    menu_items={
        'Get Help':'https://www.google.com',
        'Report a Bug': 'https://www.google.com',
        'About': '# Hello World Application'
    }
)

st.sidebar.title('Hello World')
st.write('Welcome')
