from mcp_server.server import server
from mcp_server.config import settings


if __name__ == "__main__":
    transport = settings.server.transport
    if transport in ("http", "sse", "streamable-http"):
        server.run(
            transport=transport,
            host=settings.server.host,
            port=settings.server.port,
        )
    else:
        server.run(transport=transport)
