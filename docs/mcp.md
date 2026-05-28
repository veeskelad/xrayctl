# MCP server

`xrayctl-mcp` is a [FastMCP](https://github.com/jlowin/fastmcp) server that
exposes the same `lib/*` functions as Model Context Protocol tools. It speaks
stdio, so any MCP-aware client (Claude Code, Cursor, Windsurf, Claude
Desktop) can launch it directly.

## Install

```bash
pipx install xrayctl
```

## Register in Claude Code

Edit `.claude/mcp.json` in your project (or `~/.claude/mcp.json` for
user-scope):

```json
{
  "mcpServers": {
    "xrayctl": {
      "command": "xrayctl-mcp"
    }
  }
}
```

If `xrayctl-mcp` is not on `$PATH`, point at the venv directly:

```json
{
  "command": "/path/to/venv/bin/xrayctl-mcp"
}
```

## Tools

v0.1.0 exposes one smoke-test tool (`version`). Real tools land alongside
their CLI counterparts in `lib/*`. The plan:

- `happ_build`, `happ_decode`, `happ_validate`
- `vless_parse`, `vless_build`, `xray_validate`
- `tmpl_validate_singbox`
- `net_dns_resolve`, `net_dns_leak_check`, `net_socks5_ping`
- `config_show` (reads project's `.xrayctl.yaml`)

## Read project context

The server reads `.xrayctl.yaml` the same way the CLI and skill do (CWD,
parents, `$XRAY_TOOLKIT_CONFIG`). Use `config_show` to inspect what the
server sees.
