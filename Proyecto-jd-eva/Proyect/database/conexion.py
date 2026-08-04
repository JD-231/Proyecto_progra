from pymongo import MongoClient

cliente = MongoClient(
    "mongodb://localhost:27017/"
)

db = cliente["MetaJuan"]

historial = db["historial"]