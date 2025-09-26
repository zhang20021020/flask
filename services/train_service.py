import json
import subprocess
import os
import multiprocessing
import re

# 全局变量
train_process = None   # 保存训练进程
event_queue = None     # 日志队列

EPOCH_REGEX = re.compile(r"Epoch\s+\d+/\d+")
def run_training(params, log_queue):
    """训练进程：执行 trainPose.py，把 stdout 写入 log_queue"""
    import json, subprocess, os

    config_path = os.path.join("E:/myRsearch/ultralytics", "train_config.json")
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=4)

    cmd = [
        r"D:\anaconda3\envs\yolov11\python.exe",
        "E:/myRsearch/ultralytics/trainPose.py",
        "--config", config_path
    ]

    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",   # ✅ 强制使用 UTF-8 解码
        errors="ignore",    # ✅ 遇到非法字符时忽略
        bufsize=1,
        universal_newlines=True
    )

    for line in process.stdout:
        log_queue.put(line)
    process.wait()
    log_queue.put("[训练已结束]\n")


def log_consumer(log_queue, event_queue):
    """日志消费者进程：只推送关键日志（比如一个 epoch 完成时）"""
    buffer = []
    for line in iter(log_queue.get, None):
        buffer.append(line)
        # 关键点：检测 epoch
        if EPOCH_REGEX.search(line) or "Epoch" in line:
            event_queue.put("".join(buffer))
            buffer = []
    # 把剩余的推送
    if buffer:
        event_queue.put("".join(buffer))


def start_training(params):
    """启动训练和日志传输"""
    global event_queue
    log_queue = multiprocessing.Queue()
    event_queue = multiprocessing.Queue()

    train_proc = multiprocessing.Process(target=run_training, args=(params, log_queue))
    train_proc.start()

    log_proc = multiprocessing.Process(target=log_consumer, args=(log_queue, event_queue))
    log_proc.start()

    return event_queue

def is_training():
    global train_process
    if train_process is None:
        return False
    return train_process.is_alive()

def get_event_queue():
    """获取全局日志队列"""
    global event_queue
    return event_queue
