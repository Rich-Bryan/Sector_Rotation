import datetime
import pandas as pd
import yfinance as yf

start = datetime.datetime(2004, 1, 1)
end = datetime.datetime(2024, 5, 31)
df_500 = yf.download('SPY', start=start, end=end)

print(df_500.tail()) 

# how to calculate for Daily Return
# Daily Return = (today close - yesterdays close)/yesterday close) * 100

# Calculate the daily return based on the 'Close' prices
df_500['Daily_Return'] = df_500['Close'].pct_change() * 100

# Display the last few rows of the DataFrame including the new 'Daily Return' column
print(df_500.head())


#create a csv file to store the stock data 
df_500.to_csv('stock_data/SPY_data.csv')

#read CSV file
# spy = pd.read_csv('stock_data/SPY_data.csv')
# spy.head()