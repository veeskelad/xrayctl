# ADR: GeoIP deferred to v0.2 via ip-api.com

**Status:** Accepted
**Date:** 2026-05-28
**Tags:** privacy, dependency

## Context

`xrayctl net geoip` and the related "exit-country" leak check need a way to
resolve an IP address to a country code. Three providers were evaluated:

| Provider | Free tier | Privacy | Footprint |
|---|---|---|---|
| **MaxMind GeoLite2** | License key + EULA, 90-day reconfirm | Local lookup (no requests) | ~70 MB database, monthly refresh |
| **ipinfo.io** | 1000 req/day with mandatory credit card (as of May 2025) | Logs requests | HTTP API |
| **ip-api.com** | 45 req/min, no signup | Does not log requests (per their legal page), GDPR + ISO 27001 | HTTP API |

The v0.1 surface — Happ deeplinks, VLESS parser, Xray validation,
SingBox/Mihomo/Clash/Stash templates, DNS leak check, SOCKS5 reachability —
does not require GeoIP. Including it now means either shipping a 70 MB
database in the wheel, requiring an external license + signup, or pulling
in HTTP-call complexity ahead of need.

## Decision

- **v0.1 ships without any GeoIP capability.** Commands that would need it
  (`net geoip`, `net leak --exit-country`) are deferred to v0.2.
- **v0.2 adopts ip-api.com** as the default GeoIP provider. Rationale:
  no signup, documented no-log policy, well-suited to a CLI that integrates
  into sysadmin scripts.
- Users who prefer offline lookups can wire MaxMind themselves via a
  pluggable provider interface (post-v0.2).

## Consequences

**Positive**
- v0.1 ships smaller, faster, with no third-party signup required to use
  it.
- ip-api.com avoids the request-logging concern that comes with ipinfo.io.
- No EULA, no 70 MB asset, no MaxMind license key in the install path.

**Neutral**
- `net geoip` documented as v0.2 in CHANGELOG and README; users asking for
  it in v0.1 get a clear "coming in v0.2" hint.
- A pluggable provider interface will land in v0.2 to keep the door open
  for MaxMind / ipinfo / corporate proxies.

**Negative**
- Even in v0.2, ip-api.com's free tier (45 req/min) limits use in
  high-volume audits. Heavy users will need their own provider.
- HTTP dependency for what feels like a "local lookup" — users behind
  corporate proxies must configure them.

## Alternatives considered

- **Bundle MaxMind GeoLite2 in v0.1.** Adds EULA acceptance, license-key
  management, and a 70 MB asset to a tool whose other features are
  ~3 MB. Net value too low for v0.1.
- **Use ipinfo.io.** May 2025 changes — mandatory credit card on the free
  tier — make this hostile to drive-by adoption.
- **No GeoIP, ever.** Some leak-check scenarios genuinely need to confirm
  the exit country differs from the user's expected location. The check is
  worth shipping in v0.2.

## References

- [ip-api.com legal page](https://ip-api.com/docs/legal)
- [MaxMind GeoLite2 license](https://www.maxmind.com/en/end-user-license-agreement)
- [IPinfo alternatives summary, May 2025](https://www.iplocate.io/blog/ipinfo-alternatives-2026)
- Related: [Standalone OSS repository](./2026-05-28-separate-oss-repo.md)
