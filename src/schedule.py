import time
from datetime import datetime
from random import randrange

from src import checkin, phone, input, app, utils, info
from src.info import WIDTH, HEIGHT, SCHEDULE_TIME


def test(pid, name=None, w=0, h=0):
    """
    调用相关任务进行测试
    """
    if name:
        print('任务测试 ' + datetime.now().time().__str__())
        eval(name)(pid, w, h)


# noinspection PyUnusedLocal
def midu(pid, w, h):
    def benefit_video(num):
        print('看米读福利视频 ' + datetime.now().time().__str__())
        # 1. 点击我的栏目
        input.tap(pid, (WIDTH - 0.9) * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT, gap=3)
        # 2. 点击福利中心栏目
        input.tap(pid, 1.0 * w / WIDTH, 8.9 * h / HEIGHT, gap=3)
        for i in range(0, num):
            # 1. 点击播放
            input.tap(pid, (1.2 + i * 1.5) * w / WIDTH, 7.1 * h / HEIGHT, gap=10)
            # 2. 播放30s
            time.sleep(30)
            # 3. 返回到点击页面
            # 可能返回2次
            phone.go_back(pid)

    if datetime.now().minute < SCHEDULE_TIME:
        if datetime.now().hour % 10 == 0:
            checkin.midu(pid, w, h)
            # [x] 米读福利视频
            benefit_video(num=1)
            phone.stop_app(pid, info.packages['midu'])


# noinspection PyUnusedLocal
def changdou(pid, w, h):
    return None


# noinspection PyUnusedLocal
def kulingyin(pid, w, h):
    return None


def lanmao(pid, w, h):
    def cat_food():
        print('懒猫赚猫粮 ' + datetime.now().__str__())
        # 1. 点击赚猫粮
        input.tap(pid, w / 2, 8.2 * h / HEIGHT, gap=10)
        # 2. 播放30s
        time.sleep(30)

    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        if datetime.now().hour % 3 == 0:
            checkin.lanmao(pid, w, h)
            # [x] 领取猫粮10次
            cat_food()
            phone.stop_app(pid, info.packages['lanmao'])


# noinspection PyUnusedLocal
def jingdong(pid, w, h):
    return None


def fanqie(pid, w, h):
    def open_treasure():
        print('番茄小说开宝箱 ' + datetime.now().time().__str__())
        # 1. 点击开宝箱得金币
        input.tap(pid, (WIDTH - 1.0) * w / WIDTH, (HEIGHT - 2.3) * h / HEIGHT)  # <= modify
        # 2. 点击看视频再领金币
        input.tap(pid, w / 2, 8.7 * h / HEIGHT)
        # 3. 播放30s
        time.sleep(30)
        # 4. 返回到福利页面
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT, gap=2)  # <= modify

    checkin.fanqie(pid, w, h)
    app.fanqie_benefit_page(pid, w, h)

    # [x] 开宝箱
    open_treasure()

    phone.stop_app(pid, info.packages['fanqie'])


def fanchang(pid, w, h):
    def open_treasure():
        print('番茄畅听开宝箱 ' + datetime.now().time().__str__())
        # 1. 点击开宝箱得金币
        input.tap(pid, (WIDTH - 1.0) * w / WIDTH, (HEIGHT - 2.1) * h / HEIGHT)  # <= modify
        # 2. 点击看视频再领金币
        input.tap(pid, w / 2, 9.9 * h / HEIGHT)  # <= modify
        # 3. 播放30s
        time.sleep(30)
        # 4. 返回到福利页面
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT, gap=2)  # <== modify

    # 1, 4, 7, 10, 13, 16, 19, 22上半时段
    # 2, 5, 8, 11, 14, 17, 20, 23下半时段
    if (datetime.now().hour % 3).__eq__(1) and datetime.now().minute.__lt__(SCHEDULE_TIME) or (
            (datetime.now().hour % 3).__eq__(2) and datetime.now().minute.__ge__(SCHEDULE_TIME)):
        checkin.fanchang(pid, w, h)
        app.fanchang_benefit_page(pid, w, h)
        # [x] 番茄畅听开宝箱
        open_treasure()
        phone.stop_app(pid, info.packages['fanchang'])


def kuchang(pid, w, h):
    # 看创意视频
    def kuchang_creative_video():
        print('酷狗唱唱看创意视频 ' + datetime.now().__str__())
        # 1. 获取创意视频的位置
        if '酷狗唱唱创意' not in info.contexts[pid]:
            creative_location = utils.current_words_location(pid, '创意')
            if creative_location is None:
                print('没有获取到创意视频的位置')
                return
            height = creative_location['y'] + creative_location['h']
            info.contexts[pid]['酷狗唱唱创意'] = height
        input.tap(pid, (WIDTH - 1.2) * w / WIDTH, info.contexts[pid]['酷狗唱唱创意'], gap=10)

        # 2. 播放30s
        time.sleep(30)
        # 3. 返回上级页面
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT, gap=2)

    # 每个小时一次
    # 1, 4, 7, 10, 13, 16, 19, 22开上半时段
    # 2, 5, 8, 11, 14, 17, 20, 23开下半时段
    if (datetime.now().hour % 3).__eq__(1) and datetime.now().minute.__lt__(SCHEDULE_TIME) or (
            (datetime.now().hour % 3).__eq__(2) and datetime.now().minute.__ge__(SCHEDULE_TIME)):
        checkin.kuchang(pid, w, h)
        app.kuchang_benefit_page(pid, w, h)
        kuchang_creative_video()
        phone.stop_app(pid, info.packages['kuchang'])


