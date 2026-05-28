# CLI reference

`xrayctl` is the human-facing entry point. The MCP server (`xrayctl-mcp`)
exposes the same operations to LLM clients.

## Groups

- `xrayctl happ` — Happ deeplinks and routing JSON.
- `xrayctl xray` — VLESS subscription URLs and Xray config validation.
- `xrayctl tmpl` — Cross-client subscription templates.
- `xrayctl net` — DNS, leak detection, SOCKS5 reachability.
- `xrayctl config` — Inspect the resolved `.xrayctl.yaml`.
- `xrayctl skill` — Manage the bundled Claude skill.
- `xrayctl install-xray` — Download the Xray binary on demand.

Run `xrayctl <group> --help` for command-level options. The full reference is
generated from `--help` output in v0.1.0 and rendered here.

> This document is a stub. Full command reference lands alongside the v0.1.0
> functional milestones.
