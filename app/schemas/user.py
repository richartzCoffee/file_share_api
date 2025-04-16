import re

from email_validator import EmailNotValidError, validate_email
from pydantic import BaseModel, field_validator

MIN_PASSWORD_LENGTH = 8


class User(BaseModel):

    username: str
    password: str
    email: str
    full_name : str
    coverage_plan : int 

    @field_validator('username')
    def validate_username(cls, value):
        if not re.match(r'^([a-z]|[0-9]|@)', value):
            raise ValueError('Username format invalid')
        return value

    @field_validator('email')
    def validate_email(cls, value):
        try:
            email_valid = validate_email(value)
            return email_valid.email
        except EmailNotValidError:
            raise ValueError('Email format invalid')

    @field_validator('password')
    def validate_password(cls, value):
        if len(value) < MIN_PASSWORD_LENGTH:
            raise ValueError('Password must be at least 8 characters long')
        if not re.search(r'[A-Z]', value):
            raise ValueError(
                'Password must contain at least one uppercase letter'
                )
        if not re.search(r'[a-z]', value):
            raise ValueError(
                'Password must contain at least one lowercase letter'
                )
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise ValueError(
                'Password must contain at least one special character'
                )
        return value
    
    @field_validator('full_name')
    def validate_full_name(cls, value):
        value = value.strip() 
        if not re.match(r'^[A-Za-z\s]+$', value):
            raise ValueError('Full name must contain only letters and spaces')
        return value.title()
    
    @field_validator('coverage_plan')
    def validate_coverage_plan(cls, value):
        if value not in [1, 2, 3]:
            raise ValueError('Coverage plan must be 1, 2, or 3')
        return value
