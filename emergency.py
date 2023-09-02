import tkinter as tk
import configparser as cp
import os
import sys
import re
import credHandle as ch
import popUp as alert

def askForConf():
    def closedWindow():
        rootAskForConf.destroy()
        sys.exit()
    def saveGivenConf():
        global configPath
        #configPath = os.path.join(sys._MEIPASS, 'config.ini')
        configPath = 'config.ini'
        ip = ipEntered.get()
        port = portEntered.get()
        ipPatern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        portPattern = r"^([1-9][0-9]{0,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$"
        ipRegex = re.match(ipPatern,ip)
        portRegex = re.match(portPattern,port)
        if not ipRegex or not portRegex:
            failLabel.set("Niepoprawny adres lub port")
        else:
            configHandle = cp.ConfigParser()
            configHandle.add_section('conn')
            configHandle.add_section('session')
            configHandle['conn']['ip'] = ip
            configHandle['conn']['port'] = port
            configHandle['conn']['login'] = "default"
            passwd = '';
            configHandle['conn']['passwd'] = str(passwd)
            configHandle['conn']['db'] = ""
            configHandle['session']['user'] = "default"
            if os.path.exists(configPath):
                os.remove(configPath)
            with open(configPath, 'w') as configHandlerWrite:
                configHandle.write(configHandlerWrite)
            rootAskForConf.destroy()
    alert.popUpWarn(10)
    rootAskForConf = tk.Tk()
    rootAskForConf.title("Storek Konfiguracja")
    rootAskForConf.protocol("WM_DELETE_WINDOW", closedWindow)
    ipEntered = tk.StringVar(value = "127.0.0.1")
    portEntered = tk.StringVar(value = "1234")
    failText = tk.StringVar()
    mainLabel = tk.Label(rootAskForConf, text = "Ustawienia", font = "24")
    ipLabel = tk.Label(rootAskForConf, text = "Adres serwera")
    portLabel = tk.Label(rootAskForConf, text = "Port kominikacji")
    ipEntry = tk.Entry(rootAskForConf, textvariable = ipEntered)
    portEntry = tk.Entry(rootAskForConf, textvariable = portEntered)
    failLabel = tk.Label(rootAskForConf,textvariable = failText)
    exitButton = tk.Button(rootAskForConf, text = "Wyjście", command = sys.exit)
    saveButton = tk.Button(rootAskForConf, text = "Zapisz", command = saveGivenConf)

    mainLabel.grid(column = 0, row = 0, columnspan = 2)
    ipLabel.grid(column = 0, row = 1)
    portLabel.grid(column = 1, row = 1)
    ipEntry.grid(column = 0, row = 2)
    portEntry.grid(column = 1, row = 2)
    failLabel.grid(column = 0, row = 4, columnspan = 2)
    exitButton.grid(column = 0, row = 3)
    saveButton.grid(column = 1, row = 3)

    rootAskForConf.mainloop()
    return True

    
            

