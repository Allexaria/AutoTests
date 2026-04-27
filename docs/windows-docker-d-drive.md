# Windows: Docker build on a separate drive (optional)

Some setups keep a **working clone** on `D:\` and a second folder used only for `docker build` (long paths, disk layout, or habit). This is **not required** — building from the repository root (see the main [README](../README.md#docker)) is enough.

## Minimal flow (from this repo)

From the **repository root**:

```powershell
docker build -t ae-tests:local .
docker run --rm -e SELENIUM_HEADLESS=1 ae-tests:local
```

## Optional: `D:\ae-docker-build` layout

- **`D:\AutoTests-master`** (or any path) — your git clone.
- **`D:\ae-docker-build\context`** — a mirror of the project files you pass to `docker build` (e.g. sync with `robocopy` so `.git` and large junk stay out, similar to a `.dockerignore` intent).
- **Image tag** — often `ae-tests:local` to avoid clashing with other tags.

Example build (adjust paths if your clone is elsewhere):

```powershell
cd D:\ae-docker-build
docker build -t ae-tests:local -f context/Dockerfile context
docker run --rm -e SELENIUM_HEADLESS=1 ae-tests:local
```

Prerequisites on Windows: [Docker Desktop](https://www.docker.com/products/docker-desktop/) (WSL2 backend is typical), engine running, `docker` on `PATH` after first login.

## Quick context for AI / handover

- **UI tests** use Selenium against the **live** [automationexercise.com](https://automationexercise.com/); flakiness is possible if the site or modals change.
- **Headless in Docker:** pass `-e SELENIUM_HEADLESS=1` (the image is set up for Chromium headless by default; see the root `Dockerfile`).

For CI, use the same `docker build` / `docker run` from a checkout — no D: drive is needed on the agent.
