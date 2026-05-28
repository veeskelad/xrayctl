# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Initial repository scaffold: `pyproject.toml`, MIT `LICENSE`, README,
  `src/xrayctl/` layout with `lib/`, `cli/`, `mcp/`, `skill/` stubs.
- CI matrix (`ruff`, `mypy`, `pytest`) for Python 3.11–3.13 on Ubuntu and
  macOS.
- Pre-commit `no-project-leak` guard ensuring fixtures and docs stay generic.

[Unreleased]: https://github.com/veeskelad/xrayctl/commits/main
