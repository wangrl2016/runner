from datetime import datetime
from random import randrange
import time
from src import phone, input, checkin, info
from src.info import HEIGHT, WIDTH, packages


# ~~~~~~~~~~今日头条极速版~~~~~~~~~~

def read_toutiao_article(pid, w, h, num):
    """
    阅读今日头条文章
    """
    print('阅读头条文章 ' + datetime.now().__str__())
    for i in range(0, num):
        # 1. 获取文章目录
        phone.swipe_down_to_up(pid, w, h)
        # 2. 点击文章
        input.tap(pid, w / 2, h * 3 / 4)
        # 3. 滑动阅读
        for j in range(0, 15):
            phone.swipe_down_to_up(pid, w, h)
        # 4. 返回上级目录
        phone.go_back(pid)


def toutiao_video(pid, w, h, num):
    """
    看头条视频
    """
    print('看今日头条视频 ' + datetime.now().__str__())
    # 1. 点击下方视频按钮
    input.tap(pid, 2.0 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)
    for i in range(0, num):
        # 1. 向下刷新视频
        phone.swipe_up_to_down(pid, w, h)
        # 2. 点击播放
        input.tap(pid, w / 2, h / 3)
        # 3. 播放120s
        time.sleep(120)


# ~~~~~~~~~~快手极速版~~~~~~~~~~

# 只是看视频的过程
def watch_kuaishou_video(pid, w, h, hour):
    """
    看快手视频
    """
    while datetime.now().hour.__eq__(hour):
        phone.swipe_down_to_up(pid, w, h, randrange(9, 16))


# 从打开到关闭看快手视频的完整过程
def full_watch_kuaishou_video(pid, w, h, hour):
    print('看快手视频 ' + datetime.now().__str__())
    # 1. 打开程序
    checkin.kuaishou(pid)
    # 2. 看快手视频
    watch_kuaishou_video(pid, w, h, hour)
    # 3. 关闭程序
    phone.stop_app(pid, packages['kuaishou'])


def kuaishou_reward_task(pid, w, h, num):
    """
    1000金币悬赏任务
    """
    print('快手1000金币悬赏任务 ' + datetime.now().__str__())
    # 1. 点击左上角菜单栏
    input.tap(pid, 0.6 * w / WIDTH, 0.9 * h / HEIGHT)  # <= modify
    # 2. 点击去赚钱
    input.tap(pid, w / 2, 7.2 * h / HEIGHT)
    for i in range(0, num):
        # 3. 点击福利
        input.tap(pid, (WIDTH - 1.0) * w / WIDTH, 10.6 * h / HEIGHT)
        # 4播放30s
        time.sleep(30)
        # 5. 返回到福利页面
        phone.go_back(pid)


# ~~~~~~~~~~抖音极速版~~~~~~~~~~

def watch_douyin_video(pid, w, h, hour=3):
    """
    看抖音视频
    """
    while datetime.now().hour.__eq__(hour):
        phone.swipe_down_to_up(pid, w, h, randrange(9, 16))


def full_watch_douyin_video(pid, w, h, hour):
    # [x] 看抖音视频
    print('看抖音视频 ' + datetime.now().__str__())
    # 1. 打开程序
    checkin.douyin(pid)
    # 2. 看抖音视频
    watch_douyin_video(pid, w, h, hour)
    # 3. 关闭程序
    phone.stop_app(pid, packages['douyin'])


# ~~~~~~~~~~火山极速版~~~~~~~~~~

def watch_huoshan_video(pid, w, h, hour=4):
    """
    看火山视频
    """
    while datetime.now().hour.__eq__(hour):
        phone.swipe_down_to_up(pid, w, h, randrange(9, 16))


def full_watch_huoshan_video(pid, w, h, hour):
    print('看火山视频 ' + datetime.now().__str__())
    # 1. 打开程序
    checkin.huoshan(pid)
    # 2. 看火山视频
    watch_huoshan_video(pid, w, h, hour)
    # 3. 关闭程序
    phone.stop_app(pid, packages['huoshan'])


