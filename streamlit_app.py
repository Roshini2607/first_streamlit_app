import streamlit

streamlit.title('My Mom's New Healthy Diner')


streamlit.title('Breakfast favorites')
streamlit.text('๐Omega 3 & Blueberry Oatmeal')
streamlit.text('๐ฅฌKale,Spinach & Rocket Smoothie')
streamlit.text('๐Hard-Boiled Free-Range Egg')
streamlit.text('๐ฅ๐ Avocado Toast')
streamlit.header('๐๐ฅญ Build Your Own Fruit Smoothie ๐ฅ๐')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
