import tkinter as tk
from tkinter import ttk
import sys
import popUp as alert
import credHandle as ch
import classLib as cl
import coreApp as ca
import setup
import queryHandle as qh
def loginPanelInit(defConfig):
    global flag
    def closedWindow():
        rootLogin.destroy()
        sys.exit()
    """def flushConf():
        flag = 2
        rootLogin.destroy()"""
    def loginMe():
        global resultOfCompare
        userActive = cl.UserLoggin(loginEntered.get(),passwordEntered.get())
        userActive.db = baseToGo.get()
        tables = setup.checkConfig(userActive.db)
        permCheckList = qh.queryBase('select * from '+userActive.db+'.'+tables['usertable']+';')
        for perm in permCheckList:
            if perm[1] == userActive.login:
                userActive.perms = perm[3]
                break
        resultOfCompare = ch.compareCreds(userActive,defConfig)
        if resultOfCompare == 5:
            failCause.set('Błąd logowania')
        elif resultOfCompare == 4:
            failCause.set('Brak uprawnień')
        elif resultOfCompare == 0:
            setup.loggedUser(userActive)
            failCause.set('Logowanie udane')
            print("git")
            rootLogin.destroy()
            return 0
        
    
    flag = 0
    rootLogin = tk.Tk()
    rootLogin.title("Logowanie Storek")
    rootLogin.protocol("WM_DELETE_WINDOW", closedWindow)
    mainLabel = tk.Label(rootLogin, text = "Logowanie")
    inputFrame = tk.Frame(rootLogin)

    loginEntered = tk.StringVar()
    passwordEntered = tk.StringVar()
    failCause = tk.StringVar()
    baseToGo = tk.StringVar()
    loginEntryLabel = tk.Label(inputFrame, text = "Login")
    passwordEntryLabel = tk.Label(inputFrame, text = "Hasło")
    toGobaseLabel = tk.Label(inputFrame, text = "Wybierz baze")
    #flushConfigLabel = tk.Label(inputFrame, text = "Reset konfiguracji")
    loginEntry = tk.Entry(inputFrame, textvariable = loginEntered)
    passwordEntry = tk.Entry(inputFrame, textvariable = passwordEntered, show = '*')
    failLabel = tk.Label(inputFrame,textvariable = failCause)
    loginButton = tk.Button(inputFrame, text = "Zaloguj", command = loginMe)
    #flushConfig = tk.Button(inputFrame, text = "Reset", command = flushConf)

    possibleBases = ttk.Combobox(inputFrame, textvariable = baseToGo)
    possibleBasesVar = qh.queryBase("SELECT DISTINCT TABLE_SCHEMA FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA NOT IN ('information_schema', 'mysql', 'sys','performance_schema') ORDER BY TABLE_SCHEMA;")
    if possibleBasesVar == False:
        alert.popUpWarn(21)
    comboBaseValues = []
    for base in possibleBasesVar:
        comboBaseValues.append(base)
    possibleBases['values'] = comboBaseValues
    baseToGo.set(comboBaseValues[0][0])
    

    mainLabel.grid(column = 0, row = 0, columnspan = 3)
    inputFrame.grid(column = 0, row = 1, columnspan = 3, padx = 5)
    loginEntryLabel.grid(column = 0, row = 0)
    passwordEntryLabel.grid(column = 1, row = 0)
    loginEntry.grid(column = 0, row = 1, padx = 5)
    passwordEntry.grid(column = 1, row = 1, padx = 5)
    
    failLabel.grid(column = 0, row = 2, columnspan = 3)
    loginButton.grid(column = 0, row = 3,columnspan = 3, pady = 5)
    #flushConfigLabel.grid(column = 1, row = 4, pady = 5)
    toGobaseLabel.grid(column = 0, row = 4, pady = 5)
    possibleBases.grid(column = 0, row = 5, pady = 5)
    #flushConfig.grid(column = 1, row = 5)
    rootLogin.mainloop()
    return flag
    