import RESTupdate as rup

#example of how to use the RESTupdate module to update a program
#This will currently only update one file or executable due to how the "cleanup" function is setup

#configuration data for the program to be updated
owner = 'amosquet' #rplace with the actual owner of the repository
repo = 'Random-Cypher' #replace with the actual repository name
current_version = 'v1.0.0' #replace with the current version of your program
file = 'RCCG.py' #replace with the actual name of the file with extension, as shown, to be updated
repow = str(owner+'/'+repo) #combine the owner and repository name to form the repository path
update_folder = "amcupdater" #name for the temporary directory to store the updated program

dir = rup.directory() #get the current directory of the program, used for moving the updated program to the original directory
# print(dir) #print the current directory of the program - for debugging purposes

#check if there are updates available for the program
if rup.check(current_version, repow): #True means out-of-date

    print("Updates available") #maybe temporary, for debugging purposes, but can be used to notify the user of updates
    rup.create_dir(update_folder)
    rup.clone(repow, update_folder)
    rup.cleanup(file, update_folder)
    print("Update successful") #maybe temporary, for debugging purposes, but can be used to notify the user of a successful update
    rup.py_restart(file) #for restarting python scripts
    # rup.exe_restart(file) #for restarting executables

else:
    print("No updates") #example of what to do if there are no updates available