import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('stocker-929ba-firebase-adminsdk-vewwh-6c7f47e220.json')

firebase_admin.initialize_app(cred, {

    'databaseURL' : 'https://stocker-929ba-default-rtdb.firebaseio.com/'
})

