# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2026-05-15

### Added

- Initial MCP server with `hello` tool, `resource://info` resource, and `example_prompt` prompt (`fastMCP`)
- `pyproject.toml` with `fastmcp` and `python-dotenv` dependencies; `uv.lock` for reproducible installs
- `.env.example` documenting transport (`stdio` / `sse` / `streamable-http`) and API key configuration
- `.gitignore` covering Python bytecode, virtual environments, uv artifacts, and IDE files

[Unreleased]: https://github.com/0xHackerSpace/mcpTemplate/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/0xHackerSpace/mcpTemplate/releases/tag/v0.1.0
