from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    public_frontend_url: str = "http://default-frontend-url"
    openai_api_key: str = "default-openai-api-key"

    class Config:
        env_file = ".env"

settings = Settings()