from flask import Blueprint, request, Response
from services.train_service import run_training

train_bp = Blueprint("train", __name__)

@train_bp.route("/", methods=["POST"])
def train():
    params = request.json
    return Response(run_training(params), mimetype="text/event-stream")