def shuqi(pid, w, h):
    def shuqi_invent_friend():
        print("邀请书友 " + datetime.now().__str__())
        # 1. 下滑到最下
        phone.swipe_down_to_up(pid, w / 2, h)
        # 2. 点击邀请书友
        input.tap(pid, w / 2, 9.5 * h / HEIGHT, gap=3)
        # 3. 点击微信好友
        input.tap(pid, 1.2 * w / WIDTH, (HEIGHT - 2.8) * h / HEIGHT, gap=3)
        # 4. 回退到福利页面
        phone.go_back(pid)
        # 5. 恢复原貌
        phone.swipe_up_to_down(pid, w / 2, h)

    if datetime.now().hour.__eq__(8):
        checkin.shuqi(pid, w, h)
        app.shuqi_benefit_page(pid, w, h)
        # [x] 邀请书友
        shuqi_invent_friend()
        phone.stop_app(pid, info.packages['shuqi'])


def yingke(pid, w, h):
    def benefit_video():
        print('映客福利视频 ' + datetime.now().__str__())
        # 1. 点击领金币
        input.tap(pid, (WIDTH - 1.2) * w / WIDTH, 4.7 * h / HEIGHT, gap=10)  # <== modify
        # 2. 播放30s
        time.sleep(30)

    # 开宝箱
    def open_treasure():
        print('映客开宝箱 ' + datetime.now().__str__())
        # 1. 点击开宝箱领金币
        input.tap(pid, (WIDTH - 1.1) * w / WIDTH, (HEIGHT - 2.5) * h / HEIGHT, gap=10)  # <== modify
        # 2. 播放视频30s
        time.sleep(30)

    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        if datetime.now().hour.__gt__(9):
            checkin.yingke(pid, w, h)
            app.yingke_benefit_page(pid, w, h)
            # [x] 看福利视频10次
            benefit_video()
            phone.stop_app(pid, info.packages['yingke'])

            checkin.yingke(pid, w, h)
            app.yingke_benefit_page(pid, w, h)
            # [x] 开宝箱10次
            open_treasure()
            phone.stop_app(pid, info.packages['yingke'])


def kugou(pid, w, h):
    def creative_video():
        print('酷狗刷创意视频 ' + datetime.now().time().__str__())

        # 获取创意视频的位置
        if '酷狗创意视频' not in info.contexts[pid]:
            video_location = utils.current_words_location(pid, '创')
            if video_location is None:
                print('没有获取到创意视频的位置')
                return
            height = video_location['y'] + video_location['h']
            info.contexts[pid]['酷狗创意视频'] = height

        # 1. 点击去赚钱
        input.tap(pid, (WIDTH - 1.0) * w / WIDTH, info.contexts[pid]['酷狗创意视频'], gap=10)
        # 2. 播放30s
        time.sleep(30)
        # 3. 必须点击关闭
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT, gap=2)
        # 4. 回到福利页面
        phone.go_back(pid)

    def share_friend(is_song):
        print('酷狗分享视频或歌曲 ' + datetime.now().__str__())
        if is_song:
            # 1. 点击进入播放页面
            input.tap(pid, w / 2, (HEIGHT - 0.7) * h / HEIGHT)
            # 2. 点击分享
            input.tap(pid, (WIDTH - 1.0) * w / WIDTH, 1.1 * h / HEIGHT)
        else:
            # 1. 点击看点
            input.tap(pid, 2.0 * w / WIDTH, (HEIGHT - 0.7) * h / HEIGHT)
            # 2. 点击分享
            input.tap(pid, (WIDTH - 1.0) * w / WIDTH, 7.1 * h / HEIGHT)
        # 3. 分享到微信
        input.tap(pid, w / 3, 9.5 * h / HEIGHT)  # <= modify
        # 4. 回到酷狗程序主页
        phone.go_back(pid, gap=1)

    if datetime.now().minute > SCHEDULE_TIME:
        checkin.kugou(pid, w, h)
        if datetime.now().hour.__eq__(4):
            # [x] 分享歌曲
            share_friend(is_song=True)
        elif datetime.now().hour.__eq__(5):
            # [x] 分享视频
            share_friend(is_song=False)

        app.kugou_benefit_page(pid, w, h)
        # [x] 刷创意视频
        # 总共20次定时任务
        creative_video()
        if 11 < datetime.now().hour < 15:
            phone.go_home(pid)
        else:
            phone.stop_app(pid, info.packages['kugou'])


# noinspection PyUnusedLocal
def qukan(pid, w, h):
    return None


