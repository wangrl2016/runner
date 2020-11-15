from datetime import datetime
from random import randrange
import time
from src import phone, input, utils, info
from src.info import HEIGHT, WIDTH


# ~~~~~~~~~~米读极速版~~~~~~~~~~

def midu_benefit_page(pid, w, h):
    input.tap(pid, 4.2 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)


def read_midu_novel(pid, w, h, sec):
    print('阅读米读小说 ' + datetime.now().__str__())
    # 1. 点击中间的小说
    input.tap(pid, w / 2, h / 2, gap=3)
    # 2. 向左滑动开始阅读
    minutes = sec / 60 + datetime.now().minute
    if minutes < 60:
        while datetime.now().minute < minutes:
            # 防止点击广告
            phone.swipe_right_to_left(pid, w, h * 4 / 5, randrange(3, 5))
    else:
        hour = datetime.now().hour
        while datetime.now().hour == hour:
            phone.swipe_right_to_left(pid, w, h * 4 / 5, randrange(3, 5))


# ~~~~~~~~~~长豆短视频~~~~~~~~~~
def changdou_benefit_page(pid, w, h, gap=3):
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT, gap)


# ~~~~~~~~~~长豆短视频~~~~~~~~~~

def kulingyin_benefit_page(pid, w, h):
    input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)


# ~~~~~~~~~~懒猫赚钱~~~~~~~~~~
def lanmao_benefit_page(pid, w, h):
    # 1. 点击中间下方懒猫
    input.tap(pid, w / 2, (HEIGHT - 0.7) * h / HEIGHT)


# ~~~~~~~~~~京东极速版~~~~~~~~~~

def jingdong_benefit_page(pid, w, h):
    # 1. 点击赚钱
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)


def jingdong_video_coin(pid, w, h, hour):
    """
    京东看视频赚金币
    """
    print('京东看视频赚金币 ' + datetime.now().__str__())
    # 1. 点击看视频赚金币
    input.tap(pid, w / 2, 11.0 * h / HEIGHT)  # <=== modify
    # 2. 消除可能存在的广告悬浮窗
    input.tap(pid, w / 3, h / 2)
    phone.go_back(pid)
    # 3. 任意点击视频进入
    input.tap(pid, w / 3, h / 2)
    # 4. 滑动屏幕观看
    while datetime.now().hour.__eq__(hour):
        phone.swipe_down_to_up(pid, w / 2, h, randrange(5, 16))


# ~~~~~~~~~~番茄免费小说~~~~~~~~~~

def fanqie_benefit_page(pid, w, h, gap=3):
    # 1. 点击中间下方的福利
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT, gap)


# ~~~~~~~~~~番茄畅听~~~~~~~~~~

def fanchang_benefit_page(pid, w, h):
    input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)  # <= modify


# ~~~~~~~~~~酷狗唱唱斗歌版~~~~~~~~~~
def kuchang_benefit_page(pid, w, h):
    input.tap(pid, 2.0 * w / WIDTH, 1.4 * h / HEIGHT)


# ~~~~~~~~~~书旗小说~~~~~~~~~~
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
            phone.swipe_right_to_left(pid, w, h / 8, randrange(3, 5))
    else:
        hour = datetime.now().hour
        while datetime.now().hour == hour:
            phone.swipe_right_to_left(pid, w, h / 8, randrange(3, 5))


def shuqi_video_coin(pid, w, h):
    print('书旗看视频赚金币 ' + datetime.now().__str__())
    # 1. 点击快速得百万金币
    input.tap(pid, w / 2, 10.4 * h / HEIGHT, gap=10)  # <== modify
    # 2. 播放30s
    time.sleep(30)


# 10~~~~~~~~~~映客直播极速版~~~~~~~~~~

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
            phone.swipe_down_to_up(pid, w / 2, h)
            # 2. 点击聊天文字
            input.tap(pid, w / 2, (HEIGHT - 1.3) * h / HEIGHT)

    # [x] 和主播聊天
    chat_with_anchor(times=3)


