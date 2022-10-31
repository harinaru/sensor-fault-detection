import pymongo
from sensor.constant.database import DATABASE_NAME
from sensor.constant.env_variable import MONGODB_URL_KEY
from sensor.exception import SensorException
import certifi
import os,sys
ca = certifi.where()

class MongoDBClient:
    client = None
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                # mongo_db_url = os.getenv(MONGODB_URL_KEY)
                #mongo_db_url  = "mongodb+srv://avnish:Aa327030@cluster0.or68e.mongodb.net/admin?authSource=admin&replicaSet=atlas-desfdx-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true"
                mongo_db_url= "mongodb+srv://hari:hari@cluster0.7qzesuy.mongodb.net/?retryWrites=true&w=majority"
               #mongo_db_url  = "mongodb+srv://temp-user:U8I5A6oh0jJVnVoU@ineuron-ai-projects.7eh1w4s.mongodb.net/admin?authSource=admin&replicaSet=atlas-okvkrd-shard-0&w=majority&readPreference=primary&retryWrites=true&ssl=true"
            MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
           raise SensorException(e,sys)