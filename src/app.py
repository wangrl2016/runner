from datetime import datetime
from random import randrange
import time
from src import phone, input, checkin, utils, info
from src.info import HEIGHT, WIDTH


# ~~~~~~~~~~今日头条极速版~~~~~~~~~~

def toutiao_benefit_page(pid, w, h, gap=3):
    """
    进入今日头条福利页面
    """
    # 1. 点击福利
    input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT, gap)  # <= modify


def read_toutiao_article(pid, w, h, num):
    """
    阅读今日头条文章
    """
    print('阅读头条文章 ' + datetime.now().__str__())
    for i in range(0, num):
        # 1. 获取文章目录
        if i.__ne__(0):
            phone.swipe_up_to_down(pid, w, h)
        # 2. 点击文章
        input.tap(pid, w / 2, h / 3)
        # 3. 滑动阅读
        for j in range(0, 10):
            # 阅读30s
            phone.swipe_down_to_up(pid, w, h / 2, gap=2, internal=100)
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
        if i.__ne__(0):
            phone.swipe_up_to_down(pid, w, h)
        # 2. 点击播放
        input.tap(pid, w / 2, h / 3)
        # 3. 播放60s
        time.sleep(60)


# ~~~~~~~~~~快手极速版~~~~~~~~~~

def kuaishou_benefit_page(pid, w, h, gap=3):
    """
    进入快手福利页面
    """
    # 1. 点击左上角菜单栏
    input.tap(pid, 0.6 * w / WIDTH, 0.9 * h / HEIGHT, gap)  # <= modify
    # 2. 点击去赚钱
    input.tap(pid, w / 3, 6.3 * h / HEIGHT, gap)  # <=== modify


# 只包含看视频的过程
def watch_kuaishou_video(pid, w, h, hour):
    """
    看快手视频
    """
    while datetime.now().hour.__eq__(hour):
        phone.swipe_down_to_up(pid, w, h, randrange(5, 16))


# 从打开到关闭看快手视频的完整过程
def full_watch_kuaishou_video(pid, w, h, hour):
    print('看快手视频 ' + datetime.now().__str__())
    # 1. 打开程序
    checkin.kuaishou(pid)
    # 2. 看快手视频
    watch_kuaishou_video(pid, w, h, hour)
    # 3. 关闭程序
    phone.stop_app(pid, info.packages['kuaishou'])


# noinspection PyUnusedLocal
def kuaishou_reward_task(pid, w, h, num):
    """
    1000金币悬赏任务
    """
    print('快手1000金币悬赏任务 ' + datetime.now().__str__())
    reward_location = utils.current_words_location(pid, '悬')
    if reward_location is None:
        print('没有获取到1000金币悬赏任务的位置')
        return
    height = reward_location['y'] + reward_location['h']
    for i in range(0, num):
        # 1. 点击福利按钮
        input.tap(pid, (WIDTH - 1.0) * w / WIDTH, height)
        # 2. 播放30s
        time.sleep(30)
        # 3. 返回到福利页面
        phone.go_back(pid)


# ~~~~~~~~~~抖音极速版~~~~~~~~~~

def douyin_benefit_page(pid, w, h, gap=3):
    """
    进入抖音福利页面
    """
    # 1. 点击中间下方的福利
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT, gap)


def watch_douyin_video(pid, w, h, hour=3):
    """
    看抖音视频
    """
    while datetime.now().hour.__eq__(hour):
        phone.swipe_down_to_up(pid, w, h, randrange(5, 16))


def full_watch_douyin_video(pid, w, h, hour):
    # [x] 看抖音视频
    print('看抖音视频 ' + datetime.now().__str__())
    # 1. 打开程序
    checkin.douyin(pid)
    # 2. 回退消除可能的悬浮窗
    phone.go_back(pid)
    # 3. 看抖音视频
    watch_douyin_video(pid, w, h, hour)
    # 4. 关闭程序
    phone.stop_app(pid, info.packages['douyin'])


# ~~~~~~~~~~火山极速版~~~~~~~~~~

def huoshan_benefit_page(pid, w, h, gap=3):
    """
    进入火山福利页面
    """
    # 1. 点击火山右下方红包
    input.tap(pid, 4.3 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT, gap)  # <== modify


def watch_huoshan_video(pid, w, h, hour=4):
    """
    看火山视频
    """
    while datetime.now().hour.__eq__(hour):
        phone.swipe_down_to_up(pid, w, h, randrange(5, 16))