def share_yingke_live(pid, w, h, times):
    print('分享映客直播间 ' + datetime.now().__str__())
    # 1. 滑动到最下面
    phone.swipe_down_to_up(pid, w / 2, h, internal=100)

    for i in range(0, times):
        # 2. 点击分享映客极速版
        input.tap(pid, w / 2, (HEIGHT - 3.5) * h / HEIGHT)
        # 3. 点击分享到微信
        input.tap(pid, 1.7 * w / WIDTH, (HEIGHT - 1.1) * h / HEIGHT)
        # 4. 返回到福利页面
        phone.go_back(pid)

    # 5. 滑动到最上面
    phone.swipe_up_to_down(pid, w / 2, h, internal=100)


# 11~~~~~~~~~~酷狗大字版~~~~~~~~~~

# 进入福利页面
def kugou_benefit_page(pid, w, h, gap=3):
    # 1. 点击赚钱
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, (HEIGHT - 0.7) * h / HEIGHT, gap)  # <= modify


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


# 13~~~~~~~~~~中青看点~~~~~~~~~~

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
            phone.swipe_up_to_down(pid, w / 2, h)
        # 2. 点击文章
        input.tap(pid, w / 2, h / 3)
        # 3. 滑动阅读
        for j in range(0, 10):
            phone.swipe_down_to_up(pid, w / 2, h)
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
            phone.swipe_up_to_down(pid, w / 2, h)
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


# ~~~~~~~~~~快音~~~~~~~~~~
def kuaiyin_benefit_page(pid, w, h):
    # 点击右下方福利按钮
    input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)


def watch_kuaiyin_video(pid, w, h):
    """
    看快音视频
    """
    # 1. 点击播放
    input.tap(pid, 1.1 * w / WIDTH, 4.4 * h / HEIGHT, gap=10)
    # 2. 播放30s
    time.sleep(30)


# ~~~~~~~~~~趣红包~~~~~~~~~~

def quhongbao_benefit_page(pid, w, h):
    input.tap(pid, 4.2 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)


# ~~~~~~~~~~东方头条~~~~~~~~~~
def dongfang_benefit_page(pid, w, h):
    input.tap(pid, 4.2 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)


def read_dongfang_article(pid, w, h, num):
    for i in range(0, num):
        # 1. 刷新页面
        if i.__ne__(0):
            phone.swipe_up_to_down(pid, w / 2, h)
        # 2. 进入文章
        input.tap(pid, w / 2, h / 2, gap=3)
        for j in range(0, 15):
            # 3. 浏览文章
            phone.swipe_down_to_up(pid, w / 2, h / 3, gap=2, internal=300)
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
            phone.swipe_up_to_down(pid, w / 2, h)
        # 2. 查看详情进入文章
        input.tap(pid, w * 2 / 3, 8.8 * h / HEIGHT, gap=3)  # <=== modify
        for j in range(0, 15):
            # 3. 浏览文章
            phone.swipe_down_to_up(pid, w / 2, h / 3, gap=2, internal=300)
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
            phone.swipe_up_to_down(pid, w / 2, h)
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
        phone.swipe_down_to_up(pid, w / 2, h, randrange(6, 16))
    # 3. 返回上级页面
    phone.go_back(pid, gap=1)


# ~~~~~~~~~~趣看看~~~~~~~~~~

def qukankan_benefit_page(pid, w, h):
    input.tap(pid, 4.7 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)


def read_qukankan_article(pid, w, h, num):
    print('阅读趣看看文章 ' + datetime.now().time().__str__())
    for i in range(0, num):
        # 1. 点击文章
        input.tap(pid, w / 2, h / 2)
        # 2. 阅读30s
        for j in range(0, randrange(9, 11)):
            phone.swipe_down_to_up(pid, w / 2, h, gap=randrange(2, 5), internal=400)
        # 3. 返回上级页面
        phone.go_back(pid)


# ~~~~~~~~~~妙看短视频~~~~~~~~~~
def miaokan_benefit_page(pid, w, h):
    input.tap(pid, (WIDTH - 0.6) * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)


def watch_miaokan_video(pid, w, h, num):
    print('看妙看视频 ' + datetime.now().time().__str__())
    for i in range(0, num):
        phone.swipe_down_to_up(pid, w / 2, h, randrange(5, 16))
    # 需要点开红包圈圈
    for i in range(0, 3):
        input.tap(pid, 0.7 * w / WIDTH, h / 2 + i * h / 15, gap=1)


