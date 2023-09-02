import subprocess
import platform
import popUp as alert
import mysql.connector
import credHandle as ch
def connectionInit(connSets):
    pingRes = pingCheck()
    if pingRes != 0:
        return False
    print("Internet good")
    if not estConnection(connSets):
        return False
    return True

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
    return True
    #Here call main window
def pingCheck():
    if platform.system().lower() == "windows":
        param = "-n"
    else:
        param = "-c"
    host = "8.8.8.8"
    pingGoogle = ["ping", param, "3", host]
    return subprocess.call(pingGoogle)