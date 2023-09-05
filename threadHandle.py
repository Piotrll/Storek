import threading as th
import connectionHandler as ch
import permissionHandler as ph
import setup,sys
def threadManager(*args):
    #Setup---
    confLive = setup.loadConfig(False)
    #Pausing -- 
    if args and args[0] == 2:
        #pause them
        ch.connThreads(confLive, False)
        ph.permThreads(confLive, False)
        return 0
    elif args and args[0] == 3:
        #unpause them
        ch.connThreads(confLive, 2)
        ph.permThreads(confLive, 2)
        return 0
    #Stoping ---
    elif args and args[0] == True:
        ch.connThreads(confLive, False)
        ph.permThreads(confLive, False)
        sys.exit()
        # call every thread to stop in here

    #and start here
    ch.connThreads(confLive, True)
    ph.permThreads(confLive, True)
    return 0