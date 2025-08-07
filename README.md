# Seguimiento

Boilerplate de aplicación full-stack para seguimiento de proyectos.

## Requisitos

- Docker y docker-compose

## Puesta en marcha

```bash
docker compose up --build
```

La aplicación quedará disponible en [http://localhost](http://localhost).
- API FastAPI en `/api` (docs en `/api/docs`)
- Frontend React servido por Vite

## Scripts útiles

Inicializar base de datos con datos de ejemplo:

```bash
docker compose run --rm backend python scripts/init_db.py
```

Importar proyectos desde un XLSX:

```bash
docker compose run --rm backend python scripts/import_excel.py ruta/al/archivo.xlsx
```

## Tests

Backend:

```bash
cd backend && pytest
```

Frontend:

```bash
cd frontend && npm test
```

## Estructura

- `backend/` – API FastAPI.
- `frontend/` – Aplicación React + Vite.
- `scripts/` – utilidades para la base de datos y Excel.
- `nginx/` – configuración de proxy.
- `docker-compose.yml` – orquestación de servicios.
