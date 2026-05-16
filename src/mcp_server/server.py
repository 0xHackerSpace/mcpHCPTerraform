import os


from .config import settings
from .tools import (
    get_organizations as _get_organizations,
    get_projects_by_org as _get_projects_by_org,
    get_project_details as _get_project_details,
    get_workspaces_by_org as _get_workspaces_by_org,
    get_by_org_workspace_details as _get_by_org_workspace_details,
    get_workspaces_details as _get_workspaces_details,
    get_workspace_resources as _get_workspace_resources,
)
from fastmcp import FastMCP



server = FastMCP(
    name="mcp-hcp-terraform",
    instructions="This mcp provides tools and resources for working with HCP Terraform.",
)


# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------


@server.tool(name="hello", description="Greet someone by name.")
def hello(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


# ORGANIZATION
@server.tool(name="get_organizations", description="Get a list of organizations in HCP Terraform.")
async def get_organizations() -> list[str]:
    """Return a list of organizations in HCP Terraform."""
    return await _get_organizations()


# PROJECT
@server.tool(name="get_projects_by_org", description="Get all projects for a given organization in HCP Terraform.")
async def get_projects_by_org(org_name: str) -> list[str]:
    """Return a list of projects for the given organization."""
    return await _get_projects_by_org(org_name)


@server.tool(name="get_project_details", description="Get details of a specific project in HCP Terraform.")
async def get_project_details(prj_name: str) -> dict:
    """Return details for the given project."""
    return await _get_project_details(prj_name)


# WORKSPACE
@server.tool(name="get_workspaces_by_org", description="Get all workspaces for a given organization in HCP Terraform.")
async def get_workspaces_by_org(org_name: str) -> list[str]:
    """Return a list of workspaces for the given organization."""
    return await _get_workspaces_by_org(org_name)


@server.tool(name="get_by_org_workspace_details", description="Get details of a specific workspace by organization and workspace name in HCP Terraform.")
async def get_by_org_workspace_details(org_name: str, wsp_name: str) -> dict:
    """Return details for the given workspace within an organization."""
    return await _get_by_org_workspace_details(org_name, wsp_name)


@server.tool(name="get_workspaces_details", description="Get details of a specific workspace by workspace ID in HCP Terraform.")
async def get_workspaces_details(wsp_id: str) -> dict:
    """Return details for the given workspace by ID."""
    return await _get_workspaces_details(wsp_id)

@server.tool(name="get_workspace_resources", description="Get details of a specific workspace by workspace ID in HCP Terraform.")
async def get_workspace_resources(wsp_id: str, page_number: str = "1") -> dict:
    """Return details for the given workspace by ID."""
    return await _get_workspace_resources(wsp_id,page_number)


# ---------------------------------------------------------------------------
# Resources
# ---------------------------------------------------------------------------


@server.resource("resource://info")
def server_info() -> str:
    """Basic information about this server."""
    return "MCP server template built with fastMCP."


# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------


@server.prompt()
def example_prompt(topic: str) -> str:
    """Generate a starter prompt about a topic."""
    return f"Tell me everything you know about {topic}."
