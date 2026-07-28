from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from app.config import settings


def _build_database_url(database_url: str) -> str:
    if database_url.startswith("postgresql+psycopg://"):
        return database_url

    if database_url.startswith("postgresql://"):
        return database_url.replace(
            "postgresql://",
            "postgresql+psycopg://",
            1,
        )

    raise ValueError("DATABASE_URL must use PostgreSQL.")


engine: AsyncEngine = create_async_engine(
    _build_database_url(settings.database_url),
    pool_pre_ping=True,
    connect_args={"sslmode": "require"},
)
