import streamlit
import pandas
streamlit.title("Hey Getting Started")

streamlit.header('DATA APP BUILDERS')

streamlit.text('Fruits List..!!')

# Reading From S3 Bucket
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#streamlit To Display whats there in the Data Frame
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)


# #fILTER
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#STORE THE LIST OF SELECTED FRUITS INTO A SELECTED VARIABLE 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#USE to Access a group of rows and columns by label(s) or a boolean array.
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)



