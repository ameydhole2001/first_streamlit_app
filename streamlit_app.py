import streamlit
import pandas
streamlit.title("Hey Getting Started")

streamlit.header('DATA APP BUILDERS')

streamlit.text('Fruits List..!!')

# Reading From S3 Bucket
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#streamlit To Display whats there in the Data Frame
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)



