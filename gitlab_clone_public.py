import subprocess
import os
import json


def clone_all_repos(username):
    # Get a list of repositories
    repos_info = subprocess.run(["gh", "api", f"/users/{username}/repos"], capture_output=True, text=True)
    repos_info_json = json.loads(repos_info.stdout)

    if "message" in repos_info_json and repos_info_json["message"] == "Not Found":
        print("User not found or repositories not accessible.")
        return

    if isinstance(repos_info_json, list):
        # Iterate through each repository and clone it
        for repo_info in repos_info_json:
            repo_name = repo_info["name"]
            clone_url = repo_info["clone_url"]
            print(f"Cloning repository: {repo_name}")
            subprocess.run(["gh", "repo", "clone", clone_url])


# Replace 'Element84' with the desired GitHub username
clone_all_repos("target")
