import streamlit as st

st.title('Page 7')
st.sidebar.markdown('Click Page 7')

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)