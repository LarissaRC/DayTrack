from datetime import datetime

from flask import abort, make_response

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

AGENDA_USER = {
    "1": {
        "user_id": "1",
        "user_name": "Larissa Rock",
        "user_email": "larissa.gmail.com",
        "user_password": "123456",
        "user_status": "1",
        "timestamp": get_timestamp(),
    },
    "2": {
        "user_id": "2",
        "user_name": "Zack",
        "user_email": "zack.gmail.com",
        "user_password": "123456",
        "user_status": "1",
        "timestamp": get_timestamp(),
    },
    "3": {
        "user_id": "3",
        "user_name": "Chloe",
        "user_email": "chloe.gmail.com",
        "user_password": "123456",
        "user_status": "1",
        "timestamp": get_timestamp(),
    },
}

def read_all():
    return list(AGENDA_USER.values())

def create(user):
    user_id = user.get("user_id")
    user_name = user.get("user_name")
    user_email = user.get("user_email")
    user_password = user.get("user_password")

    if user_id and user_id not in AGENDA_USER:
        AGENDA_USER[user_id] = {
            "user_id": user_id,
            "user_name": user_name,
            "user_email": user_email,
            "user_password": user_password,
            "user_status": 1,
            "timestamp": get_timestamp(),
        }
        return AGENDA_USER[user_id], 201
    else:
        abort(404, f"User with the email {user_email} already exists")

def read_one(user_id):
    if user_id in AGENDA_USER:
        return AGENDA_USER[user_id]
    else:
        abort(404, f"User not found :(")

def update(user_id, user):
    if user_id in AGENDA_USER:
        AGENDA_USER[user_id]["user_name"] = user.get("user_name", AGENDA_USER[user_id]["user_name"])
        AGENDA_USER[user_id]["user_email"] = user.get("user_email", AGENDA_USER[user_id]["user_email"])
        AGENDA_USER[user_id]["user_password"] = user.get("user_password", AGENDA_USER[user_id]["user_password"])
        AGENDA_USER[user_id]["user_status"] = user.get("user_status", AGENDA_USER[user_id]["user_status"])
        AGENDA_USER[user_id]["timestamp"] = get_timestamp()
        return AGENDA_USER[user_id]
    else:
        abort(404, f"User not found :(")

def delete(user_id):
    if user_id in AGENDA_USER:
        user_name = AGENDA_USER[user_id]["user_name"]
        del AGENDA_USER[user_id]
        return make_response(f"User with name {user_name} successfully deleted.", 200)
    else:
        abort(404, f"User not found:(")