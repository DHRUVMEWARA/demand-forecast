"""Run every .sql file in sql/ against the SQLite DB and save results as CSV."""
import sqlite3
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DB_PATH = ROOT / "data" / "store_sales.db"   # change if your loader saves elsewhere
SQL_DIR = ROOT / "sql"
OUT_DIR = ROOT / "outputs" / "sql"


def main():
    if not DB_PATH.exists():
        sys.exit(f"DB not found: {DB_PATH} - run the loader first")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DB_PATH) as conn:
        for sql_file in sorted(SQL_DIR.glob("*.sql")):
            df = pd.read_sql_query(sql_file.read_text(), conn)
            out = OUT_DIR / f"{sql_file.stem}.csv"
            df.to_csv(out, index=False)
            print(f"{sql_file.name}: {len(df)} rows -> {out.relative_to(ROOT)}")
            print(df.head(10).to_string(index=False), "\n")


if __name__ == "__main__":
    main()