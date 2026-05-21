import uuid
from backend.services.db_service import users_collection

SESSIONS = {}

def register_user(username, password):
    if users_collection.find_one({"username": username}): 
        return False

    users_collection.insert_one({
        "username": username,
        "password": password
    })
    return True


def login_user(username, password):
    user = users_collection.find_one({
        "username": username,
        "password": password
    })
    return user is not None


def create_session(username):
    token = str(uuid.uuid4())
    SESSIONS[token] = username
    return token


def get_username(token):
    return SESSIONS.get(token)