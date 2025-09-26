from flask import Blueprint, request, Response
from services.train_service import start_training, get_event_queue

train_bp = Blueprint("train", __name__)

@train_bp.route("/", methods=["POST"])
def train():
    """启动训练"""
    params = request.json
    start_training(params)
    return {"msg": "训练已启动，请通过 /api/train/logs 获取日志"}

@train_bp.route("/logs")
def stream_logs():
    """SSE 实时推送日志"""
    def generate():
        q = get_event_queue()
        if q is None:
            yield "data: 尚未启动训练\n\n"
            return

        while True:
            msg = q.get()  # 从事件队列取日志
            yield f"data: {msg}\n\n"

    return Response(generate(), mimetype="text/event-stream")
@train_bp.route("/status")
def status():
    from services.train_service import is_training
    return {"running": is_training()}
