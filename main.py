import tkinter as tk
from tkinter import ttk
import coreApp as core
import sys
import time
import psutil
import popUp as alert
import threadHandle as thh


def init():
    proces = checkForOtherInstances()
    if proces:
        alert.popUpWarn(1)
        time.sleep(5)
        sys.exit()
    else:
        errorCode = core.callAppCore()
        if errorCode != 0:
            alert.popUpWarn(errorCode)
            sys.exit()
        thh.threadManager()
        if core.callLogedView() == False:
            alert.popUpWarn(13)

def checkForOtherInstances():
    i = 0 
    processName = "Storek"
    processNameWin = "Storek.exe"
    for proc in psutil.process_iter():
        try:
            #print(proc)
            if processName in proc.name():
                i += 1
            elif processNameWin.lower() in proc.name().lower():
                i += 1
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    if i > 1:
        return True
    else:
        return False
    
init()

"""
def checkForOtherInstances():
    try:
        win32ui.FindWindow("Storek", None)
    except win32ui.error:
        return False
    else:
        return True
"""