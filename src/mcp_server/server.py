import os

from dotenv import load_dotenv
from fastmcp import FastMCP

load_dotenv()

MCP_HOST = os.getenv("MCP_HOST", "localhost")
MCP_PORT = int(os.getenv("MCP_PORT", "8000"))
MCP_TRANSPORT = os.getenv("MCP_TRANSPORT", "http")


mcp = FastMCP(
    name="mcp-server",
    instructions="Describe what this MCP server does and how to use its tools.",
)


# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------


@mcp.tool()
def hello(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


# ---------------------------------------------------------------------------
# Resources
# ---------------------------------------------------------------------------


@mcp.resource("resource://info")
def server_info() -> str:
    """Basic information about this server."""
    return "MCP server template built with fastMCP."


# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------


@mcp.prompt()
def example_prompt(topic: str) -> str:
    """Generate a starter prompt about a topic."""
    return f"Tell me everything you know about {topic}."


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    mcp.run(transport=MCP_TRANSPORT,host=MCP_HOST,port=MCP_PORT)


if __name__ == "__main__":
    main()
