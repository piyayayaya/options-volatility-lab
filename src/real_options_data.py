import yfinance as yf

spy = yf.Ticker("SPY")

expiration = spy.options[0]

option_chain = spy.option_chain(expiration)

calls = option_chain.calls
puts = option_chain.puts

important_columns = calls[
    [
        "contractSymbol",
        "strike",
        "lastPrice",
        "bid",
        "ask",
        "volume",
        "openInterest",
        "impliedVolatility",
        "inTheMoney"
    ]
]

print(important_columns.head(20))

current_price = spy.history(period="1d")["Close"].iloc[-1]

current_price = spy.history(period="1d")["Close"].iloc[-1]

atm_calls = calls[
    (calls["strike"] > current_price - 5)
    & (calls["strike"] < current_price + 5)
]

print("Current SPY Price:", current_price)
print(atm_calls[
    [
        "strike",
        "lastPrice",
        "bid",
        "ask",
        "impliedVolatility",
        "volume",
        "openInterest"
    ]
])