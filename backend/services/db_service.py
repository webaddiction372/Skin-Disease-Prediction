from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["skin_disease_db"] 

users_collection = db["users"]
predictions_collection = db["predictions"] 