import yfinance as yf
import matplotlib.pyplot as plt

spy = yf.download("SPY", period="1y")

spy["Return"] = spy["Close"].pct_change()

spy["Rolling_30D_Vol"] = spy["Return"].rolling(window=30).std()

print(spy[["Close", "Return", "Rolling_30D_Vol"]].tail(10))

plt.plot(spy.index, spy["Rolling_30D_Vol"])

plt.title("SPY 30-Day Rolling Volatility")
plt.xlabel("Date")
plt.ylabel("Volatility")

plt.show()