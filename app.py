import streamlit as st

st.header('st.button')

if st.button('Say hello', help='This is the help string'):
     st.write('Why hello there')
else:
     st.write('Goodbye')

st.button('Primary', type='primary')
st.button('Secondary', type='secondary')
st.button('On click', key='on_click', on_click=lambda: st.write('Clicked!'))
