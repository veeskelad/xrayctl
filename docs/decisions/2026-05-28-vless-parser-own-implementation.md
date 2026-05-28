# ADR: VLESS parser — own implementation

**Status:** Accepted
**Date:** 2026-05-28
**Tags:** dependency, license

## Context

xrayctl needs to parse and build `vless://...` subscription URLs (Reality,
xhttp, Vision flows) to support the v0.1 `xrayctl xray parse` and
`xrayctl xray build` commands, plus the corresponding MCP tools.

We surveyed three Python-side prior-art projects:

| Project | License | PyPI? | Coverage |
|---|---|---|---|
| `arshiacomplus/python_v2ray` | GPL-3.0 | Yes | Most complete (parses VLESS, VMess, Trojan, SS, Hysteria2; latency-tests) |
| `hopsayer/vless-link2xray-config` | GPL-3.0 | No | VLESS-only, includes Reality but lacks Vision/xhttp |
| `arminmokri/v2ray2json` | MIT | No (script) | Multi-protocol scripts, but no library API and no PyPI distribution |

xrayctl's license policy is MIT with MIT-only runtime dependencies
([see ADR](./2026-05-28-mit-license-and-mit-only-deps.md)). That rules out
both GPL libraries. `v2ray2json` is MIT-compatible but ships as a stand-alone
script without a typed library API, so consuming it would either require a
vendor-and-fork (with attribution kept) or extracting useful pieces by
hand. Either route delivers ~30% of what we need (no Vision flow, no
xhttp, no pydantic model).

## Decision

- **Write a minimal in-tree VLESS parser** under `src/xrayctl/lib/xray/`
  with a pydantic model for the parsed result.
- Support exactly the flows we ship: VLESS-Reality, VLESS-xhttp,
  VLESS-Vision. No VMess, Trojan, SS, Hysteria2 in v0.1 — out of scope.
- Use `arminmokri/v2ray2json` as a **reference** (not as a code dependency)
  for edge-case URL shapes when needed; if any code is studied closely,
  preserve MIT attribution in `LICENSE` / NOTICE.
- Treat the parser as plumbing, not as a marketed feature — the
  differentiators are Happ deeplinks and the MCP surface.

## Consequences

**Positive**
- Zero license risk; MIT runtime kept intact.
- Strongly-typed parsed result (pydantic model) integrates cleanly with
  the rest of xrayctl's lib.
- Full control over Reality / xhttp / Vision quirks; not blocked on
  upstream maintainership.

**Neutral**
- Adds a small module (~150–300 LoC estimated) to maintain.
- Surfaces a clear extension point: VMess/Trojan/SS support is opt-in v0.2+
  work.

**Negative**
- Reimplementing wheel basics that exist elsewhere.
- No upstream community improvements flow into our parser automatically.
- Risk of edge-case bugs that mature libraries already fixed; mitigated by
  property-based / roundtrip tests over generated URLs.

## Alternatives considered

- **Optional dependency on `python_v2ray` (GPL).** Forces every commercial
  consumer to consider GPL exposure even though it's "optional" — explicitly
  ruled out by the license ADR.
- **Vendor-and-fork `v2ray2json` (MIT) into xrayctl.** Possible, but the
  script-shaped API doesn't match our pydantic-typed design and would still
  require Reality/xhttp/Vision additions. Net cost roughly equals writing
  the parser cleanly from scratch.
- **Defer parser to v0.2.** Rejected because Xray-config validation and the
  MCP `vless_parse` tool both depend on it.

## References

- Related: [MIT license and MIT-only dependencies](./2026-05-28-mit-license-and-mit-only-deps.md)
- Reference (MIT): [arminmokri/v2ray2json](https://github.com/arminmokri/v2ray2json)
- Tracked GPL projects, not used: [arshiacomplus/python_v2ray](https://github.com/arshiacomplus/python_v2ray),
  [hopsayer/vless-link2xray-config](https://github.com/hopsayer/vless-link2xray-config)
- Spec: VLESS URL grammar — https://github.com/XTLS/Xray-core
