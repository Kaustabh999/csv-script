import pyrebase

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


firebase = pyrebase.initialize_app(config)

img0 = 'https://firebasestorage.googleapis.com/v0/b/csv-script.appspot.com/o/images%2Fimg1.jpg?alt=media&token=ef24eb4e-23e9-49db-8411-5cad8c6ecdfe'
img1 = 'https://firebasestorage.googleapis.com/v0/b/csv-script.appspot.com/o/images%2Fimg2.jpg?alt=media&token=80c5d58d-d8f0-49d5-9a08-4471ef18f67d'
img2 = 'https://firebasestorage.googleapis.com/v0/b/csv-script.appspot.com/o/images%2Fimg3.jpg?alt=media&token=6c576905-32b6-4a9b-b755-8be9c7ded158'
img3 = 'https://firebasestorage.googleapis.com/v0/b/csv-script.appspot.com/o/images%2Fimg4.jpg?alt=media&token=bece1a61-1285-4a70-a169-131276f11a01'
img4 = 'https://firebasestorage.googleapis.com/v0/b/csv-script.appspot.com/o/images%2Fimg5.jpg?alt=media&token=8a2226ed-e27f-423f-a291-6bbfb41a5420'

db = firebase.database()
data = {"0": img0,
        "1": img1,
        "2": img2,
        "3": img3,
        "4": img4}

db.child("renthouse").child("locations").child("0").child("guwahati").child("7").child("sixmile").child("1").child("images").set(data)
print("Data added to real time database ")
