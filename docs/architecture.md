# Architecture

Bookless follows a modular, API-first architecture designed for embedded scheduling infrastructure.

## Layers

- **API Layer**: FastAPI-based REST endpoints
- **Database Layer**: SQLAlchemy ORM with PostgreSQL (production) and SQLite (development)
- **Core Layer**: Security and shared utilities

## Deployment

- Container-based deployment with Docker
- ARM64-compatible images
- Traefik reverse proxy integration