def huoshan_money_tree(pid, w, h):
    """
    摇钱树
    """
    print('火山摇钱树 ' + datetime.now().__str__())
    # 1. 点击红包
    input.tap(pid, 4.3 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)
    # 2. 点击摇钱树
    input.tap(pid, w / 3, 5.0 * h / HEIGHT)
    # 3. 摇钱
    input.tap(pid, w / 2, h / 2)
    # 返回到上级页面
    # 是任务页面
    phone.go_back(pid)


# ~~~~~~~~~~京东极速版~~~~~~~~~~

def jingdong_good(pid, w, h, sec):
    """
    逛商品赚金币
    """
    print('京东逛商品赚金币 ' + datetime.now().__str__())
    # 1. 点击赚钱
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)
    # 2. 点击逛商品赚金币
    input.tap(pid, (WIDTH - 1.0) * w / WIDTH, 7.2 * h / HEIGHT)
    count = 0
    while count < sec:
        # 3. 逛15s
        for i in range(0, 3):
            phone.swipe_down_to_up(pid, w, h, 5)
        # 4. 点击下一个商品
        input.tap(pid, (WIDTH - 0.9) * w / WIDTH, 8.0 * h / HEIGHT)
        count += 20


def jingdong_activity(pid, w, h, sec):
    """
    逛活动赚金币
    """
    print('京东逛活动赚金币 ' + datetime.now().__str__())
    # 1. 点击赚钱
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)
    # 2. 点击逛活动赚金币
    input.tap(pid, (WIDTH - 1.0) * w / WIDTH, 8.5 * h / HEIGHT)
    count = 0
    while count < sec:
        # 3. 逛15s
        for i in range(0, 3):
            phone.swipe_down_to_up(pid, w, h, 5)
        # 4. 点击下一个商品
        input.tap(pid, (WIDTH - 0.9) * w / WIDTH, 8.0 * h / HEIGHT)
        count += 20


def jingdong_video_coin(pid, w, h, hour=5):
    """
    京东看视频赚金币
    """
    # 1. 点击赚钱按钮
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)
    # 2. 点击看视频赚金币
    input.tap(pid, (WIDTH - 1.0) * w / WIDTH, 9.7 * h / HEIGHT)  # <= modify
    # 3. 任意点击视频进入
    input.tap(pid, w / 3, h / 2)
    # 4. 滑动屏幕观看
    while datetime.now().hour.__eq__(hour):
        phone.swipe_down_to_up(pid, w, h, randrange(9, 16))


def full_jingdong_video_coin(pid, w, h, hour):
    print('京东看视频赚金币 ' + datetime.now().__str__())
    # 1. 打开程序
    checkin.jingdong(pid, w, h)
    # 2. 看视频赚金币
    jingdong_video_coin(pid, w, h, hour)
    # 3. 关闭程序
    phone.stop_app(pid, packages['jingdong'])


# ~~~~~~~~~~番茄免费小说~~~~~~~~~~

def fanqie_video_coin(pid, w, h, num=10):
    print("番茄看视频赚海量金币 " + datetime.now().__str__())
    # 1. 点击中间福利按钮
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)
    for i in range(0, num):
        # 2. 点击看视频赚海量金币
        input.tap(pid, w / 2, (HEIGHT - 1.8) * h / HEIGHT)  # <= modify
        # 3. 播放30s
        time.sleep(30)
        # 4. 点击关闭返回上级页面
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)


def read_fanqie_novel(pid, w, h, hour):
    """
    阅读番茄小说
    """
    print('阅读番茄小说 ' + datetime.now().__str__())
    # 1. 点击主页任意一本书
    input.tap(pid, w / 3, h / 2)
    # 2. 向左滑动开始阅读
    while datetime.now().hour.__eq__(hour):
        phone.swipe_right_to_left(pid, w, h / 4, randrange(3, 5))


# ~~~~~~~~~~番茄畅听~~~~~~~~~~

