import pandas as pd
import pytest
from io import StringIO
from backtester.price_loader import load_prices_from_csv
from backtester.strategy import VolatilityBreakoutStrategy
from backtester.broker import Broker
from backtester.engine import Backtester

def test_price_loader_reads_csv(tmp_path):
    # Make a temporary CSV file
    csv_content = "date,close\n2024-01-01,100\n2024-01-02,101\n"
    file_path = tmp_path / "prices.csv"
    file_path.write_text(csv_content)
    prices = load_prices_from_csv(file_path)
    assert isinstance(prices, pd.Series)
    assert len(prices) == 2
    assert prices.iloc[0] == 100
    assert prices.iloc[1] == 101

def test_strategy_invalid_window():
    with pytest.raises(ValueError):
        VolatilityBreakoutStrategy(window=0)

def test_broker_negative_cash():
    with pytest.raises(ValueError):
        Broker(cash=-50)

def test_engine_with_empty_prices(strategy):
    broker = Broker(cash=1000)
    bt = Backtester(strategy, broker)
    eq = bt.run(pd.Series([], dtype=float))
    assert eq == broker.cash
