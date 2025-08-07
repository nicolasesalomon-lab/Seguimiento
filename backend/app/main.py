from fastapi import FastAPI
from .database import Base, engine
from .routers import projects, users
from prometheus_fastapi_instrumentator import Instrumentator

# Create tables on startup for demo purposes
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Seguimiento API")

# Routers
app.include_router(projects.router)
app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "Seguimiento API running"}


Instrumentator().instrument(app).expose(app, include_in_schema=False)
