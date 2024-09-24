import RESTupdate as rup
import subprocess
import sys
#example of how to use the RESTupdate module to update a program
#This will currently only update one file or executable due to how the "cleanup" function is setup

#configuration data for the program to be updated
owner = 'amosquet' #rplace with the actual owner of the repository
repo = 'Random-Cypher' #replace with the actual repository name
current_version = 'v1.0.0' #replace with the current version of your program
file = 'RCCG.py' #replace with the actual name of the file with extension, as shown, to be updated
repow = str(owner+'/'+repo) #replace with the actual repository name
update_folder = "amcupdater" #name for the temporary directory to store the updated program

dir = rup.directory() #get the current directory of the program, used for 
# print(dir) #print the current directory of the program - for debugging purposes

#check if there are updates available for the program
if rup.check(current_version, repow): #True means out-of-date
    print("Updates available") #maybe temporary
    # user = get_user()
    rup.create_dir(update_folder)
    # update(repow)
    rup.clone(repow, update_folder)
    rup.cleanup(file, update_folder)
    rup.py_restart(file) #for restarting python scripts
    run.exe_restart(file) #for restarting executables
    print("Update successful") #maybe temporary
else:
    print("No updates")







#OLD CODE FROM WHEN I FIRST STARTED

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
