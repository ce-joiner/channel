from fastapi import FastAPI
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://channel:secret@db:5432/channel_dev"
    class Config:
        env_file = ".env"

settings = Settings()
app = FastAPI()

@app.get("/api/health")
async def health():
    return {"status": "ok", "db": settings.DATABASE_URL}
