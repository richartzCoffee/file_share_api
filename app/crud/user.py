from decouple import config
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status  
from app.schemas.user import User
from app.db.models.user import UserModel
from datetime import datetime, timezone


SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')
crypt_contect = CryptContext(schemes=['sha256_crypt'])

# CRYPTO_ALGORITHM = config('CRYPTO_ALGORITHM')



class UserUseCases:
    def __init__(self,db_session : Session):
        self.db_session = db_session
    
    
    def user_register(self,user: User):
        print(f"Password received: {user.password}") 
        user_model = UserModel(
            username=user.username,
            password=crypt_contect.hash(user.password),
            email=user.email,
            full_name=user.username,
            coverage_plan=user.coverage_plan,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        try:
            self.db_session.add(user_model)
            self.db_session.commit()
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='User already exists'
            )

