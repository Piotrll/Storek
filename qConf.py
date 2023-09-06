import configparser as cp
import popUp as alert
import threading as th
import os,sys
def cycleConfCheck(confLive, *args):
    def cycleConf():
        flag = 0
        while flag == 0:
            global configPath
            #configPath = os.path.join(sys._MEIPASS, 'config.ini')
            configPath ='config.ini'
            try:
                handle = cp.ConfigParser()
                handle.read(configPath)
                if confLive.permissionCode != int(handle.get("session", "permissioncode")):
                    print("Zmiana w pliku konfiguracyjnym")
                    alert.popUpError("Niedozwolona manipulacja uprawnień")
                    sys.exit
                flag = handle.get("th","conf")
            except (cp.NoSectionError, cp.NoOptionError):
                alert.popUpError("Błąd konifuracji, wymagane wprowadzenie nowych danych ze względów bezpieczeństwa")
                os.remove(configPath)
                sys.exit
    configuration = th.Thread(daemon = True,target = cycleConf)
    configuration.start()
    
def configGet(sect, key):
    
    global configPath
    #configPath = os.path.join(sys._MEIPASS, 'config.ini')
    configPath ='config.ini'
    handle = cp.ConfigParser()
    handle.read(configPath)
    if sect not in handle:
        return False
    return handle.get(str(sect),str(key))
def configSet(sect,key,val):
    try:
        global configPath
        #configPath = os.path.join(sys._MEIPASS, 'config.ini')
        # for builds
        configPath ='config.ini'
        handle = cp.ConfigParser()
        handle.read(configPath)
        if sect not in handle:
            handle.add_section(sect)
        handle.set(str(sect),str(key),str(val))
        with open(configPath, 'w') as c:
            handle.write(c)
    except (cp.NoOptionError, cp.NoSectionError):
        return 1
    return 0