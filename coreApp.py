import sys
import popUp as alert
import classLib as cl
import setup
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import queryHandle as qh
import credHandle as ch
import emergency as emerg
import datetime
import permissionHandler as ph
import threadHandle as thh
def callAppCore():
    setup.callSettings()
    print("Settings done")
    return 0
def callLogedView():
    def closeApp():
        #thh.threadManager(True)
        sys.exit()
    def showSelectInfo(e):
        try:
            itemInfo.destroy()
        except:
            pass
        selectedItems = listOfStorage.selection()
        dataFromList = listOfStorage.item(selectedItems[0], "values")

        storageStatusInfoLocal = qh.queryBase("select * from "+confBase.Storage+" where id="+str(dataFromList[0])+";")
        storageFieldsInfoLocal = qh.queryBase("show fields from "+confBase.Storage+";")
        dataInfoNames = []
        actualValueLabels = []
        shownLabels = []
        varsForLabels = []
        itemValueVars = []

        itemInfo = tk.Frame(infoFrameInStorage)

        i = 0
        for columnForInfo in storageFieldsInfoLocal:
            dataInfoNames.append(columnForInfo[0])
        for labelName in dataInfoNames:
            varsForLabels.append(tk.StringVar())
            shownLabels.append(tk.Label(itemInfo, text = ""))
            shownLabels[i].config(text = labelName)
            shownLabels[i].grid(column = 0, row = i+1)
            i += 1
        i = 0
        for valueForInfo in storageStatusInfoLocal:
            dataInfoNames = valueForInfo
        for value in dataInfoNames:
            itemValueVars.append(tk.StringVar())
            actualValueLabels.append(tk.Label(itemInfo, text = ""))
            actualValueLabels[i].config(text = value)
            actualValueLabels[i].grid(column = 1, row = i+1)
            i += 1
        itemInfo.grid(row=1, column=0, sticky="nsew")
        root.update_idletasks()
    def initializeBaseData():    
        def statusBeutify():
            childs = listOfStorage.get_children()
            i = -1
            for column_id in listOfStorage["columns"]:
                column_name = listOfStorage.column(column_id)["id"]
                i += 1
                if column_name[0] == "status":
                    break
            try:
                for c in childs:
                    statNum = listOfStorage.item(c, "values")[i]
                    match statNum:
                        case '0':
                            listOfStorage.set(c,i,"Wolny")
                        case _:
                            pass
            except NameError:
                pass
        def contextMenuFunc(e):
            ItemId = listOfStorage.identify_row(e.y)
            if ItemId:
                context.tk_popup(e.x_root, e.y_root)
                global Item
                Item = ItemId
        def addItem():
            def doneAdding():
                root.destroy()
                callLogedView()
            def addEnteredItem():
                
                params1 = ""
                params2 = ""
                currentDate = datetime.date.today()
                dateForDb = currentDate.strftime('%Y-%m-%d')
                i = 0
                for column_id in localStorageFields:
                    if (column_id[0] == "ostatnio_uzyty"):
                        pass
                    else:
                        params1 += column_id[0]+","
                        i += 1

                params1 = params1[:-1]
                queryAddItems = "INSERT INTO "+confBase.Storage+" ("+params1+") VALUES ("
                i = 0
                for val in valuesVar:

                    if val.get().isdigit():
                        itemEntry = val.get()
                        params2 += itemEntry+","
                        i += 1
                    else:
                        itemEntry = val.get()
                        params2 += "\'"+itemEntry+"\',"
                        i += 1
                    
                for j in range(len(localColumnNames)-i):
                    if localColumnNames[i] == "dodajacy":
                        itemEntry = confLive.logedUser
                        params2 += "\'"+itemEntry+"\',"
                        i += 1
                    elif localColumnNames[i] == "data_wejscia":
                        itemEntry = dateForDb
                        params2 += "\'"+itemEntry+"\',"
                        i += 1
                params2 = params2[:-1]
                queryAddItems += params2+");"
                resultAdd = qh.queryBase(queryAddItems)
                if resultAdd == False:
                    resultAddingItem.set("Dodawanie nie udane")
                else:
                    resultAddingItem.set("Dodano pozycje")
            localStorageFields = qh.queryBase("show fields from "+confBase.Storage+";")
            windowAddItem = tk.Toplevel(width = 300, height = 600)
            windowAddItem.protocol("WM_DELETE_WINDOW", doneAdding)
            frameAdding = tk.LabelFrame(windowAddItem, text = "Dodaj pozycje")
            frameAdding.grid(column = 0, row = 0)
            i = -1
            nameItemLabel = []
            nameItemEntry = []
            valuesVar = []
            localColumnNames = []
            addingStatusVar = tk.StringVar()
            resultAddingItem = tk.StringVar()
            addingStatusVar.set("Wolny")
            for column_id in localStorageFields:
                localColumnNames.append(column_id[0])
                if (column_id[0] == "status") or (column_id[0] == "dodajacy") or (column_id[0] == "data_wejscia") or (column_id[0] == "ostatnio_uzyty"):
                    pass
                else:
                    i += 1
                    valuesVar.append(tk.StringVar())
                    nameItemLabel.append(tk.Label(frameAdding, text = column_id[0]))
                    nameItemLabel[i].grid(column = 0, row = i)
                    nameItemEntry.append(tk.Entry(frameAdding, textvariable = valuesVar[i]))
                    nameItemEntry[i].grid(column = 1, row = i, pady = 5)
            i += 1
            for column_id in localStorageFields:
                if column_id[0] == "status":
                    valuesVar.append(tk.StringVar())
                    statusCombo = ttk.Combobox(frameAdding, textvariable=valuesVar[i])
                    statusCombo['values'] = ('Wolny', 'W użyciu', 'Uszkodzony', 'Zarezewowany')  # 0, 1, 2, 3
                    statusCombo.grid(column=1, row=i, pady=5)
                    break
                    
                #if column_id[1] == "date":
                    # if len(date_str) != 10 or date_str[4] != '-' or date_str[7] != '-':
                
            addButton = tk.Button(frameAdding, text = "Dodaj", command = addEnteredItem)
            addButton.grid(column = 0, row = i+1, columnspan = 2)
            succesLabel = tk.Label(frameAdding, textvariable = resultAddingItem)
            succesLabel.grid(column = 0, row = i+2, columnspan = 2)
        def deleteItem():
            if Item:
                valOfItem = listOfStorage.item(Item, "values")[0]
                youSureMes = listOfStorage.item(Item, "values")[1]
                confirm = tk.messagebox.askyesno("Potwierdzenie", f"Jesteś pewny że chcesz usunąć {youSureMes}'?")
            if confirm:
                params = (valOfItem,)
                res = qh.parameteredQuery("DELETE FROM "+confBase.Storage+" WHERE id = %s;", params)
                if not res:
                    return
                else:
                    listOfStorage.delete(Item)
                    listOfStorage.tag_configure(Item, background="red")
                    listOfStorage.update()

            else:
                return
        global listOfStorage
        if not ph.permCheck(confLive.permissionCode, 0):
            return False
        selectedBaseQ = "use " + confLive.Db +";"
        qh.queryBase(selectedBaseQ)
        storageStatus = qh.queryBase("select * from "+confBase.Storage+";")
        storageFields = qh.queryBase("show fields from "+confBase.Storage+";")

        while len(storageFields) > 4:
            storageFields.pop()
        #while len(storageStatus) > 4:
        #    storageStatus.pop()
        listOfStorage = ttk.Treeview(stuffFrame, columns= storageFields, show = 'headings')

        for col in storageFields:
            listOfStorage.heading(col, text = col[0])
        for stuff in storageStatus:
            listOfStorage.insert('',tk.END, values = stuff)

        listOfStorage.grid(column = 0, row = 0, sticky = "ns")
        scrollbar = ttk.Scrollbar(stuffFrame, orient="vertical", command=listOfStorage.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        context = tk.Menu(root, tearoff=0)
        context.add_command(label="Dodaj", command = addItem)
        context.add_command(label="Usuń", command = deleteItem)
        listOfStorage.configure(yscrollcommand=scrollbar.set)
        listOfStorage.bind("<Button-3>",lambda event:  contextMenuFunc(event))
        listOfStorage.bind("<ButtonRelease-1>", showSelectInfo)

        statusBeutify()
        return True
    def addRegister(confLive):
        def callAdding():
            newUser = cl.UserLoggin(newLoginVar.get(),newPasswdVar.get(),newPermVar.get())
            newUser.db = baseForUser.get()
            if newUser.db != confLive.Db:
                setup.databaseChange(newUser.db)
            if not ch.addUser(newUser):
                alert.popUpWarn(11)
            else:
                resultAddingUserVar.set("Użytkownik dodany")
                thh.threadManager(3)
        if not ph.permCheck(confLive.permissionCode,7):
            return False
        regFrame = tk.LabelFrame(settingsFrame, text = "Dodaj użytkownika")
        regFrame.grid(column = 0, row = 0)

        loginLabel = tk.Label(regFrame, text = "Nazwa")
        loginLabel.grid(column = 0, row = 0)
        passwdLabel = tk.Label(regFrame, text = "Hasło")
        passwdLabel.grid(column = 1, row = 0)
        dbLabel = tk.Label(regFrame, text = "Wybierz baze")
        dbLabel.grid(column = 2, row = 0)
        permLabel = tk.Label(regFrame, text = "Kod uprawnień")
        permLabel.grid(column = 0, row = 2)

        resultAddingUserVar = tk.StringVar()
        resultAddingUser = tk.Label(regFrame, textvariable = resultAddingUserVar)
        resultAddingUser.grid(column = 0, row = 4, columnspan= 3)

        newLoginVar = tk.StringVar()
        newPasswdVar = tk.StringVar()
        baseForUser = tk.StringVar()
        newPermVar = tk.IntVar()
        baseForUserList = []
        newLoginEntry = tk.Entry(regFrame, textvariable = newLoginVar)
        newPasswdEntry = tk.Entry(regFrame, textvariable = newPasswdVar, show = "*")
        permEntry = tk.Entry(regFrame, textvariable = newPermVar)
        newLoginEntry.grid(column = 0, row = 1)
        newPasswdEntry.grid(column = 1, row = 1)
        permEntry.grid(column = 0, row = 3)

        possibleBases = qh.queryBase("SELECT DISTINCT TABLE_SCHEMA FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA NOT IN ('information_schema', 'mysql', 'sys','performance_schema') ORDER BY TABLE_SCHEMA;")
        for base in possibleBases:
            baseForUserList.append(base)
        baseCombo = ttk.Combobox(regFrame, textvariable = baseForUser)
        baseCombo['values'] = baseForUserList
        baseCombo.grid(column = 3, row = 1)
        buttonAdd = tk.Button(regFrame, text = "Dodaj", command = callAdding)
        buttonAdd.grid(column = 0, row = 5)
        return True
    
    def baseChangingPanel():
        global actualBaseVar
        possibleBases = qh.queryBase("SELECT DISTINCT TABLE_SCHEMA FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA NOT IN ('information_schema', 'mysql', 'sys','performance_schema') ORDER BY TABLE_SCHEMA;")
        if possibleBases == 1:
            return False
        comboBaseValues = []
        for base in possibleBases:
            comboBaseValues.append(base[0])
        actualBaseLab = tk.Label(infoFrameInStorage,text = "Aktualna baza: "+confLive.Db+".")
        actualBaseLab.grid(column = 0, row = 0)
        actualBaseVar = tk.StringVar(value = confLive.Db)
        actualBase = ttk.Combobox(infoFrameInStorage, textvariable = actualBaseVar)
        actualBase['values'] = comboBaseValues
        #actualBaseVar.set(confLive.Db)
        actualBase.grid(column = 1, row = 0)
        actualBase.bind("<<ComboboxSelected>>", lambda event: changeBaseEvent(event))
        return True
        

    def changeBaseEvent(event):
        thh.threadManager(2)
        selectedBase = event.widget.get()
        root.destroy()    
        newBaseConf = setup.loadConfigForBase()
        if newBaseConf == False:
            resNewBase = emerg.askForNewBase(selectedBase)
            if resNewBase == 1:
                return
        selectedBaseUsers = qh.queryBase("select * from "+selectedBase+"."+newBaseConf.Users+";") 
        for row in selectedBaseUsers:
            if confLive.logedUser == row[1]:
                try:
                    code = row[3]
                except IndexError:
                    alert.popUpWarn(20) # to be handled
                    thh.threadManager()
                    callLogedView()
                    
        if code == 0:
            alert.popUpWarn(19)
            thh.threadManager()
            callLogedView()
            return
        if setup.checkDatabaseConf(selectedBase) == 1:
            #alert.popUpWarn(13)
            if emerg.askForNewBase(selectedBase) == 1:
                alert.popUpWarn(14)
                thh.threadManager()
                callLogedView()
            else:
                
                confLive.Db = selectedBase
                setup.databaseChange(selectedBase)
                selectedBaseQ = "use " + selectedBase
                qh.queryBase(selectedBaseQ)
                thh.threadManager()
                callLogedView()
        elif selectedBase != confLive.Db:
            confLive.Db = selectedBase
            setup.databaseChange(selectedBase)
            selectedBaseQ = "use " + selectedBase
            qh.queryBase(selectedBaseQ)
        thh.threadManager()
        callLogedView()
    #def stuffSelect(event, label):
    global root
    #load config---------------------------------------------
    confLive = setup.loadConfig(False)    
    confBase = setup.loadConfigForBase()
    if confBase == False:
        return False
    #--------------------------------------------------------

    #root window --------------------------------------------
    root = tk.Tk()
    root.title("Storek")
    root.geometry("1280x340")
    root.protocol("WM_DELETE_WINDOW", closeApp)
    #root.bind("<Button-1>", hide_context_menu)
    #--------------------------------------------------------

    #Base Frame ---------------------------------------------
    mainNotebook = ttk.Notebook(root, height = 500, width = 720)
    baseFrame = ttk.Frame(mainNotebook)
    baseFrame.columnconfigure(0, weight = 3)
    baseFrame.columnconfigure(1, weight = 2)
    baseFrame.grid(column = 0, row = 0, sticky="nsew")
    #--------------------------------------------------------

    #Settings Frame------------------------------------------
    settingsFrame = ttk.Frame(mainNotebook)
    settingsFrame.grid(column = 0, row = 0)
    
    
    #--------------------------------------------------------

    #Info frame----------------------------------------------
    infoFrame = ttk.Frame(mainNotebook)
    infoFrame.grid(column = 0, row = 0)
    #--------------------------------------------------------

    #Notebook -----------------------------------------------
    
    mainNotebook.pack(expand=1, fill='both')  
    mainNotebook.add(baseFrame, text="Magazyn")
    mainNotebook.add(settingsFrame, text="Ustawienia")
    mainNotebook.add(infoFrame, text="Info")
    #--------------------------------------------------------

    #Stuff Frame---------------------------------------------
    stuffFrame = tk.Frame(baseFrame)
    stuffFrame.grid(column = 0, row = 1, sticky="nsew")
    #--------------------------------------------------------

    #Info Frame on the right --------------------------------
    infoFrameInStorage = ttk.Frame(baseFrame)
    infoFrameInStorage.grid(row=1, column=1, sticky="nsew")
    #--------------------------------------------------------

    # Modular Panels ----------------------
    if not initializeBaseData():
        print("No permission to view storage")
    if not addRegister(confLive):
        print("Not admin user - disabling add user option")
    if not baseChangingPanel():
        print('No additional bases, panel hidden')
    #----------------------------------------------------------
    #root.bind("<Configure>", fillWindow)
    root.mainloop()
