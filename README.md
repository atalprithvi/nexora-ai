# Nexora AI

**Intelligent Agent Runtime**

From intelligent reasoning to autonomous execution.

## Project Structure

```text
nexora-ai/
│
├── src/
│   └── nexora_ai/
│       ├── __init__.py
│       └── main.py
│
├── tests/
├── .env
├── .gitignore
├── pyproject.toml
├── README.md
├── uv.lock
└── .venv/
```

## File & Folder Description

| File / Folder | Description |
|---|---|
| `src/` | Contains the application's source code. |
| `src/nexora_ai/` | Main Python package for Nexora AI. |
| `__init__.py` | Marks the directory as a Python package. |
| `main.py` | Application entry point containing the FastAPI server and LLM integration. |
| `tests/` | Contains automated application tests. |
| `.env` | Stores local environment variables and configuration. |
| `.gitignore` | Specifies files and folders Git should ignore. |
| `pyproject.toml` | Defines project metadata, dependencies, and build configuration. |
| `README.md` | Provides project documentation and setup instructions. |
| `uv.lock` | Locks exact dependency versions for reproducible installations. |
| `.venv/` | Isolated Python environment containing project dependencies. |

## Technology Stack

- **Python** – Core programming language.
- **FastAPI** – Backend API framework.
- **Ollama** – Local LLM runtime.
- **Qwen3** – Language model.
- **OpenAI Python SDK** – Communicates with Ollama's OpenAI-compatible API.
- **UV** – Python package and environment manager.
- **Pytest** – Automated testing framework.

## Getting Started

Install dependencies:

```bash
uv sync
```

Start the application:

```bash
uv run uvicorn nexora_ai.main:app --reload
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

Health check:

```text
http://127.0.0.1:8000/health
```

## Project Status

🚧 Under active development.