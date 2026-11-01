#!/usr/bin/env python3
"""Offline validation for repository-owned agent and MCP configuration."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import parse_qsl, unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
PLACEHOLDER = re.compile(r"\$\{([A-Z][A-Z0-9_]*)\}")
MARKDOWN_LINK = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
SECRET_QUERY_KEYS = {"token", "usertoken", "api_key", "apikey", "access_token"}


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def read_env_example(errors: list[str]) -> set[str]:
    path = ROOT / ".env.example"
    if not path.is_file():
        fail(".env.example is missing", errors)
        return set()

    names: set[str] = set()
    for line_number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            fail(f".env.example:{line_number}: expected KEY=value", errors)
            continue
        name, _ = line.split("=", 1)
        if not re.fullmatch(r"[A-Z][A-Z0-9_]*", name):
            fail(f".env.example:{line_number}: invalid environment key {name!r}", errors)
            continue
        if name in names:
            fail(f".env.example:{line_number}: duplicate environment key {name}", errors)
        names.add(name)
    return names


def validate_mcp_config(env_names: set[str], errors: list[str]) -> None:
    path = ROOT / ".mcp.json"
    try:
        config = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        fail(f".mcp.json cannot be parsed: {exc}", errors)
        return

    servers = config.get("mcpServers") if isinstance(config, dict) else None
    if not isinstance(servers, dict) or not servers:
        fail(".mcp.json must contain a non-empty mcpServers object", errors)
        return

    for name, spec in servers.items():
        if not isinstance(name, str) or not name.strip() or not isinstance(spec, dict):
            fail(f".mcp.json: invalid server entry {name!r}", errors)
            continue

        has_command = isinstance(spec.get("command"), str) and bool(spec["command"].strip())
        has_url = isinstance(spec.get("url"), str) and bool(spec["url"].strip())
        if has_command == has_url:
            fail(f".mcp.json: server {name!r} must define exactly one of command or url", errors)
        if has_command and not isinstance(spec.get("args", []), list):
            fail(f".mcp.json: server {name!r} args must be an array", errors)
        if has_url:
            raw_url = spec["url"]
            for variable in PLACEHOLDER.findall(raw_url):
                if variable not in env_names:
                    fail(f".mcp.json: {name!r} references {variable}, missing from .env.example", errors)
            if not PLACEHOLDER.fullmatch(raw_url):
                parsed = urlsplit(raw_url)
                if parsed.scheme != "https" and not (
                    parsed.scheme == "http" and parsed.hostname in {"localhost", "127.0.0.1", "::1"}
                ):
                    fail(f".mcp.json: {name!r} must use HTTPS or loopback HTTP", errors)
                if any(key.casefold() in SECRET_QUERY_KEYS for key, _ in parse_qsl(parsed.query)):
                    fail(f".mcp.json: {name!r} must not embed credentials in a literal URL", errors)

        serialized = json.dumps(spec, ensure_ascii=False)
        for variable in PLACEHOLDER.findall(serialized):
            if variable not in env_names:
                fail(f".mcp.json: {name!r} references {variable}, missing from .env.example", errors)


def validate_env_gitignore(errors: list[str]) -> None:
    ignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
    if ".env" not in ignore or ".env.*" not in ignore:
        fail(".gitignore must exclude .env and .env.* files", errors)
    if "!.env.example" not in ignore:
        fail(".gitignore must explicitly keep the safe .env.example template", errors)


def validate_markdown_links(errors: list[str]) -> int:
    count = 0
    for markdown in sorted(ROOT.rglob("*.md")):
        if ".git" in markdown.parts:
            continue
        text = markdown.read_text(encoding="utf-8")
        text = re.sub(r"\x60{3}[\s\S]*?\x60{3}|~~~[\s\S]*?~~~", "", text)
        for match in MARKDOWN_LINK.finditer(text):
            target = match.group(1).strip().split(maxsplit=1)[0].strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("#") or not parsed.path:
                continue
            local = (markdown.parent / unquote(parsed.path)).resolve()
            count += 1
            if not local.exists():
                fail(
                    f"{markdown.relative_to(ROOT).as_posix()}: broken local link {target!r}",
                    errors,
                )
    return count


def main() -> int:
    errors: list[str] = []
    env_names = read_env_example(errors)
    validate_mcp_config(env_names, errors)
    validate_env_gitignore(errors)
    local_links = validate_markdown_links(errors)

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        json.dumps(
            {
                "status": "passed",
                "mcp_servers": len(
                    json.loads((ROOT / ".mcp.json").read_text(encoding="utf-8"))["mcpServers"]
                ),
                "environment_keys": len(env_names),
                "local_markdown_links_checked": local_links,
                "checks": [
                    "MCP JSON structure and transport",
                    "MCP environment variable declarations",
                    "secret-safe environment template and Git ignore rules",
                    "local Markdown link integrity",
                ],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
