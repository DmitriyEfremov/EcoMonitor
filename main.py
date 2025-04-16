from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from core.config import Settings
from core.logger import logger
from src.db.connection import dispose_engine, init_models
from src.routers.base_router import base_router

app = FastAPI(
    description=Settings.API_DESCRIPTION,
    title=Settings.API_TITLE,
    version=Settings.PROJECT_VERSION,
    debug=False
)

app.include_router(base_router)

@app.on_event("startup")
async def start_up() -> None:
    await init_models()

@app.exception_handler(Exception)
async def unexpected_exception_handler(exc: Exception) ->JSONResponse:
    logger.error("Unexpected error: %s",exc)
    return JSONResponse(
        status_code=500,
        content={
            "message": "An unexpected error occurred. Please try again later.",
            "detail": str(exc)
        }
    )


@app.on_event("shutdown")
async def shutdown() -> None:
    await dispose_engine()


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
