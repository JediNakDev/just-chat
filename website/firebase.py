import firebase_admin
from firebase_admin import credentials, firestore

def initialize_firebase():
    cred = credentials.Certificate('/firebase.json')
    firebase_admin.initialize_app(cred)


def get_db():
  db = firestore.client()

  return db
