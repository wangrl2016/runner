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
    for i in range(0, num):
        # 1. 获取文章目录
        phone.swipe_down_to_up(pid, w, h)
        # 2. 点击文章
        input.tap(pid, w / 2, h * 3 / 4)
        # 3. 滑动阅读
        for j in range(0, 10):
            phone.swipe_down_to_up(pid, w, h)
        # 4. 返回上级目录
        phone.go_back(pid)


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
    # 1. 点击赚钱按钮
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)
    # 2. 点击看视频赚金币
    input.tap(pid, (WIDTH - 1.1) * w / WIDTH, 9.7 * h / HEIGHT)  # <= modify
    # 3. 任意点击视频进入
    input.tap(pid, w / 3, h / 2)
    # 4. 滑动屏幕观看
    while datetime.now().hour.__eq__(hour):
        phone.swipe_down_to_up(pid, w, h, randrange(9, 16))



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
    # 1. 点击今日必读
    input.tap(pid, w / 2, h / 2)
    # 2. 点击开始阅读
    input.tap(pid, w * 2 / 3, (HEIGHT - 0.5) * h / HEIGHT)
    minutes = sec / 60 + datetime.now().minute
    if minutes < 60:
        while datetime.now().minute < minutes:
            # 防止点击广告
            phone.swipe_right_to_left(pid, w, h / 4, randrange(3, 5))
    else:
        hour = datetime.now().hour
        while datetime.now().hour.__eq__(hour):
            phone.swipe_right_to_left(pid, w, h / 4, randrange(3, 5))


# ~~~~~~~~~~映客直播极速版~~~~~~~~~~

def watch_yingke_live(pid, w, h, sec=300):
    """
    看映客直播
    """
    # 1. 点击任意直播间
    input.tap(pid, w / 3, h / 3)
    # 2. 看直播
    time.sleep(sec)


# ~~~~~~~~~~酷狗大字版~~~~~~~~~~

def listen_kugou_music(pid, w, h, sec=300):
    """
    听酷狗音乐
    """
    # 1. 点击中间下方进入播放界面
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)
    # 2. 点击播放
    input.tap(pid, w / 2, (HEIGHT - 1.5) * h / HEIGHT)  # <= modify
    # 3. 播放
    time.sleep(sec)


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


# ~~~~~~~~~~趣头条~~~~~~~~~~
def watch_qutoutiao_svideo(pid, w, h, hour):
    """
    看趣头条小视频
    """
    # 　1. 点击中间下方小视频
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)
    while datetime.now().hour.__eq__(hour):
        phone.swipe_down_to_up(pid, w, h, randrange(9, 16))


# ~~~~~~~~~~百度极速版~~~~~~~~~~
def watch_baidu_svideo(pid, w, h, hour):
    """
    看百度小视频
    """
    # 1. 点击banner栏目中小视频
    input.tap(pid, 3.3 * w / WIDTH, 3.8 * h / HEIGHT)  # <= modify
    # 2. 点击任意小视频
    input.tap(pid, w / 3, h / 3)
    # 3. 滑动小视频
    while datetime.now().hour.__eq__(hour):
        phone.swipe_down_to_up(pid, w, h, randrange(9, 16))
