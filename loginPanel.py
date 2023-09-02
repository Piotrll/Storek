import tkinter as tk
from tkinter import ttk
import sys
import time
import credHandle as ch
import classLib as cl
import coreApp as ca
import setup
import queryHandle as qh
def loginPanelInit(defConfig):
    def closedWindow():
        rootLogin.destroy()
        sys.exit()
    def loginMe():
        global resultOfCompare
        userActive = cl.UserLoggin(loginEntered.get(),passwordEntered.get())
        userActive.db = baseToGo.get()
        resultOfCompare = ch.compareCreds(userActive,defConfig)
        if resultOfCompare == 5:
            failCause.set('Błąd logowania')
        elif resultOfCompare == 0:
            setup.loggedUser(userActive.login)
            failCause.set('Logowanie udane')
            print("git")
            rootLogin.destroy()
            return 0
        
        
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
    loginEntry = tk.Entry(inputFrame, textvariable = loginEntered)
    passwordEntry = tk.Entry(inputFrame, textvariable = passwordEntered, show = '*')
    failLabel = tk.Label(inputFrame,textvariable = failCause)
    loginButton = tk.Button(inputFrame, text = "Zaloguj", command = loginMe)

    possibleBases = ttk.Combobox(inputFrame, textvariable = baseToGo)
    possibleBasesVar = qh.queryMPKDB("SELECT DISTINCT TABLE_SCHEMA FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA NOT IN ('information_schema', 'mysql', 'sys','performance_schema') ORDER BY TABLE_SCHEMA;")
    comboBaseValues = []
    for base in possibleBasesVar:
        comboBaseValues.append(base)
    possibleBases['values'] = comboBaseValues
    baseToGo.set(defConfig.Db)
    possibleBases.grid(column = 0, row = 4, columnspan = 3, pady = 5)

    mainLabel.grid(column = 0, row = 0, columnspan = 3)
    inputFrame.grid(column = 0, row = 1, columnspan = 3, padx = 5)
    loginEntryLabel.grid(column = 0, row = 0)
    passwordEntryLabel.grid(column = 1, row = 0)
    loginEntry.grid(column = 0, row = 1, padx = 5)
    passwordEntry.grid(column = 1, row = 1, padx = 5)
    
    failLabel.grid(column = 0, row = 2, columnspan = 3)
    loginButton.grid(column = 0, row = 3, columnspan = 3, pady = 5)
    rootLogin.mainloop()
    return 0
    