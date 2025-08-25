import streamlit as st

st.title('Page 6')
st.sidebar.markdown('Click Page 6')

n1 = st.number_input("First number")
n2 = st.number_input("Second number")
if st.button("Calculate"):
    st.write("Sum =", n1 + n2)