def zhongqing(pid, w, h):
    def time_reward():
        print('中青看点时段奖励 ' + datetime.now().time().__str__())
        # 1. 点击领取
        # 有时候没有广告视频
        input.tap(pid, (WIDTH - 0.9) * w / WIDTH, 1.0 * h / HEIGHT, gap=8)
        # 消除奖励提醒
        phone.go_back(pid)

    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        checkin.zhongqing(pid, w, h)
        # [x] 时段奖励
        time_reward()
        # [x] 阅读文章
        app.read_zhongqing_article(pid, w, h, num=1)
        # [x] 看中青看点视频
        app.watch_zhongqing_video(pid, w, h, num=1)
        phone.stop_app(pid, info.packages['zhongqing'])


# noinspection PyUnusedLocal
def pinduoduo(pid, w, h):
    return None


def kuaiyin(pid, w, h):
    def drink_water(is_next):
        print('快音喝水赚钱 ' + datetime.now().__str__())
        # 1. 点击喝水赚钱
        input.tap(pid, 2.6 * w / WIDTH, 4.4 * h / HEIGHT)
        # 2. 点击水杯
        for i in range(0, 4):
            input.tap(pid, (0.9 + i * 1.5) * w / WIDTH, (5.2 if is_next else 3.5) * h / HEIGHT, gap=1)
        # 3. 看视频
        input.tap(pid, w / 2, 9.1 * h / HEIGHT, gap=10)
        # 4. 播放30s
        time.sleep(30)

    def advert_video():
        print('快音视频广告 ' + datetime.now().__str__())
        # 1. 点击看视频赚钱
        input.tap(pid, 1.0 * w / WIDTH, 4.4 * h / HEIGHT, gap=10)
        # 2. 播放30s
        time.sleep(30)

    def offline_coin():
        print('快音离线收益 ' + datetime.now().__str__())
        # 1. 看视频领取100金币
        input.tap(pid, w / 2, 8.0 * h / HEIGHT, gap=10)  # <=== modify
        # 2. 播放30s
        time.sleep(30)

    def open_treasure():
        print('快音开宝箱 ' + datetime.now().__str__())
        # 1. 点击宝箱
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 11.5 * h / HEIGHT)  # <=== modify
        # 2. 点击看视频再领金币
        input.tap(pid, w / 2, 7.8 * h / HEIGHT, gap=10)
        # 3. 播放30s
        time.sleep(30)

    def sleep_money(is_sleep):
        print('快音睡觉赚钱 ' + datetime.now().__str__())

        for i in range(0, 2):
            # 1. 点击睡觉赚钱
            input.tap(pid, 4.1 * w / WIDTH, 4.4 * h / HEIGHT)
            # 2. 消除可能存在的睡觉签到
            if i != 0:
                phone.go_back(pid)

        # 3. 点击我要睡觉/我睡醒了
        for i in range(0, 2 if is_sleep else 1):
            input.tap(pid, w / 2, (HEIGHT - 1.2) * h / HEIGHT)

    if datetime.now().minute.__lt__(SCHEDULE_TIME):

        checkin.kuaiyin(pid, w, h)
        app.kuaiyin_benefit_page(pid, w, h)
        # [x] 离线收益
        offline_coin()
        phone.stop_app(pid, info.packages['kuaiyin'])

        if (datetime.now().hour % 2).__eq__(0):
            checkin.kuaiyin(pid, w, h)
            app.kuaiyin_benefit_page(pid, w, h)
            # [x] 开宝箱
            open_treasure()
            phone.stop_app(pid, info.packages['kuaiyin'])

        hour = datetime.now().hour
        if hour.__eq__(6) or hour.__eq__(9) or hour.__eq__(11) or (hour.__gt__(12) and hour.__lt__(18)):
            checkin.kuaiyin(pid, w, h)
            app.kuaiyin_benefit_page(pid, w, h)
            # [x] 八次喝水
            drink_water(False if hour.__lt__(14) else True)
            phone.stop_app(pid, info.packages['kuaiyin'])

        # [x] 睡觉赚钱
        # 21:00-2:00为睡觉时间
        # 06:00-09:00为醒来时间
        if hour.__eq__(21):
            sleep_money(False)
        elif hour.__eq__(6):
            sleep_money(True)

        if (datetime.now().hour % 5).__eq__(0):
            checkin.kuaiyin(pid, w, h)
            app.kuaiyin_benefit_page(pid, w, h)
            # [x] 看视频赚钱
            advert_video()
            phone.stop_app(pid, info.packages['kuaiyin'])


# noinspection PyUnusedLocal
def quhongbao(pid, w, h):
    def offline_coin():
        print('趣红包离线收益 ' + datetime.now().time().__str__())
        # 1. 点击开心手下
        input.tap(pid, w / 2, 9.5 * h / HEIGHT)
        # 2. 播放30s
        time.sleep(30)

    def drink_water():
        print('趣红包喝水赚钱 ' + datetime.now().time().__str__())
        # 1. 点击喝水赚钱
        input.tap(pid, 4.2 * w / WIDTH, 7.7 * h / HEIGHT, gap=3)
        # 2. 打卡
        input.tap(pid, w / 2, 11.3 * h / HEIGHT, gap=2)

    if datetime.now().minute < SCHEDULE_TIME:
        if datetime.now().hour % 5 == 0:
            checkin.quhongbao(pid, w, h)
            # [x] 离线收益
            offline_coin()
            phone.stop_app(pid, info.packages['quhongbao'])

            if 6 <= datetime.now().hour <= 22:
                checkin.quhongbao(pid, w, h)
                # [x] 喝水赚钱
                # 每两个小时一次
                drink_water()
                phone.stop_app(pid, info.packages['quhongbao'])


