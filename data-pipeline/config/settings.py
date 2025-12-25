"""Configuration settings for the data pipeline."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Database
    database_url: str
    neo4j_uri: str
    neo4j_user: str
    neo4j_password: str

    # MusicBrainz API
    musicbrainz_user_agent: str
    musicbrainz_rate_limit: float

    # Pipeline
    batch_size: int
    max_artists: int


settings = Settings()  # type: ignore[call-arg]  # Settings loaded from environment variables