def full_watch_huoshan_video(pid, w, h, hour):
    print('看火山视频 ' + datetime.now().__str__())
    # 1. 打开程序
    checkin.huoshan(pid)
    # 2. 看火山视频
    watch_huoshan_video(pid, w, h, hour)
    # 3. 关闭程序
    phone.stop_app(pid, info.packages['huoshan'])


def huoshan_money_tree(pid, w, h):
    """
    摇钱树
    """
    print('火山摇钱树 ' + datetime.now().__str__())
    # 1. 点击右下方红包
    input.tap(pid, 4.3 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)
    # 2. 点击摇钱树
    input.tap(pid, w / 3, 5.0 * h / HEIGHT)
    # 3. 摇钱
    input.tap(pid, w / 2, h / 2)
    # 返回到任务页面
    phone.go_back(pid)


# ~~~~~~~~~~京东极速版~~~~~~~~~~

def jingdong_benefit_page(pid, w, h):
    # 1. 点击赚钱
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)


def jingdong_good(pid, w, h, num):
    """
    逛商品赚金币
    """
    print('京东逛商品赚金币 ' + datetime.now().__str__())
    jingdong_benefit_page(pid, w, h)
    # 1. 点击逛商品赚金币
    input.tap(pid, w / 2, 8.4 * h / HEIGHT)  # <=== modify
    for i in range(0, num):
        # 2. 逛10s
        for j in range(0, 2):
            phone.swipe_down_to_up(pid, w, h, gap=5)
        # 3. 点击下一个商品
        input.tap(pid, (WIDTH - 0.9) * w / WIDTH, 8.4 * h / HEIGHT)  # <=== modify


def jingdong_activity(pid, w, h, num):
    """
    逛活动赚金币
    """
    print('京东逛活动赚金币 ' + datetime.now().__str__())
    jingdong_benefit_page(pid, w, h)
    # 1. 点击逛活动赚金币
    input.tap(pid, w / 2, 9.7 * h / HEIGHT)  # <=== modify
    for i in range(0, num):
        # 2. 逛15s
        for j in range(0, 3):
            phone.swipe_down_to_up(pid, w, h, 5)
        # 3. 点击下一个商品
        input.tap(pid, (WIDTH - 0.9) * w / WIDTH, 8.0 * h / HEIGHT)


def jingdong_video_coin(pid, w, h, hour=5):
    """
    京东看视频赚金币
    """
    print('京东看视频赚金币 ' + datetime.now().__str__())
    for i in range(0, 2):
        jingdong_benefit_page(pid, w, h)
        # 1. 点击看视频赚金币
        input.tap(pid, w / 2, 11.0 * h / HEIGHT)  # <=== modify
        # 消除可能存在的悬浮窗
        if i.__eq__(0):
            phone.go_back(pid, times=3)
    # 2. 任意点击视频进入
    input.tap(pid, w / 3, h / 2)
    # 3. 滑动屏幕观看
    while datetime.now().hour.__eq__(hour):
        phone.swipe_down_to_up(pid, w, h, randrange(5, 16))


def full_jingdong_video_coin(pid, w, h, hour):
    # 打开程序
    checkin.jingdong(pid, w, h)
    # 看视频赚金币
    jingdong_video_coin(pid, w, h, hour)
    # 关闭程序
    phone.stop_app(pid, info.packages['jingdong'])


# ~~~~~~~~~~番茄免费小说~~~~~~~~~~

def fanqie_benefit_page(pid, w, h):
    # 1. 点击中间下方的福利
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)


# def fanqie_video_coin(pid, w, h, num=10):
#     print("番茄看视频赚海量金币 " + datetime.now().__str__())
#     fanqie_benefit_page(pid, w, h)
#     for i in range(0, num):
#         # 2. 点击看视频赚海量金币
#         input.tap(pid, w / 2, (HEIGHT - 1.8) * h / HEIGHT)  # <= modify
#         # 3. 播放30s
#         time.sleep(30)
#         # 4. 点击关闭返回上级页面
#         input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT, gap=3)


