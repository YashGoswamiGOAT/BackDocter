import firebase_admin
from firebase_admin import credentials, db
import json

cred = credentials.Certificate("drnearme.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : "https://drnearme-21c37-default-rtdb.firebaseio.com"
})

reff = db.reference("/")

print(reff.child('Accounts').get())