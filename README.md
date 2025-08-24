# LangGraph Lab

A simple, hands-on repo to learn LangGraph concepts using LangChain + Ollama. The code is organized in small modules (mostly notebooks) so you can learn incrementally.

## What this project is
- __Goal__: Learn core building blocks: prompts, chains, simple graphs, basic agent patterns, and memory with local models via Ollama.
- __Approach__: Short notebooks in `modules/` that you can run locally.

## Repository structure
- `modules/`
  - `module0/basic.ipynb` — Hello LangChain + Ollama basics.
  - `module1/agent.ipynb` — Minimal agent pattern.
  - `module1/agent-memory.ipynb` — Add simple memory to an agent.
  - `module1/chain ollama.ipynb` — Build a basic chain that calls an Ollama chat model.
  - `module1/router ollama.ipynb` — Simple router pattern with Ollama-backed tools/routes.
  - `module1/simple-graph.ipynb` — First steps toward a LangGraph-style flow.
  - `module2/` to `module6/` — Placeholders for upcoming lessons and experiments.
- `utils/config.py` — Small helpers to load `.env` and to get an Ollama-backed LLM via `get_llm()`.
  - Default model key: `OLLAMA_MODEL` (falls back to `deepseek-r1:7b`).
- `milvus-standalone-docker-compose.yml` — Optional local Milvus stack (for future vector/semantic memory experiments).

## Prerequisites
- __Python__: 3.13 (see `.python-version`).
- __Ollama__: Installed and running locally if you want to use local models.
  - Default model used by `utils/config.get_llm()`: `deepseek-r1:7b`.
  - Pull it once: `ollama pull deepseek-r1:7b`.
- __Pipenv__ (optional, recommended) or plain `pip`.
- __Docker__ (optional) if you want to run Milvus locally.

## Setup
### Option A: Pipenv (recommended)
```bash
pipenv install --dev
```

### Option B: pip
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

### Environment variables
Create a `.env` in the project root if you want to override defaults:
```
# Optional; default is deepseek-r1:7b
OLLAMA_MODEL=deepseek-r1:7b
```

## Quickstart
- Open the notebooks under `modules/` in your IDE or Jupyter.
- Or run a tiny script using the helper LLM:

```python
from utils.config import get_llm

llm = get_llm()  # uses OLLAMA_MODEL or falls back to deepseek-r1:7b
resp = llm.invoke("Say hello in one short sentence.")
print(resp.content)
```

## Optional: run Milvus locally
If you plan to experiment with vector stores later:
```bash
docker compose -f milvus-standalone-docker-compose.yml up -d
```
This will start etcd, MinIO, Milvus, and Attu (web UI on http://localhost:3000).

## Project status (so far)
- `module0` and `module1` contain working notebooks covering:
  - Basics with LangChain + Ollama
  - Simple chains and routing
  - Minimal agent patterns and adding memory
  - First simple graph experiment
- `module2`–`module6` are scaffolds for next topics.

## Formatting and Linting
This project uses Black (formatter) and Flake8 (linter). Config is in `pyproject.toml` and `.flake8` (line length 88).

### Using Pipenv
- Install dev dependencies:
  ```bash
  pipenv install --dev
  ```
- Format all files with Black:
  ```bash
  pipenv run black .
  ```
- Check formatting only (CI-friendly):
  ```bash
  pipenv run black --check .
  ```
- Lint with Flake8:
  ```bash
  pipenv run flake8 .
  ```

#### Useful variants
- Format a single file:
  ```bash
  pipenv run black path/to/file.py
  ```
- Show proposed changes without writing:
  ```bash
  pipenv run black --diff .
  ```
- Verify tool versions:
  ```bash
  pipenv run black --version
  pipenv run flake8 --version
  ```

### Without Pipenv
```bash
pip install black flake8
black .
flake8 .
```
