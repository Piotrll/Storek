import subprocess
import platform
import popUp as alert
import mysql.connector
import credHandle as ch
import threading as th
import time
def connectionInit(connSets):
    pingRes = pingCheck("3", "1.1.1.1")
    if pingRes != 0:
        return False
    print("Internet good")
    if not estConnection(connSets):
        return False
    return True
def maintainConnection(ip):
    failCount = 0
    while (True):
        time.sleep(2)
        if pingCheck("1",ip) != 0:
            failCount += 1
        else:
            failCount = 0
        if failCount > 3:
            alert.popUpWarn(17)
            break
            
def estConnection(creds):
    try:
        connectionInstance = mysql.connector.connect(host = creds.Ip, port = creds.Port,db = creds.Db, user = creds.Login, password = creds.Passwd)
    except mysql.connector.Error as err:
        print(mysql.connector.Error)
        alert.popUpWarn(6)
        if alert.popUpWarn(7):
            estConnection(creds)
        else:
            exit()
    connectionInstance.close()
    print("Connection good")
    connection = th.Thread(target = maintainConnection, args = (creds.Ip,))
    connection.start()
    return True
    #Here call main window
def pingCheck(howMany, who):
    if platform.system().lower() == "windows":
        param = "-n"
    else:
        param = "-c"
    pingGoogle = ["ping", param, howMany, who]
    return subprocess.call(pingGoogle)