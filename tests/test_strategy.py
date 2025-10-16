import pandas as pd
import pytest

def test_signals_length(strategy, prices):
    sig = strategy.signals(prices)
    assert len(sig) == len(prices)

def test_signals_constant_series(strategy):
    s = pd.Series([100.0] * 50)
    sig = strategy.signals(s)
    assert (sig == 0).all()

def test_invalid_input(strategy):
    with pytest.raises(TypeError):
        strategy.signals([1, 2, 3])

def test_empty_series(strategy):
    s = pd.Series([], dtype=float)
    sig = strategy.signals(s)
    assert len(sig) == 0
