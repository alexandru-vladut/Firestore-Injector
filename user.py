import firebase_admin
from firebase_admin import credentials, firestore

# Replace 'path/to/serviceAccountKey.json' with the actual path to your key file
cred = credentials.Certificate('hackitall-db-2024-70ec3-firebase-adminsdk-zbjql-8e67bb6e02.json')
firebase_admin.initialize_app(cred)

user = {
  "uid": "dafewrfdsferf123432",
  "name": "ANDREI",
  "email": "andrei@gmail.com",
  "username": "andrei89",
  "location": "New York, USA",
  "gender": "Male",
  "preferences": {
    "music": ["Rock", "Pop", "Jazz", "Rap", "Classical"],
    "sports": ["Football", "Basket", "Tennis", "Running", "Yoga"],
    "travel": ["Hiking", "Holiday", "Road Trip"],
    "culture": ["Arts", "Theater", "Museum", "Literature"],
    "community_involvement": ["Environmental Conservation", "Animal Welfare", "Charity Fundraising", "Youth Programs"],
    "entertainment": ["Movies", "Stand-Up", "Gaming"]
  },
  "xpPoints": 2500,
  "donationPoints": 150,
  "level": 1,
  "friends": [],
  "joinedEvents": [],
  "createdEvents": [],
  "tickets": {}
}



db = firestore.client()
collection_ref = db.collection('users')

collection_ref.add(user)
