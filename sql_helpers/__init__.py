# mongo_helpers.py (updated setup)

import os
from motor.motor_asyncio import AsyncIOMotorClient
from Config import Config  # assuming Config has MONGO_URL or DATABASE_URL

MONGO_URL = getattr(Config, "MONGO_URL", None) or os.getenv("MONGO_URL") or "mongodb+srv://EXONTESTMONGO:EXONTESTMONGO@cluster0.bviw7ic.mongodb.net/?retryWrites=true&w=majority"

try:
    client = AsyncIOMotorClient(MONGO_URL)
    db = client["PurviMusicDB"]  # use your DB name here or from Config if you want

except Exception as e:
    print("MongoDB connection failed. Features depending on the database might have issues.")
    print(str(e))
    client = None
    db = None
