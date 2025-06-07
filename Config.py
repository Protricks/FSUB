import os

class Config:
    ENV = bool(os.environ.get('ENV', False))

    if ENV:
        BOT_TOKEN = os.environ.get("BOT_TOKEN", "7729048941:AAFPagL2Wqk9kF1_eX0BfeWUMGC3yDw4Ym8")
        MONGO_URL = os.environ.get(
            "MONGO_URL",
            "mongodb+srv://EXONTESTMONGO:EXONTESTMONGO@cluster0.bviw7ic.mongodb.net/?retryWrites=true&w=majority"
        )
        APP_ID = os.environ.get("APP_ID", "12380656")
        API_HASH = os.environ.get("API_HASH", "d927c13beaaf5110f25c505b7c071273")
        SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "").split()))
        SUDO_USERS.append(5148293750)
        SUDO_USERS = list(set(SUDO_USERS))

    else:
        BOT_TOKEN = "7729048941:AAFPagL2Wqk9kF1_eX0BfeWUMGC3yDw4Ym8"
        MONGO_URL = "mongodb+srv://EXONTESTMONGO:EXONTESTMONGO@cluster0.bviw7ic.mongodb.net/?retryWrites=true&w=majority"
        APP_ID = "12380656"
        API_HASH = "d927c13beaaf5110f25c505b7c071273"
        SUDO_USERS = [5148293750, 6035523795]
