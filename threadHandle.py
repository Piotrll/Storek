import threading as th
import connectionHandler as ch
import setup,sys
def threadManager(*args):
    #Setup---
    confLive = setup.loadConfig(False)
    #Is it time to rest yet?
    if args and args[0] == True:

        ch.connThreads(confLive, False)
        
        sys.exit()
        # call every thread to stop in here
    #and start here
    ch.connThreads(confLive, True)
    
    return 0