
import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""

# Simple Stock Price App

Shown are the stock ***closing price*** and ***volume*** of Tesla!

""")

tickerSymbol = 'TSLA'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d',start='2015-01-09',end='2021-01-09')

st.write("""

## Opening  Price

""")
st.line_chart(tickerDf.Open)
st.write("""

## Closing Price

""")
st.line_chart(tickerDf.Close)
st.write("""

## Volume Price

""")
st.line_chart(tickerDf.Volume)
st.write("""

## Highest Price

""")
st.line_chart(tickerDf.High)
st.write("""

## Lowest Price

""")
st.line_chart(tickerDf.Low)