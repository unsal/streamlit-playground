import streamlit as st

from page1 import func_page1
from page2 import func_page2

def main_page():
    st.info("Main Page")

header = st.container()
sidebar = st.container()
body = st.container()

with header:
    st.title("Page Calling")
    
with sidebar:
    page_selection = st.sidebar.selectbox('Please select a page',['Main Page','Page1','Page2'])
    
with body:
    pages = {
        'Main Page': main_page,
        'Page1': func_page1,
        'Page2': func_page2
    }
    
    pages[page_selection]()
    

     

