import pandas as pd

def generate_signals(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generates trading signals based on moving average crossover.
    """
    df = df.copy()

    df["signal"] = 0
    df.loc[df["ma_20"] > df["ma_50"], "signal"] = 1
    df.loc[df["ma_20"] < df["ma_50"], "signal"] = -1

    return df
