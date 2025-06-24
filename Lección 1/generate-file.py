# This script generates a CSV, JSON, and Parquet file with sample data.

import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})
df.to_csv('people.csv', index=False)
df.to_json('people.json', orient='records')
df.to_parquet('people.parquet')

if( __name__ == "__main__"):
    print("Files generated successfully: people.csv, people.json, people.parquet")