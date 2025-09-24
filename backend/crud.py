from sqlalchemy.orm import Session
from . import models

def get_pets(db: Session, busca: str = "", especie: str = ""):
    query = db.query(models.Pet)
    if busca:
        query = query.filter(models.Pet.nome.ilike(f"%{busca}%"))
    if especie:
        query = query.filter(models.Pet.especie == especie)
    return query.all()

def create_pet(db: Session, nome: str, especie: str, tutor: str):
    pet = models.Pet(nome=nome, especie=especie, tutor=tutor)
    db.add(pet)
    db.commit()
    db.refresh(pet)
    return pet

def delete_pet(db: Session, pet_id: int):
    pet = db.query(models.Pet).filter(models.Pet.id == pet_id).first()
    if pet:
        db.delete(pet)
        db.commit()
    return pet

def add_servico(db: Session, pet_id: int, descricao: str):
    servico = models.Servico(pet_id=pet_id, descricao=descricao)
    db.add(servico)
    db.commit()
    db.refresh(servico)
    return servico

def get_servicos(db: Session, pet_id: int, limite: int = 5):
    return db.query(models.Servico).filter(models.Servico.pet_id == pet_id)\
        .order_by(models.Servico.data.desc()).limit(limite).all()
