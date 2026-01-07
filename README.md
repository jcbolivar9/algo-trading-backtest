📈 Bitcoin Trading Strategy with XGBoost
Overview

This project builds a machine learning–driven trading strategy for Bitcoin (BTC-USD) using XGBoost.
The goal is to predict short-term price direction and generate Buy / Hold / Sell signals, then evaluate the strategy through backtesting.

The model is trained on historical BTC price data and enhanced with technical indicators commonly used in quantitative trading.

🎯 Objectives

-Predict future Bitcoin price movement using supervised learning
-Engineer meaningful technical features
-Generate actionable Buy / Hold / Sell signals
-Backtest the strategy and evaluate performance
-Demonstrate end-to-end ML workflow for a finance + data science portfolio

🧠 Model & Methodology

-Model: XGBoost Regressor
-Target: Forward returns
-Asset: BTC-USD
-Date Range: 2024-01-01 to 2026-01-01

Feature Engineering
The model uses a combination of price-based and momentum indicators:
-Daily Returns
-Rolling Volatility
-Moving Averages (short & long windows)
-RSI (Relative Strength Index)
-MACD
-Lagged returns
-Volume-based features (if available)

These features help the model capture:
-Trend direction
-Momentum shifts
-Market volatility

📊 Trading Signal Logic

Model predictions are converted into trading signals:

Prediction	                            Signal
Positive return above threshold	        Buy
Near zero	                            Hold
Negative return below threshold	        Sell

This transforms raw ML output into interpretable trading actions, bridging the gap between modeling and real-world decision-making.

🔁 Backtesting Results

Total Strategy Return: ~11%

Period: Jan 2024 – Jan 2026

Benchmark: Buy-and-Hold BTC-USD (for comparison)

While returns are modest, the project emphasizes process, robustness, and explainability, not overfitting or unrealistic performance.

🛠️ Tech Stack

Python
pandas, numpy
scikit-learn
xgboost
yfinance
matplotlib / seaborn

📂 Project Structure
├── data/
│   └── btc_price_data.csv
├── notebooks/
│   └── btc_xgboost_strategy.ipynb
├── src/
│   ├── features.py
│   ├── model.py
│   └── backtest.py
├── README.md
└── requirements.txt

🚀 Key Takeaways

-Demonstrates ML applied to financial markets
-Shows strong understanding of:
    Feature engineering
    Model training & evaluation
    Trading signal generation
    Backtesting logic
-Designed for portfolio presentation, not hype

⚠️ Disclaimer

This project is for educational purposes only.
It does not constitute financial advice or a recommendation to trade cryptocurrencies.

👤 Author

José Bolívar
MS in Financial Technologies & Analytics
Aspiring Data Scientist / Financial Analyst