from pymongo import MongoClient

client = MongoClient("mongodb+srv://hiepph:hiep2003@cluster0.owfcn5g.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.todo_db

collection_name = db["todo_collection"]