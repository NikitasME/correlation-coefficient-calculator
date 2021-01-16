import pandas
from alpha_vantage.timeseries import TimeSeries
import sys
import random
import numpy as np

key = "D2D2SVTP4TST5MK3"

tickers = [str(sys.argv[1]), str(sys.argv[2])]

time = TimeSeries(key, 'pandas')
data1 = time.get_daily(symbol=tickers[0], outputsize='full')
data2 = time.get_daily(symbol=tickers[1], outputsize='full')

open_prices1 = data1[0]['1. open']
open_prices1 = open_prices1.reindex(index=open_prices1.index[::-1])
open_prices2 = data2[0]['1. open']
open_prices2 = open_prices2.reindex(index=open_prices2.index[::-1])

open_prices1 = open_prices1.pct_change().rolling(50).mean().dropna()
open_prices2 = open_prices2.pct_change().rolling(50).mean().dropna()

r = np.corrcoef(open_prices1, open_prices2)
print("Correlation Coefficient: ", end="")
print(r[0,1])