# ~~~~~~~~~~酷狗儿歌~~~~~~~~~~
def kuge_play_background(pid, w, h):
    print('后台播放酷狗儿歌 ' + datetime.now().__str__())
    # 1. 确认在儿歌页面
    input.tap(pid, 2.0 * h / HEIGHT, 1.2 * h / HEIGHT)
    # 2. 点击播放
    input.tap(pid, 4.7 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)  # <== modify
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
            phone.swipe_down_to_up(pid, w / 2, h, gap=3)
        # 3. 返回上级自动刷新
        phone.go_back(pid)


def makan_search_coin(pid, w, h, num):
    print('蚂蚁看点搜索赚 ' + datetime.now().__str__())
    # 1. 点击搜索赚
    input.tap(pid, 2.6 * w / WIDTH, 6.4 * h / HEIGHT)
    for i in range(0, num):
        # 2. 点击搜索词
        input.tap(pid, w / 5, 9.5 * h / HEIGHT)
        # 3. 返回上级页面
        phone.go_back(pid, gap=3)


# ~~~~~~~~~~点点新闻~~~~~~~~~~

def diandian_benefit_page(pid, w, h, gap=3):
    # 进入福利页面
    input.tap(pid, 4.3 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT, gap)


def diandian_daily_packet(pid, w, h):
    """
    天天领红包
    """
    print('天天领红包 ' + datetime.now().__str__())
    # 1. 获取今日红包的位置
    if '点点今日红包' not in info.contexts[pid]:
        packet_location = utils.current_words_location(pid, '今日红包')
        if packet_location is None:
            print('没有获取到今日红包的位置')
            return
        height = packet_location['y'] + packet_location['h']
        info.contexts[pid]['点点今日红包'] = height
    input.tap(pid, w / 2, info.contexts[pid]['点点今日红包'])

    # 2. 播放30s
    time.sleep(30)
    # 3. 必须返回到福利页面
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT, gap=3)


def read_diandian_article(pid, w, h, num):
    """
    看点点文章
    """
    print('看点点新闻文章 ' + datetime.now().__str__())
    for i in range(0, num):
        # 1. 向下刷新页面
        if i.__ne__(0):
            phone.swipe_up_to_down(pid, w / 2, h)
        # 2. 点击文章
        input.tap(pid, w / 2, h * 2 / 3, gap=5)
        for j in range(0, 8):
            # 3. 向上滑动15s
            phone.swipe_down_to_up(pid, w / 2, h, gap=2)
        # 4. 返回上级
        phone.go_back(pid, gap=2)


# ~~~~~~~~~~今日头条极速版~~~~~~~~~~

def toutiao_benefit_page(pid, w, h, gap=3):
    # 1. 点击福利
    input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT, gap)  # <= modify


def read_toutiao_article(pid, w, h, num):
    print('阅读今日头条文章 ' + datetime.now().__str__())
    for i in range(0, num):
        # 1. 获取文章目录
        phone.swipe_up_to_down(pid, w / 2, h)
        # 2. 点击文章
        input.tap(pid, w / 2, h * 2 / 5)
        # 3. 滑动阅读30s
        for j in range(0, 10):
            phone.swipe_down_to_up(pid, w / 2, h, randrange(2, 5))
        # 4. 返回上级目录
        phone.go_back(pid)


def toutiao_video(pid, w, h, num):
    print('看今日头条视频 ' + datetime.now().__str__())
    # 1. 点击下方视频按钮
    input.tap(pid, 2.0 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)
    for i in range(0, num):
        # 1. 向下刷新视频
        phone.swipe_up_to_down(pid, w / 2, h)
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
    print('看快手视频 ' + datetime.now().time().__str__())
    while datetime.now().hour.__eq__(hour):
        phone.swipe_down_to_up(pid, w / 2, h, randrange(5, 16))


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
        phone.swipe_down_to_up(pid, w / 2, h, randrange(5, 16))


# ~~~~~~~~~~火山极速版~~~~~~~~~~

def huoshan_benefit_page(pid, w, h, gap=3):
    # 1. 点击火山右下方红包
    input.tap(pid, 4.3 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT, gap)  # <== modify


