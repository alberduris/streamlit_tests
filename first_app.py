import streamlit as st
import numpy as np
import pandas as pd
import time 

st.title('Showcase app')

# Table
st.write("Here's our fist attempt at using data to create a table:")

df = pd.DataFrame({
	'first_column': [1, 2, 3, 4],
	'second_column': [10, 20, 30, 40]
	})

st.write(df)

# Line Chart
st.write("Line chart")

chart_data = pd.DataFrame(
	np.random.randn(20, 3),
	columns=['a', 'b', 'c']
	)

st.line_chart(chart_data)

# Map data
st.write('Map chart')

map_data = pd.DataFrame(
	np.random.randn(1000, 2) / [50, 50] + [43.35, -3.01],
	columns=['lat', 'lon']
	)
st.map(map_data)

# Checkboxes
st.write('Checkboxes')
if st.checkbox('Show dataframe'):
	chart_data = pd.DataFrame(
		np.random.randn(20,3), 
		columns=['a', 'b', 'c'])
	st.line_chart(chart_data)

# Selectbox
option1 = st.selectbox('Which number do you like best?', df['first_column'], key=1)
'You selected: ', option1


# Lay out the app
option2 = st.sidebar.selectbox(
	'Which number do you like best?', df['first_column'], key=2)
'You selected: ', option2

# Columns and Echo
with st.echo():

	left_column, right_column = st.beta_columns(2)
	pressed = left_column.button('Press me?')
	if pressed:
		right_column.write('Woohoo!')

	expander = st.beta_expander('FAQ')
	expander.write('Here you could put in some really, really long explanations... like lorem ipsum lalalalal foo barr bazzz lalalala loreeeeeeeeeeeem ipsum')

# Spinner
with st.spinner('Wait for it...'):
	time.sleep(5)
	st.success('Done!')

# Progress bar
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
	latest_iteration.text(f'Iteration {i+1}')
	bar.progress(i+1)
	time.sleep(0.1)

"... and now we're done"