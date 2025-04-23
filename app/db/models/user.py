from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    email = Column(String, unique=True)
    full_name = Column(String(100))
    password = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    coverage_plan = Column(Integer, ForeignKey("storage_plans.id"))  # Atualizado para ser uma ForeignKey
    deleted_at = Column(DateTime, nullable=True)


    # Relationship with StoragePlans
    storage_plan = relationship("StoragePlans", backref="users")
