import os
import uuid
from flask import Blueprint, request, redirect, session
from backend.services.inference_service import predict_image
from backend.services.auth_service import get_username
from backend.services.db_service import predictions_collection

predict_bp = Blueprint("predict", __name__) #

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True) 


@predict_bp.route("/predict", methods=["POST"])
def predict():
    token = session.get("token")
    username = get_username(token)

    if not username:
        return redirect("/login")

    file = request.files["image"] #backend receive image from frontend

    filename = str(uuid.uuid4()) + "_" + file.filename # for unique name of image
    path = os.path.join(UPLOAD_FOLDER, filename) #path for save images
    file.save(path)

    result = predict_image(path)  #backend send path to ML (img)

    # Save to DB
    predictions_collection.insert_one({
        "username": username,
        "image": filename,
        "disease": result["predicted_disease"],
        "confidence": result["confidence"]
    })

    session["result"] = result
    session["image_path"] = filename

    return redirect("/result") 