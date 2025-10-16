import numpy as np
import pandas as pd

class VolatilityBreakoutStrategy:
    """Simple rolling-volatility breakout strategy."""

    def __init__(self, window: int = 20):
        if window < 1:
            raise ValueError("window must be >= 1")
        self.window = window

    def signals(self, prices: pd.Series) -> pd.Series:
        """Return -1, 0, +1 signals based on volatility breakout."""
        if not isinstance(prices, pd.Series):
            raise TypeError("prices must be a pandas Series")
        if prices.empty:
            return pd.Series(dtype=int)

        returns = prices.pct_change()
        rolling_std = returns.rolling(self.window, min_periods=1).std().shift(1)

        sig = pd.Series(0, index=prices.index)
        sig[returns > rolling_std] = 1
        sig[returns < -rolling_std] = -1
        sig = sig.fillna(0)
        return sig
