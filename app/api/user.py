from typing import Any

from fastapi import APIRouter
from schema.user import UserIn, UserOut

router = APIRouter()


# Don't do this in production!
@router.get("/user", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user