def read_fanqie_novel(pid, w, h, sec):
    """
    阅读番茄小说
    """
    print('阅读番茄小说 ' + datetime.now().__str__())
    # 1. 点击主页任意一本书
    input.tap(pid, w / 3, h / 2)
    # 2. 向左滑动开始阅读
    minutes = sec / 60 + datetime.now().minute
    if minutes < 60:
        while datetime.now().minute < minutes:
            # 防止点击广告
            phone.swipe_right_to_left(pid, w, h / 4, randrange(3, 5))
    else:
        hour = datetime.now().hour
        while datetime.now().hour.__eq__(hour):
            phone.swipe_right_to_left(pid, w, h / 4, randrange(3, 5))


# ~~~~~~~~~~番茄畅听~~~~~~~~~~

def fanchang_benefit_page(pid, w, h):
    input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)  # <= modify


def fanchang_video_coin(pid, w, h, num):
    print("番畅看视频赚海量金币 " + datetime.now().__str__())
    for i in range(0, num):
        # 2. 点击看视频赚海量金币
        input.tap(pid, w / 2, 9.0 * h / HEIGHT, gap=3)
        # 3. 播放30s
        time.sleep(30)
        # 4. 点击返回到福利页面
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT, gap=3)


# ~~~~~~~~~~酷狗唱唱斗歌版~~~~~~~~~~
def kuchang_benefit_page(pid, w, h):
    input.tap(pid, 2.0 * w / WIDTH, 1.4 * h / HEIGHT)


# ~~~~~~~~~~微视~~~~~~~~~~

# def watch_weishi_video(pid, w, h, hour=8):
#     """
#     看微视视频
#     """
#     while datetime.now().hour.__eq__(hour):
#         phone.swipe_down_to_up(pid, w, h, randrange(5, 16))
#     # 1. 收集现金
#     input.tap(pid, 5.3 * w / WIDTH, 0.9 * h / HEIGHT)
#
#
# def full_watch_weishi_video(pid, w, h, hour):
#     print('看微视视频 ' + datetime.now().__str__())
#     # 1. 进入微视
#     checkin.weishi(pid)
#     # 2. 看视频
#     watch_weishi_video(pid, w, h, hour)
#     # 3. 退出程序
#     phone.stop_app(pid, 'weishi')


# ~~~~~~~~~~书旗小说~~~~~~~~~~

# 进入福利页面
def shuqi_benefit_page(pid, w, h, gap=3):
    # 1. 点击中间下方的福利
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT, gap)


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
            # 3. 滑动阅读小说
            # 防止点击广告
            phone.swipe_right_to_left(pid, w, h / 4, randrange(3, 5))
    else:
        hour = datetime.now().hour
        while datetime.now().hour.__eq__(hour):
            phone.swipe_right_to_left(pid, w, h / 4, randrange(3, 5))


def shuqi_video_coin(pid, w, h):
    """
    看视频赚金币
    """
    print('书旗看视频赚金币 ' + datetime.now().__str__())
    shuqi_benefit_page(pid, w, h)
    # 看视频
    # 2. 点击快速得百万金币
    input.tap(pid, w / 2, 10.4 * h / HEIGHT, gap=10)  # <== modify
    # 3. 播放30s
    time.sleep(30)


# ~~~~~~~~~~映客直播极速版~~~~~~~~~~

def yingke_benefit_page(pid, w, h, gap=5):
    # 1. 点击下面的横幅
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT, gap)  # <= modify


def watch_yingke_live(pid, w, h, sec):
    """
    看映客直播
    """
    print('看映客直播 ' + datetime.now().__str__())
    # 1. 回退消除可能的悬浮窗
    phone.go_back(pid)
    # 2. 点击任意直播间
    input.tap(pid, w / 3, h / 3)
    # 3. 看直播
    time.sleep(sec)

    def chat_with_anchor(times):
        print('和主播聊天 ' + datetime.now().__str__())
        for i in range(0, times):
            # 1. 换一个主播
            phone.swipe_down_to_up(pid, w, h)
            # 2. 点击聊天文字
            # [x] 和主播聊天
            input.tap(pid, w / 2, (HEIGHT - 1.3) * h / HEIGHT)

    # 4. 和主播聊天
    chat_with_anchor(times=3)


def share_yingke(pid, w, h, times):
    """
    分享映客直播间
    """
    print('分享映客直播间 ' + datetime.now().__str__())
    # 1. 滑动到最下面
    phone.swipe_down_to_up(pid, w, h / 2, internal=100)

    for i in range(0, times):
        # 2. 点击分享映客极速版
        input.tap(pid, w / 2, (HEIGHT - 3.5) * h / HEIGHT)
        # 3. 点击分享到微信
        input.tap(pid, 1.7 * w / WIDTH, (HEIGHT - 1.1) * h / HEIGHT)
        # 4. 返回到福利页面
        phone.go_back(pid)

    # 5. 滑动到最上面
    phone.swipe_up_to_down(pid, w, h / 2, internal=100)


