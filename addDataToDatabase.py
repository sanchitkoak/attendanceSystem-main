import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://attendancesystem-ff71f-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "2020UIC3521":
        {
            "name": "Yash Sharma",
            "major": "ICE",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-10-11 00:54:34"
        },
"2020UIC3541":
        {
            "name": "Sanchit Koak",
            "major": "ICE",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-10-11 00:54:34"
        },
"2020UIC3571":
        {
            "name": "Narayan",
            "major": "ICE",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-1-11 00:54:34"
        },
"2020UIC3525":
        {
            "name": "Abhishek",
            "major": "ICE",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)