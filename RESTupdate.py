import requests
import subprocess
import os
import shutil
import sys

#get the current directory of the program
def directory():
    return os.path.dirname(os.path.realpath(__file__))

#get the latest version of the program from the repository
def get_latest_version(repow):

    api_url = f"https://api.github.com/repos/{repow}/releases/latest"
    response = requests.get(api_url)
    response.raise_for_status()
    release_info = response.json()
    latest_version = release_info['tag_name']

    return latest_version

#check if there are updates available for the program. "True" means out-of-date
def check(current_version, repow):

    latest_version = get_latest_version(repow)

    return latest_version != current_version

#clone the repository to the temporary directory
def clone(repow, update_folder):
    subprocess.run(["git", "clone", f"https://github.com/{repow}.git", update_folder])

#create a temporary update directory in the current directory to temporarily store the updated program, if it doesn't exist. if it does, ignore
def create_dir(update_folder):
    os.makedirs(update_folder, exist_ok=True)

#cleanup the update process
def cleanup(file, update_folder):
    
    os.remove(file) #close the program, file, and delete it

    dir = directory() #get the current directory of the program
    shutil.move(update_folder+"/"+file, dir) #move the updated program, file, from the temporary directory to the original directory

#    shutil.rmtree(update_folder, ignore_errors=True) #delete the temporary directory

    #restart the program
    # os.system("python3 "+file) #for python files
    #run executable file
 #   os.system(file) #for executable files

#should restart the updated program then kill the old version.
def py_restart(file):
     subprocess.run(['python', file]) #for restarting python files
     sys.exit()
def exe_restart(file):
    subprocess.run([file]) #for restarting executables
    sys.exit()
