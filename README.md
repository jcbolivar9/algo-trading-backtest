## Project Overview
This project evaluates whether a machine learning–driven trading strategy
can generate risk-adjusted alpha in Bitcoin markets after transaction costs.

## Methodology
- Daily BTC-USD price data
- Technical & volatility feature engineering
- Multi-class XGBoost classifier (buy / hold / sell)
- Execution-aware backtesting with transaction costs

## Results
- Out-of-sample testing (2024–2025)
- Modest positive returns after costs
- Strategy underperformed buy-and-hold in some regimes,
  highlighting market efficiency and regime dependence

## Key Takeaways
- ML signals in crypto are regime-sensitive
- Transaction costs materially impact performance
- Honest backtesting is critical to strategy evaluation

## Future Improvements
- Walk-forward retraining
- Probability-weighted position sizing
- Regime detection
