from datetime import datetime
from random import randrange
import time
from src import phone, input
from src.info import HEIGHT, WIDTH


# ~~~~~~~~~~今日头条极速版~~~~~~~~~~

def read_toutiao_article(pid, w, h, num=30):
    """
    阅读今日头条文章
    """
    return None


# ~~~~~~~~~~快手极速版~~~~~~~~~~

def watch_kuaishou_video(pid, w, h, hour=2):
    """
    看快手视频
    """
    while datetime.now().hour.__eq__(hour):
        phone.swipe_down_to_up(pid, w, h, randrange(9, 16))


# ~~~~~~~~~~抖音极速版~~~~~~~~~~

def watch_douyin_video(pid, w, h, hour=3):
    """
    看抖音视频
    """
    while datetime.now().hour.__eq__(hour):
        phone.swipe_down_to_up(pid, w, h, randrange(9, 16))


# ~~~~~~~~~~火山极速版~~~~~~~~~~

def watch_huoshan_video(pid, w, h, hour=4):
    """
    看火山视频
    """
    while datetime.now().hour.__eq__(hour):
        phone.swipe_down_to_up(pid, w, h, randrange(9, 16))


# ~~~~~~~~~~京东极速版~~~~~~~~~~

def jingdong_video_coin(pid, w, h, hour=5):
    """
    京东看视频赚金币
    """
    return None


# ~~~~~~~~~~番茄免费小说~~~~~~~~~~

def read_fanqie_novel(pid, w, h, hour=6):
    """
    阅读番茄小说
    """
    return None


# ~~~~~~~~~~番茄畅听~~~~~~~~~~

def listen_fanchang_sound(pid, w, h, sec=300):
    """
    听番畅音频
    """
    # 1. 点击收听按钮
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)  # <= modify
    # 2. 收听番畅音频
    time.sleep(sec)
    # 3. 领取奖励
    input.tap(pid, (WIDTH - 1.0) * w / WIDTH, 10.0 * h / HEIGHT)  # <= modify


# ~~~~~~~~~~微视~~~~~~~~~~

def watch_weishi_video(pid, w, h, hour=8):
    """
    看微视视频
    """
    while datetime.now().hour.__eq__(hour):
        phone.swipe_down_to_up(pid, w, h, randrange(9, 16))


# ~~~~~~~~~~书旗小说~~~~~~~~~~

def read_shuqi_novel(pid, w, h, sec=300):
    """
    阅读书旗小说
    """
    return None


# ~~~~~~~~~~映客直播极速版~~~~~~~~~~

def watch_yingke_live(pid, w, h, sec=300):
    """
    看映客直播
    """
    return None


# ~~~~~~~~~~酷狗大字版~~~~~~~~~~

def listen_kugou_music(pid, w, h, sec=300):
    """
    听酷狗音乐
    """
    return None


# ~~~~~~~~~~惠头条~~~~~~~~~~

def read_huitoutiao_article(pid, w, h, num):
    """
    阅读惠头条文章
    """
    return None


# ~~~~~~~~~~中青看点~~~~~~~~~~

def read_zhongqing_article(pid, w, h, num):
    """
    阅读中青看点文章
    """
    return None


# ~~~~~~~~~~拼多多~~~~~~~~~~

# ~~~~~~~~~~淘宝特价版~~~~~~~~~~

# ~~~~~~~~~~刷宝短视频~~~~~~~~~~
def watch_shuabao_video(pid, w, h, hour):
    """
    看刷宝视频
    """
    while datetime.now().hour.__eq__(hour):
        phone.swipe_down_to_up(pid, w, h, randrange(9, 16))
