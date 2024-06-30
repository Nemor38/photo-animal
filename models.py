from sqlalchemy import Column, Integer, String, Date
from .database import Base

class Animal(Base):
    __tablename__ = 'animals'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    date_of_birth = Column(Date)
    type = Column(String)  # 'cat' or 'dog'
    breed = Column(String)  # new field for breed
    photo = Column(String)  # new field for photo URL
