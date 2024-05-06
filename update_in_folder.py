import os
import subprocess


def update_repos_in_folder(folder_path):
    # Get a list of all directories (repositories) within the folder
    repos = [d for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d))]

    # Iterate through each repository and update it
    for repo in repos:
        repo_path = os.path.join(folder_path, repo)
        print(f"Updating repository: {repo}")
        # Change directory to the repository path
        os.chdir(repo_path)
        # Run git pull to update the repository
        subprocess.run(["git", "pull"])


# Replace 'element84' with the folder name containing your cloned repositories
update_repos_in_folder("element84")
