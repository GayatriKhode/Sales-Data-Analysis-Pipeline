"""
Sales Data Analysis Pipeline
Connects to SQLite, joins orders and customers, aggregates spending,
loads results into pandas, prints the top 10 customers, and exports CSV files.
"""
from pathlib import Path
import sqlite3
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "data" / "sales.db"
OUTPUT_DIR = BASE_DIR / "output"

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if not DB_PATH.exists():
        raise FileNotFoundError(
            f"Database not found: {DB_PATH}. Keep data/sales.db inside the project."
        )

    query = """
        SELECT
            c.customer_id,
            c.customer_name,
            c.city,
            COUNT(o.order_id) AS total_orders,
            ROUND(SUM(o.amount), 2) AS total_spend
        FROM customers AS c
        INNER JOIN orders AS o
            ON c.customer_id = o.customer_id
        GROUP BY c.customer_id, c.customer_name, c.city
        ORDER BY total_spend DESC;
    """

    with sqlite3.connect(DB_PATH) as connection:
        results_df = pd.read_sql_query(query, connection)

    if results_df.empty:
        print("No sales records were found.")
        return

    top10_df = results_df.head(10)
    all_results_path = OUTPUT_DIR / "customer_spending.csv"
    top10_path = OUTPUT_DIR / "top_10_customers.csv"

    results_df.to_csv(all_results_path, index=False)
    top10_df.to_csv(top10_path, index=False)

    print("\n=== Top 10 Customers by Total Spending ===")
    print(top10_df.to_string(index=False))
    print(f"\nAll customer results saved to: {all_results_path}")
    print(f"Top 10 customers saved to: {top10_path}")

if __name__ == "__main__":
    main()
