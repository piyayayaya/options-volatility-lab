# Options Volatility Lab

## Overview

This project explores option pricing, volatility, and risk management using Python.

The project implements the Black-Scholes model from scratch, calculates option Greeks, estimates historical volatility from real market data, and compares theoretical option values to actual SPY option prices.

## Features

* Black-Scholes call and put pricing
* Delta calculation and visualization
* Gamma calculation and visualization
* Vega calculation and visualization
* Historical volatility estimation using SPY data
* Rolling volatility analysis
* Implied volatility solver
* Market vs model price comparison
* Volatility smile visualization

## Technologies Used

* Python
* NumPy
* SciPy
* Pandas
* Matplotlib
* yfinance

## Key Findings

* Option values increase as volatility increases.
* Longer expiration dates generally increase option value.
* Delta ranges between 0 and 1 for call options.
* Gamma and Vega are highest near the strike price.
* Historical volatility and implied volatility can differ substantially.
* Black-Scholes produced option prices close to observed market prices.
* Real option markets exhibit a volatility smile rather than constant volatility.

## Future Improvements

* Add Theta and Rho visualizations
* Build a volatility surface
* Create an interactive dashboard
* Backtest simple options trading strategies
* Explore stochastic volatility models

## Author

Piya Tewari
University of Pennsylvania
Mathematics Major, Statistics Minor
