
from .utils import hcp_request


# ORGANIZATION
async def get_organizations():
    return await hcp_request(method="GET",endpoint="/organizations")

# PROJECT
async def get_projects_by_org(org_name: str):
    return await hcp_request(method="GET",endpoint=f"/organizations/{org_name}/projects")
async def get_project_details(prj_name: str):
    return await hcp_request(method="GET",endpoint=f"/projects/{prj_name}")

# WORKSPACE
async def get_workspaces_by_org(org_name: str):
    return await hcp_request(method="GET",endpoint=f"/organizations/{org_name}/workspaces")

async def get_by_org_workspace_details(org_name: str,wsp_name: str):
    return await hcp_request(method="GET",endpoint=f"/organizations/{org_name}/workspaces/{wsp_name}")

async def get_workspaces_details(wsp_id: str):
    return await hcp_request(method="GET",endpoint=f"/workspaces/{wsp_id}")


# WORKSPACE RESOURCES
async def get_workspace_resources(wsp_id: str, params:str = None):
    params = {"page[number]": params} if params else None
    return await hcp_request(method="GET",endpoint=f"/workspaces/{wsp_id}/resources",params=params)
