from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from .models import Animal as AnimalModel
from .schemas import Animal, AnimalCreate

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/animals/", response_model=Animal)
def create_animal(animal: AnimalCreate, db: Session = Depends(get_db)):
    db_animal = AnimalModel(**animal.dict())
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)
    return db_animal

@app.get("/animals/{animal_id}", response_model=Animal)
def read_animal(animal_id: int, db: Session = Depends(get_db)):
    db_animal = db.query(AnimalModel).filter(AnimalModel.id == animal_id).first()
    if db_animal is None:
        raise HTTPException(status_code=404, detail="Animal not found")
    return db_animal
