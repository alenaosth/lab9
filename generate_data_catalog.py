import os
import pandas as pd

OUTPUT_CSV = "data_catalog.csv"
DATAFILE = "output/lab9.csv"

def generate_catalog():
    rows = []
    for root, dirs, files in os.walk("."):
        for f in files:
            if f.startswith(".git"):
                continue

            path = os.path.join(root, f)
            info = {
                "filename": f,
                "path": path,
                "size": os.path.getsize(path),
                "extension": os.path.splitext(f)[1],
                "rows": "",
                "columns": "",
                "description": "Файл проекта"
            }

            # Если это итоговый датасет — анализируем
            if path == DATAFILE:
                df = pd.read_csv(path)
                info["rows"] = df.shape[0]
                info["columns"] = df.shape[1]
                info["description"] = "Итоговый датасет, созданный в lab9.ipynb"

            rows.append(info)

    pd.DataFrame(rows).to_csv(OUTPUT_CSV, index=False, encoding="utf-8")
    print("Каталог создан:", OUTPUT_CSV)

if __name__ == "__main__":
    generate_catalog()
