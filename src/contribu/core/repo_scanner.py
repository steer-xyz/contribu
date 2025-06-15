from typing import List
import httpx
from contribu.core.models.profile import UserProfile

GITHUB_SEARCH_URL = "https://api.github.com/search/repositories"

def fetch_repos(profile: UserProfile, max_repos=10) -> List[dict]:
    query = "+".join(profile.interests)
    url = f"{GITHUB_SEARCH_URL}?q={query}&sort=stars&order=desc&per_page={max_repos}"

    headers = {"Accept": "application/vnd.github+json"}

    response = httpx.get(url, headers=headers)
    response.raise_for_status()

    repos = response.json().get("items", [])
    return [
        {
            "name": repo["full_name"],
            "url": repo["html_url"],
            "description": repo["description"],
            "stars": repo["stargazers_count"]
        }
        for repo in repos
    ]
