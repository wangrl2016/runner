from datetime import datetime
from random import randrange

from src import phone


def watch_kuaishou_video(pid, w, h, hour=2):
    """
    看快手视频
    """
    while datetime.now().hour.__eq__(hour):
        phone.swipe_down_to_up(pid, w, h, randrange(9, 16))


def watch_douyin_video(pid, w, h, hour=3):
    """
    看抖音视频
    """
    while datetime.now().hour.__eq__(hour):
        phone.swipe_down_to_up(pid, w, h, randrange(9, 16))
