"""xrayctl CLI entry point.

The actual subcommand implementations live in dedicated modules; this file
wires them into a Click group. v0.1 stubs raise NotImplementedError to fail
loudly until the corresponding lib module lands.
"""

from __future__ import annotations

import click

from xrayctl import __version__


@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
    help="Programmatic Happ deeplink builder + MCP server for the Xray/Reality stack.",
)
@click.version_option(__version__, prog_name="xrayctl")
def cli() -> None:
    """Top-level group."""


@cli.group()
def happ() -> None:
    """Happ deeplinks and routing profiles."""


@happ.command("build")
@click.option("--preset", required=False, help="Built-in preset name.")
@click.option("--from-file", "from_file", type=click.Path(exists=True), required=False)
def happ_build(preset: str | None, from_file: str | None) -> None:
    """Build a happ:// routing deeplink from a preset or file."""
    raise NotImplementedError("happ build — implementation pending in v0.1.0")


@happ.command("decode")
@click.argument("url")
def happ_decode(url: str) -> None:
    """Decode a happ:// routing deeplink back to JSON."""
    raise NotImplementedError("happ decode — implementation pending in v0.1.0")


@happ.command("validate")
@click.argument("path", type=click.Path(exists=True))
def happ_validate(path: str) -> None:
    """Validate a Happ routing JSON file against the schema."""
    raise NotImplementedError("happ validate — implementation pending in v0.1.0")


@cli.group()
def xray() -> None:
    """Xray subscription URLs and config validation."""


@xray.command("parse")
@click.argument("url")
def xray_parse(url: str) -> None:
    """Parse a vless:// URL into a structured config."""
    raise NotImplementedError("xray parse — implementation pending in v0.1.0")


@xray.command("validate")
@click.argument("path", type=click.Path(exists=True))
def xray_validate(path: str) -> None:
    """Validate an Xray JSON config (schema + optional `xray test`)."""
    raise NotImplementedError("xray validate — implementation pending in v0.1.0")


@cli.group()
def tmpl() -> None:
    """Cross-client subscription templates (SingBox/Mihomo/Clash/Stash)."""


@tmpl.command("validate")
@click.argument("client", type=click.Choice(["singbox", "mihomo", "clash", "stash"]))
@click.argument("path", type=click.Path(exists=True))
def tmpl_validate(client: str, path: str) -> None:
    """Validate a client-specific subscription template."""
    raise NotImplementedError(f"tmpl validate {client} — implementation pending in v0.1.0")


@cli.group()
def net() -> None:
    """Network diagnostics: ping, DNS, leak detection."""


@net.command("dns")
@click.option("--resolver", default="1.1.1.1", help="DNS resolver to query.")
@click.argument("hostname")
def net_dns(resolver: str, hostname: str) -> None:
    """Resolve a hostname via the given resolver (UDP/DoH/DoT)."""
    raise NotImplementedError("net dns — implementation pending in v0.1.0")


@net.command("ping")
@click.option("--proxy", required=False, help="SOCKS5 proxy URL.")
@click.argument("host")
def net_ping(proxy: str | None, host: str) -> None:
    """TCP-ping a host (optionally through a SOCKS5 proxy)."""
    raise NotImplementedError("net ping — implementation pending in v0.1.0")


@cli.group()
def config() -> None:
    """Inspect the .xrayctl.yaml config."""


@config.command("show")
def config_show() -> None:
    """Print the resolved config (from CWD, parents, or XRAY_TOOLKIT_CONFIG)."""
    raise NotImplementedError("config show — implementation pending in v0.1.0")


@cli.group()
def skill() -> None:
    """Manage the bundled Claude skill."""


@skill.command("install")
@click.option(
    "--target",
    type=click.Path(),
    default=".claude/skills/xrayctl",
    show_default=True,
    help="Destination directory for SKILL.md.",
)
def skill_install(target: str) -> None:
    """Copy SKILL.md into the target skills directory."""
    raise NotImplementedError("skill install — implementation pending in v0.1.0")


@cli.command("install-xray")
@click.option("--version", "version", default="latest", show_default=True)
def install_xray(version: str) -> None:
    """Download the Xray binary into ~/.cache/xrayctl/bin/."""
    raise NotImplementedError("install-xray — implementation pending in v0.1.0")


if __name__ == "__main__":
    cli()
