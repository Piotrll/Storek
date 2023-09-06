import os
import sys
import popUp as alert
import configparser as cp
import connectionHandler as ch
import classLib as cl
import emergency as emerg
import loginPanel as lp
import threadHandle as thh
def checkConfig(db):
    try:
        configHandle = cp.ConfigParser()
        configHandle.read(configPath)
        tables = {}
        tables['usertable'] = configHandle.get(db,'usertable')
        tables['storagetable'] = configHandle.get(db,'storagetable')
        return tables
    except (cp.NoSectionError, cp.NoOptionError):
        alert.popUpWarn(13)
def checkDatabaseConf(selectedBase):
    
    configHandle = cp.ConfigParser()
    configHandle.read(configPath)
    if selectedBase not in configHandle:
        return 1
    else:
        return 0
    

def loggedUser(user):

    configHandle = cp.ConfigParser()
    configHandle.read(configPath)
    if 'session' not in configHandle:
        configHandle.add_section('session')
    configHandle.set('session', 'user', user.login)
    configHandle.set('session', 'permissioncode', str(user.perms))
    configHandle.set('conn', 'db', user.db)
    with open(configPath, 'w') as configHandlerWrite:
        configHandle.write(configHandlerWrite)

def databaseChange(choosenDb):
    configHandle = cp.ConfigParser()
    configHandle.read(configPath)
    if 'conn' not in configHandle:
        configHandle.add_section('conn')
    configHandle.set('conn', 'db', choosenDb)
    with open(configPath, 'w') as configHandlerWrite:
        configHandle.write(configHandlerWrite)

def checkExistance():
    global configPath
    #configPath = os.path.join(sys._MEIPASS, 'config.ini')
    configPath ='config.ini'
    settingsCheck = os.path.exists(configPath)
    if settingsCheck:
        configReader = cp.ConfigParser()
        try:
            configReader.read(configPath)
        except cp.Error():
            alert.popUpWarn(2)
            return 2
        try:
            port = configReader.get('conn', 'port')
            ip = configReader.get('conn', 'ip')
            login = configReader.get('conn', 'login')
            passwd = configReader.get('conn', 'passwd')
            db = configReader.get('conn', 'db')

        except cp.Error:
            print(cp.Error)
            return 3
        return 0
    else:
        return 3
def emergencyConfig():
    connConfig = {}
    configReader = cp.ConfigParser()
    configReader.read(configPath)
    connConfig["Ip"] = configReader.get('conn', 'ip')
    connConfig["Port"] = configReader.get('conn', 'port')
    connConfig["Login"] = configReader.get('conn', 'login')
    connConfig["Passwd"] = configReader.get('conn', 'passwd')
    confEmerg = cl.ServerQueryConf(connConfig)
    return confEmerg
def loadConfigForBase():
    global confBase
    try:
        connConfigNow = loadConfig(False)
        baseConfig = {}
        configReader = cp.ConfigParser()
        configReader.read(configPath)
        baseConfig["userTable"] = configReader.get(connConfigNow.Db, 'usertable')
        baseConfig["storageTable"] = configReader.get(connConfigNow.Db, 'storagetable')
        confBase = cl.BaseConf(baseConfig['storageTable'],baseConfig['userTable'])
    except (cp.NoOptionError, cp.NoSectionError):
        return False
    return confBase    
def loadConfig(isBoot, *args):
    global confLive
    try:
        connConfig = {}
        configReader = cp.ConfigParser()
        configReader.read(configPath)
        connConfig["Ip"] = configReader.get('conn', 'ip')
        connConfig["Port"] = configReader.get('conn', 'port')
        connConfig["Login"] = configReader.get('conn', 'login')
        connConfig["Passwd"] = configReader.get('conn', 'passwd')
        connConfig['Db'] = configReader.get('conn', 'db')
        if 'session' in configReader:
            connConfig['logedUser'] = configReader.get('session', 'user')
            connConfig['permissionCode'] = int(configReader.get('session', 'permissionCode'))
            confLive = cl.ConfigLoaded(connConfig,True)
        else:
            confLive = cl.ConfigLoaded(connConfig)
    except cp.NoOptionError:
        return False
    if isBoot:
        return True
    else:
        return confLive

def callSettings():
    isConfig = checkExistance()

    match isConfig:
        case 3:
            if not emerg.askForConf():
                alert.popUpWarn(9)
                callSettings()
            else:
                isConfig = 0
                callSettings()
        case 2:
            exit()
        case 0:
            if not loadConfig(True):
                alert.popUpWarn(2)
                emerg.askForConf()
                callSettings()
            loginResult = lp.loginPanelInit(confLive)
            if loginResult == 1:
                sys.exit()
            if not ch.connectionInit(confLive):
                alert.popUpWarn(4)
                isConfig = 3
                callSettings()
            return
        case _:
            alert.popUpWarn(-1)
        

