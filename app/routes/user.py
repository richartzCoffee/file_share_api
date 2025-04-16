from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.crud.user import UserUseCases
from app.schemas.user import User
from app.depends import get_db_session


unauthorized_user = APIRouter(prefix='/user')


@unauthorized_user.post('/register')
def user_register(user: User, db_session: Session = Depends(get_db_session)):
    uc = UserUseCases(db_session=db_session)
    uc.user_register(user=user)
    return JSONResponse(
        content={'msg': 'sucess'},
        status_code=status.HTTP_201_CREATED
    )
