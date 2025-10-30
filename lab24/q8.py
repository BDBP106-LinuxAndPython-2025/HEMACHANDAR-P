#!/usr/bin/python3
# (8) Read in the file diabetes.csv, and after obtaining the pandas dataframe, do the following:
# (i) Print all the column names
# (ii) Print the first 10 rows
# (iii) Print the mean of the BloodPressure column values
# (iv) Print the first 4 rows of columns 3,4,5
# (v) Add another column ’NormalizedBP’ using (max-min) normalization to the dataframe
# as: BP[i] -min(BP) / (max(BP) - min(BP)).
# (vi) Write a function categorize_age(age) that returns ”Youth”, ”Adult” or ”Se-
# nior” based on the age brackets (1-18, 19-50, ¿50). Create a new column in the
# dataframe with this function called age category.
import pandas as pd

# (8) Read the CSV file
df = pd.read_csv('diabetes.csv')

# (i) Print all column names
print("Column names:", df.columns.tolist())

# (ii) Print the first 10 rows
print("\nFirst 10 rows:\n", df.head(10))

# (iii) Print the mean of the BloodPressure column
print("\nMean BloodPressure:", df['BloodPressure'].mean())

# (iv) Print the first 4 rows of columns 3, 4, 5 (indexing starts from 0)
print("\nFirst 4 rows of columns 3, 4, 5:\n", df.iloc[:4, 2:5])

# (v) Add 'NormalizedBP' column using min-max normalization
df['NormalizedBP'] = (df['BloodPressure'] - df['BloodPressure'].min()) / \
                     (df['BloodPressure'].max() - df['BloodPressure'].min())
print("\nDataFrame with NormalizedBP:\n", df.head())