def jukandian(pid, w, h):
    def time_reward():
        print('聚看点时段奖励 ' + datetime.now().time().__str__())
        input.tap(pid, 0.8 * w / WIDTH, 0.9 * h / HEIGHT)
        phone.go_back(pid)

    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        checkin.jukandian(pid, w, h)
        # [x] 阅读文章
        app.read_jukandian_article(pid, w, h, num=1)

        # [x] 时段奖励
        time_reward()
        phone.stop_app(pid, info.packages['jukandian'])


def qukankan(pid, w, h):
    def time_reward():
        print('趣看看时段奖励 ' + datetime.now().time().__str__())
        # 1. 点击领取
        input.tap(pid, (WIDTH - 0.8) * w / WIDTH, 0.9 * h / HEIGHT, gap=2)
        # 2. 消除奖励提醒
        phone.go_back(pid, gap=1)

    if datetime.now().minute < SCHEDULE_TIME:
        if datetime.now().hour % 7 == 0:
            checkin.qukankan(pid, w, h)
            # [x] 时段奖励
            time_reward()

            # [x] 阅读文章
            app.read_qukankan_article(pid, w, h, num=2)
            phone.stop_app(pid, info.packages['qukankan'])


# noinspection PyUnusedLocal
def miaokan(pid, w, h):
    return None


def kuge(pid, w, h):
    def share_song():
        print('酷狗儿歌分享歌曲 ' + datetime.now().time().__str__())
        # 1. 确认在儿歌页面
        input.tap(pid, 2.0 * h / HEIGHT, 1.2 * h / HEIGHT, gap=2)
        # 2. 点击进入全屏播放页面
        input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT, gap=2)
        # 3. 点击右上角分享
        input.tap(pid, (WIDTH - 0.6) * w / WIDTH, 0.9 * h / HEIGHT)
        # 4. 点击微信
        input.tap(pid, w / 6, h * 6 / 7)
        # 5. 返回
        phone.go_back(pid, gap=1)

    if datetime.now().minute.__gt__(SCHEDULE_TIME):
        if datetime.now().hour.__eq__(23):
            checkin.kuge(pid, w, h)
            # [x] 分享歌曲
            share_song()
            # 关闭酷狗儿歌后台播放
            phone.stop_app(pid, info.packages['kuge'])


def makan(pid, w, h):
    def time_reward():
        print('蚂蚁看点时段奖励 ' + datetime.now().time().__str__())
        # 1. 点击领取
        input.tap(pid, 0.8 * w / WIDTH, 1.0 * h / HEIGHT, gap=2)

    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        if datetime.now().hour % 5 == 0:
            checkin.makan(pid, w, h)
            # 消除悬浮窗
            phone.go_back(pid, gap=1)

            # [x] 时段奖励
            time_reward()
            phone.stop_app(pid, info.packages['makan'])

        if datetime.now().hour.__eq__(21):
            checkin.makan(pid, w, h)
            phone.go_back(pid, gap=2)
            # [x] 阅读蚂蚁看点文章
            app.read_makan_article(pid, w, h, num=1)
            # 解决彩蛋问题
            input.tap(pid, 1.0 * w / WIDTH, 2.3 * h / HEIGHT, gap=2)
            phone.stop_app(pid, info.packages['makan'])


def diandian(pid, w, h):
    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        if (datetime.now().hour % 3).__eq__(0):
            checkin.diandian(pid, w, h)
            # [x] 阅读点点文章
            app.read_diandian_article(pid, w, h, num=3)
            phone.stop_app(pid, info.packages['diandian'])


# noinspection PyUnusedLocal
def xingqiu(pid, w, h):
    return None


