from pymongo import MongoClient
import os
import json

def handler(request):
    if request["method"] != "POST":
        return {
            "statusCode": 405,
            "body": json.dumps({"error": "Método no permitido"})
        }

    data = json.loads(request["body"])
    client = MongoClient(os.environ["MONGODB_URI"])
    db = client["rifas-db"]

    db.tickets.insert_one({
        "nombre": data.get("nombre"),
        "email": data.get("email"),
        "metodo_pago": data.get("metodo_pago"),
        "cantidad": data.get("cantidad")
    })

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"mensaje": "Compra registrada correctamente"})
    }
