# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

## [0.2.0] - 2026-05-16

### Added
- `hcp_request` helper in `utils.py` for authenticated HCP Terraform REST API calls
- Tools for organizations, projects, and workspaces (read operations) in `tools.py`
  - `get_organizations` — list all organizations
  - `get_projects_by_org` — list projects for an organization
  - `get_project_details` — get details of a specific project
  - `get_workspaces_by_org` — list workspaces for an organization
  - `get_by_org_workspace_details` — get workspace details by org and workspace name
  - `get_workspaces_details` — get workspace details by workspace ID
  - `get_workspace_resources` — list resources for a workspace
- Registered all tools on the FastMCP server in `server.py`
- Usage instructions in `README.md`

## [0.1.0] - 2026-05-16

### Added
- Base configuration (`config.py`) with HCP API settings
- Initial FastMCP server scaffolding (`server.py`)
- Project entry point (`src/main.py`)
- Initial project structure and dependencies (`pyproject.toml`)
