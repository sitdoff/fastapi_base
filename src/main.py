from fastapi import FastAPI

from api import router as api_router
from core.config import settings

app = FastAPI()
app.include_router(api_router, prefix=settings.api_prifix.prefix)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        **settings.run.model_dump(),
    )
