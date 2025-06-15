from contribu.core.models.profile import load_profile
from contribu.core.repo_scanner import fetch_repos

def run():
    print("🔍 Finding open source repos based on your profile...\n")
    profile = load_profile()
    repos = fetch_repos(profile)

    for i, repo in enumerate(repos, 1):
        print(f"{i}. {repo['name']} ⭐️ {repo['stars']}")
        print(f"   {repo['description']}")
        print(f"   {repo['url']}\n")
