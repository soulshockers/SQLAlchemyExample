from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base


# Define the Address model
class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    country = Column(String(10))
    street = Column(String)
    city = Column(String)
    zip_code = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="addresses")
