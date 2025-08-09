"""Import projects from an Excel file into the database."""
import argparse
import pandas as pd
from app.database import SessionLocal
from app import models


FIELDS = [
    "grupo",
    "modelo",
    "marca",
    "proveedor",
    "producto",
    "detalles",
]


def import_projects(path: str) -> None:
    df = pd.read_excel(path)
    db = SessionLocal()
    for _, row in df.iterrows():
        data = {field: row.get(field) for field in FIELDS}
        project = models.Project(**data)
        db.add(project)
    db.commit()
    db.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Import projects from XLSX")
    parser.add_argument("path", help="Path to the Excel file")
    args = parser.parse_args()
    import_projects(args.path)
