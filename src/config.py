from pydantic_settings import BaseSettings 

class Settings(BaseSettings):
    DB_URL: str 
    class Config:
        env_file=".env"
        extra="forbid"

settings=Settings()
