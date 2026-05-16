import os

from dataclasses import dataclass
from functools import lru_cache

from dotenv import load_dotenv

load_dotenv()


MCP_HOST = os.getenv("MCP_HOST", "localhost")
MCP_PORT = int(os.getenv("MCP_PORT", "8000"))
MCP_TRANSPORT = os.getenv("MCP_TRANSPORT", "http")


HCP_URL = os.getenv("HCP_URL", "")
HCP_TOKEN = os.getenv("HCP_TOKEN", "")



@dataclass(frozen=True)
class HCPApiConfig:
    url: str
    token: str


@dataclass(frozen=True)
class ServerConfig:
    host: str
    port: int
    transport: str


@dataclass(frozen=True)
class Settings:
    hcp_api: HCPApiConfig
    server: ServerConfig


    def __init__(self, hcp_api: HCPApiConfig, server: ServerConfig):
        object.__setattr__(self, 'hcp_api', hcp_api)
        object.__setattr__(self, 'server', server)

    def validate(self):
        errors = [] 
        
        if not self.hcp_api.url:
            errors.append("HCP API URL is required")
        if not self.hcp_api.token:
            errors.append("HCP API token is required")
        if not self.server.host:
            errors.append("Server host is required")
        if not self.server.port:
            errors.append("Server port is required")
        if not self.server.transport:
            errors.append("Server transport is required")
    
        if errors:
            raise ValueError("Invalid configuration: " + "; ".join(errors))
        

@lru_cache(maxsize=1)
def get_settings() -> Settings:
    hcp_api=HCPApiConfig(
        url=HCP_URL,
        token=HCP_TOKEN
    )

    server_config=ServerConfig(
        host=MCP_HOST,
        port=MCP_PORT,
        transport=MCP_TRANSPORT
    )

    return Settings(
        hcp_api=hcp_api,
        server=server_config
    )


settings = get_settings()