import os
import json
from pymongo import MongoClient

MONGO_URI = os.environ.get("MONGODB_URI")

def handler(request, response):
    client = MongoClient(MONGO_URI)
    db = client["rifas-db"]
    settings = db.settings.find_one({"_id": "main-settings"}, {"_id": 0})

    if not settings:
        settings = {
            "raffle_name": "Rifa pendiente",
            "ticket_price": 0,
            "image_url": ""
        }

    return response.json(settings)
