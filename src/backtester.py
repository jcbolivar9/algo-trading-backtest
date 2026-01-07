import pandas as pd

def backtest_strategy(
    df: pd.DataFrame,
    transaction_cost: float = 0.0005
) -> pd.DataFrame:
    """
    Backtests a trading strategy with transaction costs.
    """
    df = df.copy()

    # Position is yesterday's signal
    df["position"] = df["signal"].shift(1)

    # Strategy returns
    df["strategy_return"] = df["position"] * df["return"]

    # Transaction costs when position changes
    df["trade"] = df["position"].diff().abs()
    df["cost"] = df["trade"] * transaction_cost

    df["strategy_return"] = df["strategy_return"] - df["cost"]

    df.dropna(inplace=True)
    return df
