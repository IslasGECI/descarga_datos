# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.5.0] - 2026-06-22

### Added
- `get_token_from_environment_variable()` — read `BITBUCKET_API_TOKEN` from environment
- `get_email_from_environment_variable()` — read `BITBUCKET_EMAIL` from environment

### Changed
- `DataFile.get_url_to_file()` authenticates with `BITBUCKET_EMAIL` + `BITBUCKET_API_TOKEN` instead of `BITBUCKET_USERNAME` + `BITBUCKET_PASSWORD`

### Removed
- `get_user_from_environment_variable()` — use `get_email_from_environment_variable()` instead
- `get_password_from_environment_variable()` — use `get_token_from_environment_variable()` instead

## [0.4.5] - 2025-08-05

### Fixed
- CLI command `descarga-archivo` no longer stops when a non-CSV format is passed. It now issues a warning only when a non-CSV format is passed.

## [0.4.4] - 2025-08-05

### Fixed
- CLI command `descarga-archivo` no longer stops when a non-CSV format is passed. It now issues a warning if there are no columns to be renamed.

## [0.4.3] - 2025-07-01

### Fixed
- CLI command `descarga-archivo` now has a contract: Always return column date type as "Fecha".

## [0.4.2] - 2025-06-10

### Fixed
- Update to python 3.12
- Resolve `requests` dependency

## [0.4.1] - 2023-10-24

### Fixed
- Drop NaN values in `Fecha` before extract year

## [0.4.0] - 2023-08-08

### Added

- Entrypoint `setup_data`


## [0.3.3] - 2023-08-07

### Added
- Add setup_data field to `Analysis` class

### Changed
- Use pyproject to install package
- Add docker compose

[Unreleased]: https://github.com/IslasGECI/descarga_datos/compare/v0.5.0...HEAD
[0.5.0]: https://github.com/IslasGECI/descarga_datos/compare/v0.4.5...v0.5.0
[0.4.5]: https://github.com/IslasGECI/descarga_datos/compare/v0.4.4...v0.4.5
[0.4.4]: https://github.com/IslasGECI/descarga_datos/compare/v0.4.3...v0.4.4
[0.4.3]: https://github.com/IslasGECI/descarga_datos/compare/v0.4.2...v0.4.3
[0.4.2]: https://github.com/IslasGECI/descarga_datos/compare/v0.4.1...v0.4.2
[0.4.1]: https://github.com/IslasGECI/descarga_datos/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/IslasGECI/descarga_datos/compare/v0.3.3...v0.4.0
[0.3.3]: https://github.com/IslasGECI/descarga_datos/compare/v0.3.2...v0.3.3
