import math
import pandas as pd
import tushare as ts
import stockstats as ss
from matplotlib import pyplot as plt
from datetime import datetime

begin = '2019-01-01'
end = '2019-04-01'
code = "000001"

stock = ts.get_hist_data(code, start=begin, end=end)
# stock["date"] = stock.index.values
stock = stock.sort_index(0)
stockStat = ss.StockDataFrame.retype(stock)
# stockStat = stockStat.StockDataFrame.retype(stock)
print(stockStat['kdjk'])
stockStat[['close', 'kdjk', 'kdjd', 'kdjj']].plot(figsize=(20,10), grid=True)
plt.show()

