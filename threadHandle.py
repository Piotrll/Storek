import threading as th
import connectionHandler as ch
import permissionHandler as ph
import setup,sys
def threadManager(*args):
    #Setup---
    confLive = setup.loadConfig(False)
    #Is it time to rest yet?
    if args and args[0] == True:

        ch.connThreads(confLive, False)
        ph.permThreads(confLive, False)
        sys.exit()
        # call every thread to stop in here
    #and start here
    ch.connThreads(confLive, True)
    ph.permThreads(confLive, True)
    return 0