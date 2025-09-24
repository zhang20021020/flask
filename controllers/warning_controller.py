from flask import Blueprint, jsonify
from services.warning_service import WarningService

# 定义蓝图
warning_bp = Blueprint("warning", __name__, url_prefix="/api/warnings")

@warning_bp.route("/", methods=["GET"])
def get_warnings():
    data = WarningService.get_warning_statistics()
    return jsonify(data)

