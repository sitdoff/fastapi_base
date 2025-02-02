# В этом файле создаются конфигурации для различных частей приложения.

from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunConfig(BaseModel):
    """
    Настроки uvicorn при запуске.
    """

    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = True


class ApiV1Prefix(BaseModel):
    """
    Настройки для конкретной версии api.
    """

    prefix: str = "/v1"
    users: str = "/users"


class ApiPrefix(BaseModel):
    """
    Общие настройки api.
    """

    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()


class DatabaseConfig(BaseSettings):
    """
    Настройки базы данных.
    """

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
        """
        Свойство возвращает адрес для подключения к базе данных.
        """
        return PostgresDsn(
            url=f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        )

    # Конвенция имён для миграций.
    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class Settings(BaseSettings):
    """
    Общий файл настроек.
    """

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
