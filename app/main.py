from fastapi import FastAPI
from app.routes.user import unauthorized_user

app = FastAPI()

app.include_router(unauthorized_user)