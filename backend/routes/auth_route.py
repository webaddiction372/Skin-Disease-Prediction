from flask import Blueprint, request, redirect, session
from backend.services.auth_service import register_user, login_user, create_session

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]

    if register_user(username, password):
        return redirect("/login")

    return "User already exists"


@auth_bp.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if login_user(username, password):
        token = create_session(username)
        session["token"] = token
        return redirect("/")

    return "Invalid credentials"