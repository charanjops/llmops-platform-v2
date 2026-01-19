
from fastapi import FastAPI
from app.llm.router import handle_request

app = FastAPI()

@app.post("/ask")
def ask(question: str):
    return handle_request(question)
