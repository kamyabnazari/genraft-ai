from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str = "default-openai-api-key"

    class Config:
        env_file = ".env"

settings = Settings()