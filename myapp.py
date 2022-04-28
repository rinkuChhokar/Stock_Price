import yfinance as yf

from PIL import Image

import streamlit as st

import pandas as pd

st.title("Simple Stock Price App")
image = Image.open('title.jpg')

st.image(image, caption='Stock Price')



tickerSymbol = st.radio(
	"Choose one of the below FAANG Companies-",
	('Google','Amazon','Facebook','Apple','Netflix')
	)

# get data on this ticker

if tickerSymbol == 'Google':

	st.write(f"""

	Choose Start and End Date of {tickerSymbol} stock price below!

	""")

	tickerData = yf.Ticker("GOOGL")

	d = st.date_input(
     "Start Date-")

	d1 = st.date_input(
     "End Date-")



	# get the historical prices for this ticker

	tickerDf = tickerData.history(period='1d',start=d,end=d1)

	st.subheader("Closing Price")
	st.line_chart(tickerDf.Close)

	st.subheader("Volume Price")
	st.line_chart(tickerDf.Volume)



if tickerSymbol == 'Amazon':

	st.write(f"""

	Choose Start and End Date of {tickerSymbol} stock price below!

	""")

	tickerData = yf.Ticker("AMZN")

	d = st.date_input(
     "Start Date-")

	d1 = st.date_input(
     "End Date-")

	# get the historical prices for this ticker

	tickerDf = tickerData.history(period='1d',start=d,end=d1)

	st.subheader("Closing Price")
	st.line_chart(tickerDf.Close)

	st.subheader("Volume Price")
	st.line_chart(tickerDf.Volume)




if tickerSymbol == 'Facebook':

	st.write(f"""

	Choose Start and End Date of {tickerSymbol} stock price below!

	""")

	tickerData = yf.Ticker("FB")

	d = st.date_input(
     "Start Date-")

	d1 = st.date_input(
     "End Date-")

	# get the historical prices for this ticker

	tickerDf = tickerData.history(period='1d',start=d,end=d1)

	st.subheader("Closing Price")
	st.line_chart(tickerDf.Close)

	st.subheader("Volume Price")
	st.line_chart(tickerDf.Volume)


if tickerSymbol == 'Apple':

	st.write(f"""

	Choose Start and End Date of {tickerSymbol} stock price below!

	""")

	tickerData = yf.Ticker("AAPL")

	d = st.date_input(
     "Start Date-")

	d1 = st.date_input(
     "End Date-")

	# get the historical prices for this ticker

	tickerDf = tickerData.history(period='1d',start=d,end=d1)

	st.subheader("Closing Price")
	st.line_chart(tickerDf.Close)

	st.subheader("Volume Price")
	st.line_chart(tickerDf.Volume)



if tickerSymbol == 'Netflix':

	st.write(f"""

	Choose Start and End Date of {tickerSymbol} stock price below!

	""")

	tickerData = yf.Ticker("NFLX")

	d = st.date_input(
     "Start Date-")

	d1 = st.date_input(
     "End Date-")

	# get the historical prices for this ticker

	tickerDf = tickerData.history(period='1d',start=d,end=d1)

	st.subheader("Closing Price")
	st.line_chart(tickerDf.Close)

	st.subheader("Volume Price")
	st.line_chart(tickerDf.Volume)


