from fastapi import APIRouter
from fastapi.responses import JSONResponse



unauthorized_user = APIRouter(prefix='/user')


@unauthorized_user.get('/register')
async def new_user():  
    return {
        "message": "Hello, this is a new user!"
    }