# ~~~~~~~~~~酷狗大字版~~~~~~~~~~

# 进入福利页面
def kugou_benefit_page(pid, w, h):
    # 1. 点击赚钱
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, (HEIGHT - 0.7) * h / HEIGHT)  # <= modify


def kugou_background_music(pid, w, h):
    """
    听酷狗音乐
    """
    print('听酷狗音乐 ' + datetime.now().__str__())
    # 1. 点击下方图标进入播放页面
    input.tap(pid, w / 2, (HEIGHT - 0.7) * h / HEIGHT)
    # 2. 点击播放
    input.tap(pid, w / 2, (HEIGHT - 1.4) * h / HEIGHT)
    # 3. 回到主页
    phone.go_back(pid)
    # 4. 后台播放
    phone.go_home(pid)


# ~~~~~~~~~~惠头条~~~~~~~~~~

def huitoutiao_benefit_page(pid, w, h):
    # 1. 点击中间下方的任务中心
    input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)


def read_huitoutiao_article(pid, w, h, num):
    """
    阅读惠头条文章
    """
    print('阅读惠头条文章 ' + datetime.now().__str__())
    # 1. 消除可能存在的悬浮窗
    phone.go_back(pid, gap=1)
    for i in range(0, num):
        # 2. 获取文章目录
        if i.__ne__(0):
            phone.swipe_up_to_down(pid, w, randrange(h / 2, h))
        # 3. 阅读中间文章
        input.tap(pid, randrange(w / 3, w * 2 / 3), h * 3 / 5)
        # 4. 滑动阅读
        for j in range(0, randrange(9, 12)):
            phone.swipe_down_to_up(pid, w, randrange(h / 2, h), randrange(2, 5), internal=300)
        # 5. 返回上级目录
        phone.go_back(pid)


def watch_huitoutiao_video(pid, w, h, sec):
    """
    看惠头条视频
    """
    print('看惠头条视频 ' + datetime.now().__str__())
    # 1. 点击惠头条视频
    input.tap(pid, 2.0 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)
    # 2. 点击视频
    input.tap(pid, w / 2, h / 4)
    # 3. 播放
    time.sleep(sec)
    # 4. 返回到首页
    phone.go_back(pid)


# ~~~~~~~~~~中青看点~~~~~~~~~~

def zhongqing_benefit_page(pid, w, h):
    input.tap(pid, 4.3 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)  # <= modify


def read_zhongqing_article(pid, w, h, num):
    """
    阅读中青看点文章
    """
    print('阅读中青看点文章 ' + datetime.now().__str__())
    for i in range(0, num):
        # 1. 获取文章目录
        if i.__ne__(0):
            phone.swipe_up_to_down(pid, w, h)
        # 2. 点击文章
        input.tap(pid, w / 2, h / 3)
        # 3. 滑动阅读
        for j in range(0, 10):
            phone.swipe_down_to_up(pid, w, h)
        # 4. 返回上级目录
        phone.go_back(pid)


def watch_zhongqing_video(pid, w, h, num):
    """
    看中青看点视频
    """
    print('看中青看点视频 ' + datetime.now().__str__())
    # 1. 进入视频页面
    input.tap(pid, 2.5 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)
    for i in range(0, num):
        # 2. 获取视频目录
        if i.__ne__(0):
            phone.swipe_up_to_down(pid, w, h)
        # 3. 点击视频
        input.tap(pid, w / 2, h / 4)
        # 4. 播放30s
        time.sleep(30)
        # 5. 返回上级页面
        phone.go_back(pid)


def zhongqing_weixin_article(pid, w, h, num):
    # 1. 点击个人对话框
    input.tap(pid, w / 2, 2.0 * h / HEIGHT, gap=3)
    # 2. 点击领取奖励
    input.tap(pid, w * 2 / 3, h / 5)
    # 3. 点击开始阅读
    for i in range(0, 2):
        input.tap(pid, w / 2, 9.8 * h / HEIGHT)
    for i in range(0, num):
        # 4. 阅读10s
        time.sleep(10)
        # 5. 返回到自动播放页面
        phone.go_back(pid, gap=5)


