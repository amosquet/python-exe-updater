import requests
import subprocess
import os
import shutil

def directory():
    return os.path.dirname(os.path.realpath(__file__))

# def get_user():
#     return os.getlogin()
#     print(user)

def get_latest_version(repow):
    api_url = f"https://api.github.com/repos/{repow}/releases/latest"
    response = requests.get(api_url)
    response.raise_for_status()
    release_info = response.json()
    latest_version = release_info['tag_name']
    return latest_version

def check(current_version, repow):
    latest_version = get_latest_version(repow)
    return latest_version != current_version

def clone(repow, dir):
    subprocess.run(["git", "clone", f"https://github.com/{repow}.git", dir])


def create_dir(dir):
    #create a temporary update directory in the user's documents folder to temporarily store the updated program, if it doesn't exist. if it does, ignore
    os.makedirs("amcupdater", exist_ok=True)


def update(repow):
    
    clone(repow, "amcupdater")


def cleanup(dir, file):
    
    #close the program, file, and delete it
    os.remove(file)
    #move the updated program, file, from the temporary directory to the original directory
    shutil.move("amcupdater/"+file, dir)
    #delete the temporary directory
    shutil.rmtree("amcupdater", ignore_errors=True)
    #check to see if amcupdater is empty, if it is, delete it
    # if not os.listdir("amcupdater"):
    #     os.rmdir("amcupdater")

    #restart the program
    # os.system("python3 "+file) #for python files
    #run executable file
    os.system(file) #for executable files


# # Example usage
# owner = 'owner'  # Replace with the actual owner of the repository
# repo = 'repo'  # Replace with the actual repository name
# current_version = 'v1.0.0'  # Replace with the current version of your program
# file = 'program.py'  # Replace with the actual name of the file to be updated
# repow = 'owner/repo'  # Replace with the actual repository name
# # repo_url = f"https://github.com/{repow}.git"
# dir = directory()

# if check(current_version, repo):
#     update(True, repow, dir)
# else:
#     update(False, repow, dir)

owner = 'amosquet'  # Replace with the actual owner of the repository
repo = 'Random-Cypher'  # Replace with the actual repository name
current_version = 'v1.0.0'  # Replace with the current version of your program
file = 'RCCG.py'  # Replace with the actual name of the file to be updated
repow = str(owner+'/'+repo)  # Replace with the actual repository name
# repo_url = f"https://github.com/{repow}.git"
dir = directory()
print(dir)

if check(current_version, repow):
    print("Updates available")
    # user = get_user()
    create_dir(dir)
    update(repow)
    cleanup(dir, file)
    print("Update successful")
else:
    print("No updates")