import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title('Covid-19 explorer')

# Fetch data
DATE_COLUMN = 'date'
INFECTIONS_COLUMN = 'confirmed'
DATA_URL = ('data/covid-19-all.csv')

@st.cache
def load_data(nrows):
	data = pd.read_csv(DATA_URL, nrows=nrows)
	lowercase = lambda x: str(x).lower()
	data.rename(lowercase, axis='columns', inplace=True)
	data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
	data['latitude'] = pd.to_numeric(data['latitude'])
	data['longitude'] = pd.to_numeric(data['longitude'])
	data.dropna(axis=0, subset=['latitude', 'longitude'], inplace=True)
	aggregated_infections = data.groupby(DATE_COLUMN)[INFECTIONS_COLUMN].count().to_frame()

	return data, aggregated_infections

data_load_state = st.text('Loading data...')

data, aggregated_infections = load_data(None)

data_load_state.text('Done! (using st.cache)')

# Inspect raw data
if st.checkbox('Show raw data'):
	st.subheader('Raw data')
	st.dataframe(data.head(100))

# Draw a histogram
st.subheader('Number of infections by month')
infections_per_month = aggregated_infections.resample('M').sum()
st.bar_chart(infections_per_month)

# Plot data on a map
st.subheader('Map of all infections')
month_to_filter = st.slider('month of 2020', 1, 12, 1)
filtered_data = data[data[DATE_COLUMN].dt.month == month_to_filter]
st.subheader(f'Map of all infections at {month_to_filter}/2020')
st.map(filtered_data)


