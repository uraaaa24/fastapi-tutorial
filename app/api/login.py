from fastapi import APIRouter, Form

router = APIRouter()


@router.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}
