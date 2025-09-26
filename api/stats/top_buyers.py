from pymongo import MongoClient
import os, json
from datetime import datetime

def _auth_ok(request):
    token = request.get("headers", {}).get("x-admin-token") or request.get("query", {}).get("token")
    return token == os.environ.get("ADMIN_TOKEN")

def handler(request):
    # puede permitirse público? Lo dejamos protegido
    if not _auth_ok(request):
        return {"statusCode":401,"body":json.dumps({"error":"Unauthorized"})}

    client = MongoClient(os.environ["MONGODB_URI"])
    db = client["rifas-db"]

    # Suponiendo que cada purchase doc tiene 'name' y 'quantity'
    pipeline = [
        {
            "$group": {
                "_id": "$name",
                "total_tickets": {"$sum": "$quantity"},
                "purchases": {"$sum": 1}
            }
        },
        {"$sort": {"total_tickets": -1}},
        {"$limit": 50}
    ]
    rows = list(db.purchases.aggregate(pipeline))
    for r in rows:
        r["name"] = r["_id"]
        del r["_id"]
    return {"statusCode":200,"headers":{"Content-Type":"application/json"}, "body": json.dumps({"top_buyers": rows})}
