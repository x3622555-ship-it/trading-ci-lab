import pandas as pd

def load_prices_from_csv(path: str) -> pd.Series:
    """
    Loads closing prices from a CSV file with a 'close' column.
    Used only for demonstration, not in tests.
    """
    df = pd.read_csv(path, index_col=0, parse_dates=True)
    return df["close"].copy()
