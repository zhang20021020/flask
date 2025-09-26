from flask import Flask
from controllers.warning_controller import warning_bp
from controllers.train_controller import train_bp

def create_app():
    app = Flask(__name__)

    # 注册蓝图
    app.register_blueprint(warning_bp, url_prefix="/api/warnings")
    app.register_blueprint(train_bp, url_prefix="/api/train")

    # 根路由
    @app.route("/")
    def index():
        return "Flask 后端已启动，API 请访问 /api/warnings/ 或 /api/train/"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
