import os
import pandas as pd
from datetime import datetime

FILES_TO_SCAN = [
    "README.md",
    "lab9.ipynb",
    "generate_data_catalog.py",
    "data/lab9.csv"
]

OUTPUT_CSV = "data_catalog.csv"


def get_file_metadata(filepath):
    """Сбор метаданных по одному файлу"""
    stats = os.stat(filepath)
    size = stats.st_size
    modified = datetime.fromtimestamp(stats.st_mtime)

    file_info = {
        "filename": os.path.basename(filepath),
        "path": filepath,
        "extension": os.path.splitext(filepath)[1],
        "size_bytes": size,
        "modified": modified,
        "rows": None,
        "columns": None,
        "column_names": None,
        "column_types": None,
        "description": "Файл проекта lab9"
    }

    # Если CSV — читаем структуру таблицы
    if file_info["extension"].lower() == ".csv":
        try:
            df = pd.read_csv(filepath)
            file_info["rows"] = df.shape[0]
            file_info["columns"] = df.shape[1]
            file_info["column_names"] = list(df.columns)
            file_info["column_types"] = df.dtypes.astype(str).to_dict()
        except Exception as e:
            print(f"Ошибка чтения {filepath}: {e}")

    return file_info


def generate_catalog():
    """Создание датакаталога только по выбранным файлам"""
    all_files = []

    for filepath in FILES_TO_SCAN:
        if os.path.exists(filepath):
            metadata = get_file_metadata(filepath)
            all_files.append(metadata)
        else:
            print(f"⚠ Файл не найден: {filepath}")

    # Создание CSV-каталога
    df = pd.DataFrame(all_files)
    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8")

    print("\nКаталог данных создан.")
    print(f"Файл каталога: {OUTPUT_CSV}")
    print(f"Найдено файлов: {len(all_files)}")


if __name__ == "__main__":
    generate_catalog()
