from implied_vol import implied_volatility_call

market_price = 10.45
S = 100
K = 100
T = 1
r = 0.05

iv = implied_volatility_call(market_price, S, K, T, r)

print("Implied Volatility:", round(iv, 4))
print("Implied Volatility Percentage:", round(iv * 100, 2), "%")
