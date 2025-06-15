from pydantic import BaseModel

class GitHubRepo(BaseModel):
    full_name: str
    description: str | None
    url: str
    stars: int
