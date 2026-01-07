from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    ENV: str = "development"

    SQLITE_PATH: str = "./dev.db"
    POSTGRES_URL: str | None = None

    @property
    def database_url(self) -> str:
        if self.ENV == "production":
            if not self.POSTGRES_URL:
                raise ValueError("POSTGRES_URL is required in production")
            return self.POSTGRES_URL
        return f"sqlite:///{self.SQLITE_PATH}"

    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    return Settings()
