import os
from pymongo import MongoClient



class MConnections:
    def __init__(self):
        self.mongo_uri = os.getenv("MONGO_URI", "mongodb://mongo:27017")
        self._mongo_client = MongoClient(self.mongo_uri)
        self.db = self._mongo_client[os.getenv("MONGO_DB", "pizza_orders")]
        self.collection = self.db[os.getenv("MONGO_COLLACTION","orders")]
       
        print("connection to mongo is ready!")

    def get_mongo_collection(self):
        return self.collection

  

    


