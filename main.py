import json
import firebase_admin
from firebase_admin import credentials, firestore
from config import *

# Replace 'path/to/serviceAccountKey.json' with the actual path to your key file
cred = credentials.Certificate(FIREBASE_ADMIN_SDK_PATH)
firebase_admin.initialize_app(cred)

# Load data from JSON file
with open(INPUT_DATA_PATH, 'r') as file:
    data = json.load(file)

db = firestore.client()
collection_ref = db.collection(FIREBASE_COLLECTION_NAME)

for event in data:
    collection_ref.add(event)
