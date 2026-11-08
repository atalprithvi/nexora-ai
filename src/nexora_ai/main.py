
import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from openai import OpenAI
from pydantic import BaseModel, Field

load_dotenv()

MODEL = os.getenv("OPENAI_MODEL", "qwen3:4b")
API_KEY = os.getenv("OPENAI_API_KEY", "ollama")
BASE_URL = os.getenv(
    "OPENAI_BASE_URL",
    "http://localhost:11434/v1",
)

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY,
    timeout=120.0,
)

app = FastAPI(
    title="Nexora AI",
    description="Intelligent Agent Runtime",
    version="0.1.0",
)


class ChatRequest(BaseModel):
    question: str = Field(min_length=1, max_length=4000)


class ChatResponse(BaseModel):
    answer: str
    model: str


def ask_llm(question: str) -> str:
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are Nexora AI, a helpful AI assistant.",
                },
                {
                    "role": "user",
                    "content": question,
                },
            ],
        )

        answer = response.choices[0].message.content

        if not answer:
            raise RuntimeError("Empty response from model")

        return answer

    except Exception as exc:
        raise RuntimeError(f"LLM request failed: {exc}") from exc


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "Nexora AI",
        "model": MODEL,
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        answer = ask_llm(request.question)

        return ChatResponse(
            answer=answer,
            model=MODEL,
        )

    except RuntimeError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
