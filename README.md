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

1. **Python 3.10+** and **Google Chrome** (Selenium 4 uses bundled driver resolution; a matching Chrome is required).
2. Create and activate a virtual environment.
3. Install dependencies (either path installs the same set):

```bash
pip install -r requirements.txt
```

(Equivalent: `pip install -r AutoTests-abobatests/requirements.txt`.)

## Run tests

From workspace root:

```bash
pytest AutoTests-abobatests/tests -q
```

Run with Allure results:

```bash
pytest AutoTests-abobatests/tests --alluredir=allure-results
```

The `allure-pytest` package only **writes** raw results (JSON) into `--alluredir`. To get an **HTML** report, install a [JDK](https://adoptium.net/) and the [Allure command-line](https://github.com/allure-framework/allure2/releases), then run `allure generate <dir> -o <output> --clean` and open the report over **http** (e.g. `allure open <output>`) — opening `index.html` via `file://` may show a blank UI in some browsers.

## Docker

Optional: [Windows: build on `D:\` and notes for handover](docs/windows-docker-d-drive.md).

Build the image from the **repository root** (`.dockerignore` keeps the context small):

```bash
docker build -t ae-tests .
```

Run tests (Chromium in the image is **headless** by default; `CHROME_BIN` and `SELENIUM_HEADLESS` are set in the `Dockerfile`):

```bash
docker run --rm -e SELENIUM_HEADLESS=1 ae-tests
```

Save Allure **raw** results to the host (then `allure generate` / `allure open` on the host, or use the Allure CLI inside the image on that folder):

```bash
# Linux / macOS / Git Bash
docker run --rm -e SELENIUM_HEADLESS=1 -v "$(pwd)/allure-results:/app/allure-results" ae-tests
```

In PowerShell (Docker Desktop):

```powershell
docker run --rm -e SELENIUM_HEADLESS=1 -v "${PWD}/allure-results:/app/allure-results" ae-tests
```

Override the test command, e.g. only API or smoke:

```bash
docker run --rm ae-tests pytest AutoTests-abobatests/tests/api_requests_test.py -q
```

**Inside the image:** `allure` and `java` (JRE 17) are installed so you can run `allure generate allure-results -o allure-report --clean` after a run if you keep `/app/allure-results` in a volume.

## Security

- Secrets are never stored in this repository.
- Use environment variables or CI/CD variables for tokens.
- If a token is exposed, rotate/revoke it immediately and replace it in CI.
- `.env.example` provides placeholders only; real `.env` files are ignored by git.
- `pre-commit` includes `gitleaks` to prevent committing new secrets.

## Code Quality Gates

This project uses formatter/linter/type checks to keep codebase production-ready:

- `black` for formatting
- `ruff` for linting/import sorting
- `mypy` for static type checking (critical modules)
- `pre-commit` to run checks before commits

Install dev/lint dependencies (same as test install):

```bash
pip install -r requirements.txt
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
- Import paths are configured in `pytest.ini` (`pythonpath`) instead of runtime `sys.path` mutations.
- Canonical automated test suite lives in `AutoTests-abobatests/tests`.
