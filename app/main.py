from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Submission(BaseModel):
    answer: str

@app.post("/grade")
async def grade(sub: Submission):
    # Dummy grading logic
    return {"score": 1.0 if sub.answer else 0.0}

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": "1.0.0"
    } 