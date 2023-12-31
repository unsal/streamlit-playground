import streamlit as st
from datetime import datetime

st.title('Clock')
clock = st.empty()  # st.empty() is placeholder

while True:
    time = datetime.now().strftime("%H:%M:%S")
    clock.info('**Current time: ** %s' % (time))
    if time == '18:44:50':
        clock.empty()
        st.warning('Alarm!!')
        break