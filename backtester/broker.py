class Broker:
    """Simulated broker with cash and position."""

    def __init__(self, cash: float = 1_000_000):
        if cash < 0:
            raise ValueError("Initial cash cannot be negative.")
        self.cash = float(cash)
        self.position = 0

    def market_order(self, side: str, qty: int, price: float):
        """Execute market order and update cash/position."""
        if side not in {"BUY", "SELL"}:
            raise ValueError("side must be 'BUY' or 'SELL'")
        if not isinstance(qty, int) or qty <= 0:
            raise ValueError("qty must be a positive integer")
        if price <= 0:
            raise ValueError("price must be positive")

        cost = qty * price

        if side == "BUY":
            if self.cash < cost:
                raise RuntimeError("Insufficient cash")
            self.cash -= cost
            self.position += qty
        else:  # SELL
            if self.position < qty:
                raise RuntimeError("Insufficient shares")
            self.cash += cost
            self.position -= qty