# 25-48
def toutiao(pid, w, h):
    def open_treasure():
        print('今日头条开宝箱 ' + datetime.now().time().__str__())
        # 1. 点击宝箱
        input.tap(pid, (WIDTH - 1.2) * w / WIDTH, (HEIGHT - 1.7) * h / HEIGHT)  # <== modify
        # 2. 点击看视频再领金币
        input.tap(pid, w / 2, 9.4 * h / HEIGHT)  # <== modify
        # 3. 播放15s
        time.sleep(15)
        # 4. 返回到任务页面
        phone.go_back(pid)

    def meal_allowance():
        print('今日头条吃饭补贴 ' + datetime.now().time().__str__())
        # 1. 获取吃饭补贴的位置
        if '今日头条吃饭补贴' not in info.contexts[pid]:
            eat_location = utils.current_words_location(pid, '饭')
            if eat_location is None:
                print('没有获取到吃饭补贴的位置')
                return
            width = eat_location['x'] + eat_location['w']
            height = eat_location['y'] + eat_location['h']
            info.contexts[pid]['今日头条吃饭补贴'] = str(width) + 'x' + str(height)
        input.tap(pid, int(info.contexts[pid]['今日头条吃饭补贴'].split('x')[0]),
                  int(info.contexts[pid]['今日头条吃饭补贴'].split('x')[1]))

        # 2. 领取补贴
        input.tap(pid, w / 2, (HEIGHT - 1.3) * h / HEIGHT, gap=3)  # <= modify
        # 3. 返回到福利页面
        phone.go_back(pid)

    # 睡觉赚钱
    def sleep_money(is_sleep):
        print('今日头条睡觉赚钱 ' + datetime.now().time().__str__())
        # 1. 获取睡觉赚钱的位置
        if '今日头条睡觉' not in info.contexts[pid]:
            sleep_location = utils.current_words_location(pid, '睡')
            if sleep_location is None:
                print('没有获取到睡觉赚钱的位置')
                return
            width = sleep_location['x'] + sleep_location['w']
            height = sleep_location['y'] + sleep_location['h']
            info.contexts[pid]['今日头条睡觉'] = str(width) + 'x' + str(height)
        input.tap(pid, int(info.contexts[pid]['今日头条睡觉'].split('x')[0]),
                  int(info.contexts[pid]['今日头条睡觉'].split('x')[1]))

        # 2. 点击我要睡了/我睡醒了
        for i in range(0, 2 if is_sleep else 1):
            input.tap(pid, w / 2, (HEIGHT - 1.0) * h / HEIGHT, gap=3)  # <= modify
        # 3. 返回到福利页面
        phone.go_back(pid)

    # 打开头条
    checkin.toutiao(pid)

    # [x] 阅读头条文章
    app.read_toutiao_article(pid, w, h, num=1)

    app.toutiao_benefit_page(pid, w, h)

    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        # [x] 吃饭补贴
        # 早中晚夜宵4次
        hour = datetime.now().hour
        if hour.__eq__(6) or hour.__eq__(12) or hour.__eq__(18) or hour.__eq__(22):
            meal_allowance()

        # [x] 睡觉赚钱
        # 20:00-2:00为睡觉时间
        if hour.__eq__(20):
            sleep_money(is_sleep=False)
        elif hour.__eq__(3):
            sleep_money(is_sleep=True)

    # [x] 开宝箱
    # 每10分钟一次
    open_treasure()

    # 关闭头条
    phone.stop_app(pid, info.packages['toutiao'])


def kuaishou(pid, w, h):
    def open_treasure():
        print('快手开宝箱 ' + datetime.now().time().__str__())
        # 1. 点击开宝箱得金币
        input.tap(pid, 5.7 * w / WIDTH, (HEIGHT - 3.1) * h / HEIGHT)  # <== modify
        # 2. 返回到播放视频的页面
        phone.go_back(pid)

    def watch_live(num):
        print('快手看直播领金币 ' + datetime.now().__str__())
        # 1. 向上滑动到页面底部
        phone.swipe_down_to_up(pid, w / 2, h)
        # 2. 点击看直播按钮
        live_location = utils.current_words_location(pid, '看直播领金币')
        if live_location is None:
            print('没有获取到看直播领金币的位置')
            return
        height = live_location['y'] + live_location['h']
        input.tap(pid, (WIDTH - 1.0) * w / WIDTH, height)

        for i in range(0, num):
            # 3. 观看30s
            time.sleep(30)
            # 4. 上滑出现下一个
            phone.swipe_down_to_up(pid, w / 2, h, gap=5)

        # 5. 返回到福利页面
        phone.go_back(pid)
        # 6. 福利页面恢复原样
        phone.swipe_up_to_down(pid, w / 2, h)

    # 每隔一个小时开一次宝箱
    if datetime.now().minute.__lt__(SCHEDULE_TIME) and (datetime.now().hour % 2).__eq__(0):
        checkin.kuaishou(pid)
        app.kuaishou_benefit_page(pid, w, h)

        if datetime.now().hour.__eq__(20) or datetime.now().hour.__eq__(22):
            # [x] 看直播领金币
            # 20:00-24:00
            watch_live(num=5)

        # [x] 开宝箱
        open_treasure()

        phone.stop_app(pid, info.packages['kuaishou'])


