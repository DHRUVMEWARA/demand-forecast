"""Load Kaggle Store Sales CSVs from data/raw into SQLite (data/store_sales.db)."""
import sqlite3
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "raw"
DB_PATH = ROOT / "data" / "store_sales.db"

TABLES = ["train", "stores", "transactions", "oil", "holidays_events"]


def main():
    with sqlite3.connect(DB_PATH) as conn:
        for name in TABLES:
            csv = RAW / f"{name}.csv"
            if not csv.exists():
                print(f"skip {name}: {csv.name} not found")
                continue
            df = pd.read_csv(csv)
            df.to_sql(name, conn, if_exists="replace", index=False, chunksize=50_000)
            print(f"{name}: {len(df):,} rows loaded")
    print(f"Done -> {DB_PATH}")


if __name__ == "__main__":
    main()