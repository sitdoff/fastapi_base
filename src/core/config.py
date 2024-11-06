from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = True


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class DatabaseConfig(BaseSettings):
    database: str
    user: str
    password: str
    host: str
    port: int
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 5
    max_overflow: int = 10

    @property
    def url(self) -> PostgresDsn:
        return PostgresDsn(
            url=f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        )


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env", "src/.env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig


settings = Settings()  # pyright: ignore
print(settings.db.echo)
