from typing import List

from db import models
from db.database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import schema, utils

router = APIRouter()


@router.post("/symptoms/", response_model=schema.SymptomDisplay)
def create_symptom(symptom: schema.SymptomBase, db: Session = Depends(get_db)):
    # Leverage Pydantic model for validation and data extraction
    db_symptom = models.Symptom(**symptom.dict())
    db.add(db_symptom)
    db.commit()
    db.refresh(db_symptom)

    # Create and return SymptomDisplay object
    symptom_display = schema.SymptomDisplay(
        id=db_symptom.id,
        description=db_symptom.description,
        problem_title=db_symptom.problem.title if db_symptom.problem else None,
    )
    return symptom_display


@router.post("/problems/", response_model=schema.ProblemDisplay)
def create_problem(problem: schema.ProblemBase, db: Session = Depends(get_db)):
    db_problem = models.Problem(**problem.dict())
    db.add(db_problem)
    db.commit()
    db.refresh(db_problem)

    # Create and return ProblemDisplay object
    problem_display = schema.ProblemDisplay(
        id=db_problem.id,
        title=db_problem.title,
        description=db_problem.description,
        solution=db_problem.solution,
        symptoms=(
            [
                schema.SymptomDisplay(
                    id=symptom.id,
                    description=symptom.description,
                )
                for symptom in db_problem.symptoms
            ]
            if db_problem.symptoms
            else None
        ),
    )
    return problem_display


@router.get("/problems/", response_model=List[schema.ProblemDisplay])
def get_all_problems(db: Session = Depends(get_db)):
    problems = db.query(models.Problem).all()
    return problems


@router.get("/symptoms/", response_model=List[schema.SymptomDisplay])
def get_all_symptoms(db: Session = Depends(get_db)):
    symptoms = db.query(models.Symptom).all()
    return symptoms


@router.post("/diagnose", response_model=schema.ProblemDisplay)
def diagnose_route(symptoms: schema.UserSymptoms, db: Session = Depends(get_db)):
    diagnose = utils.diagnose(symptoms)
    if diagnose is None:
        raise HTTPException(status_code=404, detail="Problem not found")
    return db.query(models.Problem).filter(models.Problem.title == diagnose).first()
