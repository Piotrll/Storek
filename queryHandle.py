import mysql.connector as mc
import popUp as alert
import connectionHandler as ch
import setup
import sys
def parameteredQuery(query,params):
    defConfig = setup.loadConfig(False)
    try:
        queryListConn = mc.connect(
            host = defConfig.Ip, 
            port = defConfig.Port,
            user = defConfig.Login,
            password = defConfig.Passwd,
            database = defConfig.Db
            )
        cursor = queryListConn.cursor()
        cursor.execute(query,params)
        queryListConn.commit()
        dataCreds = cursor.fetchall()
        queryListConn.close()
        return dataCreds
    except mc.Error as e:
        alert.popUpError(e)
        return False
    
def queryBase(query, *args):
    #if not ch.pingCheck():
    #   alert.popUpWarn(4)
    defConfig = setup.loadConfig(False)
    try:
        queryListConn = mc.connect(
            host = defConfig.Ip, 
            port = defConfig.Port,
            user = defConfig.Login,
            password = defConfig.Passwd,
            database = defConfig.Db
            )
        cursor = queryListConn.cursor()
    
        cursor.execute(query)
        
        dataCreds = cursor.fetchall()
        queryListConn.commit()
        return dataCreds
    except mc.Error as e:
        alert.popUpError("Wystąpił błąd zapytania bazy danych, treść :"+str(e))
        return False
def queryServer(query, *args):
    #if not ch.pingCheck():
    #   alert.popUpWarn(4)
    defConfig = setup.emergencyConfig()
    try:
        queryListConn = mc.connect(
            host = defConfig.Ip, 
            port = defConfig.Port,
            user = defConfig.Login,
            password = defConfig.Passwd
            )
        cursor = queryListConn.cursor()
    
        cursor.execute(query)
        
        dataCreds = cursor.fetchall()
        return dataCreds
    except mc.Error as e:
        alert.popUpError(e)
        return False