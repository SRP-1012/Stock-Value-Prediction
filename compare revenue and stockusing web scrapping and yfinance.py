import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#method to make a graph with the given stock data
def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data.Date, infer_datetime_format=True), y=stock_data.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data.Date, infer_datetime_format=True), y=revenue_data.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()

#extract Tesla stock price data using yfinance
tesla = yf.Ticker('TSLA')
tesla_data = tesla.history(period='max')
tesla_data.reset_index(inplace=True)

print(tesla_data)

print('\n\n\n')

#extract Tesla revenue details by web scrapping
html_data = requests.get('https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue').text
soup1 = BeautifulSoup(html_data)
tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for row in soup1.find_all('tbody')[1].find_all('tr'):
    col = row.find_all("td")
    date =col[0].text
    rev =str(col[1].text)[1:].replace(',','')
    tesla_revenue = tesla_revenue.append({"Date":date, "Revenue":rev}, ignore_index=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue']!='']
tesla_revenue = tesla_revenue[tesla_revenue['Revenue']!='NaN']
print(tesla_revenue)

make_graph(tesla_data, tesla_revenue, 'Tesla')
