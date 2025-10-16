import pytest
import numpy as np
import pandas as pd
from backtester.strategy import VolatilityBreakoutStrategy
from backtester.broker import Broker

@pytest.fixture
def prices():
    # Deterministic rising prices
    return pd.Series(np.linspace(100, 120, 200))

@pytest.fixture
def short_prices():
    return pd.Series([100.0, 100.5, 101.0])

@pytest.fixture
def strategy():
    return VolatilityBreakoutStrategy(window=5)

@pytest.fixture
def broker():
    return Broker(cash=1000)
