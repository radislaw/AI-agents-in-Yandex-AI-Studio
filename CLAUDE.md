# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project context

This repository is coursework for Yandex's "Создание ИИ-агентов в Yandex AI Studio" (Building AI Agents in Yandex AI Studio) course. It is at an early stage ([main.py](main.py) is the only script so far, making a single Responses API call). Expect to build this out incrementally as the course progresses; do not assume architecture beyond what is actually present in the repo at the time.

The course uses the `openai` Python library as its client, pointed at Yandex AI Studio's OpenAI-compatible API rather than OpenAI's own endpoint. When writing client code, expect a custom `base_url` and a Yandex-issued API key/folder ID rather than an OpenAI key.

## Environment setup

Dependencies and the virtualenv are managed with [`uv`](https://docs.astral.sh/uv/) (installed via Homebrew: `brew install uv`), not raw `pip`/`venv`. Python on this machine is Homebrew-managed and externally-managed (PEP 668), which is part of why `uv` is used instead of a bare `pip install`.

```bash
uv sync          # create .venv and install dependencies from uv.lock
uv run main.py   # run a script inside the project's venv, no manual activation needed
uv add <package> # add a new dependency (updates pyproject.toml and uv.lock)
```

`.venv/` is gitignored; `pyproject.toml` and `uv.lock` are committed and are the source of truth for dependencies.

## Secrets

API keys/credentials for Yandex AI Studio must not be committed. `.env` and `.env.*` are gitignored — put credentials there rather than hardcoding them in source.