def douyin(pid, w, h):
    def open_treasure():
        print('抖音开宝箱 ' + datetime.now().time().__str__())
        # 1. 点击开宝箱得金币
        input.tap(pid, (WIDTH - 1.1) * w / WIDTH, (HEIGHT - 1.1) * h / HEIGHT)  # <== modify
        # 2. 点击看广告视频再赚金币
        input.tap(pid, w / 2, 8.4 * h / HEIGHT)  # <== modify
        # 3. 播放30s
        time.sleep(30)
        # 4. 返回到播放页面
        phone.go_back(pid, times=3, gap=1)

    def limit_duty():
        print('抖音限时任务赚金币 ' + datetime.now().__str__())
        # 获取限时任务的位置
        if '抖音限时' not in info.contexts[pid]:
            limit_location = utils.current_words_location(pid, '限时')
            if limit_location is None:
                print('没有获取到限时任务的位置')
                return
            height = limit_location['y'] + limit_location['h']
            info.contexts[pid]['抖音限时'] = height

        # 点击限时赚金币
        input.tap(pid, w / 3, info.contexts[pid]['抖音限时'])

        # 2. 播放30s
        time.sleep(30)
        # 3. 返回福利页面
        phone.go_back(pid)

    def sleep_money(is_sleep):
        print('抖音睡觉赚钱 ' + datetime.now().time().__str__())
        # 获取抖音睡觉的位置
        if '抖音睡觉' not in info.contexts[pid]:
            sleep_location = utils.current_words_location(pid, '觉')
            if sleep_location is None:
                print('没有获取到睡觉赚钱的位置')
                return
            info.contexts[pid]['抖音睡觉'] = sleep_location['y'] + sleep_location['h']

        # 1. 点击睡觉赚金币
        input.tap(pid, w / 4, info.contexts[pid]['抖音睡觉'])

        # 2. 点击我要睡了/我睡醒了
        for i in range(0, 2 if is_sleep else 1):
            input.tap(pid, w / 2, (HEIGHT - 1.0) * h / HEIGHT)
        # 3. 返回到福利页面
        phone.go_back(pid)

    def meal_allowance():
        print('抖音吃饭补贴 ' + datetime.now().time().__str__())
        # 1. 下滑到任务页最下面
        phone.swipe_down_to_up(pid, w / 2, h)

        if '抖音吃饭' not in info.contexts[pid]:
            eat_location = utils.current_words_location(pid, '饭')
            if eat_location is None:
                print('没有获取到抖音吃饭补贴的位置')
                return
            info.contexts[pid]['抖音吃饭'] = eat_location['y'] + eat_location['h']

        # 2. 点击吃饭补贴
        input.tap(pid, w / 3, info.contexts[pid]['抖音吃饭'])
        # 3. 领取补贴
        input.tap(pid, w / 2, (HEIGHT - 1.3) * h / HEIGHT, gap=2)  # <= modify
        # 4. 返回到播放页面
        phone.go_back(pid, times=3, gap=1)

    checkin.douyin(pid)
    app.douyin_benefit_page(pid, w, h)

    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        # [x] 睡觉赚金币
        # 20:00-2:00为睡觉时间
        if datetime.now().hour.__eq__(20):
            sleep_money(False)
        elif datetime.now().hour.__eq__(5):
            sleep_money(True)

        # [x] 吃饭补贴
        # 早中晚夜宵4次
        hour = datetime.now().hour
        if hour.__eq__(6) or hour.__eq__(12) or hour.__eq__(18) or hour.__eq__(22):
            meal_allowance()
            app.douyin_benefit_page(pid, w, h)
            phone.swipe_up_to_down(pid, w / 2, h)

    # [x] 开宝箱得金币
    # 每20分钟一次
    open_treasure()

    app.douyin_benefit_page(pid, w, h)
    # [x] 限时任务赚金币
    # 每20分钟一次
    limit_duty()

    phone.stop_app(pid, info.packages['douyin'])


def huoshan(pid, w, h):
    def open_treasure():
        print('火山视频开宝箱 ' + datetime.now().time().__str__())
        # 1. 点击开宝箱得金币
        input.tap(pid, (WIDTH - 1.0) * w / WIDTH, (HEIGHT - 2.1) * h / HEIGHT)  # <= modify
        # 2. 点击看视频金币翻倍按钮
        input.tap(pid, w / 2, 9.4 * h / HEIGHT)  # <= modify
        # 3. 播放30s
        time.sleep(30)
        # 4. 返回到福利页面
        phone.go_back(pid)

    def video_money():
        print('火山视频看视频赚海量金币 ' + datetime.now().time().__str__())
        # 1. 点击看视频赚海量金币
        input.tap(pid, w / 2, 7.5 * h / HEIGHT)
        # 2. 播放30s
        time.sleep(30)
        # 3. 返回到福利页面
        phone.go_back(pid)

    def sleep_money(is_sleep):
        print('火山睡觉赚钱 ' + datetime.now().__str__())

        # 获取火山睡觉的位置
        if '火山睡觉' not in info.contexts[pid]:
            sleep_location = utils.current_words_location(pid, '觉')
            if sleep_location is None:
                print('没有获取到火山睡觉的位置')
                return
            info.contexts[pid]['火山睡觉'] = sleep_location['y'] + sleep_location['h']

        # 1. 点击睡觉赚金币
        input.tap(pid, w / 2, info.contexts[pid]['火山睡觉'])  # <=== modify
        # 2. 点击我要睡了/我睡醒了
        for i in range(0, 2 if is_sleep else 1):
            input.tap(pid, w / 2, (HEIGHT - 1.0) * h / HEIGHT, gap=3)  # <= modify
        # 3. 返回到回到福利页面
        phone.go_back(pid)

    checkin.huoshan(pid)
    app.huoshan_benefit_page(pid, w, h)

    if datetime.now().minute.__lt__(SCHEDULE_TIME):

        # [x] 睡觉赚金币
        # 20:00-2:00为睡觉时间
        if datetime.now().hour.__eq__(20):
            sleep_money(False)
        elif datetime.now().hour.__eq__(3):
            sleep_money(True)

        # [x] 看视频赚海量金币
        # 总计20次
        if datetime.now().hour.__gt__(3):
            video_money()

    # [x] 开宝箱
    # 每20分钟一次
    open_treasure()

    phone.stop_app(pid, info.packages['huoshan'])


