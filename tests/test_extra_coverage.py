import pandas as pd
import pytest
from backtester.broker import Broker
from backtester.strategy import VolatilityBreakoutStrategy
from backtester.price_loader import load_prices_from_csv
from io import StringIO

def test_broker_negative_cash():
    with pytest.raises(ValueError):
        Broker(cash=-100)

def test_strategy_invalid_window():
    with pytest.raises(ValueError):
        VolatilityBreakoutStrategy(window=0)

def test_engine_empty(prices, strategy):
    from backtester.engine import Backtester
    broker = Broker(cash=1000)
    bt = Backtester(strategy, broker)
    eq = bt.run(pd.Series([], dtype=float))
    assert eq == 1000

def test_price_loader_reads_csv(tmp_path):
    # Create a dummy CSV
    csv_content = "date,close\n2024-01-01,100\n2024-01-02,101\n"
    fpath = tmp_path / "prices.csv"
    fpath.write_text(csv_content)
    series = load_prices_from_csv(fpath)
    assert isinstance(series, pd.Series)
    assert series.iloc[0] == 100
    assert series.iloc[1] == 101
