import subprocess
import platform
import popUp as alert
import mysql.connector
import credHandle as ch
import threading as th
import qConf as conf
import time, sys
def connectionInit(connSets):
    pingRes = pingCheck("3", "1.1.1.1")
    if pingRes != 0:
        return False
    print("Internet good")
    if not estConnection(connSets):
        return False
    return True
def connThreads(confLive, *args):
    def singleTry():
        for i in range(10):
            res = pingCheck("1",confLive.Ip)
            if res == 0:
                return True
            else:
                return False
                
    def maintainConnection(ip,*args):
        failCount = 0
        stop = 0
        while (stop != 1):
            time.sleep(2)
            if pingCheck("1",ip) != 0:
                failCount += 1
            else:
                failCount = 0
                flag = 0
            if failCount > 1:
                #alert.popUpWarn(6)
                while True:
                    if alert.tryAgain("Nastąpiło zerwanie połączenia - Ponowić próbe połączenia ?"):
                        if singleTry():
                            break
                    else: 
                        sys.exit
            stop = conf.configGet("th","conn") 
    connection = th.Thread(daemon = True,target = maintainConnection, args = (confLive.Ip,))
    connection.start()
    return

    
    
            
def estConnection(creds):
    try:
        connectionInstance = mysql.connector.connect(host = creds.Ip, port = creds.Port,db = creds.Db, user = creds.Login, password = creds.Passwd)
    except mysql.connector.Error as err:
        print(mysql.connector.Error)
        alert.popUpWarn(6)
        if alert.tryAgain("Ponowić próbe połączenia ?"):
            estConnection(creds)
        else:
            exit()
    connectionInstance.close()
    print("Connection good")
    return True
    #Here call main window
def pingCheck(howMany, who):
    if platform.system().lower() == "windows":
        param = "-n"
        pingGoogle = ["ping", param , howMany, who]
    else:
        param = "-c"
        param2 = "-q"
        pingGoogle = ["ping", param , howMany, param2, who]
    return subprocess.call(pingGoogle)