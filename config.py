from datetime import date, timedelta
from pathlib import Path

WATCHLIST = ["RELIANCE", "HDFCBANK", "SBIN"]

# Capped to GDELT's free ~1-year search limit (tightest constraint of our
# data sources); price data is fetched for the same window to stay aligned.
GDELT_MAX_LOOKBACK_DAYS = 365
BACKTEST_END_DATE = date.today()
BACKTEST_START_DATE = BACKTEST_END_DATE - timedelta(days=GDELT_MAX_LOOKBACK_DAYS)

DATA_DIR = Path(__file__).parent / "data"
HISTORICAL_DIR = DATA_DIR / "historical"
NEWS_DIR = DATA_DIR / "news"

for _dir in (HISTORICAL_DIR, NEWS_DIR):
    _dir.mkdir(parents=True, exist_ok=True)
