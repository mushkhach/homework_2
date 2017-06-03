import pandas_datareader.data as web
import matplotlib.pyplot as plt
our_list=["AMZN","TSLA","GOOGL"]
for stock in our_list:
    data=plt.plot(web.DataReader(stock, 'google')["Open"])
    print(plt.show())