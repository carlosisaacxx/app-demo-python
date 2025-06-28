import pandas as pd
from pathlib import Path

BASE_DIR_CREATE = Path('data/filecreate')
BASE_DIR_CREATE.mkdir(parents=True, exist_ok=True)

def generate_sample_files():
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago'],
    })

    df.to_csv(BASE_DIR_CREATE / 'people.csv', index=False)
    df.to_json(BASE_DIR_CREATE / 'people.json', orient='records')
    df.to_parquet(BASE_DIR_CREATE / 'people.parquet')
    print(f"[OK] Archivos generados en: {BASE_DIR_CREATE}")

if __name__ == '__main__':
    generate_sample_files()