def qutoutiao(pid, w, h):
    def time_reward():
        print('趣头条时段奖励 ' + datetime.now().time().__str__())
        # 1. 点击进入文章页面
        input.tap(pid, 0.7 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)
        # 2. 点击领取
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.0 * h / HEIGHT)

    def open_treasure():
        print('趣头条开宝箱 ' + datetime.now().__str__())
        # 1. 点击宝箱
        input.tap(pid, (WIDTH - 1.0) * w / WIDTH, (HEIGHT - 1.6) * h / HEIGHT)
        # 2. 播放广告50s
        time.sleep(50)
        # 3. 回退到程序主页
        phone.go_back(pid, times=2, gap=1)

    # 睡觉赚钱
    def sleep_money(is_sleep):
        print('趣头条睡觉赚钱 ' + datetime.now().time().__str__())
        # 1. 点击睡觉赚金币
        input.tap(pid, w / 2, 9.3 * h / HEIGHT)  # <=== modify
        # 2. 点击我要睡了/我睡醒了
        for i in range(0, 2 if is_sleep else 1):
            input.tap(pid, w / 2, (HEIGHT - 1.0) * h / HEIGHT, gap=8)  # <= modify
        # 3. 返回到福利页面
        phone.go_back(pid)

    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        checkin.qutoutiao(pid)
        app.qutoutiao_benefit_page(pid, w, h)

        # [x] 睡觉赚金币
        # 20:00-08:00为睡觉时间
        # 12:00-14:00为午休时间
        if datetime.now().hour.__eq__(20):
            sleep_money(False)
        elif datetime.now().hour.__eq__(9):
            sleep_money(True)
        elif datetime.now().hour.__eq__(12):
            sleep_money(False)
        elif datetime.now().hour.__eq__(15):
            sleep_money(True)
        phone.stop_app(pid, info.packages['qutoutiao'])

    if ((datetime.now().hour % 3).__eq__(1) and datetime.now().minute.__lt__(SCHEDULE_TIME)) or (
            (datetime.now().hour % 3).__eq__(2) and datetime.now().minute.__ge__(SCHEDULE_TIME)):
        checkin.qutoutiao(pid)
        # [x] 时段奖励
        time_reward()

        app.qutoutiao_benefit_page(pid, w, h)
        # [x] 开宝箱
        # 每个小时一次
        # 1, 4, 7, 10, 13, 16, 19, 22开上半时段
        # 2, 5, 8, 11, 14, 17, 20, 23开下半时段
        open_treasure()
        phone.stop_app(pid, info.packages['qutoutiao'])


def baidu(pid, w, h):
    # 时段奖励
    def time_reward():
        print('百度时段奖励 ' + datetime.now().time().__str__())
        # 1. 点击时段奖励
        input.tap(pid, (WIDTH - 0.9) * w / WIDTH, 0.9 * h / HEIGHT)
        # 2. 返回到程序主页
        phone.go_back(pid)

    if datetime.now().minute.__lt__(SCHEDULE_TIME) and (datetime.now().hour % 7).__eq__(0):
        checkin.baidu(pid)
        # [x] 时段奖励
        time_reward()
        phone.stop_app(pid, info.packages['baidu'])


# noinspection PyUnusedLocal
def weishi(pid, w, h):
    return None


# noinspection PyUnusedLocal
def ximalaya(pid, w, h):
    return None


# noinspection PyUnusedLocal
def wuba(pid, w, h):
    def time_reward():
        print('五八同城时段奖励 ' + datetime.now().time().__str__())
        # 点击右上角
        input.tap(pid, (WIDTH - 0.6) * w / WIDTH, 1.1 * h / HEIGHT)
        # 返回到程序主页
        phone.go_back(pid)

    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        if (datetime.now().hour % 4).__eq__(0):
            checkin.wuba(pid)
            # [x] 时段奖励
            time_reward()
            phone.stop_app(pid, info.packages['wuba'])


def taobao(pid, w, h):
    def everyday_coin():
        print('淘宝天天赚特币 ' + datetime.now().time().__str__())
        # 1. 点击天天赚特币
        input.tap(pid, w / 2, 2.6 * h / HEIGHT)
        # 2. 点击口袋
        input.tap(pid, w * 2 / 3, h / 2, gap=2)

    if datetime.now().minute < SCHEDULE_TIME:
        if datetime.now().hour % 5 == 0:
            checkin.taobao(pid)
            everyday_coin()
            phone.stop_app(pid, info.packages['taobao'])


# noinspection PyUnusedLocal
def shuabao(pid, w, h):
    def open_treasure():
        print('刷宝开宝箱 ' + datetime.now().time().__str__())
        # 1. 点击宝箱
        input.tap(pid, (WIDTH - 0.9) * w / WIDTH, 10.8 * h / HEIGHT, gap=3)
        # 2. 额外领取88元宝
        input.tap(pid, w / 2, 10.0 * h / HEIGHT)
        # 3. 播放30s
        time.sleep(30)
        # 4. 返回上级页面
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT, gap=2)

    if datetime.now().minute < SCHEDULE_TIME:
        if datetime.now().hour % 5 == 0:
            checkin.shuabao(pid)
            app.shuabao_benefit_page(pid, w, h)
            # [x] 开宝箱
            open_treasure()
            phone.stop_app(pid, info.packages['shuabao'])


