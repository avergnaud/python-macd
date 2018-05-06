from pymongo import MongoClient
import json

client = MongoClient()

db = client.market_data_database

collection = db.macd_collection

def insert_or_update(macd):
        
    # http://api.mongodb.com/python/current/api/pymongo/operations.html#pymongo.operations.UpdateOne

    collection.replace_one(
        { 
                "exchange": macd["exchange"], 
                "marketName": macd["marketName"],
                "tickInterval": macd["tickInterval"], 
                "timestamp": macd["timestamp"]
        },
        macd,
        upsert=True)

def get_all():
        returned_macd = []
        macd_cursor = collection.find({})
        for macd in macd_cursor:
                returned_macd.append(macd)
        return returned_macd

def update_one(macd):
        collection.update_one({"_id":macd["_id"]}, {"$set": macd}, upsert=False)