import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.greeks import call_gamma

import matplotlib.pyplot as plt 

stock_prices = []
gammas = []

for S in range(50, 151):

    gamma = call_gamma(
        S=S,
        K=100,
        T=1,
        r=0.05,
        sigma=0.20
    )

    stock_prices.append(S)
    gammas.append(gamma)

plt.plot(stock_prices, gammas)

plt.title("Call Gamma vs Stock Price")
plt.xlabel("Stock Price")
plt.ylabel("Gamma")

plt.savefig("data/call_gamma.png")

plt.show()