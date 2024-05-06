import os
import subprocess

# Configuration: Replace with your GitHub details
github_username = "YOUR_GITHUB_USERNAME"
clone_directory = '/path/to/clone/directory'

# Authenticate with GitHub (if you haven't already)
subprocess.run(["gh", "auth", "login"])

# List all your accessible repositories
projects = subprocess.run(["gh", "repo", "list", github_username], capture_output=True, text=True).stdout.splitlines()

# Clone each project
for project_slug in projects:
    clone_path = os.path.join(clone_directory, project_slug)
    if not os.path.exists(clone_path):
        print(f"Cloning https://github.com/{project_slug} into {clone_path}")
        subprocess.run(["gh", "repo", "clone", project_slug, clone_path])
    else:
        print(f"Repository already exists: {clone_path}")

print("All projects cloned.")
