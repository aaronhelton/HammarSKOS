from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_base_url: str = "http://127.0.0.1:8000"
    vocabularies: list = []
    app_title: str = "HammarSKOS Linked Data"
    description: str = "A FastAPI powered SKOS REST API."

    model_config = SettingsConfigDict(env_file=".env")