from pydantic_settings import BaseSettings ,SettingsConfigDict

class settings(BaseSettings):
    TAVILY_API_KEY: str

    OLLAMA_BASE_URL:str
    OLLAMA_MODEL: str

    GROQ_API_KEY: str
    GROQ_MODEL: str

    OPENAI_API_KEY: str
    OPENAI_MODEL: str

    TEMPERATURE: float = 0.0

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings=settings()