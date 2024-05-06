import os
import subprocess


def update_repositories(root_directory):
    """
    Update all GitHub repositories in the given root directory using the GitHub CLI.
    """
    # Find all .git directories
    for dirpath, dirnames, filenames in os.walk(root_directory):
        if '.git' in dirnames:
            print(f"Updating repository in {dirpath}")

            # Change to the repository directory
            os.chdir(dirpath)

            # Fetch remote changes (avoids unnecessary merge commits)
            subprocess.run(['gh', 'repo', 'sync'], check=True)

            # Change back to the root directory
            os.chdir(root_directory)


# Path to the root directory containing all your git repositories
root_dir = '/path/to/your/repositories'

update_repositories(root_dir)
