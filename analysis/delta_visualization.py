from src.greeks import call_delta
import matplotlib.pyplot as plt

stock_prices = []
deltas = []

for S in range(50, 151):

    delta = call_delta(
        S=S,
        K=100,
        T=1,
        r=0.05,
        sigma=0.20
    )

    stock_prices.append(S)
    deltas.append(delta)

plt.plot(stock_prices, deltas)

plt.title("Call Delta vs Stock Price")
plt.xlabel("Stock Price")
plt.ylabel("Delta")

plt.savefig("data/call_delta.png")

plt.show()