from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .database import Base


class Symptom(Base):
    __tablename__ = "symptoms"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    problem_id = Column(Integer, ForeignKey("problems.id"))

    problem = relationship("Problem", back_populates="symptoms")


class Problem(Base):
    __tablename__ = "problems"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    solution = Column(Text)

    symptoms = relationship("Symptom", back_populates="problem")
