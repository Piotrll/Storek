import tkinter as tk
from tkinter import ttk
import configparser as cp
import os
import sys
import re
import credHandle as ch
import queryHandle as qh
import popUp as alert

def askForNewBase(selectedBase):
    global configPath
    configPath ='config.ini'
    def saveNewBase():
        try:
            users = tablesUsers.get()
            storage = tablesStorage.get()
            
            configHandle = cp.ConfigParser()
            configHandle.read(configPath)
            configHandle.add_section(selectedBase)
            configHandle[selectedBase]['userTable'] = users
            configHandle[selectedBase]['storageTable'] = storage
            with open(configPath, 'w') as configHandlerWrite:
                configHandle.write(configHandlerWrite)
        except cp.NoOptionError:
            alert.popUpWarn(13)
        finally:
            newBase.destroy()
            return
    global newBaseTableForStorage,newBaseTableForStorage, tablesStorage, tablesUsers
    newBase = tk.Tk()
    tablesUsers = tk.StringVar()
    tablesStorage = tk.StringVar()
    failCause = tk.StringVar()
    newBaseTableForUsers = ttk.Combobox(newBase, textvariable = tablesUsers)
    newBaseTableForStorage = ttk.Combobox(newBase, textvariable = tablesStorage)
    labelForUsersCombo = tk.Label(newBase, text = "Tabela użytkowników")
    labelForStorageCombo = tk.Label(newBase, text = "Tabela magazynu")

    saveBaseConfButton = tk.Button(newBase, text = "Zapisz", command = saveNewBase)
    failLabel = tk.Label(newBase, textvariable = failCause)
    tablesList = []
    tablesInBase = qh.queryBase("SHOW TABLES FROM "+selectedBase+";")
    if tablesInBase is None:
        alert.popUpWarn(15)
    for table in tablesInBase:
        tablesList.append(table[0])
    newBaseTableForUsers['values'] = tablesList
    newBaseTableForStorage['values'] = tablesList
    tablesUsers.set(tablesList[0])
    tablesStorage.set(tablesList[1])
    labelForUsersCombo.grid(column = 0, row = 0)
    labelForStorageCombo.grid(column = 1, row = 0)
    newBaseTableForUsers.grid(column = 0, row = 1)
    newBaseTableForStorage.grid(column = 1, row = 1)
    saveBaseConfButton.grid(column = 0, row = 2, columnspan = 2)
    failLabel.grid(column = 0,row = 3, columnspan = 2)
    newBase.mainloop()
    return 
