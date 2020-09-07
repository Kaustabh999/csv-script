import pyrebase
import json
import random
import string
from random import randint

config = {
    'apiKey': "AIzaSyAniIteTxT-8YjjFxyVNVluGbZGZ_w-W60",
    'authDomain': "csv-script.firebaseapp.com",
    'databaseURL': "https://csv-script.firebaseio.com",
    'projectId': "csv-script",
    'storageBucket': "csv-script.appspot.com",
    'messagingSenderId': "951133013328",
    'appId': "1:951133013328:web:5df0c2227e6c0148e11855",
    'measurementId': "G-DDPFCSL8FJ"
}

json_data = ""
with open('newid.json') as json_file:
    json_data = json.load(json_file)
        # next(csv_reader)
        # print(data['bookings'])

    random = ''.join([random.choice(string.ascii_letters
            + string.digits) for n in range(32)])

    def random_with_N_digits(n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)

# for x in range(0,no):

    json_data['id'] = random

    randomNo = str(random_with_N_digits(10))
    addString = "+91"
    phoneNumber = addString + randomNo
    # print(phoneNumber)
    json_data['phoneNumber'] = phoneNumber


        # This code is to push data into firebase database.
    firebase = pyrebase.initialize_app(config)
        # data = {"json_data": json_data
        #          }
    db = firebase.database()

    db.child("users2").child(random).set(json_data)
    print("Data added to real time database ")
