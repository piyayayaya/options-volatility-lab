from src.black_scholes import black_scholes_call, black_scholes_put
import matplotlib.pyplot as plt

S = 100
K = 100
T = 1
r = 0.05

volatilities = []
call_prices = []
put_prices = []

for i in range(5, 81):
    sigma = i / 100

    call_price = black_scholes_call(S, K, T, r, sigma)
    put_price = black_scholes_put(S, K, T, r, sigma)

    volatilities.append(sigma)
    call_prices.append(call_price)
    put_prices.append(put_price)

plt.plot(volatilities, call_prices, label="Call Price")
plt.plot(volatilities, put_prices, label="Put Price")

plt.title("Option Price vs Volatility")
plt.xlabel("Volatility")
plt.ylabel("Option Price")
plt.legend()

plt.savefig("data/option_price_vs_volatility.png")
plt.show()