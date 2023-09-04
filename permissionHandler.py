import queryHandle as qh
import threadHandle as thh
import threading as th
import popUp as alert
import setup, time

def permThreads(confLive, *args):
    def cyclePermCheck(ip,*args):
        tables = setup.loadConfigForBase()
        while stop != 1:
            time.sleep(2)
            print("Checking perms...")
            users = qh.queryBase("select * from "+confLive.Db+"."+tables.Users+";")
            for row in users:
                if confLive.logedUser == row[1]:
                    if confLive.permissionCode != row[3]:
                        alert.popUpWarn(18)
                        break
        
    global stop
    if args and args[0] == True:
        stop = 0
        permC = th.Thread(target = cyclePermCheck, args = (confLive,))
        permC.start()
        return
    elif args and args[0] == False:
        stop = 1
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