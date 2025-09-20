from pymongo import MongoClient
import os
import json

def handler(request):
    client = MongoClient(os.environ["MONGODB_URI"])
    db = client["rifas-db"]
    raffles = list(db.raffles.find({}, {"_id": 0}))
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(raffles)
    }
