import time
from random import randrange

from src import checkin, input, phone
from src.info import WIDTH, HEIGHT


def toutiao(pid, w, h):
    # 1. 点击右下方任务
    # 签到成功
    input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)  # <= modify
    # 2. 看视频再领金币
    input.tap(pid, w / 2, 9.4 * h / HEIGHT)  # <= modify
    # 3. 看15s视频
    time.sleep(15)
    # 4. 点击关闭


def kuaishou(pid, w, h):
    # 1. 播放视频一小会
    # 解决弹出青少年模式悬浮窗的问题
    for i in range(0, 10):
        phone.swipe_down_to_up(pid, w, h, randrange(9, 16))
    # 2. 点击左上角的菜单栏
    input.tap(pid, 0.6 * w / WIDTH, 0.9 * h / HEIGHT)  # <= modify
    # 3. 点击去赚钱
    input.tap(pid, w / 2, 7.2 * h / HEIGHT)  # <= modify
    # 4. 点击立即签到
    # 签到成功
    input.tap(pid, w / 2, 10.4 * h / HEIGHT)  # <= modify


def douyin(pid, w, h):
    # 1. 播放视频一小会
    # 解决弹出青少年模式悬浮窗的问题
    for i in range(0, 10):
        phone.swipe_down_to_up(pid, w, h, randrange(9, 16))
    # 2. 点击下方的福袋
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)
    # 3. 点击立即签到
    # 签到成功
    input.tap(pid, w / 2, 9.7 * h / HEIGHT)


def huoshan(pid, w, h):
    # 1. 播放视频一小会
    # 解决弹出青少年模式悬浮窗的问题
    for i in range(0, 10):
        phone.swipe_down_to_up(pid, w, h, randrange(9, 16))
    # 2. 点击右下方红包
    # 签到成功
    input.tap(pid, 4.3 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)  # <= modify


def jingdong(pid, w, h):
    # 1. 点击现金签到
    input.tap(pid, w / 2, 6.8 * h / HEIGHT)  # <= modify
    # 2. 点击立即签到
    # 签到成功
    input.tap(pid, w / 2, 5.8 * h / HEIGHT)  # <= modify


def fanqie(pid, w, h):
    # 1. 点击福利签到
    # 签到成功
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)
    # 2. 点击看视频再领金币
    input.tap(pid, w / 2, 10.1 * h / HEIGHT)  # <= modify
    # 3. 播放视频30s
    time.sleep(30)
    # 4. 点击关闭
    # 无法回退关闭
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)  # <= modify


def fanchang(pid, w, h):
    # 1. 点击福利签到
    # 签到成功
    input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)  # <= modify
    # 2. 点击看视频再领金币
    input.tap(pid, w / 2, 10.1 * h / HEIGHT)  # <= modify
    # 3. 播放视频30s
    time.sleep(30)
    # 4. 点击关闭
    # 无法回退关闭
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)  # <= modify

