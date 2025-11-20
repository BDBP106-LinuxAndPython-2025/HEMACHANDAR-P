# use_csv_processor.py
import q1 as cp

# Load Titanic CSV file
df = cp.load_csv("titanic.csv")

if df is not None:
    print(" Total Columns:", cp.total_columns(df))
    print(" Total Rows:", cp.total_rows(df))

    df_filled = cp.fill_missing_with_zero(df)
    print("\n Missing values filled with zero. First 5 rows:")
    print(df_filled.head())
