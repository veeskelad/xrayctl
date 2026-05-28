# Contributing to xrayctl

Thanks for the interest. xrayctl is small, opinionated, and built to stay
that way. The fastest path from idea to merge:

1. Open an issue first if your change is consequential. "Consequential" =
   anything that would warrant an ADR (see below).
2. Match house style: ruff/format pre-commit, mypy strict, ≥ 90% coverage
   target on `src/xrayctl/lib/`.
3. Keep fixtures and examples **generic** — `example.com`, RFC-5737 IPs,
   placeholder UUIDs. The `scripts/check_no_leak.sh` pre-commit hook fails
   commits that mention real hostnames, IPs, or operator names.

## Architecture Decision Records

xrayctl keeps an **ADR** (Architecture Decision Record) for every
consequential architectural choice. ADRs live in
[`docs/decisions/`](docs/decisions/) in
[MADR 3.0](https://adr.github.io/madr/) style.

**Open an ADR for:**

- Technology / framework / runtime / language choice
- License or accepting a dependency with a non-trivial license
- Packaging / distribution model
- Architectural pattern with long-term consequences
- Major dependency adoption or drop
- Deprecation / supersedure / breaking change
- Security or privacy tradeoff

**Don't open an ADR for:**

- Bug fix
- Refactor without architectural impact
- Tactical implementation detail
- Temporary stub or TODO
- Config tweak or cosmetic change

### Workflow

1. Copy [`docs/decisions/_template.md`](docs/decisions/_template.md) to
   `docs/decisions/YYYY-MM-DD-kebab-slug.md`.
2. Fill mandatory sections: Title, Status, Date, Context, Decision,
   Consequences. Add Alternatives considered when the decision had real
   competitors.
3. Add a row to [`docs/decisions/INDEX.md`](docs/decisions/INDEX.md) at the
   top of the table.
4. If your ADR supersedes another, change the old ADR's Status to
   `Superseded by [link]` and reference the new one.
5. Include the ADR in the PR that implements (or formally accepts) the
   decision. Atomic commits preferred — one ADR + one related code change
   per commit when possible.

## Development setup

```bash
git clone https://github.com/veeskelad/xrayctl.git
cd xrayctl
uv sync --extra dev
uv run pre-commit install
uv run pytest
```

Pre-commit hooks run ruff (lint + format), mypy strict, gitleaks, and a
`no-project-leak` guard that grep'es staged files for project-specific
identifiers.

## Pull requests

- Atomic commits. One logical change per commit.
- Conventional commit prefixes (`feat:`, `fix:`, `docs:`, `ci:`, `chore:`,
  `refactor:`) preferred.
- Tests + types + ruff/format clean before requesting review.
- Reference the relevant ADR in your PR description for consequential
  changes; cite the no-ADR criteria for everything else.

## License

By contributing, you agree your contributions are licensed under the
project's MIT License (see [`LICENSE`](LICENSE)).
