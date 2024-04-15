from pydantic import BaseModel


class SymptomBase(BaseModel):
    description: str
    problem_id: int


class ProblemBase(BaseModel):
    title: str
    description: str
    solution: str


class UserSymptoms(BaseModel):
    symptom1: str
    symptom2: str
    symptom3: str


class SymptomDisplay(BaseModel):
    description: str

    class Config:
        orm_mode = True


class ProblemDisplay(BaseModel):
    title: str
    description: str
    solution: str

    class Config:
        orm_mode = True
