"""Sanity checks proving the package imports and CLI/MCP entry points wire up."""

from __future__ import annotations

from click.testing import CliRunner

from xrayctl import __version__
from xrayctl.cli.main import cli
from xrayctl.mcp.server import mcp


def test_version_string() -> None:
    assert isinstance(__version__, str)
    assert __version__


def test_cli_help_lists_groups() -> None:
    result = CliRunner().invoke(cli, ["--help"])
    assert result.exit_code == 0
    for group in ("happ", "xray", "tmpl", "net", "config", "skill", "install-xray"):
        assert group in result.output


def test_cli_version_flag() -> None:
    result = CliRunner().invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.output


def test_mcp_server_importable() -> None:
    assert mcp is not None
