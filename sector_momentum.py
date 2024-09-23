import yfinance as yf
import pandas as pd

# Define the sectors using representative ETFs
sectors = ['XLY', 'XLP', 'XLE', 'XLF', 'XLV', 'XLI', 'XLRE', 'XLK', 'XLC']

# Fetch historical data
data = yf.download(sectors, start='2022-01-01', end='2023-01-01')['Adj Close']
print(data)

# Compute momentum as rate of change over a defined period (e.g., 90 trading days)
momentum = data.pct_change(90).mean(axis=1)

# Determine the sector with the highest momentum
top_sector = momentum.idxmax()

# Output the top-performing sector
print(f'The sector with the highest momentum is: {top_sector}')