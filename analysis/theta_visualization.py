from src.black_scholes import black_scholes_call
import matplotlib.pyplot as plt

times = []
call_prices = []

for days in range(1, 366):
    T = days / 365

    call_price = black_scholes_call(
        S=100,
        K=100,
        T=T,
        r=0.05,
        sigma=0.20
    )

    times.append(days)
    call_prices.append(call_price)

plt.plot(times, call_prices)

plt.title("Call Option Value vs Time to Expiration")
plt.xlabel("Days to Expiration")
plt.ylabel("Call Option Value")

plt.show()