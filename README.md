# Sales Data Analysis Pipeline

## Aim
To build an end-to-end data pipeline that queries sales data from SQLite, analyzes it using pandas, and exports the results to CSV files.

## Project features
- Connects to a SQLite database using Python's built-in `sqlite3` module.
- Joins the `orders` and `customers` tables.
- Calculates each customer's total spending and number of orders.
- Loads query results into a pandas DataFrame.
- Displays the top 10 customers by total spending.
- Exports all customer summaries and the top 10 list to CSV files.

## Folder structure
```text
Sales_Data_Analysis_Pipeline/
├── data/
│   └── sales.db
├── output/
├── sales_analysis.py
├── requirements.txt
└── README.md
```

## Requirements
- Python 3.9 or newer
- pandas

## How to run in VS Code
1. Extract the ZIP file.
2. Open the `Sales_Data_Analysis_Pipeline` folder in VS Code.
3. Open Terminal → New Terminal.
4. Install the required library:
   ```bash
   python -m pip install -r requirements.txt
   ```
5. Run the program:
   ```bash
   python sales_analysis.py
   ```
6. Check the `output` folder. It will contain:
   - `customer_spending.csv`
   - `top_10_customers.csv`

If the `python` command is not recognized on Windows, try `py` instead.

## Database tables
- `customers`: customer ID, customer name, and city.
- `orders`: order ID, customer ID, order date, and order amount.

The included database contains sample data for practice and demonstration.

## Result
The program successfully joins customer and order data, calculates total spending per customer, displays the top 10 customers, and saves the analysis results as CSV files.
