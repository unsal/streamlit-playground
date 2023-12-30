import streamlit as st

st.title('Form Application')

with st.form('feedback_form'):
    st.header('Feedback Form')
    
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input('Please enter your name')
        rating = st.slider('Pleaase rate this app', 0, 10, 20)
        
    with col2:
        birth_date = st.date_input('Please enter your date of birth')
        recommend = st.radio('Would you recommend this app?', ('Yes', 'No'))
        
    submit_button = st.form_submit_button('Submit')
    
    if submit_button:
        st.write('**Name:**',name, '**Date of Birth:**',birth_date, '**Rating:**', rating, '**Would Recommend?',recommend )
