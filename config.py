from datetime import date, timedelta
from pathlib import Path

WATCHLIST = ["RELIANCE", "HDFCBANK", "SBIN"]

# GDELT's free DOC 2.0 API (used for historical news, Chunk 4) only supports
# searching back ~1 year from today - that's the tightest constraint of any
# data source we use, so the whole backtest window is capped to match it.
# Historical price data (Chunk 2) is fetched for this same range, even though
# jugaad-data itself could go back much further, so price and sentiment stay
# aligned for the correlation study.
GDELT_MAX_LOOKBACK_DAYS = 365
BACKTEST_END_DATE = date.today()
BACKTEST_START_DATE = BACKTEST_END_DATE - timedelta(days=GDELT_MAX_LOOKBACK_DAYS)

DATA_DIR = Path(__file__).parent / "data"
HISTORICAL_DIR = DATA_DIR / "historical"
NEWS_DIR = DATA_DIR / "news"

for _dir in (HISTORICAL_DIR, NEWS_DIR):
    _dir.mkdir(parents=True, exist_ok=True)
