import streamlit
import pandas
streamlit.title("Hey Getting Started")

streamlit.header('DATA APP BUILDERS')

streamlit.text('Fruits List..!!')

# Reading From S3 Bucket
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#streamlit To Display whats there in the Data Frame
streamlit.dataframe(my_fruit_list)


