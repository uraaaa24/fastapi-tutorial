from typing import Any

from fastapi import APIRouter
from schema.user import UserIn, UserInDB, UserOut

router = APIRouter()


def fake_password_hasher(raw_password: str) -> str:
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


@router.get("/user/", response_model=UserOut)
async def create_user(user_in: UserIn) -> Any:
    user_saved = fake_save_user(user_in)
    return user_saved
