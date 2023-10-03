#import yfinance as yf
import pandas as pd

ticker_symbol = input('Please enter the Ticker Symbol the stock you want deatails of \n')

#AAPL is the ticker symbol of the company Apple
# yf.Ticker('<ticker symbol of desired stock>') gets a Ticker object that can used to see other info
#stock = yf.Ticker(ticker_symbol)

# .info returns a Dictionary with all the details od the stock
#stock_info = stock.info

# .history on a Ticker object gives share prices over a period of time, specified by the period attribute
# Here, we are setting period to max. It can be 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y or max
#stock_share_price_data = stock.history(period='max')

#We notice that the Date heading is not in line with the other headings
#This is taken care by using the .reset_index(inplace=True) to Data Frame
# .reset_index can be used with any pandas Data Frame i.e <Data Frame>.reset_index(inplace=True)
#stock_share_price_data.reset_index(inplace=True)
#
##gives country of the company
#print('Country : ')
#print(stock_info['country'])
#print('\n *********************************\n')
#print('\n\n')
#
##gives sector of the company
#print('Sector : ')
#print(stock_info['sector'])
#print('\n *********************************\n')
#print('\n\n')
#
##gives max volume of the company
#max_volume = max(stock_share_price_data['Volume'])
#print('Max Voulume : ')
#print(max_volume)
#print('\n *********************************\n')
#print('\n\n')
#
##gives stock history of the company
#print('Stock History \n *********************************\n')
#print(stock_share_price_data)
#print('\n\n')
#
##gets dividends
#if len(stock.dividends) > 0 :
#    print('Dividends \n *********************************\n')
#    print(stock.dividends)
#else :
#    print('No Dividens given')

# fuction to calculate area of square


