import numpy as np
from scipy.stats import norm


# Black Scholes Model where:
# S = Current Stock Price, K = Option Strike Price, sigma = volatility of the stock, r = Risk Free interest rate, T = Time remaining until stock expiration
def black_scholes(S, K, sigma, r, T):

    if S <= 0 or K <= 0 or T <= 0:
        raise ValueError("Stock Price (S), Strike Price (K) and Time to expiration (T) must be positive\n Please check your inputs")


    d1 = np.log(S/K) + (r + (sigma**2 / 2) * T) / sigma * np.sqrt(T)
    d2 = d1 - (sigma * np.sqrt(T))
    C = S * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)
    return C

