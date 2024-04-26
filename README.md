# PC Troubleshooting Helper Backend
This backend API serves as an expert system for diagnosing PC issues. It leverages the AIMA package and FastAPI. Key features include:

Rule-Based Inference: Utilizes AIMA’s rule-based engine for diagnosis.
RESTful API: Exposes endpoints for managing diseases, symptoms, and diagnosing issues.
Database: Stores disease and symptom information.


## API Endpoints

### Disease Management
Create Disease (POST /disease/): Create a new disease.
Get All Diseases (GET /diseases/): Retrieve a list of all diseases.

### Symptom Management
Create Symptom (POST /symptoms/): Add a new symptom.
Get All Symptoms (GET /symptoms/): Retrieve all symptoms.

### Diagnosis
Diagnose Plant Disease (POST /diagnose): Provide a list of symptom IDs to get a disease diagnosis.


## Running the Server
Install dependencies: pip install -r requirements.txt
Start the development server: uvicorn routes.py:app --reload