def qqyuedu(pid, w, h):
    def open_treasure():
        print('QQ阅读开宝箱 ' + datetime.now().time().__str__())
        # 1. 点击宝箱
        input.tap(pid, (WIDTH - 1.0) * w / WIDTH, (HEIGHT - 2.4) * h / HEIGHT, gap=2)

    if (datetime.now().hour % 4) == 0:
        checkin.qqyuedu(pid)
        app.qqyuedu_benefit_page(pid, w, h)
        # [x] 开宝箱5次
        open_treasure()
        phone.stop_app(pid, info.packages['qqyuedu'])


# noinspection PyUnusedLocal
def chejia(pid, w, h):
    return None


def uc(pid, w, h):
    def collect_coin():
        print('UC浏览器收集金币 ' + datetime.now().time().__str__())
        # 1. 点击收集金币
        for i in range(0, 2):
            input.tap(pid, w / 2, 9.5 * h / HEIGHT, gap=8)
        # 2. 回到程序主页
        phone.go_back(pid, times=3, gap=1)

    def video_coin():
        print('UC浏览器看视频领元宝 ' + datetime.now().time().__str__())
        # 1. 点击看视频领元宝
        input.tap(pid, (WIDTH - 1.3) * w / WIDTH, (HEIGHT - 1.4) * h / HEIGHT, gap=10)
        # 2. 播放30s
        time.sleep(30)
        # 3. 返回到领取页面
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT, gap=3)
        # 4. 点击领取
        input.tap(pid, (WIDTH - 1.3) * w / WIDTH, 5.8 * h / HEIGHT, gap=2)

    if datetime.now().minute < SCHEDULE_TIME:
        if datetime.now().hour > 7:
            checkin.uc(pid)
            app.uc_benefit_page(pid, w, h, gap=5)
            # [x] 收集金币
            collect_coin()

            app.uc_benefit_page(pid, w, h)
            # [x] 看视频领元宝
            video_coin()
            phone.stop_app(pid, info.packages['uc'])


# noinspection PyUnusedLocal
def kuaikandian(pid, w, h):
    def time_reward():
        print('快看点时段奖励 ' + datetime.now().time().__str__())
        input.tap(pid, (WIDTH - 0.8) * w / WIDTH, 6.8 * h / HEIGHT, gap=2)

    if datetime.now().minute < SCHEDULE_TIME:
        if datetime.now().hour % 3 == 0:
            checkin.kuaikandian(pid)
            app.kuaikandian_benefit_page(pid, w, h)
            # [x] 快看点时段奖励
            time_reward()
            phone.stop_app(pid, info.packages['kuaikandian'])

    return None


# noinspection PyUnusedLocal
def hongshi(pid, w, h):
    return None


# noinspection PyUnusedLocal
def doudou(pid, w, h):
    def hour_benefit():
        print('豆豆小说整点福利 ' + datetime.now().time().__str__())
        checkin.doudou(pid)
        phone.stop_app(pid, info.packages['doudou'])

    if datetime.now().minute < SCHEDULE_TIME:
        # 12-14或者17-19点两次
        if datetime.now().hour == 13 or datetime.now().hour == 17:
            hour_benefit()


# noinspection PyUnusedLocal
def qimao(pid, w, h):
    return None


# noinspection PyUnusedLocal
def kankuai(pid, w, h):
    return None


# noinspection PyUnusedLocal
def douhuo(pid, w, h):
    return None


# noinspection PyUnusedLocal
def moji(pid, w, h):
    return None


def ersansi(pid, w, h):
    def time_reward():
        print('2345浏览器时段奖励 ' + datetime.now().time().__str__())
        phone.swipe_down_to_up(pid, w / 2, h)
        input.tap(pid, (WIDTH - 0.8) * w / WIDTH, 1.0 * h / HEIGHT, gap=2)
        phone.go_back(pid)

    if datetime.now().minute < SCHEDULE_TIME:
        checkin.ersansi(pid)
        # [x] 时段奖励
        time_reward()

        # [x] 阅读文章
        app.read_ersansi_article(pid, w, h, num=1)
        phone.stop_app(pid, info.packages['ersansi'])


# noinspection PyUnusedLocal
def tangdou(pid, w, h):
    return None


# noinspection PyUnusedLocal
def yangcong(pid, w, h):
    return None


# 49-72
# noinspection PyUnusedLocal
def weixin(pid, w, h):
    return None


# noinspection PyUnusedLocal
def sougou(pid, w, h):
    return None


# noinspection PyUnusedLocal
def zhuanshi(pid, w, h):
    def time_reward():
        # 1. 点击领取
        input.tap(pid, 1.1 * (w - randrange(-50, 50)) / WIDTH, 1.1 * h / HEIGHT, gap=3)

    if datetime.now().minute < SCHEDULE_TIME:
        if datetime.now().hour % 8 == 0:
            checkin.zhuanshi(pid)
            # [x] 时段奖励
            time_reward()
            phone.stop_app(pid, info.packages['zhuanshi'])


# noinspection PyUnusedLocal
def qizhu(pid, w, h):
    return None