def watch_huoshan_video(pid, w, h, hour=4):
    print('看火山视频 ' + datetime.now().time().__str__())
    # 消除可能的悬浮窗
    phone.go_back(pid, gap=1)
    while datetime.now().hour.__eq__(hour):
        phone.swipe_down_to_up(pid, w * 2 / 3, h * 3 / 4, randrange(5, 16))


# ~~~~~~~~~~趣头条~~~~~~~~~~
def qutoutiao_benefit_page(pid, w, h):
    # 1. 点击左下角任务
    input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)


# ~~~~~~~~~~百度极速版~~~~~~~~~~
def baidu_benefit_page(pid, w, h):
    input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)


def baidu_haokan_video(pid, w, h, num):
    print('看好看视频 ' + datetime.now().time().__str__())
    # 1. 点击好看视频
    input.tap(pid, 2.1 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)  # <= modify
    for i in range(0, num):
        # 2. 刷新页面
        phone.swipe_up_to_down(pid, w / 2, h)
        # 3. 点击播放
        input.tap(pid, w / 2, h / 3)
        # ４. 播放35s
        time.sleep(35)


def watch_baidu_svideo(pid, w, h, hour):
    print('看百度小视频 ' + datetime.now().__str__())
    # 1. 点击banner栏目中小视频
    input.tap(pid, 3.3 * w / WIDTH, 3.8 * h / HEIGHT)  # <= modify
    # 2. 点击任意小视频
    input.tap(pid, w / 3, h / 3)
    # 3. 滑动小视频
    while datetime.now().hour.__eq__(hour):
        phone.swipe_down_to_up(pid, w / 2, h, randrange(5, 16))


# ~~~~~~~~~~微视~~~~~~~~~~
def watch_weishi_video(pid, w, h, sec):
    print('看微视视频 ' + datetime.now().time().__str__())
    # 1. 消除可能存在的悬浮窗
    phone.go_back(pid, gap=1)
    # 2. 从下往上翻页
    minutes = sec / 60 + datetime.now().minute
    if minutes < 60:
        while datetime.now().minute < minutes:
            phone.swipe_down_to_up(pid, w / 2, h, randrange(5, 16))
    else:
        hour = datetime.now().hour
        while datetime.now().hour == hour:
            phone.swipe_down_to_up(pid, w / 2, h, randrange(5, 16))
    # 3. 收集现金
    input.tap(pid, 5.3 * w / WIDTH, 0.9 * h / HEIGHT, gap=2)


# ~~~~~~~~~~喜马拉雅极速版~~~~~~~~~~
def ximalaya_benefit_page(pid, w, h, gap=3):
    input.tap(pid, 4.3 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT, gap)


# ~~~~~~~~~~五八同城本地版~~~~~~~~~~
def wuba_benefit_page(pid, w, h, gap=3):
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT, gap)


def watch_wuba_video(pid, w, h, num):
    print('看五八同城广告视频 ' + datetime.now().time().__str__())
    # 1. 点击看视频赚金币
    input.tap(pid, w / 2, 9.5 * h / HEIGHT, gap=10)  # <== modify
    for i in range(0, num):
        # 2. 播放30s
        time.sleep(30)
        # 3. 点击关闭
        # 等待5s自动播放下一个
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT, gap=10)


# ~~~~~~~~~~淘宝特价版~~~~~~~~~~


# ~~~~~~~~~~刷宝短视频~~~~~~~~~~
def shuabao_benefit_page(pid, w, h):
    # 1. 点击右下方任务
    input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT, gap=3)
    # 2. 消除悬浮窗
    phone.go_back(pid)


def watch_shuabao_video(pid, w, h, num):
    """
    看刷宝视频
    """
    print('看刷宝短视频 ' + datetime.now().time().__str__())
    for i in range(0, num):
        phone.swipe_down_to_up(pid, w / 2, h, randrange(5, 16))


# ~~~~~~~~~~QQ阅读~~~~~~~~~~
def qqyuedu_benefit_page(pid, w, h, gap=3):
    # 1. 点击中间下方免费
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT, gap)
    # 2. 点击福利
    input.tap(pid, 1.7 * w / WIDTH, 1.0 * h / HEIGHT, gap)


