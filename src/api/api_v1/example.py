# Здесь объявляем функции-пердставления

from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.models import db_helper
from core.schemas.user import UserCreate, UserOut

from .crud.example import create_user as create_user_crud
from .crud.example import get_all_users

router = APIRouter(
    prefix=settings.api.v1.users,
    tags=["Users"],
)


@router.get("", response_model=list[UserOut])
async def get_users(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    users = await get_all_users(session=session)
    return users


@router.post("", response_model=UserOut)
async def create_user(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    user_create: UserCreate,
):
    user = await create_user_crud(
        session=session,
        user_create=user_create,
    )
    return user
