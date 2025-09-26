import json
import subprocess
import os
import threading

def run_training(params):
    config_path = os.path.join("E:/myRsearch/ultralytics", "train_config.json")
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=4)

    log_path = os.path.join("E:/myRsearch/ultralytics", "train.log")

    cmd = [
        r"D:\anaconda3\envs\yolov11\python.exe",
        "E:/myRsearch/ultralytics/trainPose.py",
        "--config", config_path
    ]

    # 后台线程运行训练，日志写入文件
    def run_process():
        with open(log_path, "w", encoding="utf-8") as log_file:
            process = subprocess.Popen(
                cmd,
                stdout=log_file,
                stderr=subprocess.STDOUT,
                text=True
            )
            process.wait()

    threading.Thread(target=run_process, daemon=True).start()

    # SSE 从日志文件读
    def generate():
        with open(log_path, "r", encoding="utf-8") as f:
            while True:
                line = f.readline()
                if line:
                    yield f"data: {line}\n\n"

    return generate()
