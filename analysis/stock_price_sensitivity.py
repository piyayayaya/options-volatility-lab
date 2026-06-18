from src.black_scholes import black_scholes_call
import matplotlib.pyplot as plt

stock_prices = []
call_prices = []

for S in range(50, 151):

    call_price = black_scholes_call(
        S=S,
        K=100,
        T=1,
        r=0.05,
        sigma=0.20
    )

    stock_prices.append(S)
    call_prices.append(call_price)

plt.plot(stock_prices, call_prices)

plt.title("Call Option Value vs Stock Price")
plt.xlabel("Stock Price")
plt.ylabel("Call Option Value")

plt.savefig("data/call_price_vs_stock_price.png")

plt.savefig("data/call_price_vs_stock_price.png")
plt.show()