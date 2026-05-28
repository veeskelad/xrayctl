# Architecture Decision Records

This directory holds xrayctl's ADRs in [MADR 3.0](https://adr.github.io/madr/)
style. ADRs capture **consequential architectural decisions** — technology
choices, license, packaging, security tradeoffs, deprecations. Bug fixes and
tactical refactors do not belong here.

See [`_template.md`](_template.md) when creating a new ADR. File naming:
`YYYY-MM-DD-kebab-slug.md`.

## Index

| Status | Date | Title | Tags |
|---|---|---|---|
| Accepted | 2026-05-28 | [Use Architecture Decision Records](./2026-05-28-use-adr.md) | meta |
| Accepted | 2026-05-28 | [Standalone OSS repository](./2026-05-28-separate-oss-repo.md) | packaging, distribution |
| Accepted | 2026-05-28 | [MIT license and MIT-only dependencies](./2026-05-28-mit-license-and-mit-only-deps.md) | license, dependency |
| Accepted | 2026-05-28 | [VLESS parser: own implementation](./2026-05-28-vless-parser-own-implementation.md) | dependency, license |
| Accepted | 2026-05-28 | [CLI and MCP server share one package](./2026-05-28-cli-plus-mcp-single-package.md) | packaging, architecture |
| Accepted | 2026-05-28 | [Xray binary from system PATH, not bundled](./2026-05-28-xray-binary-system-path.md) | packaging, distribution |
| Accepted | 2026-05-28 | [GeoIP deferred to v0.2 via ip-api.com](./2026-05-28-geoip-deferred-to-v02.md) | privacy, dependency |
