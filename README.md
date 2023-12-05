# GitLab Project Cloner
This script allows you to clone multiple projects from an on-prem GitLab instance using SSH. It uses the GitLab API to list all projects and then clones them to a specified directory. To use this script, you must have an SSH key added to your GitLab account.

## Prerequisites
- Python 3.6 or higher
- Conda (Miniconda or Anaconda)
- Git
- SSH Key added to your GitLab account

##Setting up the Environment
### Install Conda
If you don't have Conda installed, download and install it from Miniconda or Anaconda.

### Create and Activate a Conda Environment   
Open your terminal (or Anaconda Prompt on Windows).   
Create a new Conda environment: ```conda create -n gitlab_clone_env python=3.8```   
Activate the environment: ```conda activate gitlab_clone_env```   
### Install Required Package   
Within the activated environment, install python-gitlab using pip install python-gitlab.   

## SSH Key Setup
Ensure you have an SSH key generated and added to your GitLab account. If you do not have an SSH key or have not added it to GitLab, follow these steps:    

Generate an SSH Key (if you don't have one): ```ssh-keygen -t rsa -b 4096 -C "your_email@example.com"```  
Copy the SSH key to your clipboard: ```pbcopy < ~/.ssh/id_rsa.pub```  
Add the SSH key to your GitLab account under the SSH Keys section in your user settings.  
## Configuration
### GitLab Personal Access Token:
Create a Personal Access Token in GitLab with API access and note the token for the script.   

### Script Setup:   
Save the provided Python script as gitlab_clone.py. Replace the necessary fields with your GitLab instance URL, your personal access token, and the path where you want to clone the repositories.   

## Running the Script
Open the terminal or command prompt.   
Navigate to the directory containing gitlab_clone.py.   
Ensure the Conda environment is activated: ```conda activate gitlab_clone_env```   
Run the script: ```python3 gitlab_clone.py```   
Monitor the terminal for progress updates. The script will clone each project into the specified directory using SSH.   
## Deactivating the Environment (Optional)   
After running the script, you can deactivate the Conda environment: conda deactivate   

##  Troubleshooting   
Ensure you have sufficient permissions and storage space for cloning the repositories.   
Check that your Personal Access Token has the correct permissions.   
Verify that your GitLab instance URL and clone directory path are correctly set in the script.   
Make sure your SSH key is correctly set up and added to your GitLab account.   
