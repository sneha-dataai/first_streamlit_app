import streamlit #as st
import pandas
import snowflake.connector



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
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#New section to display fruityvice api response
import requests

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)


# take the json and normalize - expand the attributes
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# load the table into a dataframe
streamlit.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

#st.markdown('<p class="big-font">Breakfast Menu</p>', unsafe_allow_html=True)
#st.markdown('<p class="small-font">Omega 3 & blueberry Oatmeal</p>', unsafe_allow_html=True)
#st.markdown('<p class="small-font">Kale, Spinach & Rocket Smoothie</p>', unsafe_allow_html=True)
#st.markdown('<p class="small-font">Hard-Boiled Free-Range Egg</p>', unsafe_allow_html=True)
