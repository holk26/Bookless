# Architectural Decisions

## ADR-001: FastAPI as Web Framework

**Status**: Accepted

**Context**: Need a modern, performant Python web framework for REST APIs.

**Decision**: Use FastAPI for automatic OpenAPI documentation, type validation, and async support.

## ADR-002: SQLAlchemy 2.0

**Status**: Accepted

**Context**: Need ORM with strong typing and migration support.

**Decision**: Use SQLAlchemy 2.0+ with Alembic for database management.

## ADR-003: Dual Database Strategy

**Status**: Accepted

**Context**: Development should be simple; production should be scalable.

**Decision**: SQLite for local development, PostgreSQL for production.
