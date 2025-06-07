import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7729048941:AAFPagL2Wqk9kF1_eX0BfeWUMGC3yDw4Ym8")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://rahul:rahulkr@cluster0.szdpcp6.mongodb.net/?retryWrites=true&w=majority")
    APP_ID = os.environ.get("APP_ID", "12380656")
    API_HASH = os.environ.get("API_HASH", "d927c13beaaf5110f25c505b7c071273")
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
    SUDO_USERS.append(5148293750)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = "7729048941:AAFPagL2Wqk9kF1_eX0BfeWUMGC3yDw4Ym8"
    DATABASE_URL = "mongodb+srv://rahul:rahulkr@cluster0.szdpcp6.mongodb.net/?retryWrites=true&w=majority"
    APP_ID = "12380656"
    API_HASH = "d927c13beaaf5110f25c505b7c071273"
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(5148293750,6035523795)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "**Force Subscribe**\n__Force group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.__",
        
        "**Setup**\n__First of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and i will leave the chat if i am not an admin in the chat.__",
        
        "**Commmands**\n__/ForceSubscribe - To get the current settings.\n/ForceSubscribe no/off/disable - To turn of ForceSubscribe.\n/ForceSubscribe {channel username} - To turn on and setup the channel.\n/ForceSubscribe clear - To unmute all members who muted by me.\n\nNote: /FSub is an alias of /ForceSubscribe__",
        
        "**Developed by @majorgameapp**"
      ]

      START_MSG = "**Hey [{}](tg://user?id={})**\n__I can force members to join a specific channel before writing messages in the group.\nLearn more at /help__"
