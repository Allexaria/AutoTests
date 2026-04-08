# AutomationExercise QA Project

Python-based UI and API test automation project for [automationexercise.com](https://automationexercise.com/).

## What this project contains

- `AutoTests-abobatests/` - pytest test suite, fixtures, CI, Docker setup.
- `UI-framework-abobatests/` - Selenium page-object layer used by UI tests.
- `API-framework-develope/` - API client/wrapper used by API tests.

## Tech stack

- Python 3.10+
- pytest
- Selenium (Chrome)
- requests
- Faker
- allure-pytest

## Project story (for recruiters)

This project is my end-to-end automation playground for a demo e‑commerce site.  
I use it to practice:

- designing UI page objects and API clients
- keeping tests deterministic and readable
- wiring CI, Docker, and quality gates (lint/format/type checks)

If I were evolving this into a production test suite, I would:

- split fast smoke tests vs. heavier flows with markers
- add parallel execution and cross-browser coverage
- introduce richer reporting (dashboards, flaky-test tracking)

## Local setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r AutoTests-abobatests/requirements.txt
```

## Run tests

From workspace root:

```bash
pytest AutoTests-abobatests/tests -q
```

Run with Allure results:

```bash
pytest AutoTests-abobatests/tests --alluredir=allure-results
```

## Docker build (token is required at build time)

Token is not stored in repository. Pass it explicitly:

```bash
docker build -f AutoTests-abobatests/Dockerfile ^
  --build-arg GITLAB_API_TOKEN=YOUR_TOKEN ^
  -t ae-tests .
```

## Security

- Secrets are never stored in this repository.
- Use environment variables or CI/CD variables for tokens.
- If a token is exposed, rotate/revoke it immediately and replace it in CI.
- `.env.example` provides placeholders only; real `.env` files are ignored by git.

## Code Quality Gates

This project uses formatter/linter/type checks to keep codebase production-ready:

- `black` for formatting
- `ruff` for linting/import sorting
- `mypy` for static type checking (critical modules)
- `pre-commit` to run checks before commits

Install dependencies:

```bash
pip install -r AutoTests-abobatests/requirements.txt
```

Run checks from workspace root:

```bash
ruff check .
black --check .
mypy AutoTests-abobatests/tests/conftest.py
```

Install git hooks:

```bash
git init
git add .
pre-commit install
pre-commit run --all-files
```

Note: `pre-commit run --all-files` checks tracked files only, so initialize git first.

## Notes

- This repository intentionally keeps UI and API framework code in sibling folders.
- `conftest.py` configures import paths so tests can import both frameworks.