def read_qqyuedu_novel(pid, w, h, sec):
    print('QQ阅读小说 ' + datetime.now().time().__str__())
    # 1. 点击书架
    input.tap(pid, 0.7 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT, gap=3)
    # 2. 点击任意书
    input.tap(pid, w / 6, h * 2 / 5, gap=3)
    # 3. 开始阅读
    minutes = sec / 60 + datetime.now().minute
    if minutes < 60:
        while datetime.now().minute < minutes:
            phone.swipe_right_to_left(pid, w, h * 7 / 8, randrange(2, 5))
    else:
        hour = datetime.now().hour
        while datetime.now().hour == hour:
            phone.swipe_right_to_left(pid, w, h * 7 / 8, randrange(2, 5))


# ~~~~~~~~~~汽车之家~~~~~~~~~~
def chejia_benefit_page(pid, w, h, gap=3):
    input.tap(pid, 4.7 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT, gap)


def chejia_benefit_video(pid, w, h, num):
    print('观看汽车之家福利视频 ' + datetime.now().time().__str__())
    # 1. 滑动进入到最下面
    phone.swipe_down_to_up(pid, w / 2, h)
    for i in range(0, num):
        # 2. 点击观看视频
        input.tap(pid, (WIDTH - 1.0) * w / WIDTH, (HEIGHT - 3.4) * h / HEIGHT, gap=10)
        # 3. 播放30s
        time.sleep(30)
        # 3. 关闭返回福利页面
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)


# ~~~~~~~~~~UC浏览器~~~~~~~~~~
def uc_benefit_page(pid, w, h, gap=3):
    input.tap(pid, (WIDTH - 1.2) * w / WIDTH, 1.4 * h / HEIGHT, gap)


# ~~~~~~~~~~快看点~~~~~~~~~~
def kuaikandian_benefit_page(pid, w, h, gap=3):
    input.tap(pid, (WIDTH - 0.6) * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT, gap)


def watch_kuaikandian_video(pid, w, h, sec):
    print('快看点视频播放 ' + datetime.now().time().__str__())
    # 1. 点击左下角视频
    input.tap(pid, 2.2 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)
    # 2. 点击播放
    input.tap(pid, w / 2, h / 5)
    # 3. 自动播放
    time.sleep(sec)


# ~~~~~~~~~~红包短视频~~~~~~~~~~
def watch_hongbao_video(pid, w, h, sec):
    print('看红包短视频 ' + datetime.now().time().__str__())
    # 2. 从下往上翻页
    minutes = sec / 60 + datetime.now().minute
    if minutes < 60:
        while datetime.now().minute < minutes:
            phone.swipe_down_to_up(pid, w / 2, h, randrange(5, 16))
    else:
        hour = datetime.now().hour
        while datetime.now().hour == hour:
            phone.swipe_down_to_up(pid, w / 2, h, randrange(5, 16))
    # 3. 收集金币
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)


# ~~~~~~~~~~豆豆免费小说~~~~~~~~~~
def doudou_benefit_page(pid, w, h):
    input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)


def read_doudou_novel(pid, w, h, sec):
    print('阅读豆豆小说 ' + datetime.now().time().__str__())
    # 1. 点击书架
    input.tap(pid, 0.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)
    # 2. 点击任意一本书
    input.tap(pid, w / 3, h * 3 / 5)
    # 3. 开始阅读
    minutes = sec / 60 + datetime.now().minute
    if minutes < 60:
        while datetime.now().minute < minutes:
            phone.swipe_right_to_left(pid, w, h / 7, randrange(2, 5))
    else:
        hour = datetime.now().hour
        while datetime.now().hour == hour:
            phone.swipe_right_to_left(pid, w, h / 7, randrange(2, 5))


# ~~~~~~~~~~七猫免费小说~~~~~~~~~~
def qimao_benefit_page(pid, w, h, sec=3):
    input.tap(pid, (WIDTH - 0.8) * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT, sec)


def read_qimao_novel(pid, w, h, sec):
    print('阅读七猫免费小说 ' + datetime.now().time().__str__())
    # 1. 点击任意一本书
    input.tap(pid, w / 2, h / 2, gap=3)
    # 2. 开始阅读
    minutes = sec / 60 + datetime.now().minute
    if minutes < 60:
        while datetime.now().minute < minutes:
            phone.swipe_right_to_left(pid, w, h / 7, randrange(2, 5))
    else:
        hour = datetime.now().hour
        while datetime.now().hour == hour:
            phone.swipe_right_to_left(pid, w, h / 7, randrange(2, 5))


