## Contributing Guide

Even though this is a personal project, it is structured as if it were a team repository.

### 1. Environment setup

- Install Python 3.10+
- Create and activate a virtualenv
- Install dependencies:

```bash
pip install -r AutoTests-abobatests/requirements.txt
```

### 2. Running tests

From workspace root:

```bash
pytest AutoTests-abobatests/tests -q
```

With Allure reports:

```bash
pytest AutoTests-abobatests/tests --alluredir=allure-results
```

### 3. Quality checks

Before opening a PR, run:

```bash
ruff check .
black --check .
mypy AutoTests-abobatests/tests/conftest.py
pre-commit run --all-files
```

### 4. Code style

- Follow Black formatting (do not fight the formatter)
- Keep Selenium waits explicit and deterministic
- Prefer page-object methods over raw locators in tests

### 5. Git / PR workflow

- Use small, focused branches
- Write meaningful commit messages (what + why)
- Keep PRs small and reviewable:
  - summary of changes
  - how to test
  - known limitations or follow-ups

