import streamlit as st

st.title('Hello World')
st.write('This is a simple Streamlit app.')

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")


st.text_input('Please enter your name')



st.title('Hello World')
st.write('This is a simple Streamlit app.')


if st.button('Say hello'):
   st.text('Hello, Streamlit!')


name = st.text_input('Please enter your name:')
if name:
   st.write(f'Hello, {name}!')


if st.file_uploader('Please upload a file:', type=['txt', 'csv']):
   st.write('Thanks for uploading a file!')
