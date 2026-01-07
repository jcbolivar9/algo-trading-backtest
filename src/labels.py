import pandas as pd

def create_labels(
        df: pd.DataFrame,
        horizon: int = 5,
        threshold: float = 0.02
    ) -> pd.DataFrame:
    """
    Creates labels for price movement over a specified horizon.
    Labels:
        1 : buy signal - Price increases by more than threshold
        -1: sell signal - Price decreases by more than threshold
        0 : hold signal - Price change within threshold
    """
    df = df.copy()

    future_return = df["price"].shift(-horizon) / df["price"] - 1

    df["label"] = 0
    df.loc[future_return > threshold, "label"] = 1
    df.loc[future_return < -threshold, "label"] = -1

    df.dropna(inplace=True)
    return df