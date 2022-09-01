import streamlit as st

streamlit.title('My Parents New Healthy Diner')
streamlit.markdown("""
<style>
.big-font {
    font-size:50px !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="big-font">Breakfast Menu</p>', unsafe_allow_html=True)
