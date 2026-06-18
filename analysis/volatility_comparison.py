from src.black_scholes import black_scholes_call

S = 100
K = 100
T = 1
r = 0.05

historical_vol = 0.1228
assumed_vol = 0.20

historical_price = black_scholes_call(
    S, K, T, r, historical_vol
)

assumed_price = black_scholes_call(
    S, K, T, r, assumed_vol
)

print("Using Historical Volatility (12.28%)")
print("Call Price:", round(historical_price, 2))

print()

print("Using Assumed Volatility (20%)")
print("Call Price:", round(assumed_price, 2))