def askForConf():
    def dbConfig():
        def saveConf():
            if tablesStorage.get() == tablesUsers.get():
                failCause.set("Wybierz różne tabele")
                return
            users = tablesUsers.get()
            storage = tablesStorage.get()
            
            configHandle = cp.ConfigParser()
            configHandle.read(configPath)
            configHandle.add_section(firstBase.get())
            configHandle[firstBase.get()]['userTable'] = users
            configHandle[firstBase.get()]['storageTable'] = storage
            with open(configPath, 'w') as configHandlerWrite:
                configHandle.write(configHandlerWrite)
            rootFinalConf.destroy()
            return
        def configureBase():
            global tablesStorage, tablesUsers, failCause, rootFinalConf
            rootFinalConf = tk.Tk()
            rootFinalConf.title("Storek Konfiguracja")
            rootFinalConf.protocol("WM_DELETE_WINDOW", closedWindow)

            tablesUsers = tk.StringVar()
            tablesStorage = tk.StringVar()
            failCause = tk.StringVar()
            tableForUsers = ttk.Combobox(rootFinalConf, textvariable = tablesUsers)
            tableForStorage = ttk.Combobox(rootFinalConf, textvariable = tablesStorage)
            labelForUsersCombo = tk.Label(rootFinalConf, text = "Tabela użytkowników")
            labelForStorageCombo = tk.Label(rootFinalConf, text = "Tabela magazynu")
            saveBaseConfButton = tk.Button(rootFinalConf, text = "Zapisz", command = saveConf)
            failLabel = tk.Label(rootFinalConf, textvariable = failCause)
            tablesList = []
            tablesInBase = qh.queryBase('SHOW TABLES;')
            for table in tablesInBase:
                tablesList.append(table)
            tableForUsers['values'] = tablesList
            tableForStorage['values'] = tablesList

            labelForUsersCombo.grid(column = 0, row = 0)
            labelForStorageCombo.grid(column = 1, row = 0)
            tableForUsers.grid(column = 0, row = 1)
            tableForStorage.grid(column = 1, row = 1)
            saveBaseConfButton.grid(column = 0, row = 2, columnspan = 2)
            failLabel.grid(column = 0,row = 3, columnspan = 2)
            rootFinalConf.mainloop()
            return
        def saveBase():
            configHandle = cp.ConfigParser()
            configHandle.read(configPath)
            configHandle['conn']['db'] = firstBase.get()
            with open(configPath, 'w') as configHandlerWrite:
                configHandle.write(configHandlerWrite)
            rootDbConf.destroy()
            configureBase()   
            return 
        rootDbConf = tk.Tk()
        rootDbConf.title("Storek Konfiguracja")
        rootDbConf.protocol("WM_DELETE_WINDOW", closedWindow)
        firstBase = tk.StringVar()
        basesToChooseLabel = tk.Label(rootDbConf, text = "Wybierz baze")
        basesToChoose = ttk.Combobox(rootDbConf, textvariable = firstBase)
        proceedButton = tk.Button(rootDbConf, text = "Dalej", command = saveBase)
        basesPossible = []

        databases = qh.queryServer('SHOW DATABASES;')

        databasesSanitize = [db[0] for db in databases if not db[0].startswith(("mysql", "sys", "information_schema", "performance_schema"))]
        if not databasesSanitize:
            alert.popUpWarn(12)
            rootDbConf.destroy()
            connectionConf()
        firstBase.set(databasesSanitize[0])
        for db in databasesSanitize:
            basesPossible.append(db)
        basesToChoose['values'] = basesPossible

        basesToChooseLabel.grid(column = 0, row = 0)
        basesToChoose.grid(column = 0, row = 1)
        proceedButton.grid(column = 0, row = 2)
        rootDbConf.mainloop()
        return
    def closedWindow():
        sys.exit()
    def connectionConf():
        global configPath
        #configPath = os.path.join(sys._MEIPASS, 'config.ini')
        configPath = 'config.ini'
        ip = ipEntered.get()
        port = portEntered.get()
        masterLogin = masterLoginEntered.get()
        masterPasswd = masterPasswdEntered.get()
        ipPatern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        portPattern = r"^([1-9][0-9]{0,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$"
        ipRegex = re.match(ipPatern,ip)
        portRegex = re.match(portPattern,port)
        if not ipRegex or not portRegex:
            failLabel.set("Niepoprawny adres lub port")
        elif masterLogin == "" or masterPasswd == "":
            failLabel.set("Podaj login i hasło bazy MYSQL")
        else:
            configHandle = cp.ConfigParser()
            configHandle.add_section('conn')
            configHandle['conn']['ip'] = ip
            configHandle['conn']['port'] = port
            configHandle['conn']['login'] = masterLogin
            configHandle['conn']['passwd'] = masterPasswd
            if os.path.exists(configPath):
                os.remove(configPath)
            with open(configPath, 'w') as configHandlerWrite:
                configHandle.write(configHandlerWrite)
            rootAskForConf.destroy()
            dbConfig()
            return
    alert.popUpWarn(10)
    rootAskForConf = tk.Tk()
    rootAskForConf.title("Storek Konfiguracja")
    rootAskForConf.protocol("WM_DELETE_WINDOW", closedWindow)
    ipEntered = tk.StringVar(value = "127.0.0.1")
    portEntered = tk.StringVar(value = "1234")
    masterLoginEntered = tk.StringVar()
    masterPasswdEntered = tk.StringVar()
    failText = tk.StringVar()
    mainLabel = tk.Label(rootAskForConf, text = "Ustawienia", font = "24")
    ipLabel = tk.Label(rootAskForConf, text = "Adres serwera")
    portLabel = tk.Label(rootAskForConf, text = "Port kominikacji")
    masterLoginLabel = tk.Label(rootAskForConf, text = "Login SQL")
    masterPasswdLabel = tk.Label(rootAskForConf, text = "Hasło SQL")
    ipEntry = tk.Entry(rootAskForConf, textvariable = ipEntered)
    portEntry = tk.Entry(rootAskForConf, textvariable = portEntered)
    masterLoginEntry = tk.Entry(rootAskForConf, textvariable = masterLoginEntered)
    masterPasswdEntry = tk.Entry(rootAskForConf, textvariable = masterPasswdEntered, show = '*')
    failLabel = tk.Label(rootAskForConf,textvariable = failText)
    exitButton = tk.Button(rootAskForConf, text = "Wyjście", command = sys.exit)
    saveButton = tk.Button(rootAskForConf, text = "Zapisz", command = connectionConf)

    mainLabel.grid(column = 0, row = 0, columnspan = 2)
    ipLabel.grid(column = 0, row = 1)
    portLabel.grid(column = 1, row = 1)
    masterLoginLabel.grid(column = 0, row = 3)
    masterPasswdLabel.grid(column = 1, row = 3)
    ipEntry.grid(column = 0, row = 2)
    portEntry.grid(column = 1, row = 2)
    masterLoginEntry.grid(column = 0,row = 4)
    masterPasswdEntry.grid(column = 1,row = 4)
    failLabel.grid(column = 0, row = 6, columnspan = 2)
    exitButton.grid(column = 0, row = 5)
    saveButton.grid(column = 1, row = 5)

    rootAskForConf.mainloop()
    return True

    
            

