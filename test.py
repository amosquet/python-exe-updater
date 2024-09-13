import RESTupdate

import requests
import subprocess
import os
import shutil




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