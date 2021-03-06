import datetime

import matplotlib.pyplot as plt
from matplotlib import style
from pandas_datareader import data

style.use('fivethirtyeight') # style the graph

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 8, 22)

df = data.DataReader("XOM", "yahoo", start, end)

print(df.head())

df['High'].plot()
plt.legend()
plt.show()