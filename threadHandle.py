import threading as th
import connectionHandler as ch
import permissionHandler as ph
import qConf as conf
import setup,sys
def setupThreads():
    res = conf.configSet('th','conn',0)
    if res == 1:
        return False
    res = conf.configSet('th','perm',0)
    if res == 1:
        return False
    res = conf.configSet('th','conf',0)
    if res == 1:
        return False
    return True
def stopThreads():
    res = conf.configSet('th','conn',1)
    if res == 1:
        return False
    res = conf.configSet('th','perm',1)
    if res == 1:
        return False
    res = conf.configSet('th','conf',1)
    if res == 1:
        return False
    return True
def threadManager(*args):
    #Setup---
    confLive = setup.loadConfig(False)
    ch.connThreads(confLive, True)
    ph.permThreads(confLive, True)
    conf.cycleConfCheck(confLive)
    return 0