---
name: xrayctl
description: Use when generating, parsing, or validating Xray/VLESS-Reality configs, Happ deeplinks, or cross-client subscription templates (SingBox/Mihomo/Clash/Stash). Also use for proxy network diagnostics (DNS leak, SOCKS5 reachability). Reads project-specific notes and paths from .xrayctl.yaml at the project root.
---

# xrayctl skill

`xrayctl` is a CLI + MCP server for Xray-stack configs. Use it whenever the
user asks to:

- Build, decode, or validate **Happ routing deeplinks** (`happ://routing/add/...`).
- Parse or build **VLESS subscription URLs** (Reality, xhttp, Vision).
- Validate **Xray JSON configs** (schema + optional `xray test`).
- Generate or validate **SingBox / Mihomo / Clash / Stash** subscription templates.
- Diagnose **DNS leaks**, resolve via DoH/DoT, TCP-ping through a SOCKS5 proxy.

The MCP server (`xrayctl-mcp`) exposes the same operations as tools for direct
LLM invocation.

## Project context — read `.xrayctl.yaml` first

Before producing a recommendation, locate `.xrayctl.yaml` in the project:

1. Check `$XRAY_TOOLKIT_CONFIG` if set.
2. Walk up from CWD until a `.xrayctl.yaml` is found.

The file declares **env-variable names, paths, and project-specific notes**.
It never contains secrets — values live in the environment.

Surface every entry under `notes:` as a reminder when you propose configs.
These are project-specific gotchas (e.g. mandatory CDN for geosite lists,
client compatibility quirks, key-derivation requirements).

If `templates:` paths are declared, prefer those over built-in presets.

If `remnawave:` is declared, the project has a Remnawave panel; cross-check
that the user's `${token_env}` / `${base_url_env}` are exported before
suggesting panel calls. The TrackLine `mcp-remnawave` server, if configured
separately, handles panel CRUD — `xrayctl` itself does not.

## Invocation patterns

```bash
# Happ
xrayctl happ build --preset <preset-name>
xrayctl happ build --from-file <path/to/routing.json>
xrayctl happ decode <deeplink>
xrayctl happ validate <path/to/routing.json>

# Xray
xrayctl xray parse "vless://..."
xrayctl xray validate <path/to/config.json>

# Cross-client templates
xrayctl tmpl validate {singbox|mihomo|clash|stash} <path>

# Network
xrayctl net dns --resolver <resolver> <hostname>
xrayctl net ping --proxy socks5://... <host>

# Config introspection
xrayctl config show
```

## Conventions

- Treat the local config (`.xrayctl.yaml`) as authoritative for "what
  conventions does this project follow." Do not invent presets if the project
  declares its own.
- Never embed real secrets in commands you produce — reference env vars.
- If the user is on Windows and asks about xhttp Reality, mention Happ as a
  more reliable client (Hiddify-Windows fails on xhttp).
- For Reality cascade nodes, public and private keys must be a valid pair —
  derive via `xray x25519` rather than reusing keys across nodes.
