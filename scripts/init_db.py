"""Initialize the database with sample data."""
from app import models
from app.database import engine, SessionLocal


def main() -> None:
    models.Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    if not db.query(models.Stage).first():
        idea = models.Stage(name="Idea", order=1)
        db.add(idea)
        db.commit()
        db.refresh(idea)
        sample = models.Project(modelo="PE-CT4205", producto="Producto de ejemplo", stage_id=idea.id)
        db.add(sample)
        db.commit()
    db.close()


if __name__ == "__main__":
    main()
