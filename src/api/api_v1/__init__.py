# Здесь регистрируем роуты из файлов с функциями представлениями в единый роут версии api

from fastapi import APIRouter

from core.config import settings

from .example import router as example_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(example_router)
