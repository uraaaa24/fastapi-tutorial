from api.files import router as files_router
from api.items import router as items_router
from api.login import router as login_router
from api.models import router as models_router
from api.root import router as root_router
from api.user import router as user_router
from api.users import router as users_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(login_router)
app.include_router(items_router)
app.include_router(user_router)
app.include_router(users_router)
app.include_router(files_router)
app.include_router(root_router)
app.include_router(models_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
