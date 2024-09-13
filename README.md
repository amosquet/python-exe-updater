# python exe updater
 Updater for python executables, could also maybe be used to update non-python executables


 RESTupdate.py contains a current, mostly, working build of the updater.
 
 Rtest.py is an example of how to implement RESTupdate in an updater.
 
 NOTE: You would not have all of the code in Rtest be in your main program, it would be wiser to call the update check within your program
 and run the actual updating functions as its own independent application initially launched by your main program.

Clearer explaination of how this should be used:
 Check for updates in main program.
 Main program launches a separate application, if it is out of date, then kills itself
 This separate application then downloads the new version, cleans up and launches the new version, then kills itself (updater kills itself).
