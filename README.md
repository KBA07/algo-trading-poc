# algo-trading-poc

Personal proof-of-concept for algorithmic trading on NSE stocks (RELIANCE, HDFCBANK, SBIN),
built and run entirely on local compute before any live capital is involved.

## Goal

Backtest a strategy that combines historical price action with historical news
sentiment, over a trailing 1-year window, to see whether the sentiment signal adds
anything over a price-only baseline.

## Status

This is being built chunk by chunk, each as its own PR into `master`:

1. Scaffold + repo setup *(this PR)*
2. Historical price data fetch (`jugaad-data`)
3. Baseline backtest engine (`Backtesting.py`, SMA crossover)
4. Historical news headline fetch (GDELT, dated)
5. Local sentiment scoring (FinBERT, CPU)
6. Sentiment-gated strategy + baseline comparison

Live execution (Zerodha Kite Connect for orders, Upstox for live ticks) is a later,
separate phase — not part of this simulation POC.

## Setup

```
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

## Layout

- `config.py` — watchlist and data directory paths
- `src/` — reusable modules (data fetch, news fetch, sentiment, strategy)
- `scripts/` — CLI entry points that use `src/`
- `data/` — local cache of fetched price/news data (git-ignored)
