import gitlab
import os
import subprocess

# Configuration
gitlab_url = 'https://your.gitlab.instance'  # Replace with your GitLab instance URL
private_token = 'YOUR_ACCESS_TOKEN'  # Replace with your personal access token
clone_directory = '/path/to/clone/directory'  # Replace with the path where you want to clone the repositories

# Initialize GitLab
gl = gitlab.Gitlab(gitlab_url, private_token=private_token)

# List all projects
projects = gl.projects.list(all=True)

# Clone each project
for project in projects:
    clone_path = os.path.join(clone_directory, project.path_with_namespace)
    if not os.path.exists(clone_path):
        print(f"Cloning {project.ssh_url_to_repo} into {clone_path}")
        subprocess.run(["git", "clone", project.ssh_url_to_repo, clone_path])
    else:
        print(f"Repository already exists: {clone_path}")

print("All projects cloned.")
