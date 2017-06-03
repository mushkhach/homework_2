import pandas_datareader.data as web
our_list=["AMZN","TSLA","GOOGL"]
for stock in our_list:
    data=web.DataReader(stock, 'google')
    print(data.head(7))