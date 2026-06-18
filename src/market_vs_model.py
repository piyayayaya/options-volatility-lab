from black_scholes import black_scholes_call

S = 741.75
K = 742

T = 3 / 365

r = 0.05

sigma = 0.135385

model_price = black_scholes_call(
    S,
    K,
    T,
    r,
    sigma
)

print("Black-Scholes Price:", round(model_price, 2))
print("Market Price:", 3.48)