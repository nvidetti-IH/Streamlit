import streamlit

streamlit.header('streamlit.button')

if streamlit.button('Say hello'):
    streamlit.write('Why hello there')
else:
    streamlit.write('Goodbye')