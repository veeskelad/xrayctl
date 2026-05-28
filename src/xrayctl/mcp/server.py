"""xrayctl MCP server.

Exposes the lib/* functionality over the Model Context Protocol using
FastMCP. v0.1 ships with a single smoke-test tool; real tools land alongside
their lib counterparts.
"""

from __future__ import annotations

from fastmcp import FastMCP

from xrayctl import __version__

mcp: FastMCP = FastMCP(
    name="xrayctl",
    version=__version__,
    instructions=(
        "Build and validate Happ deeplinks, VLESS subscription URLs, "
        "Xray configs, and cross-client templates. Run network diagnostics. "
        "Reads .xrayctl.yaml from CWD or XRAY_TOOLKIT_CONFIG for project context."
    ),
)


@mcp.tool()
def version() -> str:
    """Return the running xrayctl version."""
    return __version__


def main() -> None:
    """Entry point for the xrayctl-mcp script."""
    mcp.run()


if __name__ == "__main__":
    main()
