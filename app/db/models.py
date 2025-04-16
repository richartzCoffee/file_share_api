from sqlalchemy import Column, Integer, String, DateTime
from app.db.base import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    email = Column(String, unique=True)
    full_name = Column(String(100))
    password = Column(String)
    created_at = Column(DateTime)
    coverage_plan = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime, nullable=True)
    
