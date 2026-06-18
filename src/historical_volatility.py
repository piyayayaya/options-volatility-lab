import yfinance as yf

spy = yf.download("SPY", period="1y")

spy["Return"] = spy["Close"].pct_change()

daily_volatility = spy["Return"].std()

annual_volatility = daily_volatility * (252 ** 0.5)

print("Daily Volatility:", daily_volatility)
print("Annual Volatility:", annual_volatility)