# ~~~~~~~~~~拼多多~~~~~~~~~~
def pinduoduo_street_money(pid, w, h):
    """
    拼多多逛街得现金
    """
    # 1. 点击现金签到
    input.tap(pid, w / 2, 5.4 * h / HEIGHT)  # <= modify
    # 2. 点击定时红包
    input.tap(pid, 2.5 * w / WIDTH, 5.0 * h / HEIGHT, gap=8)  # <= modify
    # 3. 浏览商品70s
    for i in range(0, 35):
        phone.swipe_down_to_up(pid, w, h, gap=2)


# ~~~~~~~~~~快音~~~~~~~~~~
def kuaiyin_benefit_page(pid, w, h):
    # 点击右下方福利按钮
    input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)


def watch_kuaiyin_video(pid, w, h):
    """
    看快音视频
    """
    # 1. 点击播放
    input.tap(pid, 1.1 * w / WIDTH, 4.4 * h / HEIGHT)
    # 2. 播放40s
    time.sleep(40)
    # 3. 关闭返回上级页面
    # TODO: 关闭的位置
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 0.7 * h / HEIGHT)


# ~~~~~~~~~~糖豆~~~~~~~~~~
def tangdou_benefit_page(pid, w, h):
    # 1. 点击右下角我的栏目
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)
    # 2. 点击任务中心
    input.tap(pid, w / 2, 9.6 * h / HEIGHT)


def tangdou_funny_video(pid, w, h, num):
    print('糖豆有趣短视频 ' + datetime.now().__str__())
    """
    刷有趣短视频
    """
    # 1. 向上滑动
    phone.swipe_down_to_up(pid, w, h, gap=3)
    # 2. 点击有趣短视频按钮
    video_location = utils.current_words_location(pid, '有趣')
    if video_location is None:
        print('没有刷有趣短视频的位置')
        return
    height = video_location['y'] + video_location['h']
    input.tap(pid, w / 2, height)
    # 3. 刷视频
    for i in range(0, num):
        phone.swipe_down_to_up(pid, w, h)
        time.sleep(15)
    # 4. 返回上级页面
    phone.go_back(pid, gap=1)
    # 5. 向下滑动
    phone.swipe_up_to_down(pid, w, h, gap=1, internal=100)


# ~~~~~~~~~~东方头条~~~~~~~~~~
def dongfang_benefit_page(pid, w, h):
    input.tap(pid, 4.2 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)


def read_dongfang_article(pid, w, h, num):
    for i in range(0, num):
        # 1. 刷新页面
        if i.__ne__(0):
            phone.swipe_up_to_down(pid, w, h)
        # 2. 进入文章
        input.tap(pid, w / 2, h / 2, gap=3)
        for j in range(0, 15):
            # 3. 浏览文章
            phone.swipe_down_to_up(pid, w, h / 3, gap=2, internal=300)
        # 4. 返回上级目录
        phone.go_back(pid, gap=1)


# ~~~~~~~~~~聚看点~~~~~~~~~~
def jukandian_benefit_page(pid, w, h):
    input.tap(pid, 4.7 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)


def read_jukandian_article(pid, w, h, num):
    print('聚看点文章 ' + datetime.now().__str__())
    # 可能存在悬浮窗
    for i in range(0, num):
        # 1. 刷新页面
        if i.__ne__(0):
            phone.swipe_up_to_down(pid, w, h)
        # 2. 进入文章
        input.tap(pid, w / 2, h / 2, gap=3)
        for j in range(0, 15):
            # 3. 浏览文章
            phone.swipe_down_to_up(pid, w, h / 3, gap=2, internal=300)
        # 4. 返回上级目录
        phone.go_back(pid, gap=1)


def watch_jukandian_video(pid, w, h, num):
    print('聚看点视频 ' + datetime.now().__str__())
    # 可能存在悬浮窗
    # 1. 点击视频按钮
    input.tap(pid, 2.1 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)
    for i in range(0, num):
        if i.__ne__(0):
            # 2. 刷新页面
            phone.swipe_up_to_down(pid, w, h)
        # 3. 点击播放
        input.tap(pid, w / 2, h / 5)
        # 4. 播放30s
        time.sleep(30)
        # 5. 返回上级页面
        phone.go_back(pid)


def watch_jukandian_svideo(pid, w, h, num):
    print('聚看点小视频 ' + datetime.now().__str__())
    # 1. 点击小视频
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)
    for i in range(0, num):
        # 2. 看小视频
        phone.swipe_down_to_up(pid, w, h, randrange(6, 16))
    # 3. 返回上级页面
    phone.go_back(pid, gap=1)


