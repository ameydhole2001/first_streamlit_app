# import streamlit
# import pandas
# streamlit.title("Hey Getting Started")

# streamlit.header('DATA APP BUILDERS')

# streamlit.text('Fruits List..!!')

# # Reading From S3 Bucket
# my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# my_fruit_list = my_fruit_list.set_index('Fruit')
# #streamlit To Display whats there in the Data Frame
# streamlit.dataframe(my_fruit_list)

# # Let's put a pick list here so they can pick the fruit they want to include 
# # streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))



# # #fILTER
# # streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# #STORE THE LIST OF SELECTED FRUITS INTO A SELECTED VARIABLE 
# fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# #USE to Access a group of rows and columns by label(s) or a boolean array.
# fruits_to_show = my_fruit_list.loc[fruits_selected]
# streamlit.dataframe(fruits_to_show)

# streamlit.header("Fruityvice Fruit Advice!")

# import requests

# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# streamlit.text(fruityvice_response.json())

# # write your own comment -what does the next line do? 
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# # write your own comment - what does this do?
# streamlit.dataframe(fruityvice_normalized)
# import snowflake.connector

# import streamlit
# import pandas
# import requests
# import snowflake.connector
# from urllib.error import URLError
# streamlit.title('My Mom\'s New Healthy Dinner')
# streamlit.header('Breakfast Favourites')
# streamlit.text(':bowl_with_spoon: Ómega 3 & Blueberry Oatmeal')
# streamlit.text(':green_salad: Kale, Spinach & Rocket Smmoothie')
# streamlit.text(':chicken:Hard-Boiled Free-Range Egg')
# streamlit.text(':avocado::bread: Avocado Toast')
# streamlit.header(':banana::mango: Build Your Own Fruit Smoothie :kiwifruit::grapes:')
# #import pandas
# my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# my_fruit_list = my_fruit_list.set_index('Fruit')
# fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
# fruits_to_show = my_fruit_list.loc[fruits_selected]
# streamlit.dataframe(fruits_to_show)
# def get_fruityvice_data(this_fruit_choice):
#   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
#   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#   return fruityvice_normalized
# streamlit.header("Fruityvice Fruit Advice!")
# try:
#   fruit_choice = streamlit.text_input('What fruit would you like information about?')
#   if not fruit_choice:
#     streamlit.error("Please select a fruit to get information.")
#   else:
#     back_from_function = get_fruityvice_data(fruit_choice)
#     streamlit.dataframe(back_from_function)
# streamlit.stop()
import streamlit as st
import pandas as pd
import requests

st.title("My Mom's New Healthy Dinner")
st.header("Breakfast Favourites")
st.text(":bowl_with_spoon: Ómega 3 & Blueberry Oatmeal")
st.text(":green_salad: Kale, Spinach & Rocket Smoothie")
st.text(":chicken: Hard-Boiled Free-Range Egg")
st.text(":avocado::bread: Avocado Toast")

# Load fruit list
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")

# Fruit selection
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), ["Avocado", "Strawberries"])
fruits_to_show = my_fruit_list.loc[fruits_selected]
st.dataframe(fruits_to_show)

# Function to get Fruityvice data
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

st.header("Fruityvice Fruit Advice!")
fruit_choice = st.text_input("What fruit would you like information about?")
if not fruit_choice:
    st.error("Please select a fruit to get information.")
else:
    try:
        back_from_function = get_fruityvice_data(fruit_choice)
        st.dataframe(back_from_function)
    except requests.exceptions.RequestException as e:
        st.error("An error occurred while fetching the data. Please try again later.")

# Allow the end user to add a fruit to the list
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values (%s)", (new_fruit,))
    return "Thanks for adding " + new_fruit

new_fruit = st.text_input("Add a new fruit:")
if st.button("Add Fruit") and new_fruit:
    result = insert_row_snowflake(new_fruit)
    st.success(result)