def fanchang_video_coin(pid, w, h, num):
    print("番畅看视频赚海量金币 " + datetime.now().__str__())
    # 1. 点击福利按钮
    input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)
    for i in range(0, num):
        # 2. 点击看视频赚海量金币
        input.tap(pid, w / 2, 9.0 * h / HEIGHT)
        # 3. 播放30s
        time.sleep(30)
        # 4. 点击返回到福利页面
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)


def listen_fanchang_sound(pid, w, h, sec=300):
    """
    听番畅音频
    """
    print('听番畅音频 ' + datetime.now().__str__())
    for i in range(0, 2):
        # 1. 点击收听按钮
        input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT, 15)  # <= modify
        # 返回上级页面消除可能存在的悬浮窗
        if i.__eq__(0):
            # 2. 返回上级页面
            phone.go_back(pid, 2)
    # 3. 收听番畅音频
    time.sleep(sec)
    # 4. 领取奖励
    input.tap(pid, (WIDTH - 1.0) * w / WIDTH, 10.5 * h / HEIGHT)  # <= modify

    # 分多次领取
    for i in range(0, 2):
        # 5. 点击领红包
        input.tap(pid, w / 2, (HEIGHT - 0.9) * h / HEIGHT)
        # 6. 点击看视频再领金币
        input.tap(pid, w / 2, 8.4 * h / HEIGHT)
        # 7. 播放30s
        time.sleep(30)
        # 8. 关闭广告
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 0.7 * h / HEIGHT)


# ~~~~~~~~~~微视~~~~~~~~~~

def watch_weishi_video(pid, w, h, hour=8):
    """
    看微视视频
    """
    while datetime.now().hour.__eq__(hour):
        phone.swipe_down_to_up(pid, w, h, randrange(9, 16))


def full_watch_weishi_video(pid, w, h, hour):
    print('看微视视频 ' + datetime.now().__str__())
    # 1. 进入微视
    checkin.weishi(pid)
    # 2. 看视频
    watch_weishi_video(pid, w, h, hour)
    # 3. 退出程序
    phone.stop_app(pid, 'weishi')


# ~~~~~~~~~~书旗小说~~~~~~~~~~

def read_shuqi_novel(pid, w, h, sec=300):
    """
    阅读书旗小说
    """
    print('阅读书旗小说 ' + datetime.now().__str__())
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


def shuqi_video_coin(pid, w, h, num):
    """
    看视频赚金币
    """
    print('书旗看视频赚金币 ' + datetime.now().__str__())
    # 1. 点击中间下方的福利
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)
    # 看num次视频
    for i in range(0, num):
        # 2. 点击快速得百万金币
        input.tap(pid, w / 2, 10.4 * h / HEIGHT)
        # 3. 播放30s
        time.sleep(30)
        # 4. 返回上级页面
        # 无法通过回退返回
        # 返回到福利页面
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)


def shuqi_invent_friend(pid, w, h):
    # 1. 下滑到最下
    phone.swipe_down_to_up(pid, w, h, internal=100)
    # 2. 点击邀请书友
    input.tap(pid, w / 2, 9.5 * h / HEIGHT)
    # 3. 点击微信好友
    input.tap(pid, 1.2 * w / WIDTH, (HEIGHT - 2.8) * h / HEIGHT)
    # 4. 回退到福利页面
    phone.go_back(pid)


# ~~~~~~~~~~映客直播极速版~~~~~~~~~~

def watch_yingke_live(pid, w, h, sec=300):
    """
    看映客直播
    """
    print('看映客直播 ' + datetime.now().__str__())
    # 1. 点击任意直播间
    input.tap(pid, w / 3, h / 3)
    # 2. 看直播
    time.sleep(sec)


# ~~~~~~~~~~酷狗大字版~~~~~~~~~~

