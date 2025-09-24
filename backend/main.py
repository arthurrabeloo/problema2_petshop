from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models, crud
from .database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/pets")
def listar_pets(busca: str = "", especie: str = "", db: Session = Depends(get_db)):
    return crud.get_pets(db, busca, especie)

@app.post("/pets")
def cadastrar_pet(nome: str, especie: str, tutor: str, db: Session = Depends(get_db)):
    return crud.create_pet(db, nome, especie, tutor)

@app.delete("/pets/{pet_id}")
def remover_pet(pet_id: int, db: Session = Depends(get_db)):
    pet = crud.delete_pet(db, pet_id)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet não encontrado")
    return {"msg": "Pet removido"}

@app.post("/pets/{pet_id}/servicos")
def adicionar_servico(pet_id: int, descricao: str, db: Session = Depends(get_db)):
    return crud.add_servico(db, pet_id, descricao)

@app.get("/pets/{pet_id}/servicos")
def listar_servicos(pet_id: int, limite: int = 5, db: Session = Depends(get_db)):
    return crud.get_servicos(db, pet_id, limite)
