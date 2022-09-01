import streamlit as st

st.title('My Parents New Healthy Diner')
st.markdown("""
<style>
.big-font {
    font-size:50px !important;
}
.small-font {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)
st.header('Breakfast Menu')
st.text('🥦Omega 3 & blueberry Oatmeal')
st.text('🥬Kale, Spinach & Rocket Smoothie')
st.text('🥚Hard-Boiled Free-Range Egg')
st.header('🍌Bulild your own fruit smoothie')


#st.markdown('<p class="big-font">Breakfast Menu</p>', unsafe_allow_html=True)
#st.markdown('<p class="small-font">Omega 3 & blueberry Oatmeal</p>', unsafe_allow_html=True)
#st.markdown('<p class="small-font">Kale, Spinach & Rocket Smoothie</p>', unsafe_allow_html=True)
#st.markdown('<p class="small-font">Hard-Boiled Free-Range Egg</p>', unsafe_allow_html=True)
