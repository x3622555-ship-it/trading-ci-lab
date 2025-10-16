# Trading CI Lab — Assignment 5

### Description
A minimal daily-bar backtester built to demonstrate software testing and continuous integration for financial engineering.

### Components
- **PriceLoader:** loads price series
- **Strategy:** Volatility Breakout Strategy
- **Broker:** handles buy/sell orders
- **Backtester:** runs daily simulation

### Tests
All modules are tested with pytest.
Coverage target: **≥90%**

### How to Run Locally
```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m coverage run -m pytest -q
python -m coverage report -m
