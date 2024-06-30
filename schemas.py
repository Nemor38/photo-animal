from pydantic import BaseModel
from datetime import date

class AnimalCreate(BaseModel):
    name: str
    date_of_birth: date
    type: str
    breed: str  # new field for breed
    photo: str  # new field for photo URL

class Animal(BaseModel):
    id: int
    name: str
    date_of_birth: date
    type: str
    breed: str
    photo: str  # new field for photo URL

    @property
    def age(self) -> int:
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

    class Config:
        orm_mode: True
