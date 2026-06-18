import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.greeks import call_vega
import matplotlib.pyplot as plt

stock_prices = []
vegas = []

for S in range(50, 151):

    vega = call_vega(
        S=S,
        K=100,
        T=1,
        r=0.05,
        sigma=0.20
    )

    stock_prices.append(S)
    vegas.append(vega)

plt.plot(stock_prices, vegas)

plt.title("Call Vega vs Stock Price")
plt.xlabel("Stock Price")
plt.ylabel("Vega")

plt.savefig("data/call_vega.png")

plt.show()