# ~~~~~~~~~~看点快报~~~~~~~~~~
def kankuai_benefit_page(pid, w, h):
    # 1. 点击右下角我的栏目
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)
    # 2. 点击福利红包
    input.tap(pid, w / 2, 9.5 * h / HEIGHT)


def watch_kankuai_advert(pid, w, h, num):
    print("看点快报广告 " + datetime.now().__str__())
    for i in range(0, num):
        # 1. 点击去观看
        input.tap(pid, (WIDTH - 1.1) * w / WIDTH, (HEIGHT - 2.5) * h / HEIGHT, gap=3)
        # 2. 播放15s
        time.sleep(15)
        # 3. 点击关闭
        input.tap(pid, 0.5 * w / WIDTH, 1.7 * h / HEIGHT, gap=2)  # <=== modify


# ~~~~~~~~~~淘宝特价版~~~~~~~~~~

# ~~~~~~~~~~刷宝短视频~~~~~~~~~~
#
# def shuabao_benefit_page(pid, w, h):
#     # 1. 点击福利
#     input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)  # <= modify
#     # 2. 回退关闭悬浮窗
#     phone.go_back(pid)
#
#
# def watch_shuabao_video(pid, w, h, hour):
#     """
#     看刷宝视频
#     """
#     print('看刷宝视频 ' + datetime.now().__str__())
#     while datetime.now().hour.__eq__(hour):
#         phone.swipe_down_to_up(pid, w, h, randrange(5, 16))
#
#
# def shuabao_video(pid, w, h, num):
#     """
#     以次数来看刷宝视频
#     """
#     print('看刷宝视频 ' + datetime.now().__str__())
#     for i in range(0, num):
#         phone.swipe_down_to_up(pid, w, h, randrange(5, 16))
#
#

#
#
# # noinspection PyUnusedLocal
# def read_qutoutiao_article(pid, w, h, num):
#     return None
#
#
# # noinspection PyUnusedLocal
# def watch_qutoutiao_video(pid, w, h, num):
#     return None
#
#
# def watch_qutoutiao_svideo(pid, w, h, hour):
#     """
#     看趣头条小视频
#     """
#     # 　1. 点击中间下方小视频
#     input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)
#     while datetime.now().hour.__eq__(hour):
#         # TODO: 中途出现彩蛋需要点击
#         phone.swipe_down_to_up(pid, w, h, randrange(5, 16))
#
#
# def full_watch_qutoutiao_svideo(pid, w, h, hour):
#     print('看趣头条小视频 ' + datetime.now().__str__())
#     # 1. 打开程序
#     checkin.qutoutiao(pid)
#     # 2. 看趣头条小视频
#     watch_qutoutiao_svideo(pid, w, h, hour)
#     # 3. 关闭程序
#     phone.stop_app(pid, packages['qutoutiao'])
#

#
#
# def baidu_haokan_video(pid, w, h, num):
#     # 1. 点击好看视频
#     input.tap(pid, 2.1 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)  # <= modify
#     for i in range(0, num):
#         # 2. 刷新页面
#         phone.swipe_up_to_down(pid, w, h)
#         # 3. 点击播放
#         input.tap(pid, w / 2, h / 3)
#         # ４. 播放35s
#         time.sleep(35)
#
#
# def watch_baidu_svideo(pid, w, h, hour):
#     """
#     看百度小视频
#     """
#     # 1. 点击banner栏目中小视频
#     input.tap(pid, 3.3 * w / WIDTH, 3.8 * h / HEIGHT)  # <= modify
#     # 2. 点击任意小视频
#     input.tap(pid, w / 3, h / 3)
#     # 3. 滑动小视频
#     while datetime.now().hour.__eq__(hour):
#         phone.swipe_down_to_up(pid, w, h, randrange(5, 16))
#


# ~~~~~~~~~~抖音火山版~~~~~~~~~~
def watch_douhuo_video(pid, w, h, sec=300):
    print('看抖音火山视频 ' + datetime.now().__str__())
    start = datetime.now()
    # 1. 点击进入视频播放界面
    input.tap(pid, w / 3, h / 3)
    # 2. 逐个看视频
    while (datetime.now() - start).seconds < sec:
        phone.swipe_down_to_up(pid, w * 2 / 3, h * 2 / 3, randrange(5, 16))


