import math
from scipy.stats import norm


def call_delta(S, K, T, r, sigma):

    d1 = (
        math.log(S / K)
        + (r + 0.5 * sigma**2) * T
    ) / (sigma * math.sqrt(T))

    return norm.cdf(d1)


def call_gamma(S, K, T, r, sigma):

    d1 = (
        math.log(S / K)
        + (r + 0.5 * sigma**2) * T
    ) / (sigma * math.sqrt(T))

    return norm.pdf(d1) / (S * sigma * math.sqrt(T))

def call_vega(S, K, T, r, sigma):

    d1 = (
        math.log(S / K)
        + (r + 0.5 * sigma**2) * T
    ) / (sigma * math.sqrt(T))

    return S * norm.pdf(d1) * math.sqrt(T)