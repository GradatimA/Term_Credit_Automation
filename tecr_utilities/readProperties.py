import configparser

config = configparser.RawConfigParser()
config.read(".\\tecr_Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        appurl = config.get("login info", "appUrl")
        return appurl
    @staticmethod
    def getUsername():
        username = config.get("login info", "username")
        return username

    @staticmethod
    def getPassword():
        password = config.get("login info", "password")
        return password
