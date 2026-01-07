from src.data_loader import load_price_data
from src.features import add_features
from src.labels import create_labels
from src.ml_strategy import train_xgb_strategy
from src.backtester import backtest_strategy

FEATURES = [
    "ma_10", "ma_20", "ma_50",
    "momentum_10",
    "volatility_20",
    "rsi_14"
]

def main():
    df = load_price_data(
        ticker="BTC-USD",
        start_date="2024-01-01",
        end_date="2025-01-01"
    )

    df = add_features(df)
    df = create_labels(df)
    df, model = train_xgb_strategy(df, FEATURES)
    df = backtest_strategy(df)

    print(df[["signal", "position", "strategy_return"]].tail())
    print(f"\nTotal Return: {(1 + df['strategy_return']).prod() - 1:.2%}")

    buy_hold_return = (df["return"] + 1).prod() - 1
    print(f"Buy & Hold Return: {buy_hold_return:.2%}")

if __name__ == "__main__":
    main()


