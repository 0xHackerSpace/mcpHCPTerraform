import os




from .config import settings
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

