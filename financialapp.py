import yfinance as yf
import streamlit as st


st.write("""
# Financial App

""")

stock = 'AMZN'

get_stock_data = yf.Ticker(stock)

ticket_df = get_stock_data.history(period='1d', start='2021-1-02', end='2021-12-12')

st.line_chart(ticket_df.Close)
st.line_chart(ticket_df.Volume)

