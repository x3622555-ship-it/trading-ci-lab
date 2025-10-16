# 🧮 Assignment 5 — Testing & CI in Financial Engineering  
*A minimal daily-bar backtester demonstrating testing discipline and continuous integration.*

---

## 🎯 Learning Objectives
- Design testable components (data loader, strategy, broker, backtester).  
- Write focused unit tests using **pytest**, fixtures, and mocks.  
- Measure and enforce **≥90% coverage**.  
- Implement **Continuous Integration (CI)** using **GitHub Actions**.  

---

## ⚙️ Components Overview

| Module | Description |
|--------|--------------|
| **PriceLoader** | Returns a synthetic or CSV-based `pandas.Series` of prices. |
| **VolatilityBreakoutStrategy** | Generates -1, 0, +1 signals based on rolling volatility breakout. |
| **Broker** | Executes market orders and tracks cash/position. |
| **Backtester** | Runs end-of-day simulation: applies signals, trades, computes equity. |

---

## 🧩 Folder Structure
trading-ci-lab/
│
├── backtester/
│ ├── init.py
│ ├── price_loader.py
│ ├── strategy.py
│ ├── broker.py
│ └── engine.py
│
├── tests/
│ ├── conftest.py
│ ├── test_strategy.py
│ ├── test_broker.py
│ └── test_engine.py
│
├── .github/
│ └── workflows/
│ └── ci.yml
│
├── requirements.txt
├── pyproject.toml
└── README.md


---

## 🧠 Design Notes
- **Determinism:** Tests use synthetic, predictable price data.  
- **No randomness or network calls:** Everything is local and reproducible.  
- **Isolation:** Each component (strategy, broker, backtester) is tested separately.  
- **Speed:** Test suite completes in < 30 seconds.  

---

## 🧪 Running Tests Locally

### 1️⃣ Install dependencies
```bash
python -m pip install -r requirements.txt