# ~~~~~~~~~~酷狗儿歌~~~~~~~~~~
def kuge_play_background(pid, w, h):
    print('后台播放酷狗儿歌 ' + datetime.now().__str__())
    # 1. 确认在儿歌页面
    input.tap(pid, 2.0 * h / HEIGHT, 1.2 * h / HEIGHT)
    # 2. 点击播放
    input.tap(pid, 4.2 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)  # <== modify
    # 3. 回到后台
    phone.go_home(pid)


# ~~~~~~~~~~抖音火山版~~~~~~~~~~

# ~~~~~~~~~~蚂蚁看点~~~~~~~~~~

def makan_benefit_page(pid, w, h):
    input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)


def read_makan_article(pid, w, h, num):
    print('看蚂蚁看点文章 ' + datetime.now().__str__())
    for i in range(0, num):
        # 1. 点击文章
        input.tap(pid, w / 2, h / 3)
        for j in range(0, 10):
            # 2. 向上滑动
            phone.swipe_down_to_up(pid, w, h, gap=3)
        # TODO: 如何解决可能出现的彩蛋
        # 3. 返回上级
        phone.go_back(pid)
        # 4. 刷新页面
        phone.swipe_up_to_down(pid, w, h)


def makan_search_coin(pid, w, h, num):
    print('蚂蚁看点搜索赚 ' + datetime.now().__str__())
    # 1. 点击搜索赚
    input.tap(pid, 2.6 * w / WIDTH, 6.4 * h / HEIGHT)
    for i in range(0, num):
        # 2. 点击搜索词
        input.tap(pid, w / 3, (HEIGHT - 1.2) * h / HEIGHT)
        # 3. 返回上级页面
        phone.go_back(pid, gap=5)


# ~~~~~~~~~~点点新闻~~~~~~~~~~

def diandian_benefit_page(pid, w, h, gap=3):
    # 进入福利页面
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT, gap)


def daily_packet(pid, w, h):
    """
    天天领红包
    """
    print('天天领红包 ' + datetime.now().__str__())
    # 1. 进入福利页面
    diandian_benefit_page(pid, w, h)
    # 2. 获取今日红包的位置
    if '点点今日红包' not in info.contexts[pid]:
        packet_location = utils.current_words_location(pid, '今日红包')
        if packet_location is None:
            print('没有获取到今日红包的位置')
            return
        height = packet_location['y'] + packet_location['h']
        info.contexts[pid]['点点今日红包'] = height
    input.tap(pid, w / 2, info.contexts[pid]['点点今日红包'])

    # 3. 播放30s
    time.sleep(30)
    # 4. 必须返回到福利页面
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT, gap=3)


def read_diandian_article(pid, w, h, num):
    """
    看点点文章
    """
    print('看点点新闻文章 ' + datetime.now().__str__())
    for i in range(0, num):
        # 1. 向下刷新页面
        if i.__ne__(0):
            phone.swipe_up_to_down(pid, w, h)
        # 2. 点击文章
        input.tap(pid, w / 2, h * 2 / 3, gap=5)
        for j in range(0, 8):
            # 3. 向上滑动
            phone.swipe_down_to_up(pid, w, h, gap=2)
        # 4. 返回上级
        phone.go_back(pid, gap=2)


# ~~~~~~~~~~墨迹天气~~~~~~~~~~
def moji_benefit_page(pid, w, h):
    input.tap(pid, 4.2 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)


# ~~~~~~~~~~趣头条~~~~~~~~~~
def qutoutiao_benefit_page(pid, w, h):
    # 1. 点击左下角任务
    input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)


# ~~~~~~~~~~百度极速版~~~~~~~~~~
def baidu_benefit_page(pid, w, h):
    input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)


# ~~~~~~~~~~微视~~~~~~~~~~

# ~~~~~~~~~~喜马拉雅极速版~~~~~~~~~~
def ximalaya_benefit_page(pid, w, h):
    input.tap(pid, 4.3 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)


# ~~~~~~~~~~五八同城本地版~~~~~~~~~~
def wuba_benefit_page(pid, w, h):
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)

# ~~~~~~~~~~淘宝特价版~~~~~~~~~~

# ~~~~~~~~~~刷宝短视频~~~~~~~~~~

# ~~~~~~~~~~悦头条~~~~~~~~~~

# ~~~~~~~~~~米读极速版~~~~~~~~~~
