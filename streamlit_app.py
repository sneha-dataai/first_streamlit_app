import streamlit #as st
import pandas

streamlit.title('My Parents New Healthy Diner')
streamlit.markdown("""
<style>
.big-font {
    font-size:50px !important;
}
.small-font {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)
streamlit.header('Breakfast Menu')
streamlit.text('🥦Omega 3 & blueberry Oatmeal')
streamlit.text('🥬Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚Hard-Boiled Free-Range Egg')
streamlit.header('🍌Bulild your own fruit smoothie')




my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)


#st.markdown('<p class="big-font">Breakfast Menu</p>', unsafe_allow_html=True)
#st.markdown('<p class="small-font">Omega 3 & blueberry Oatmeal</p>', unsafe_allow_html=True)
#st.markdown('<p class="small-font">Kale, Spinach & Rocket Smoothie</p>', unsafe_allow_html=True)
#st.markdown('<p class="small-font">Hard-Boiled Free-Range Egg</p>', unsafe_allow_html=True)
