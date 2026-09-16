# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project context

This repository is coursework for Yandex's "Создание ИИ-агентов в Yandex AI Studio" (Building AI Agents in Yandex AI Studio) course. It is at an early, mostly empty stage — no application code exists yet, only the Python environment scaffold. Expect to build this out incrementally as the course progresses; do not assume architecture beyond what is actually present in the repo at the time.

The course uses the `openai` Python library as its client, pointed at Yandex AI Studio's OpenAI-compatible API rather than OpenAI's own endpoint. When writing client code, expect a custom `base_url` and a Yandex-issued API key/folder ID rather than an OpenAI key.

## Environment setup

Python on this machine is Homebrew-managed and externally-managed (PEP 668) — installing packages into the system Python directly will fail. Always use the project virtualenv:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

After adding or upgrading a dependency, regenerate the lockfile-style `requirements.txt`:

```bash
pip freeze > requirements.txt
```

`.venv/` is gitignored; `requirements.txt` is committed and is the source of truth for dependencies.

## Secrets

API keys/credentials for Yandex AI Studio must not be committed. `.env` and `.env.*` are gitignored — put credentials there rather than hardcoding them in source.
