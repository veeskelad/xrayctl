# ADR: MIT license and MIT-only dependencies

**Status:** Accepted
**Date:** 2026-05-28
**Tags:** license, dependency

## Context

xrayctl will be consumed by other open-source tools and by closed-source
commercial services. License choice has three knock-on effects:

1. The license users grant to redistribute and modify xrayctl.
2. The transitive license constraint on every dependency we adopt.
3. Whether commercial integrators can build proprietary products on top.

The proxy/VPN ecosystem has both MIT and GPL-3.0 projects. Two of the most
mature VLESS parsers we surveyed (`arshiacomplus/python_v2ray`,
`hopsayer/vless-link2xray-config`) are GPL-3.0. Pulling either in as a
runtime dependency would either force xrayctl itself to GPL-3.0 (full
copyleft) or sit in legal grey territory (`mere aggregation` debate for
optional deps).

## Decision

- **License xrayctl under MIT.**
- **Accept only MIT/BSD/Apache-2.0/PSF dependencies** at runtime. Dev-only
  tooling (linters, formatters, test runners) may carry permissive licenses
  with required attribution but never copyleft.
- A new runtime dependency requires an ADR if it changes the license
  surface or pulls in transitive non-permissive code.
- The pre-commit guard (`scripts/check_no_leak.sh`) currently enforces
  project-data hygiene; a future check should verify license metadata of
  pinned dependencies.

## Consequences

**Positive**
- Maximum downstream adoption — works for any commercial or proprietary
  consumer.
- Compatible with FastMCP (MIT), pydantic (MIT), click (BSD-3), dnspython
  (ISC), httpx (BSD-3) — our actual stack.
- No legal grey area around "optional GPL dep".

**Neutral**
- We must implement small features (e.g. VLESS URL parsing) ourselves when
  the only mature library is GPL.
- A formal license-audit step belongs in CI eventually.

**Negative**
- Forfeits the GPL "improvements flow back upstream" effect.
- Higher maintenance: we own code we could have imported.

## Alternatives considered

- **Apache-2.0.** Patent grant is nice, but adds NOTICE-file overhead and
  permissive-with-strings reputation. The proxy domain has no realistic
  patent threats that MIT's silence creates.
- **GPL-3.0 (matching upstream projects).** Lets us depend on
  `python_v2ray`, but eliminates closed-source adoption — direct conflict
  with the standalone-OSS goal.
- **Dual-license MIT + commercial.** Premature complexity for a v0.1 tool.

## References

- [SPDX MIT license text](https://spdx.org/licenses/MIT.html)
- [SPDX GPL-3.0 license text](https://spdx.org/licenses/GPL-3.0-only.html)
- Related: [VLESS parser: own implementation](./2026-05-28-vless-parser-own-implementation.md)
- Related: [Standalone OSS repository](./2026-05-28-separate-oss-repo.md)
