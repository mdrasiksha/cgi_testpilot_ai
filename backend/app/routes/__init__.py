from fastapi import APIRouter

from .generate import router as generate_router
from .health import router as health_router

api_router = APIRouter()
api_router.include_router(health_router)
api_router.include_router(generate_router, prefix="/generate")
