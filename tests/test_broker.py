import pytest

def test_buy_and_sell_updates_cash_and_pos(broker):
    broker.market_order("BUY", 2, 10.0)
    assert broker.position == 2
    assert broker.cash == 1000 - 20
    broker.market_order("SELL", 1, 10.0)
    assert broker.position == 1
    assert broker.cash == 1000 - 10

def test_invalid_orders(broker):
    with pytest.raises(ValueError):
        broker.market_order("BUY", 0, 10)
    with pytest.raises(ValueError):
        broker.market_order("INVALID", 1, 10)
    with pytest.raises(ValueError):
        broker.market_order("BUY", 1, -10)

def test_insufficient_cash(broker):
    with pytest.raises(RuntimeError):
        broker.market_order("BUY", 200, 10)

def test_insufficient_shares(broker):
    with pytest.raises(RuntimeError):
        broker.market_order("SELL", 1, 10)
