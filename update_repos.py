import os
import subprocess

def update_repositories(root_directory):
    """
    Update all git repositories in the given root directory.
    """
    # Find all .git directories
    for dirpath, dirnames, filenames in os.walk(root_directory):
        if '.git' in dirnames:
            print(f"Updating repository in {dirpath}")
            # Change to the repository directory
            os.chdir(dirpath)
            # Pull the latest changes
            try:
                subprocess.run(['git', 'pull'], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Failed to update repository in {dirpath}: {e}")
            # Change back to the root directory
            os.chdir(root_directory)

# Path to the root directory containing all your git repositories
root_dir = '/path/to/your/repositories'

update_repositories(root_dir)
