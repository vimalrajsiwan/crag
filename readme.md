# CRAG - Corrective Retrieval-Augmented Generation

CRAG is a Python project for exploring **Corrective Retrieval-Augmented
Generation**: a RAG approach that checks whether retrieved context is useful
before relying on it to answer a question.

> **Project status:** This repository is currently a documentation and setup
> starter. The application code, dependencies, and tests have not been added yet.

## What CRAG aims to do

A conventional RAG application retrieves passages for a question and gives
them to a language model. A corrective RAG workflow adds a relevance check so
that weak or irrelevant retrieval results can be handled instead of being
treated as reliable context.

The intended high-level flow is:

1. Accept a question.
2. Retrieve relevant documents or passages.
3. Evaluate whether the retrieved context is useful.
4. Use, refine, or replace the context when retrieval is insufficient.
5. Generate an answer grounded in the resulting context.

This describes the project goal, not implemented behavior.

## Requirements

- Python 3.12 or newer
- [`uv`](https://docs.astral.sh/uv/) for Python and project dependency
  management

Install `uv` using the instructions for your operating system in the
[official installation guide](https://docs.astral.sh/uv/getting-started/installation/).

## Getting started

From the repository root, initialize a Python project. The `--bare` option
avoids generating a second README:

```bash
uv init --bare --python 3.12
```

Add the dependencies that fit the implementation, then sync the environment:

```bash
uv add package-name
uv sync
```

Run a Python module or script with the project environment:

```bash
uv run python path/to/script.py
```

For example, after adding an application entry point at `src/crag/main.py`:

```bash
uv run python -m crag.main
```

`uv init` creates the project metadata in `pyproject.toml`; `uv add` records
dependencies there and updates `uv.lock`. Commit both files so other developers
can reproduce the environment with `uv sync --locked`.

## Project layout

The implementation has not been created yet. A possible layout as the project
grows is:

```text
.
├── README.md
├── pyproject.toml
├── uv.lock
└── src/
    └── crag/
```

## Development

Once tests and lint tools are configured as development dependencies, run them
through `uv` so they use the project environment. For example:

```bash
uv run pytest
uv run ruff check .
```

These commands are examples for a future test/lint setup; those tools and a
test suite are not configured in this starter repository yet.

## Contributing

Contributions are welcome. Please keep dependency management in `pyproject.toml`
and `uv.lock`, and include tests for new behavior as the implementation is
added.

## pkg install

uv add langchain langgraph python-dotenv beautifulsoup4 langchainhub langchain-community tavily-python langchain-chroma black isort pytest langchain-unstructured langchain-text-splitters
