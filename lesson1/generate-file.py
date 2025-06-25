# This script generates a CSV, JSON, and Parquet file with sample data.
import pandas as pd
from pathlib import Path

# Create the output directory if it doesn't exist
output_dir = Path('lesson1/filecreate')
output_dir.mkdir(parents=True, exist_ok=True)

# 📝 Generar DataFrame
df = pd.DataFrame(
    {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago'],
    }
)

# Geberate files in different formats
df.to_csv(output_dir / 'people.csv', index=False)
df.to_json(output_dir / 'people.json', orient='records')
df.to_parquet(output_dir / 'people.parquet')

if __name__ == "__main__":
    print(
        "✅ Se crearon los archivos: people.csv, people.json, people.parquet en la carpeta 'filecreate'."
    )
