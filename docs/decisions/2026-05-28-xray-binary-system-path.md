# ADR: Xray binary from system PATH, not bundled

**Status:** Accepted
**Date:** 2026-05-28
**Tags:** packaging, distribution

## Context

`xrayctl xray validate` and similar commands need a working `xray`
executable to run `xray test`-style smoke checks against generated configs.
We have three ways to make one available:

1. **System PATH.** Look up `xray` in `$PATH` or `$XRAY_BIN`. If absent,
   print an actionable install hint.
2. **Bundle.** Ship the Go binary inside the Python wheel via a
   platform-specific build, like `xray-core-python` does.
3. **On-demand download.** Provide a `xrayctl install-xray` command that
   fetches the latest release from GitHub into `~/.cache/xrayctl/bin/` with
   checksum verification.

Each option trades user friction against distribution complexity.

## Decision

- **Default behaviour: read `xray` from `$PATH` (or `$XRAY_BIN` override).**
- **Ship an optional `xrayctl install-xray [--version]` command** that
  downloads the official Xray-core release, verifies the SHA-256 checksum,
  and places the binary in `~/.cache/xrayctl/bin/`. Users who run this once
  get a clean experience without bundling.
- **Do not vendor the binary into the Python wheel.** No multi-arch wheel
  matrix, no Apple-notarization story, no 30 MB wheels for users who
  already have Xray installed.

## Consequences

**Positive**
- Pure-Python wheel; trivial PyPI release pipeline.
- Users who manage Xray themselves (e.g. via `XTLS/Xray-install`, `apt`,
  `brew`) get out-of-the-box compatibility.
- Auditable: users see exactly which Xray version is in play via standard
  shell tools.
- `install-xray` covers the new-user "I just want it to work" case without
  blocking everyone else.

**Neutral**
- New users must run a one-time command (or already have Xray) before
  validation features work.
- `install-xray` needs to follow Xray-core's release-asset naming, which can
  change.

**Negative**
- Validation features error out cleanly when Xray is absent — must produce
  a friendly install hint, not a cryptic `FileNotFoundError`.
- We carry a small download/verification module (`_runners/xray.py` or a
  dedicated installer) that has to handle Linux/macOS/Windows + arm64/x86_64.

## Alternatives considered

- **Bundle Xray binaries via platform-specific wheels.** Adds a four-axis
  build matrix (OS × arch), notarization on macOS, signing on Windows, and
  ~30 MB wheels. Maintenance cost outweighs the convenience win.
- **Auto-download silently on first use.** Surprising side effect during
  normal command runs; we prefer an explicit `install-xray` step.
- **Embed Xray-core via C bindings (`xray-core-python` style).** Forces
  multi-arch wheel maintenance and pulls in a heavyweight Go runtime.

## References

- [XTLS/Xray-install](https://github.com/XTLS/Xray-install) — official
  installer pattern.
- [Xray-core releases](https://github.com/XTLS/Xray-core/releases) — asset
  naming and checksums.
- Related: [Standalone OSS repository](./2026-05-28-separate-oss-repo.md)
