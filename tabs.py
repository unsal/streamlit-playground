import streamlit as st

tab1, tab2 = st.tabs(['Tab1','Tab2'])

tab1.write('This is Tab 1 selected')
tab2.write('This is Tab 2 selected')

with tab1:
    st.radio('Select one:', [1,2])