import json
import firebase_admin
from firebase_admin import credentials, firestore
from config import *

def read_from_json(file_path):
    # Load data from JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    if isinstance(data, dict):  # If it's a single JSON object
        data = [data]  # Convert it into a JSON array with one object

    if not isinstance(data, list):
        raise ValueError("Invalid JSON format: Expected a JSON array or a single JSON object.")
    
    return data

def get_firestore_collection(firebase_admin_sdk_path, firestore_collection_name):
    cred = credentials.Certificate(firebase_admin_sdk_path)
    firebase_admin.initialize_app(cred)

    db = firestore.client()
    collection_ref = db.collection(firestore_collection_name)

    return collection_ref

def main():
    data = read_from_json(INPUT_DATA_PATH)
    firestore_collection = get_firestore_collection(FIREBASE_ADMIN_SDK_PATH, FIRESTORE_COLLECTION_NAME)

    for object in data:
        firestore_collection.add(object)

if __name__ == "__main__":
    main()
