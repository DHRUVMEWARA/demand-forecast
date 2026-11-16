"""Load Kaggle Store Sales train.csv into a local SQLite database."""
import sqlite3
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
RAW_CSV = ROOT / "data" / "raw" / "train.csv"
DB_PATH = ROOT / "data" / "store_sales.db"


def main() -> None:
    df = pd.read_csv(RAW_CSV, parse_dates=["date"])
    with sqlite3.connect(DB_PATH) as conn:
        df.to_sql("train", conn, if_exists="replace", index=False, chunksize=50_000)
    print(f"Rows: {len(df):,}")
    print(f"Date range: {df['date'].min().date()} to {df['date'].max().date()}")
    print(f"Saved to {DB_PATH}")


if __name__ == "__main__":
    main()