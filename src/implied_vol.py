from black_scholes import black_scholes_call


def implied_volatility_call(market_price, S, K, T, r):
    low_vol = 0.01
    high_vol = 3.00

    for i in range(100):
        mid_vol = (low_vol + high_vol) / 2

        price = black_scholes_call(S, K, T, r, mid_vol)

        if price < market_price:
            low_vol = mid_vol
        else:
            high_vol = mid_vol

    return mid_vol