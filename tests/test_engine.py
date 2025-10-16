import pytest
import pandas as pd
from unittest.mock import MagicMock
from backtester.engine import Backtester
from backtester.broker import Broker

def test_engine_runs_and_returns_equity(prices, strategy):
    rich_broker = Broker(cash=1_000_000)  # plenty of cash to avoid RuntimeError
    bt = Backtester(strategy, rich_broker)
    eq = bt.run(prices)
    assert isinstance(eq, float)
    assert eq > 0


def test_engine_empty_series(broker, strategy):
    bt = Backtester(strategy, broker)
    empty_prices = pd.Series([], dtype=float)
    eq = bt.run(empty_prices)
    assert eq == broker.cash

def test_engine_tminus1_logic(prices, broker):
    fake_strategy = MagicMock()
    sig = pd.Series(0, index=prices.index)
    sig.iloc[9] = 1
    fake_strategy.signals.return_value = sig
    bt = Backtester(fake_strategy, broker)
    eq = bt.run(prices)
    assert broker.position >= 1
    assert eq > 0

def test_engine_broker_error(prices):
    fake_strategy = MagicMock()
    sig = pd.Series(1, index=prices.index)
    fake_strategy.signals.return_value = sig
    broker = Broker(cash=0)
    bt = Backtester(fake_strategy, broker)
    with pytest.raises(RuntimeError):
        bt.run(prices)
