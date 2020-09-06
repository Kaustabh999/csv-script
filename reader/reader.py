import pyrebase
import csv

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

with open('userId.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)

    for row in csv_reader:
        email, id, name, owner, phoneno, points, reference, token = row
        print(row)
        Id = str(id)

        # This code is to push data into firebase database.
        firebase = pyrebase.initialize_app(config)

        db = firebase.database()
        data = {"email": email,
                 "id": id,
                 "name": name,
                 "owner": owner,
                 "phone_number": phoneno,
                 "points": points,
                 "reference": reference,
                 "token": token}

        # db.child("users").child(Id).child("bookings").set(data)
        print("Data added to real time database ")
