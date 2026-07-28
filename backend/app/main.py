from fastapi import FastAPI

from app.config import settings


app = FastAPI(
    title="WorthFlow API",
    version="0.1.0",
)

app.state.settings = settings


@app.get("/health", tags=["Health"])
async def health_check() -> dict[str, str]:
    return {"status": "healthy"}
