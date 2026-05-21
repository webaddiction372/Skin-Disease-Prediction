from flask import Flask, render_template, session, redirect, request
from backend.routes.auth_route import auth_bp
from backend.routes.predict_route import predict_bp
from backend.services.auth_service import get_username
from backend.services.db_service import predictions_collection
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = "secret123"

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(predict_bp, url_prefix="/api")


# ================= DASHBOARD =================
@app.route("/")
def dashboard():
    token = session.get("token")
    user = get_username(token)
    return render_template("dashboard.html", logged_in=bool(user))


# ================= LOGIN =================
@app.route("/login")
def login_page():
    return render_template("login.html")


# ================= REGISTER =================
@app.route("/register")
def register_page():
    return render_template("register.html")


# ================= RESULT =================
@app.route("/result")
def result_page():
    result = session.get("result")
    image_path = session.get("image_path")# for show image in result page

    # 🔥 safety check
    if not result:
        return redirect("/")

    return render_template("result.html", result=result, image_path=image_path)


# ================= PROFILE =================
@app.route("/profile")
def profile():
    token = session.get("token")
    username = get_username(token)

    if not username:
        return redirect("/login")

    # 🔥 FILTER SUPPORT
    disease_filter = request.args.get("disease")

    query = {"username": username}

    if disease_filter:
        query["disease"] = disease_filter

    history = list(predictions_collection.find(query))

    # 🔥 convert ObjectId to string
    for h in history:
        h["_id"] = str(h["_id"])

    # 🔥 get unique diseases for dropdown
    diseases = predictions_collection.distinct("disease", {"username": username})

    return render_template(
        "profile.html",
        history=history,
        username=username,
        diseases=diseases,
        selected=disease_filter
    )


# ================= DELETE SINGLE =================
@app.route("/delete_prediction/<id>")
def delete_prediction(id):
    token = session.get("token")
    username = get_username(token)

    if not username:
        return redirect("/login")

    predictions_collection.delete_one({
        "_id": ObjectId(id),
        "username": username
    })

    return redirect("/profile")


# ================= DELETE ALL =================
@app.route("/delete_all")
def delete_all():
    token = session.get("token")
    username = get_username(token)

    if not username:
        return redirect("/login")

    predictions_collection.delete_many({
        "username": username
    })

    return redirect("/profile")


# ================= LOGOUT =================
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)