# ADR: CLI and MCP server share one package

**Status:** Accepted
**Date:** 2026-05-28
**Tags:** packaging, architecture

## Context

xrayctl exposes its functionality to two very different consumers:

- **Humans and scripts** — via a `click`-based CLI invoked as `xrayctl`.
- **LLM agents** — via a Model Context Protocol stdio server invoked as
  `xrayctl-mcp`.

Both interfaces ultimately call the same `lib/*` functions (Happ deeplink
builder, VLESS parser, template validators, network diagnostics). The
question is whether they ship as one PyPI distribution with two console
scripts, or as two distributions with `xrayctl-core` shared between them.

## Decision

Ship **a single PyPI distribution `xrayctl`** that exposes two
`[project.scripts]` entry points:

- `xrayctl` → `xrayctl.cli.main:cli`
- `xrayctl-mcp` → `xrayctl.mcp.server:main`

Build the MCP layer with [FastMCP](https://github.com/jlowin/fastmcp) (MIT)
on top of the shared `xrayctl.lib.*` modules. The MCP server is a thin
wrapper over the same functions the CLI calls, so behaviour stays in sync
by construction.

## Consequences

**Positive**
- One `pip install xrayctl` gives users both interfaces. No coordinating
  versions of two packages.
- Shared validation, models, and tests across CLI and MCP — no risk of
  drift between the two surfaces.
- New `lib/*` features become available in both interfaces in the same
  release.
- Smaller dependency surface than splitting; FastMCP and click coexist
  cheaply.

**Neutral**
- MCP server dependencies (FastMCP and its transitive `uvicorn`,
  `starlette`, etc.) are installed even for users who only want the CLI.
  Acceptable: the wheel stays under ~5 MB.
- The MCP server can be disabled by not invoking `xrayctl-mcp`; no runtime
  cost when unused.

**Negative**
- If FastMCP ever undergoes a major redesign, both surfaces share the
  upgrade work.
- Users who only want the CLI still download MCP deps. Mitigated by uv's
  fast resolver and PyPI bandwidth being effectively free at this scale.

## Alternatives considered

- **Two packages (`xrayctl` and `xrayctl-mcp`) sharing `xrayctl-core`.**
  Three releases per change instead of one. The split is mostly cosmetic at
  this size and introduces version-skew risk.
- **MCP-only package.** Forfeits human/script CLI usage, which is a key
  audience.
- **CLI-only package, MCP added later as a separate distribution.** Plausible
  v0.1-only delay, rejected because MCP availability is a primary
  differentiator (zero existing Xray MCP servers in the ecosystem).

## References

- [FastMCP](https://github.com/jlowin/fastmcp)
- Related: [Standalone OSS repository](./2026-05-28-separate-oss-repo.md)
- Code: `src/xrayctl/cli/main.py`, `src/xrayctl/mcp/server.py`
