from fastapi import FastAPI
from pydantic import BaseModel, Field, ConfigDict

app = FastAPI()

class AddRequest(BaseModel):
    # Pydantic v2 style config
    model_config = ConfigDict(extra="forbid")  # reject unknown fields

    a: int = Field(..., ge=-1_000_000, le=1_000_000, description="First integer")
    b: int = Field(..., ge=-1_000_000, le=1_000_000, description="Second integer")

@app.get("/")
def root():
    return {"message": "This is a simple API."}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

@app.post("/add")
def add_post(payload: AddRequest):
    return {"result": payload.a + payload.b}

