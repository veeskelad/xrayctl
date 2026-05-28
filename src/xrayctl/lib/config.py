"""Load and validate the .xrayctl.yaml user config.

The config carries env-variable *names* and paths — never real secrets. CLI
and MCP both resolve values from the environment at runtime.
"""

from __future__ import annotations

import os
from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict, Field

CONFIG_FILENAME = ".xrayctl.yaml"
CONFIG_ENV_VAR = "XRAY_TOOLKIT_CONFIG"


class RemnawaveConfig(BaseModel):
    """Remnawave panel connection hints (env-var names, not values)."""

    model_config = ConfigDict(extra="forbid")

    base_url_env: str = "REMNAWAVE_BASE_URL"
    token_env: str = "REMNAWAVE_API_TOKEN"
    readonly: bool = True


class XrayctlConfig(BaseModel):
    """Top-level .xrayctl.yaml schema."""

    model_config = ConfigDict(extra="forbid")

    default_proxy_env: str | None = None
    remnawave: RemnawaveConfig | None = None
    notes: list[str] = Field(default_factory=list)
    templates: dict[str, str] = Field(default_factory=dict)


def find_config(start: Path | None = None) -> Path | None:
    """Locate `.xrayctl.yaml`.

    Lookup order:
    1. `$XRAY_TOOLKIT_CONFIG` if set and exists.
    2. CWD and parents up to the filesystem root.
    """
    env_path = os.environ.get(CONFIG_ENV_VAR)
    if env_path:
        candidate = Path(env_path).expanduser()
        if candidate.is_file():
            return candidate
        return None

    current = (start or Path.cwd()).resolve()
    for directory in (current, *current.parents):
        candidate = directory / CONFIG_FILENAME
        if candidate.is_file():
            return candidate
    return None


def load_config(path: Path | None = None) -> XrayctlConfig:
    """Load `.xrayctl.yaml` from `path` or via `find_config`.

    Returns a default-empty config when no file is found — callers that need
    a project to declare itself should check `find_config()` first.
    """
    resolved = path or find_config()
    if resolved is None:
        return XrayctlConfig()

    with resolved.open("r", encoding="utf-8") as fh:
        raw = yaml.safe_load(fh) or {}
    return XrayctlConfig.model_validate(raw)
