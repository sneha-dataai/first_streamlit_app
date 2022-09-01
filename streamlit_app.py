import streamlit #as st
import pandas
import requests
import snowflake.connector
from urllib.error import URLError



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

#create function
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    # take the json and normalize - expand the attributes
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
        
        

#New section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:    
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information.")
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        # load the table into a dataframe
        streamlit.dataframe(back_from_function)       
except URLError as e:
    streamlit.error()
        
streamlit.write('The user entered ', fruit_choice)



#streamlit.stop()

streamlit.header("The fruit load list contains:")
#snowflake-related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * from fruit_load_list")
        my_data_row = my_cur.fetchall()
        
#Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)
    #my_cur = my_cnx.cursor()




#streamlit.dataframe(my_data_row)

fruit_add = streamlit.text_input('What fruit would you like to add?')
#streamlit.write(fruit_add)
streamlit.text('Thanks for adding '+ fruit_add)

my_cur.execute("insert into fruit_load_list values ('from streamlit')");

#st.markdown('<p class="big-font">Breakfast Menu</p>', unsafe_allow_html=True)
#st.markdown('<p class="small-font">Omega 3 & blueberry Oatmeal</p>', unsafe_allow_html=True)
#st.markdown('<p class="small-font">Kale, Spinach & Rocket Smoothie</p>', unsafe_allow_html=True)
#st.markdown('<p class="small-font">Hard-Boiled Free-Range Egg</p>', unsafe_allow_html=True)
