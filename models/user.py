from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.base import Base


# Define the User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    addresses = relationship("Address", back_populates="user")
