from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session



class UserUseCases:
    def __init__(self,db_session : Session):
        self.db_session = db_session
    
    
    def user_register(self,user: User):
        user_model = UserModel(
            username=user.username,
            password=crypt_contect.hash(user.password)
        )
        try:
            self.db_session.add(user_model)
            self.db_session.commit()
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='User already exists'
            )