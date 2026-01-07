# src/data_loader.py

import yfinance as yf
import pandas as pd

def load_price_data(
    ticker: str,
    start_date: str,
    end_date: str
) -> pd.DataFrame:
    df = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        auto_adjust=False,
        progress=False
    )

    # Flatten columns if MultiIndex
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # Handle column naming differences
    if "Adj Close" in df.columns:
        price_col = "Adj Close"
    elif "Close" in df.columns:
        price_col = "Close"
    else:
        raise ValueError("No price column found in downloaded data.")

    df = df[[price_col, "Volume"]]
    df.rename(columns={price_col: "price"}, inplace=True)

    df.dropna(inplace=True)
    return df

