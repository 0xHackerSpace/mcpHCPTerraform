from typing import Any

import httpx

from .config import settings


async def hcp_request(
    method: str,
    endpoint: str,
    *,
    params: dict[str, Any] | None = None,
    json: dict[str, Any] | None = None,
) -> Any:
    """Make an authenticated request to the HCP Terraform REST API.

    Args:
        method: HTTP method (GET, POST, PATCH, DELETE, etc.).
        endpoint: Path relative to HCP_URL, e.g. "/api/v2/organizations".
        params: Optional query parameters.
        json: Optional JSON body for POST/PATCH requests.

    Returns:
        Parsed JSON response.

    Raises:
        httpx.HTTPStatusError: On 4xx/5xx responses.
    """
    base_url = settings.hcp_api.url.rstrip("/")
    url = f"{base_url}{endpoint}"

    headers = {
        "Authorization": f"Bearer {settings.hcp_api.token}",
        "Content-Type": "application/vnd.api+json",
    }

    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=method.upper(),
            url=url,
            headers=headers,
            params=params,
            json=json,
        )
        response.raise_for_status()
        return response.json()
