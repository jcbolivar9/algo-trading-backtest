import pandas as pd
import numpy as np

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Returns
    df["return"] = df["price"].pct_change()

    # Moving averages
    df["ma_10"] = df["price"].rolling(10).mean()
    df["ma_20"] = df["price"].rolling(20).mean()
    df["ma_50"] = df["price"].rolling(50).mean()

    # Momentum
    df["momentum_10"] = df["price"] / df["price"].shift(10) - 1

    # Volatility
    df["volatility_20"] = df["return"].rolling(20).std()

    # RSI (14)
    delta = df["price"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()
    rs = avg_gain / avg_loss
    df["rsi_14"] = 100 - (100 / (1 + rs))

    df.dropna(inplace=True)
    return df