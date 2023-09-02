import bcrypt as bc
import queryHandle as qh
import classLib as cl
import setup
def compareCreds(toCompare, defConfig):
    global confBase
    confBase = setup.loadConfigForBase()
    credsExisting = qh.queryBase("select * from "+toCompare.db+"."+confBase.Users+";")
    for row in credsExisting:
        if (row[1] == toCompare.login) and (bc.checkpw(toCompare.passwd.encode('utf-8'), row[2].encode('utf-8'))):
            return 0
    return 5 

def hashPassword(passLoad):
    bytes = passLoad.encode('utf-8')
    salt = bc.gensalt()
    hash = bc.hashpw(bytes,salt)
    return hash

def addUser(newUser):

    newUser.passwd = hashPassword(newUser.passwd)
    queryAddUser = " INSERT INTO "+newUser.db+"."+confBase.Users+"(login, passwd) VALUES (%s, %s);"
    query_params = (newUser.login, newUser.passwd)
    res = qh.parameteredQuery(queryAddUser,query_params)
    
    if res != False:
        return True
    return False

    