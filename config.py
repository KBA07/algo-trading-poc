from pathlib import Path

WATCHLIST = ["RELIANCE", "HDFCBANK", "SBIN"]

DATA_DIR = Path(__file__).parent / "data"
HISTORICAL_DIR = DATA_DIR / "historical"
NEWS_DIR = DATA_DIR / "news"

for _dir in (HISTORICAL_DIR, NEWS_DIR):
    _dir.mkdir(parents=True, exist_ok=True)
