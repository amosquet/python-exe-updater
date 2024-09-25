# python exe updater
 Updater for python executables, can also be used to update non-python executables, like scripts


 RESTupdate.py contains a current, mostly, working build of the updater.
 
 Rtest.py is an example of how to implement RESTupdate in an updater.

 To implement this inside of your script or executable, you can can call the updater directly from your main script or executable, it does not have to be a separate application.
 For example, you could place the entirety of the code in "Rtest.py" at the start of your main function if you wanted to automatically check for updates on launch.

 Alternatively you can run it as a separate process but you would have to modify it to be compatible for that scenario.