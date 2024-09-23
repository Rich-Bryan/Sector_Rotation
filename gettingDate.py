import datetime
import pandas as pd
import pandas_datareader.data as web
import yfinance as yf

start = datetime.datetime(2019, 1, 1)
end = datetime.datetime(2019, 5, 31)
df_500 = yf.download('SPY', start=start, end=end)

print(df_500.tail())

# how to calculate for Daily Return
# Daily Return = (today close - yesterdays close)/yesterday close) * 100

# Calculate the daily return based on the 'Close' prices
df_500['Daily Return'] = df_500['Close'].pct_change() * 100

# Display the last few rows of the DataFrame including the new 'Daily Return' column
print(df_500.head())