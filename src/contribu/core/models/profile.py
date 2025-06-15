from pydantic import BaseModel
from typing import List
import json
from pathlib import Path

PROFILE_PATH = Path.home() / ".contribu_profile.json"

class UserProfile(BaseModel):
    name: str
    github_username: str
    email: str
    interests: List[str]

def save_profile(profile: UserProfile):
    PROFILE_PATH.write_text(profile.model_dump_json(indent=2))

def load_profile() -> UserProfile:
    return UserProfile.model_validate_json(PROFILE_PATH.read_text())


