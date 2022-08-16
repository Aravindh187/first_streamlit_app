import streamlit

streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

import pandas as pd
my_fruit_list = pd.read_csv('fruit_macros.txt')
streamlit.DataFrame(my_fruit_list)
