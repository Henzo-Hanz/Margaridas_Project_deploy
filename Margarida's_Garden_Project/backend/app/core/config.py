"""Configurações da aplicação com Pydantic Settings."""
from pathlib import Path
from typing import List

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configurações via variáveis de ambiente."""

    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).resolve().parent.parent.parent.parent / ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Diretório base (computado)
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent.parent

    # Banco de dados
    DATABASE_URL: str = ""

    # Segurança - JWT
    SECRET_KEY: str = "margarida-garden-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 horas

    # Usuário padrão
    DEFAULT_USER_NAME: str = "Margarida"
    DEFAULT_USER_EMAIL: str = "margarida@garden.local"
    DEFAULT_USER_PASSWORD: str = "garden123"

    # CORS - origens permitidas
    CORS_ORIGINS: str = "http://localhost:3000,http://localhost:5173,http://127.0.0.1:5173"

    # Ambiente
    ENVIRONMENT: str = "development"

    @field_validator("DATABASE_URL", mode="before")
    @classmethod
    def set_default_database_url(cls, v: str) -> str:
        """Define DATABASE_URL padrão se vazio."""
        if v:
            return v
        base = Path(__file__).resolve().parent.parent.parent.parent
        db_path = (base / "backend" / "gardendb.sqlite").as_posix()
        return f"sqlite:///{db_path}"

    @property
    def cors_origins_list(self) -> List[str]:
        """Lista de origens CORS permitidas."""
        return [o.strip() for o in self.CORS_ORIGINS.split(",") if o.strip()]

    @property
    def is_production(self) -> bool:
        """Indica se está em produção."""
        return self.ENVIRONMENT.lower() == "production"

    def require_secret_key_in_production(self) -> None:
        """Garante que SECRET_KEY foi definida em produção."""
        default = "margarida-garden-secret-key-change-in-production"
        if self.is_production and (not self.SECRET_KEY or self.SECRET_KEY == default):
            raise ValueError(
                "SECRET_KEY deve ser definida em produção. "
                "Gere com: python -c \"import secrets; print(secrets.token_urlsafe(32))\""
            )


settings = Settings()
