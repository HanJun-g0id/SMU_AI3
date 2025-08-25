import streamlit as st

st.sidebar.markdown('Click Page 1')
st.sidebar.markdown("Sid Menu")
st.sidebar.button('Click')
st.sidebar.radio("성별",["여자","남자"])

st.title('Page 1')
st.markdown("Markdown")
st.header('Header')
st.subheader('SubHeader')
st.caption('Caption')
st.code("""
        def func():
            print("OK")
        def func2():
            print("OK2")
""",language='python')