class ConfigLoaded:
    def __init__(self, dictionaryConfs, *args):
        self.Ip = dictionaryConfs["Ip"]
        self.Port = dictionaryConfs["Port"]
        self.Login = dictionaryConfs["Login"]
        self.Passwd = dictionaryConfs["Passwd"]
        self.Db = dictionaryConfs["Db"]
        self.logedUser = ''
        self.permissionCode = 0
        if args and args[0]:
            self.logedUser = dictionaryConfs["logedUser"]
            self.permissionCode = dictionaryConfs["permissionCode"]
class ServerQueryConf:
    def __init__(self, dictionaryConfs):
        self.Ip = dictionaryConfs["Ip"]
        self.Port = dictionaryConfs["Port"]
        self.Login = dictionaryConfs["Login"]
        self.Passwd = dictionaryConfs["Passwd"]
class UserLoggin:
    def __init__(self,loginin, passwdin, *args):
        self.login = loginin
        self.passwd = passwdin
        self.db = ""
        self.perms = 0
        if args and args[0]:
            self.perms = args[0]
class Base:
    def __init__(self):
        self.columns = []
        self.data = []
class BaseConf:
    def __init__(self, storage,users):
        self.Users = users
        self.Storage = storage