# ADR: Standalone OSS repository

**Status:** Accepted
**Date:** 2026-05-28
**Tags:** packaging, distribution

## Context

xrayctl was prototyped while building a Telegram-bot VPN service. The first
design sketch suggested keeping it as a sub-package inside that downstream
service's monorepo (`xrayctl/` next to `app/`, sharing the same
`pyproject.toml` workspace).

Two pressures pulled against that:

1. **Audience.** xrayctl is generic VPN-config tooling that any
   Xray/Reality/Happ user could benefit from. Burying it in a downstream
   service blocks discoverability, search, and external contribution.
2. **Generic-by-construction.** Living next to project-specific code makes
   it tempting to import internal types or special-case hostnames, IPs, or
   user lists. A separate repo enforces "no project-specific data" as a
   structural invariant, not a discipline rule.

## Decision

Ship `xrayctl` as a **standalone public GitHub repository** with its own
CI, PyPI release pipeline, and version cadence. No downstream service
should ever vendor or sub-package it; downstream uses `pip install xrayctl`
plus a project-local `.xrayctl.yaml` for context.

## Consequences

**Positive**
- Independent release cadence; downstream projects pin versions.
- Public discoverability and external contribution path.
- Clean license boundary — xrayctl is MIT, downstream services keep
  whatever they need.
- "No project-specific data" enforced by repo isolation plus a pre-commit
  guard (`scripts/check_no_leak.sh`).

**Neutral**
- Two CI pipelines (one in xrayctl, one in downstream that consumes it).
- Coordinated changes (xrayctl API + downstream call site) need two PRs.

**Negative**
- Slightly higher operational overhead (separate issues, releases,
  workflows) than a sub-package.
- v0.1 development requires a release before downstream can pin, vs. a
  monorepo where downstream could consume an unreleased branch.

## Alternatives considered

- **Sub-package in a downstream monorepo.** Faster initial dev velocity,
  but no external audience and constant pressure to leak project specifics.
- **Vendor the code into downstream `tools/` directory.** Same isolation
  problem as sub-package, plus the explicit anti-pattern of unforked
  vendored code drifting from upstream.

## References

- Generic-fixtures rule: enforced by `scripts/check_no_leak.sh`.
- Related: [MIT license and MIT-only dependencies](./2026-05-28-mit-license-and-mit-only-deps.md)
