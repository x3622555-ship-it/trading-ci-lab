import pandas as pd

class Backtester:
    """End-of-day backtesting engine."""

    def __init__(self, strategy, broker):
        self.strategy = strategy
        self.broker = broker

    def run(self, prices: pd.Series) -> float:
        if prices.empty:
            return self.broker.cash

        signals = self.strategy.signals(prices)

        for i in range(1, len(prices)):
            signal = signals.iloc[i - 1]
            price = float(prices.iloc[i])
            if signal == 1:
                self.broker.market_order("BUY", 1, price)
            elif signal == -1:
                self.broker.market_order("SELL", 1, price)

        final_price = float(prices.iloc[-1])
        equity = self.broker.cash + self.broker.position * final_price
        return float(equity)
