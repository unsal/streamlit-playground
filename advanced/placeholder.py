import streamlit as st
from datetime import datetime

header = st.container()
body = st.container()

with header:
    st.title('Clock Ticking...')
    
with body:    
    clock = st.empty()  # st.empty() is placeholder

while True:
    time = datetime.now().strftime("%H:%M:%S")
    clock.info('**Current time:** %s' % (time))
    if time == '00:56:00':
        clock.empty()
        st.warning('Alarm!!')
        break