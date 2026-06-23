# Agents

## Commands

All commands run inside the Docker container:
```
docker exec descarga_datos_ci make <target>
```

Key targets: `check` (lint+format), `format` (black), `tests` (pytest), `init` (git config + setup + tests), `mutants` (mutation testing), `red`/`green`/`refactor` (TDD cycle helpers).

## Bitbucket REST API auth

The Bitbucket REST API (`api.bitbucket.org/2.0/...`) requires the **Atlassian account email** as the Basic auth username paired with an **API token** as the password.

- `BITBUCKET_EMAIL` (Atlassian account email) + `BITBUCKET_API_TOKEN` — works.
- `BITBUCKET_USERNAME` (Bitbucket username) + token — returns 401.
- `x-bitbucket-api-token-auth` header — returns 401.

## Environment variables

Required at runtime: `BITBUCKET_EMAIL`, `BITBUCKET_API_TOKEN`. Forwarded via `docker-compose.yml` from host environment.

Supplied as GitHub secrets in CI: `BITBUCKET_EMAIL`, `BITBUCKET_API_TOKEN`.

## Style

- black with `--line-length 100`
- flake8 with `--max-line-length 100`
- pytest with `--verbose`

## CI pipeline

GitHub Actions workflow: build image → check formatting → run tests (`make init`) → mutation resistance (`make mutants`) → publish to PyPI.

## Package

Published via flit. Two CLI entrypoints defined in `pyproject.toml`:
- `descarga_datos` → `descarga_datos.cli:cli`
- `setup_data` → `descarga_datos.app:app`

## TDD convention

The session used a manual TDD cycle (Red → Green → Refactor) with commits per phase. The Makefile also provides automated helpers: `make red`, `make green`, `make refactor`.
