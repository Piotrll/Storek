class ConfigLoaded:
    def __init__(self, dictionaryConfs):
        self.Ip = dictionaryConfs["Ip"]
        self.Port = dictionaryConfs["Port"]
        self.Login = dictionaryConfs["Login"]
        self.Passwd = dictionaryConfs["Passwd"]
        self.Db = dictionaryConfs["Db"]
        self.logedUser = dictionaryConfs['logedUser']
class UserLoggin:
    def __init__(self,loginin, passwdin):
        self.login = loginin
        self.passwd = passwdin
        self.db = ""
class Base:
    def __init__(self):
        self.columns = []
        self.data = []