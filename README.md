# xrayctl

> Programmatic Happ deeplink builder + MCP server for the Xray/Reality stack.
> For VPN developers and AI agents.

[![CI](https://github.com/veeskelad/xrayctl/actions/workflows/ci.yml/badge.svg)](https://github.com/veeskelad/xrayctl/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python: 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](pyproject.toml)

> **Status:** alpha. v0.1.0 in development.

## What

`xrayctl` is a single Python package that exposes two interfaces over the same
core:

- **`xrayctl`** — a Click-based CLI for humans and scripts.
- **`xrayctl-mcp`** — a [FastMCP](https://github.com/jlowin/fastmcp)-based
  Model Context Protocol server for AI agents (Claude Code, Cursor, Windsurf).

The core covers:

- **Happ deeplinks** — build/decode `happ://routing/add/{base64}` profiles
  with Pydantic validation.
- **VLESS subscription URLs** — parse/build `vless://...` for Reality, xhttp,
  Vision flows.
- **Xray config** — JSON-schema validation, optional `xray test` smoke run.
- **Cross-client templates** — SingBox / Mihomo / Clash / Stash subscription
  templates (v0.1: SingBox first, others in v0.2).
- **Network checks** — DNS resolve via DoH/DoT/UDP-53, leak detection, SOCKS5
  TCP-ping.

It does **not** ship curated proxy lists or routing data — it generates,
parses, and validates configs. Pair it with data repositories (e.g.
[hydraponique/roscomvpn-routing](https://github.com/hydraponique/roscomvpn-routing))
as input.

## Why

There is no programmatic builder for Happ deeplinks (only web UIs and static
dumps), and there is no MCP server for the Xray/Reality stack. `xrayctl`
fills that niche so engineers can script proxy operations and AI agents can
manage VPN configuration through a typed tool surface.

## Install

```bash
pip install xrayctl
# or with pipx
pipx install xrayctl
```

`xrayctl` looks for the `xray` binary on `$PATH` (or `$XRAY_BIN`). To install
it on demand:

```bash
xrayctl install-xray            # downloads latest into ~/.cache/xrayctl/bin/
```

## Quickstart

### CLI

```bash
# Build a Happ deeplink from a routing JSON
xrayctl happ build --preset ru-direct-loyalsoldier > my.deeplink

# Decode someone else's deeplink
xrayctl happ decode "happ://routing/add/eyJSZW1vd..."

# Validate a VLESS subscription URL
xrayctl xray parse "vless://uuid@vpn.example.com:443?type=tcp&security=reality&..."

# DNS leak detection through a SOCKS5 proxy
xrayctl net leak --proxy socks5://user:pass@proxy.example.com:1080
```

### MCP server

```bash
xrayctl-mcp                     # stdio transport, exposes tools to LLM clients
```

Register in Claude Code via `.claude/mcp.json`:

```json
{
  "mcpServers": {
    "xrayctl": {
      "command": "xrayctl-mcp"
    }
  }
}
```

### Claude skill

```bash
xrayctl skill install --target .claude/skills/   # or ~/.claude/skills/
```

The skill reads `.xrayctl.yaml` in your project root for project-specific
notes and paths. See [`docs/.xrayctl.example.yaml`](docs/.xrayctl.example.yaml).

## Config

Drop `.xrayctl.yaml` at the project root (or point `XRAY_TOOLKIT_CONFIG` to
it):

```yaml
default_proxy_env: HTTP_PROXY
remnawave:
  base_url_env: REMNAWAVE_BASE_URL
  token_env: REMNAWAVE_API_TOKEN
  readonly: true
notes:
  - "geosite/geoip URLs must point to Loyalsoldier CDN, not Happ built-in"
  - "Hiddify-Windows fails on xhttp Reality; use Happ for that profile"
templates:
  singbox: ./templates/singbox.json
```

The config holds **environment-variable names and paths only** — never
secrets. Real credentials live in your shell/`.env` file.

## Status & roadmap

- v0.1.0 (in progress): Happ builder, VLESS parser, Xray validator, SingBox
  template, DNS/leak checks, MCP server, generic Claude skill.
- v0.2.0: Mihomo / Clash / Stash templates, GeoIP via `ip-api.com`, TCP-ping
  reachability metrics.
- v0.3.0+: web-UI playground, headless probe via embedded sing-box.

## Contributing

Issues and PRs welcome. Conventional commits, MIT-only dependencies, no
project-specific data in fixtures (`example.com`, RFC-5737 IPs only).

## License

MIT — see [LICENSE](LICENSE).
