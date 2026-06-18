import yfinance as yf
import matplotlib.pyplot as plt

spy = yf.Ticker("SPY")

expiration = spy.options[0]
option_chain = spy.option_chain(expiration)

calls = option_chain.calls

current_price = spy.history(period="1d")["Close"].iloc[-1]

near_money_calls = calls[
    (calls["strike"] > current_price - 50)
    & (calls["strike"] < current_price + 50)
]

plt.plot(
    near_money_calls["strike"],
    near_money_calls["impliedVolatility"],
    marker="o"
)

plt.title("SPY Call Implied Volatility by Strike")
plt.xlabel("Strike Price")
plt.ylabel("Implied Volatility")

plt.show()