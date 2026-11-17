from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn, SecretStr

class Settings(BaseSettings):
    PROJECT_NAME: str = "Merchant Intelligence Copilot"
    DATABASE_URL: PostgresDsn 
    GROQ_API_KEY: SecretStr  # Changed from str to SecretStr
    GROQ_MODEL: str = "openai/gpt-oss-20b" 
    E2B_API_KEY: SecretStr   # Good practice to do this for E2B as well
    
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings: Settings = Settings() # type: ignore