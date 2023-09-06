import queryHandle as qh
import threadHandle as thh
import threading as th
import popUp as alert
import qConf as conf
import setup, time

def permThreads(confLive, *args):
    def cyclePermCheck(ip,*args):
        
        tables = setup.loadConfigForBase()
        stop = 0
        while stop != 1:
            time.sleep(2)
            print("Checking perms...")
            users = qh.queryBase("select * from "+confLive.Db+"."+tables.Users+";")
            if not users:
                print("Błąd zapytania Bazy")
                break
            else:
                for row in users:
                    if confLive.logedUser == row[1]:
                        if confLive.permissionCode != row[3]:
                            alert.popUpWarn(18)
                            break
            stop = conf.configGet("th","perm")
    
    permC = th.Thread(daemon = True,target = cyclePermCheck, args = (confLive,))
    permC.start()
    return

def permCheck(code,panel):
    posInCode = panel
    posInCode2 = panel + 8
    bitmask = 1 << posInCode
    bitmask2 = 1 << posInCode2
    result = int(code) & bitmask
    result2 = int(code) & bitmask2
    if result == bitmask and result2 == bitmask2:
        print("Granted acces panel "+str(panel))
        return True
    else:
        return False