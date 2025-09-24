from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from .database import Base
from sqlalchemy.orm import relationship

class Pet(Base):
    __tablename__ = "pets"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(Text, nullable=False)
    especie = Column(Text, nullable=False)
    tutor = Column(Text, nullable=False)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    servicos = relationship("Servico", back_populates="pet", cascade="all, delete-orphan")

class Servico(Base):
    __tablename__ = "servicos"
    id = Column(Integer, primary_key=True, index=True)
    pet_id = Column(Integer, ForeignKey("pets.id", ondelete="CASCADE"), nullable=False)
    descricao = Column(Text, nullable=False)
    data = Column(DateTime(timezone=True), server_default=func.now())
    pet = relationship("Pet", back_populates="servicos")