def listen_kugou_music(pid, w, h, sec=300):
    """
    听酷狗音乐
    """
    print('听酷狗音乐 ' + datetime.now().__str__())
    # 1. 点击中间下方进入播放页面
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
    print('阅读惠头条文章 ' + datetime.now().__str__())
    for i in range(0, num):
        # 1. 获取文章目录
        phone.swipe_down_to_up(pid, w, h)
        # 2. 点击文章
        input.tap(pid, w / 2, h * 3 / 4)
        # 3. 滑动阅读
        for j in range(0, 5):
            phone.swipe_down_to_up(pid, w, h)
        # 4. 返回上级目录
        phone.go_back(pid)


# ~~~~~~~~~~中青看点~~~~~~~~~~

def read_zhongqing_article(pid, w, h, num):
    """
    阅读中青看点文章
    """
    print('阅读中青看点文章 ' + datetime.now().__str__())
    for i in range(0, num):
        # 1. 获取文章目录
        phone.swipe_down_to_up(pid, w, h)
        # 2. 点击文章
        input.tap(pid, w / 2, h * 3 / 4)
        # 3. 滑动阅读
        for j in range(0, 5):
            phone.swipe_down_to_up(pid, w, h)
        # 4. 返回上级目录
        phone.go_back(pid)


# ~~~~~~~~~~拼多多~~~~~~~~~~
def pinduoduo_street_money(pid, w, h):
    """
    拼多多逛街得现金
    """
    # 1. 点击现金签到
    input.tap(pid, w / 2, 5.4 * h / HEIGHT)  # <= modify
    # 2. 点击定时红包
    input.tap(pid, 2.5 * w / WIDTH, 5.0 * h / HEIGHT, gap=8)  # <= modify
    # 3. 浏览商品60s
    for i in range(0, 20):
        phone.swipe_down_to_up(pid, w, h, gap=3)


# ~~~~~~~~~~淘宝特价版~~~~~~~~~~

# ~~~~~~~~~~刷宝短视频~~~~~~~~~~
def watch_shuabao_video(pid, w, h, hour):
    """
    看刷宝视频
    """
    print('看刷宝视频 ' + datetime.now().__str__())
    while datetime.now().hour.__eq__(hour):
        phone.swipe_down_to_up(pid, w, h, randrange(9, 16))


def shuabao_video(pid, w, h, num):
    """
    以次数来看刷宝视频
    """
    print('看刷宝视频 ' + datetime.now().__str__())
    for i in range(0, num):
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


def full_watch_qutoutiao_svideo(pid, w, h, hour):
    print('看趣头条小视频 ' + datetime.now().__str__())
    # 1. 打开程序
    checkin.qutoutiao(pid)
    # 2. 看趣头条小视频
    watch_qutoutiao_svideo(pid, w, h, hour)
    # 3. 关闭程序
    phone.stop_app(pid, packages['qutoutiao'])


# ~~~~~~~~~~百度极速版~~~~~~~~~~

def baidu_haokan_video(pid, w, h, num):
    # 1. 点击好看视频
    input.tap(pid, 2.1 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)  # <= modify
    for i in range(0, num):
        # 2. 刷新页面
        phone.swipe_up_to_down(pid, w, h)
        # 3. 点击播放
        input.tap(pid, w / 2, h / 3)
        # ４. 播放35s
        time.sleep(35)


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


# ~~~~~~~~~~喜马拉雅~~~~~~~~~~
def listen_ximalaya_sound(pid, w, h, sec=300):
    """
    收听喜马拉雅音频
    """
    print('听喜马拉雅音频 ' + datetime.now().__str__())
    # 1. 点击中间的播放按钮
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)
    # 2. 收听
    time.sleep(sec)
    # 3. 点击气泡进行收集
    input.tap(pid, 0.7 * w / WIDTH, 3.5 * h / HEIGHT)  # <= modify


# ~~~~~~~~~~抖音火山版~~~~~~~~~~
def watch_douhuo_video(pid, w, h, sec=300):
    print('看抖音火山视频 ' + datetime.now().__str__())
    start = datetime.now()
    # 1. 点击进入视频播放界面
    input.tap(pid, w / 3, h / 3)
    # 2. 逐个看视频
    while (datetime.now() - start).seconds < sec:
        phone.swipe_down_to_up(pid, w, h / 2, randrange(9, 16))
