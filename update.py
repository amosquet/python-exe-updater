import subprocess, shutil, os

#get current directory of the file
def directory():
    return os.path.dirname(os.path.realpath(__file__))

#clone the latest release of the program from the repository to the directory
def clone(repo_url, dir):
    subprocess.run(["git", "-q", "clone", repo_url, dir])

#check the version of the program to the latest version on the repository
def check(current_version):
    subprocess.run(["git", "-q", "pull", "origin", "master"])
    with open(directory() + "/version.txt", "r") as file:
        version = file.read()
    if version != current_version:
        return True
    return False

def update(check, repo_url, dir):

    if check == True:
        
