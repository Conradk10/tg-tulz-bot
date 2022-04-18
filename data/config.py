import configparser
from rich import print

config = configparser.ConfigParser()
config.read("settings.ini")

BOT_TOKEN = config["Bot Settings"]["bot_token"]

admins = config["Bot Settings"]["admins_list"]

ip = {
    'db':    config["DB Settings"]["db_host"],
    'redis': config["DB Settings"]["redis_host"],
}

mysql_info = {
    'host':     ip['db'],
    'user':     config["DB Settings"]["db_user"],
    'password': config["DB Settings"]["db_password"],
    'db':       config["DB Settings"]["db_db"],
    'maxsize':  5,
    'port':     3306,
}

redis = {
    'host':     ip['redis'],
    'password': config["DB Settings"]["redis_password"]
}

if "," in admins:
    admins = admins.split(",")
else:
    if len(admins) >= 1:
        admins = [admins]
    else:
        admins = []
        print("[yellow bold]❗️ Не указан ни один администратор!")

bot_version = "1.0"
