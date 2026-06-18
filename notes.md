# Options Volatility Lab

## Project Overview

The goal of this project was to understand how options derive value from uncertainty and how traders quantify risk using volatility and the Greeks. To accomplish this, I implemented the Black-Scholes option pricing model from scratch, calculated option Greeks, estimated historical volatility from real SPY data, recovered implied volatility from option prices, and compared theoretical model prices to real market prices.

Through a series of visualizations and experiments, I explored how stock price, volatility, and time affect option valuation and developed a deeper understanding of the risks managed by options traders.

---

# Black-Scholes Pricing

## Question

How can a European option be valued using a mathematical model?

## Method

Implemented the Black-Scholes model from scratch in Python using stock price, strike price, time to expiration, risk-free interest rate, and volatility as inputs.

## Observation

The model produced reasonable call and put prices and behaved consistently with financial intuition.

## Interpretation

The Black-Scholes model provides a theoretical estimate of option value by modeling future stock price uncertainty.

## Key Insight

Option prices depend primarily on:

* Stock price
* Strike price
* Volatility
* Time to expiration
* Interest rate

---

# Option Price vs Volatility

## Question

How does volatility affect option prices?

## Observation

As volatility increased, both call and put prices increased.

## Interpretation

Higher volatility increases the probability of large future stock price movements. Since option buyers have limited downside risk but potentially large upside gains, additional uncertainty increases option value.

## Trading Insight

Volatility itself has value. Options become more expensive when traders expect larger future price movements.

---

# Call Option Value vs Stock Price

## Question

How does stock price affect call option value?

## Observation

Call option value increased as stock price increased.

The relationship was nonlinear and convex.

## Interpretation

As the stock approaches and exceeds the strike price, the option becomes increasingly valuable.

## Trading Insight

Call options have asymmetric payoffs. The maximum loss is limited to the premium paid, while gains can continue increasing as the stock rises.

---

# Delta

## Question

How sensitive is option value to stock price movements?

## Observation

Delta ranged from approximately 0 to 1.

Examples:

* Stock Price = 50 → Delta ≈ 0
* Stock Price = 100 → Delta ≈ 0.60
* Stock Price = 150 → Delta ≈ 0.99

## Interpretation

Deep out-of-the-money calls have very low sensitivity to stock price changes, while deep in-the-money calls behave similarly to owning stock.

## Trading Insight

Delta measures directional exposure.

A delta of 0.60 means the option price is expected to increase by approximately $0.60 for every $1 increase in the underlying stock price.

---

# Gamma

## Question

How quickly does delta change?

## Observation

Gamma reached its highest values near the strike price.

## Interpretation

Delta changes most rapidly when the stock price is near the strike because the probability of finishing in-the-money is most sensitive to small stock movements.

## Trading Insight

At-the-money options carry the greatest gamma risk because small stock movements can significantly change directional exposure.

---

# Vega

## Question

How sensitive is option value to volatility?

## Observation

Vega reached its highest values near the strike price.

## Interpretation

Volatility has the greatest impact when the option is near the boundary between finishing in-the-money and out-of-the-money.

## Trading Insight

At-the-money options are most sensitive to changes in market uncertainty.

Because of this, volatility traders often focus heavily on at-the-money contracts.

---

# Historical Volatility

## Question

How volatile was SPY over the previous year?

## Method

Downloaded one year of SPY price data using yfinance.

Calculated daily returns and estimated annualized volatility using:

Annualized Volatility = Daily Standard Deviation × sqrt(252)

## Result

Annualized Volatility ≈ 12.28%

## Interpretation

Recent realized volatility in SPY was lower than the 20% volatility assumption used in earlier Black-Scholes examples.

## Trading Insight

Historical volatility describes what actually happened in the past, while implied volatility reflects what traders expect to happen in the future.

---

# Historical vs Assumed Volatility

## Question

How does volatility affect theoretical option value?

## Results

Using Historical Volatility (12.28%):

Call Price = $7.61

Using Assumed Volatility (20%):

Call Price = $10.45

Difference = $2.84

## Interpretation

Option prices are highly sensitive to volatility assumptions.

## Trading Insight

Small changes in volatility can produce significant changes in option valuation. This explains why volatility forecasting is a critical component of options trading.

---

# Theta and Time to Expiration

## Question

How does time affect option value?

## Observation

Option value increased as time to expiration increased.

The relationship was increasing and concave downward.

## Interpretation

Additional time increases the probability of favorable outcomes.

However, the value gained from each additional day becomes smaller as expiration moves further away.

## Trading Insight

Time is valuable for option buyers.

As expiration approaches, options experience time decay, commonly referred to as Theta.

---

# Market Price vs Model Price

## Question

Can Black-Scholes approximate real market prices?

## Method

Collected real SPY option chain data using yfinance.

Selected an at-the-money call option and used its implied volatility as an input to the Black-Scholes model.

## Results

Market Price = $3.48

Black-Scholes Price = $3.66

Difference = $0.18

## Interpretation

The theoretical model produced a price that was very close to the observed market price.

## Trading Insight

Differences between model and market prices can arise due to bid-ask spreads, dividends, timing differences, interest rate assumptions, and market microstructure effects.

---

# Volatility Smile

## Question

Does implied volatility remain constant across strikes?

## Observation

Implied volatility varied significantly across strike prices.

Rather than forming a flat line, the graph produced a U-shaped pattern known as a volatility smile.

## Interpretation

The Black-Scholes model assumes a single volatility for all strikes, but real markets assign different implied volatilities to different contracts.

## Trading Insight

Options far from the current stock price derive most of their value from the possibility of unusually large price movements.

Because of this, traders are often willing to pay a volatility premium for these contracts, resulting in higher implied volatility.

---

# Key Lessons Learned

1. Volatility is one of the most important drivers of option prices.

2. Option prices increase with both volatility and time to expiration.

3. Delta, Gamma, Vega, and Theta each measure different dimensions of risk.

4. At-the-money options typically exhibit the highest Gamma and Vega.

5. Historical volatility and implied volatility describe different concepts.

6. Black-Scholes provides a useful approximation of market prices but cannot fully capture real-world option markets.

7. Real markets exhibit volatility smiles, demonstrating that volatility is not constant across strikes.

8. Building financial models from scratch provides a much deeper understanding than relying solely on pre-built libraries.