# ~~~~~~~~~~看点快报~~~~~~~~~~
def kankuai_benefit_page(pid, w, h, gap=3):
    # 1. 点击右下角我的栏目
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT, gap)
    # 2. 点击福利红包
    input.tap(pid, w / 2, 9.5 * h / HEIGHT, gap)


def watch_kankuai_advert(pid, w, h, num):
    print("看点快报广告 " + datetime.now().__str__())
    for i in range(0, num):
        # 1. 点击去观看
        input.tap(pid, (WIDTH - 1.1) * w / WIDTH, (HEIGHT - 2.5) * h / HEIGHT, gap=3)
        # 2. 播放15s
        time.sleep(15)
        # 3. 点击关闭
        input.tap(pid, 0.5 * w / WIDTH, 1.7 * h / HEIGHT, gap=2)  # <=== modify


# ~~~~~~~~~~抖音火山版~~~~~~~~~~
def watch_douhuo_video(pid, w, h, sec=300):
    print('看抖音火山视频 ' + datetime.now().__str__())
    start = datetime.now()
    # 1. 点击进入视频播放界面
    input.tap(pid, w / 3, h / 3)
    # 2. 逐个看视频
    while (datetime.now() - start).seconds < sec:
        phone.swipe_down_to_up(pid, w / 3, h * 2 / 3, randrange(5, 16))


# ~~~~~~~~~~墨迹天气~~~~~~~~~~
def moji_benefit_page(pid, w, h):
    input.tap(pid, 4.2 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)


def moji_benefit_video(pid, w, h, num):
    print('墨迹福利视频 ' + datetime.now().time().__str__())
    for i in range(0, num):
        # 1. 点击看视频
        input.tap(pid, (WIDTH - 0.9) * w / WIDTH, 10.8 * h / HEIGHT)
        # 2. 播放30s
        time.sleep(30)
        # 3. 关闭返回福利页面
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 0.7 * h / HEIGHT, gap=2)


# ~~~~~~~~~~2345浏览器~~~~~~~~~~
def ersansi_benefit_page(pid, w, h):
    input.tap(pid, (WIDTH - 0.6) * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)


def read_ersansi_article(pid, w, h, num):
    print('阅读2345浏览器文章 ' + datetime.now().time().__str__())
    for i in range(0, num):
        # 1. 获取文章目录
        if i != 0:
            phone.swipe_up_to_down(pid, w / 2, h)
        # 2. 点击文章
        input.tap(pid, w / 2, h / 2)
        # 3. 滑动阅读30s
        for j in range(0, 10):
            phone.swipe_down_to_up(pid, w / 2, h, randrange(2, 5))
        # 4. 返回上级目录
        phone.go_back(pid)


# ~~~~~~~~~~糖豆~~~~~~~~~~
def tangdou_benefit_page(pid, w, h):
    # 1. 点击右下角我的栏目
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)
    # 2. 点击任务中心
    input.tap(pid, w / 2, 9.6 * h / HEIGHT)


def tangdou_funny_video(pid, w, h, num):
    print('糖豆有趣短视频 ' + datetime.now().__str__())
    # 1. 点击有趣短视频按钮
    video_location = utils.current_words_location(pid, '有趣')
    if video_location is None:
        print('没有刷有趣短视频的位置')
        return
    height = video_location['y'] + video_location['h']
    input.tap(pid, w / 2, height)
    # 2. 刷视频
    for i in range(0, num):
        phone.swipe_down_to_up(pid, w / 2, h)
        time.sleep(15)
    # 3. 返回上级页面
    phone.go_back(pid, gap=1)


# ~~~~~~~~~~洋葱免费小说~~~~~~~~~~
def yangcong_benefit_page(pid, w, h, gap=3):
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT, gap)


# ~~~~~~~~~~搜狗浏览器极速版~~~~~~~~~~
def sougou_benefit_page(pid, w, h, gap=3):
    input.tap(pid, (WIDTH - 1.2) * w / WIDTH, 1.2 * h / HEIGHT, gap)
