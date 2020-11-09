import time
from datetime import datetime

from src import checkin, phone, input, app, utils
from src.info import packages, WIDTH, HEIGHT, SCHEDULE_TIME, contexts


def toutiao_open_treasure(pid, w, h, gap=15):
    """
    今日头条开宝箱
    """
    # 1. 点击宝箱
    input.tap(pid, (WIDTH - 1.2) * w / WIDTH, (HEIGHT - 1.7) * h / HEIGHT)  # <== modify
    # 2. 点击看视频再领金币
    input.tap(pid, w / 2, 9.4 * h / HEIGHT)  # <== modify
    # 3. 播放15s
    time.sleep(gap)
    # 4. 返回到任务页面
    phone.go_back(pid)


def toutiao(pid, w, h):
    # 吃饭补贴
    def meal_allowance():
        # 1. 获取吃饭补贴的位置
        eat_location = utils.current_words_location(pid, '饭')
        if eat_location is None:
            print('没有获取到吃饭补贴的位置')
            return
        width = eat_location['x'] + eat_location['w']
        height = eat_location['y'] + eat_location['h']
        input.tap(pid, width, height)

        # 2. 领取补贴
        input.tap(pid, w / 2, (HEIGHT - 1.3) * h / HEIGHT, gap=3)  # <= modify
        # 3. 返回到福利页面
        phone.go_back(pid)

    # 睡觉赚钱
    def sleep_money(is_sleep):
        # 1. 获取睡觉赚钱的位置
        sleep_location = utils.current_words_location(pid, '睡觉')
        if sleep_location is None:
            print('没有获取到睡觉赚钱的位置')
            return
        width = sleep_location['x'] + sleep_location['w']
        height = sleep_location['y'] + sleep_location['h']
        input.tap(pid, width, height)

        # 2. 点击我要睡了/我睡醒了
        for i in range(0, 2 if is_sleep else 1):
            input.tap(pid, w / 2, (HEIGHT - 1.0) * h / HEIGHT, gap=8)  # <= modify
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
            sleep_money(False)
        elif hour.__eq__(8):
            sleep_money(True)

    # [x] 开宝箱
    # 每10分钟一次
    toutiao_open_treasure(pid, w, h)

    # 关闭头条
    phone.stop_app(pid, packages['toutiao'])


def kuaishou(pid, w, h):
    # 开宝箱
    # 时间跨度依次递增
    # 每天有次数限制
    def open_treasure():
        # 1. 点击开宝箱得金币
        input.tap(pid, 5.7 * w / WIDTH, (HEIGHT - 3.1) * h / HEIGHT)  # <== modify
        # 2. 返回到播放视频的页面
        phone.go_back(pid)

    # [x] 看直播领金币
    def watch_live():
        # 1. 向上滑动页面打开看直播领金币
        phone.swipe_down_to_up(pid, w, h, gap=3, internal=200)
        # 2. 点击看直播按钮
        live_location = utils.current_words_location(pid, '看直播领金币')
        if live_location is None:
            print('没有获取到看直播领金币的位置')
            return
        height = live_location['y'] + live_location['h']
        input.tap(pid, (WIDTH - 1.0) * w / WIDTH, height)

        for i in range(0, 10):
            # 3. 观看30s
            time.sleep(30)
            # 4. 上滑出现下一个
            phone.swipe_down_to_up(pid, w, h / 2, internal=100, gap=5)

        # 5. 返回到福利页面
        phone.go_back(pid, gap=2)
        # 6. 福利页面恢复原样
        phone.swipe_up_to_down(pid, w, h, gap=1, internal=100)

    # 每隔一个小时开一次宝箱
    if datetime.now().minute.__lt__(SCHEDULE_TIME) and (datetime.now().hour % 2).__eq__(0):
        checkin.kuaishou(pid)
        app.kuaishou_benefit_page(pid, w, h)

        if datetime.now().hour.__eq__(20):
            # [x] 看直播领金币
            # 20:00-24:00
            watch_live()

        # [x] 开宝箱
        open_treasure()

        phone.stop_app(pid, packages['kuaishou'])


# 开宝箱得金币
def douyin_open_treasure(pid, w, h):
    # 1. 点击开宝箱得金币
    input.tap(pid, (WIDTH - 1.1) * w / WIDTH, (HEIGHT - 1.1) * h / HEIGHT)  # <== modify
    # 2. 点击看广告视频再赚金币
    input.tap(pid, w / 2, 8.4 * h / HEIGHT)  # <== modify
    # 3. 播放30s
    time.sleep(30)
    # 4. 返回到播放页面
    # 存在超过30s的广告需要返回三次
    # 利用播放页面需要快速两次才能退出
    phone.go_back(pid, times=3, gap=3)


def douyin(pid, w, h):
    # 限时任务赚金币
    def limit_duty():
        print('抖音限时任务赚金币 ' + datetime.now().__str__())
        # 1. 获取限时任务的位置
        if '抖音限时' not in contexts[pid]:
            limit_location = utils.current_words_location(pid, '限时')
            if limit_location is None:
                print('没有获取到限时任务的位置')
                return
            height = limit_location['y'] + limit_location['h']
            contexts[pid]['抖音限时'] = height
        input.tap(pid, w / 3, contexts[pid]['抖音限时'])

        # 2. 播放30s
        time.sleep(30)
        # 3. 返回福利页面
        phone.go_back(pid)

    # 睡觉赚钱
    def sleep_money(is_sleep):
        # 1. 下滑到最下面
        phone.swipe_down_to_up(pid, w, h, internal=100)
        # 2. 点击睡觉赚金币
        # 可能点到中间某个部位导致无效
        input.tap(pid, w / 3, 3.6 * h / HEIGHT)  # <==== modify
        # 3. 点击我要睡了/我睡醒了
        for i in range(0, 2 if is_sleep else 1):
            input.tap(pid, w / 2, (HEIGHT - 1.0) * h / HEIGHT, gap=8)
        # 4. 返回到福利页面
        phone.go_back(pid)
        # 5. 滑到最上面
        phone.swipe_up_to_down(pid, w, h, internal=100)

    # 吃饭补贴
    def meal_allowance():
        # 1. 下滑任务页面到最下面
        phone.swipe_down_to_up(pid, w, h, gap=5)

        eat_location = utils.current_words_location(pid, '饭')
        if eat_location is None:
            print('没有获取到吃饭补贴的位置')
            return
        height = eat_location['y'] + eat_location['h']

        # 2. 点击吃饭补贴
        input.tap(pid, w / 3, height)
        # 3. 领取补贴
        input.tap(pid, w / 2, (HEIGHT - 1.3) * h / HEIGHT)  # <= modify
        # 4. 看视频再领金币
        input.tap(pid, w / 2, 9.0 * h / HEIGHT)
        # 5. 播放30s
        time.sleep(30)
        # 6. 返回到福利页面
        phone.go_back(pid, times=2, gap=1)
        # 7. 滑到最上面
        phone.swipe_up_to_down(pid, w, h, internal=100)

    # 游戏抽奖
    def game_lottery():
        # 1. 点击游戏中心
        input.tap(pid, (WIDTH - 1.0) * w / WIDTH, 5.5 * h / HEIGHT)
        # 2. 点击右下角抽奖
        input.tap(pid, (WIDTH - 0.9) * w / WIDTH, (HEIGHT - 1.2) * h / HEIGHT)
        # 3. 点击开始抽奖
        input.tap(pid, w / 2, 10.8 * h / HEIGHT, 8)
        # 4. 返回到福利页面
        phone.go_back(pid, 2)

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

        # [x] 抽奖两次
        if hour.__eq__(14) or hour.__eq__(15):
            game_lottery()

    # [x] 开宝箱得金币
    # 每20分钟一次
    douyin_open_treasure(pid, w, h)

    app.douyin_benefit_page(pid, w, h)
    # [x] 限时任务赚金币
    # 每20分钟一次
    limit_duty()

    # 关闭抖音
    phone.stop_app(pid, packages['douyin'])


# 火山开宝箱
def huoshan_open_treasure(pid, w, h):
    # 1. 点击开宝箱得金币
    input.tap(pid, (WIDTH - 1.0) * w / WIDTH, (HEIGHT - 2.1) * h / HEIGHT)  # <= modify
    # 2. 点击看视频金币翻倍按钮
    input.tap(pid, w / 2, 9.4 * h / HEIGHT)  # <= modify
    # 3. 播放30s
    time.sleep(30)
    # 4. 返回到福利页面
    phone.go_back(pid, gap=2)


def huoshan(pid, w, h):
    def benefit_page():
        # 1. 点击红包
        input.tap(pid, 4.3 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)  # <= modify

    # 看视频赚海量金币
    def video_money():
        # 1. 点击看视频赚海量金币
        input.tap(pid, w / 2, 7.5 * h / HEIGHT)
        # 2. 播放30s
        time.sleep(30)
        # 3. 返回到福利页面
        phone.go_back(pid)

    # # 晒收入
    # def show_income():
    #     # 1. 点击晒收入
    #     input.tap(pid, w / 2, (HEIGHT - 3.3) * h / HEIGHT)
    #     # 2. 点击微信
    #     input.tap(pid, w / 2, 8.3 * h / HEIGHT)
    #     for i in range(0, 3):
    #         # 3. 点击去粘贴
    #         # 进入微信页面
    #         input.tap(pid, w / 2, 9.2 * h / HEIGHT, 8)
    #         # 4. 返回到火山微信悬浮窗
    #         phone.go_back(pid)
    #         # 5. 返回到福利页面
    #         phone.go_back(pid)

    # 睡觉赚金币
    def sleep_money(is_sleep):
        print('火山睡觉赚钱 ' + datetime.now().__str__())
        # 1. 点击睡觉赚金币
        input.tap(pid, w / 2, 8.3 * h / HEIGHT)  # <=== modify
        # 2. 点击我要睡了/我睡醒了
        for i in range(0, 2 if is_sleep else 1):
            input.tap(pid, w / 2, (HEIGHT - 1.0) * h / HEIGHT, 8)  # <= modify
        # 3. 返回到回到福利页面
        phone.go_back(pid)

    # 打开火山
    checkin.huoshan(pid)
    benefit_page()

    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        # if datetime.now().hour.__eq__(1):
        #     # [x] 晒收入
        #     # 因为会打乱顺序
        #     # 所以应该早于看视频
        #     # 晚于签到
        #     show_income()

        # [x] 睡觉赚金币
        # 20点睡觉3点起床收金币
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
    huoshan_open_treasure(pid, w, h)

    # 关闭火山
    phone.stop_app(pid, packages['huoshan'])


# noinspection PyUnusedLocal
def jingdong(pid, w, h):
    return None


# 番茄开宝箱
def fanqie_open_treasure(pid, w, h):
    # 1. 点击开宝箱得金币
    input.tap(pid, (WIDTH - 1.0) * w / WIDTH, (HEIGHT - 2.3) * h / HEIGHT)  # <= modify
    # 2. 点击看视频再领金币
    input.tap(pid, w / 2, 8.7 * h / HEIGHT)
    # 3. 播放30s
    time.sleep(30)
    # 4. 返回到福利页面
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT, gap=2)  # <= modify


def fanqie(pid, w, h):
    # 分享好书给好友
    def book_share():
        # 1. 点击任意一本书
        input.tap(pid, w / 2, h / 3)
        # 2. 点击分享
        input.tap(pid, (WIDTH - 0.6) * w / WIDTH, 0.9 * h / HEIGHT)
        # 3. 点击微信
        input.tap(pid, 1.0 * w / WIDTH, 9.5 * h / HEIGHT)
        # 4. 返回到程序主页
        phone.go_back(pid, gap=2)

    # 加入书架
    # 可能存在重复加入
    def add_bookshelf():
        # 1. 点击任意一本书
        input.tap(pid, w / 2, h * 2 / 3)
        # 2. 点击加入书架图标
        input.tap(pid, 4.6 * w / WIDTH, 1.2 * h / HEIGHT)
        # 3. 返回到程序主页
        phone.go_back(pid, gap=2)

    # 打开番茄
    checkin.fanqie(pid, w, h)

    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        if datetime.now().hour.__eq__(3):
            # [x] 分享好书给好友
            book_share()
        elif datetime.now().hour.__eq__(4):
            # [x] 加入书架
            add_bookshelf()

    app.fanqie_benefit_page(pid, w, h)

    # [x] 开宝箱
    # 每20分钟一次开宝箱任务
    fanqie_open_treasure(pid, w, h)

    # 关闭番茄
    phone.stop_app(pid, packages['fanqie'])


# 番茄畅听开宝箱
def fanchang_open_treasure(pid, w, h):
    # 1. 点击开宝箱得金币
    input.tap(pid, (WIDTH - 1.0) * w / WIDTH, (HEIGHT - 2.1) * h / HEIGHT)  # <= modify
    # 2. 点击看视频再领金币
    input.tap(pid, w / 2, 9.9 * h / HEIGHT)  # <= modify
    # 3. 播放30s
    time.sleep(30)
    # 4. 返回到福利页面
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT, gap=2)  # <== modify


def fanchang(pid, w, h):
    # 完整的开宝箱流程
    def full_fanchang_open_treasure():
        checkin.fanchang(pid, w, h)
        app.fanchang_benefit_page(pid, w, h)
        fanchang_open_treasure(pid, w, h)
        phone.stop_app(pid, packages['fanchang'])

    # # 收听音频
    # def listen_sound():
    #     # 1. 点击中间下方的播放界面
    #     input.tap(pid, w / 2, (HEIGHT - 0.6) * h / HEIGHT)

    # def collect_listen_coin():
    #     # 1. 点击中间下方的播放界面
    #     listen_sound()
    #     # 2. 点击立即领取
    #     input.tap(pid, (WIDTH - 1.0) * w / WIDTH, 10.0 * h / HEIGHT)
    #     for i in range(0, 9):
    #         # 3. 点击领红包
    #         input.tap(pid, w / 2, (HEIGHT - 0.9) * h / HEIGHT)
    #         # 4. 点击看视频再领金币
    #         input.tap(pid, w / 2, 8.3 * h / HEIGHT)
    #         # 5. 播放30s
    #         time.sleep(30)
    #         # 返回到领取界面
    #         input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)

    # # [x] 听番畅音频
    # # 08:00-09:00-10:00-11:00-12:00
    # if datetime.now().minute.__lt__(SCHEDULE_TIME):
    #     if datetime.now().hour.__eq__(8):
    #         checkin.fanchang(pid, w, h)
    #         # [x] 收听番唱音频
    #         listen_sound()
    #         # 回退到程序主页
    #         phone.go_back(pid)
    #         # 后台播放
    #         phone.go_home(pid)
    #     elif datetime.now().hour.__eq__(9):
    #         # 解锁广告
    #         # 1. 进入番畅音频
    #         checkin.fanchang(pid, w, h)
    #         listen_sound()
    #         # 2. 点击看小视频免费听
    #         input.tap(pid, 4.7 * w / WIDTH, 0.9 * h / HEIGHT)
    #         # 3. 播放45s
    #         time.sleep(45)
    #         # 4. 点击关闭
    #         # 播放页面
    #         input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)
    #         # 5. 回退到主页
    #         phone.go_back(pid)
    #         # ６．后台播放
    #         phone.go_home(pid)
    #     elif datetime.now().hour.__eq__(12):
    #         checkin.fanchang(pid, w, h)
    #         collect_listen_coin()
    #         phone.stop_app(pid, packages['fanchang'])

    # [x] 开宝箱
    # 每个小时一次
    # 1, 4, 7, 10, 13, 16, 19, 22开上半时段
    # 2, 5, 8, 11, 14, 17, 20, 23开下半时段
    if (datetime.now().hour % 3).__eq__(1) and datetime.now().minute.__lt__(SCHEDULE_TIME):
        full_fanchang_open_treasure()
    elif (datetime.now().hour % 3).__eq__(2) and datetime.now().minute.__ge__(SCHEDULE_TIME):
        full_fanchang_open_treasure()


# # noinspection PyUnusedLocal
# def weishi(pid, w, h):
#     return None

def kuchang(pid, w, h):
    # 看创意视频
    def kuchang_creative_video():
        print('酷狗唱唱看创意视频 ' + datetime.now().__str__())
        # 1. 获取创意视频的位置
        if '酷狗唱唱创意' not in contexts[pid]:
            creative_location = utils.current_words_location(pid, '创意')
            if creative_location is None:
                print('没有获取到创意视频的位置')
                return
            height = creative_location['y'] + creative_location['h']
            contexts[pid]['酷狗唱唱创意'] = height
        input.tap(pid, (WIDTH - 1.2) * w / WIDTH, contexts[pid]['酷狗唱唱创意'], gap=10)

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
        phone.stop_app(pid, packages['kuchang'])


def shuqi(pid, w, h):
    def shuqi_invent_friend():
        print("邀请书友 " + datetime.now().__str__())
        # 1. 下滑到最下
        phone.swipe_down_to_up(pid, w, h, gap=2, internal=100)
        # 2. 点击邀请书友
        input.tap(pid, w / 2, 9.5 * h / HEIGHT, gap=3)
        # 3. 点击微信好友
        input.tap(pid, 1.2 * w / WIDTH, (HEIGHT - 2.8) * h / HEIGHT, gap=3)
        # 4. 回退到福利页面
        phone.go_back(pid, gap=1)
        # 5. 恢复原貌
        phone.swipe_up_to_down(pid, w, h, gap=1, internal=100)

    if datetime.now().hour.__eq__(8):
        checkin.shuqi(pid, w, h)
        app.shuqi_benefit_page(pid, w, h)
        # [x] 邀请书友
        # 20s赚0.01元
        shuqi_invent_friend()
        phone.stop_app(pid, packages['shuqi'])


def yingke(pid, w, h):
    # 看福利视频
    def benefit_video():
        print('映客福利视频 ' + datetime.now().__str__())
        # 1. 点击领金币
        input.tap(pid, (WIDTH - 1.2) * w / WIDTH, 4.7 * h / HEIGHT)  # <== modify
        # 2. 播放45s
        # 播放时间不同
        time.sleep(45)

    # 开宝箱
    def open_treasure():
        print('映客开宝箱 ' + datetime.now().__str__())
        # 1. 点击开宝箱领金币
        input.tap(pid, (WIDTH - 1.1) * w / WIDTH, (HEIGHT - 2.5) * h / HEIGHT)  # <== modify
        # 2. 播放视频45s
        # 播放时间不同
        time.sleep(45)

    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        # 小米手机无法解决振动问题
        if datetime.now().hour.__gt__(9) and datetime.now().hour.__le__(20):
            checkin.yingke(pid, w, h)
            app.yingke_benefit_page(pid, w, h)
            # [x] 看福利视频
            # 10次
            benefit_video()
            phone.stop_app(pid, packages['yingke'])

            checkin.yingke(pid, w, h)
            app.yingke_benefit_page(pid, w, h)
            # [x] 开宝箱
            # 10次
            open_treasure()
            phone.stop_app(pid, packages['yingke'])


def kugou(pid, w, h):
    # 刷创意视频
    def creative_video():
        # 1. 点击去赚钱
        # 获取创意视频的位置
        if '酷狗创意视频' not in contexts[pid]:
            video_location = utils.current_words_location(pid, '创')
            if video_location is None:
                print('没有获取到创意视频的位置')
                return
            height = video_location['y'] + video_location['h']
            contexts[pid]['酷狗创意视频'] = height
        input.tap(pid, (WIDTH - 1.0) * w / WIDTH, contexts[pid]['酷狗创意视频'], gap=8)

        # 2. 播放30s
        time.sleep(30)
        # 3. 点击返回到福利页面
        # 再次回退消除奖励页面
        phone.go_back(pid, times=2, gap=1)

    # 分享歌曲或者视频
    def share_friend(is_song):
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
        phone.go_back(pid)

    if datetime.now().minute.__lt__(SCHEDULE_TIME) and datetime.now().hour.__gt__(3):
        # 进入程序
        checkin.kugou(pid, w, h)
        app.kugou_benefit_page(pid, w, h)

        # [x] 刷创意视频
        # 总共20次定时任务
        creative_video()

        if datetime.now().hour.__eq__(4):
            # [x] 分享歌曲
            # 每天1次
            share_friend(True)
        elif datetime.now().hour.__eq__(5):
            # [x] 分享视频
            # 每天1次
            share_friend(False)

        # 关闭程序
        phone.stop_app(pid, packages['kugou'])


def huitoutiao(pid, w, h):
    # 平台检测到作弊工具
    return None

    # # 时段奖励
    # def time_reward():
    #     # 1. 点击领取
    #     # 有时候没有广告视频
    #     input.tap(pid, (WIDTH - 1.3) * w / WIDTH, 1.0 * h / HEIGHT, 2)
    #
    # if ((datetime.now().hour % 3).__eq__(1) and datetime.now().minute.__lt__(SCHEDULE_TIME)) or (
    #         (datetime.now().hour % 3).__eq__(2) and datetime.now().minute.__ge__(SCHEDULE_TIME)):
    #     checkin.huitoutiao(pid)
    #     # [x] 阅读惠头条文章
    #     app.read_huitoutiao_article(pid, w, h, num=1)
    #
    #     # [x] 时段奖励
    #     # 每个小时一次
    #     # 1, 4, 7, 10, 13, 16, 19, 22开上半时段
    #     # 2, 5, 8, 11, 14, 17, 20, 23开下半时段
    #     time_reward()
    #
    #     phone.stop_app(pid, packages['huitoutiao'])


def zhongqing(pid, w, h):
    # 时段奖励
    def time_reward():
        # 1. 点击领取
        # 有时候没有广告视频
        input.tap(pid, (WIDTH - 0.9) * w / WIDTH, 1.0 * h / HEIGHT, gap=8)

    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        checkin.zhongqing(pid, w, h)
        # [x] 时段奖励
        time_reward()

        # 消除奖励提醒
        phone.go_back(pid, gap=2)
        # [x] 阅读文章
        app.read_zhongqing_article(pid, w, h, num=1)

        # [x] 看中青看点视频
        app.watch_zhongqing_video(pid, w, h, num=1)
        phone.stop_app(pid, packages['zhongqing'])

        if (datetime.now().hour % 4).__eq__(0):
            checkin.weixin(pid)
            # [x] 阅读微信文章
            app.zhongqing_weixin_article(pid, w, h, num=5)
            phone.stop_app(pid, packages['weixin'])


def pinduoduo(pid, w, h):
    # 定时红包
    def timed_envelope():
        # 1. 点击现金签到
        input.tap(pid, w / 2, 5.4 * h / HEIGHT)  # <= modify
        # 2. 点击定时红包
        input.tap(pid, 0.8 * w / WIDTH, 5.0 * h / HEIGHT)  # <= modify
        # 3. 点击开
        input.tap(pid, w / 2, 10.0 * h / HEIGHT)  # <= modify
        # 4. 点击限时福利
        # 提示获取签到金成功
        input.tap(pid, 5.5 * w / WIDTH, 6.0 * h / HEIGHT)

    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        if (datetime.now().hour % 5).__eq__(0):
            checkin.pinduoduo(pid, w, h)
            timed_envelope()
            phone.stop_app(pid, 'pinduoduo')


def kuaiyin(pid, w, h):
    def drink_water(is_next):
        print('快音喝水赚钱 ' + datetime.now().__str__())
        # 1. 点击喝水赚钱
        input.tap(pid, 2.6 * w / WIDTH, 4.5 * h / HEIGHT)
        # 2. 点击水杯
        for i in range(0, 4):
            input.tap(pid, (1.2 + i * 1.5) * w / WIDTH, (5.2 if is_next else 3.5) * h / HEIGHT, gap=1)
        # 3. 看视频
        input.tap(pid, w / 2, 9.3 * h / HEIGHT, gap=10)
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
        input.tap(pid, w / 2, 8.0 * h / HEIGHT, gap=10)
        # 2. 播放30s
        time.sleep(30)

    def open_treasure():
        print('快音开宝箱 ' + datetime.now().__str__())
        # 1. 点击宝箱
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 11.5 * h / HEIGHT)
        # 2. 点击看视频再领金币
        input.tap(pid, w / 2, 7.8 * h / HEIGHT, gap=10)
        # 3. 播放30s
        time.sleep(30)

    def sleep_money(is_sleep):
        print('快音睡觉赚钱 ' + datetime.now().__str__())
        # 1. 点击睡觉赚钱
        input.tap(pid, 4.1 * w / WIDTH, 4.4 * h / HEIGHT)
        # 3. 点击我要睡觉/我睡醒了
        for i in range(0, 2 if is_sleep else 1):
            input.tap(pid, w / 2, (HEIGHT - 1.2) * h / HEIGHT, gap=8)

    if datetime.now().minute.__lt__(SCHEDULE_TIME):

        checkin.kuaiyin(pid, w, h)
        app.kuaiyin_benefit_page(pid, w, h)
        # [x] 离线收益
        offline_coin()
        phone.stop_app(pid, packages['kuaiyin'])

        checkin.kuaiyin(pid, w, h)
        app.kuaiyin_benefit_page(pid, w, h)
        # [x] 开宝箱
        open_treasure()
        phone.stop_app(pid, packages['kuaiyin'])

        hour = datetime.now().hour
        if hour.__eq__(6) or hour.__eq__(9) or hour.__eq__(11) or (hour.__gt__(12) and hour.__lt__(18)):
            checkin.kuaiyin(pid, w, h)
            app.kuaiyin_benefit_page(pid, w, h)
            # [x] 八次喝水
            drink_water(False if hour.__lt__(14) else True)
            phone.stop_app(pid, packages['kuaiyin'])

        # [x] 睡觉赚钱
        # 21:00-2:00为睡觉时间
        # 06:00-09:00为醒来时间
        if hour.__eq__(21):
            sleep_money(False)
        elif hour.__eq__(6):
            sleep_money(True)

        if (datetime.now().hour % 3).__eq__(0):
            checkin.kuaiyin(pid, w, h)
            app.kuaiyin_benefit_page(pid, w, h)
            # [x] 看视频赚钱
            advert_video()
            phone.stop_app(pid, packages['kuaiyin'])


# noinspection PyUnusedLocal
def tangdou(pid, w, h):
    return None


def dongfang(pid, w, h):
    # 时段奖励
    def time_reward():
        # 1. 点击领取奖励
        input.tap(pid, (WIDTH - 0.8) * w / WIDTH, 1.0 * h / HEIGHT, gap=3)
        # 2. 消除奖励页面
        phone.go_back(pid)

    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        checkin.dongfang(pid, w, h)
        # [x] 时段奖励
        time_reward()

        # [x] 阅读文章
        app.read_dongfang_article(pid, w, h, num=1)

        phone.stop_app(pid, packages['dongfang'])


def jukandian(pid, w, h):
    # 时段奖励
    def time_reward():
        input.tap(pid, 0.8 * w / WIDTH, 0.9 * h / HEIGHT)
        phone.go_back(pid, gap=1)

    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        checkin.jukandian(pid, w, h)
        # [x] 时段奖励
        time_reward()

        # [x] 阅读文章
        app.read_jukandian_article(pid, w, h, num=1)

        phone.stop_app(pid, packages['jukandian'])


# noinspection PyUnusedLocal
def kankuai(pid, w, h):
    return None


# def taobao(pid, w, h):
#     # [x] 天天赚特币
#     if datetime.now().minute.__lt__(SCHEDULE_TIME) and (datetime.now().hour % 4).__eq__(0):
#         # 1. 打开淘宝
#         checkin.taobao(pid)
#         # 2. 点击天天赚特币
#         input.tap(pid, w / 2, 2.4 * h / HEIGHT, gap=10)  # <= modify
#         # 3. 收取特币
#         input.tap(pid, 4.3 * w / WIDTH, 6.9 * h / HEIGHT)  # <= modify
#         # 4. 关闭淘宝
#         phone.stop_app(pid, packages['taobao'])
#
#
# def shuabao(pid, w, h):
#     # 看福利视频
#     def benefit_video():
#         # 1. 点击去观看
#         # 等待关闭按钮弹出
#         input.tap(pid, (WIDTH - 1.0) * w / WIDTH, (HEIGHT - 1.6) * h / HEIGHT, gap=10)  # <== modify
#         # 2. 播放30s
#         time.sleep(30)
#         # 3. 点击关闭
#         input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)
#
#     if datetime.now().minute < SCHEDULE_TIME and datetime.now().hour.__gt__(13):
#         # 打开刷宝
#         checkin.shuabao(pid)
#         app.shuabao_benefit_page(pid, w, h)
#         # [x] 看福利视频
#         # 10次
#         benefit_video()
#         # 关闭刷宝
#         phone.stop_app(pid, packages['shuabao'])
#
#
# def qutoutiao(pid, w, h):
#     # 看广告视频拿金币
#     def video_coin():
#         # 1. 点击看广告视频拿金币
#         input.tap(pid, w / 2, (HEIGHT - 1.2) * h / HEIGHT)  # <=== modify
#         # 2. 播放50s
#         time.sleep(50)
#         # 3. 回退到播放页面
#         phone.go_back(pid, times=2, gap=1)
#

#
#     # 睡觉赚钱
#     def sleep_money(is_sleep):
#         # 1. 点击睡觉赚金币
#         input.tap(pid, w / 2, (HEIGHT - 1.7) * h / HEIGHT)  # <=== modify
#         # 2. 点击我要睡了/我睡醒了
#         for i in range(0, 2 if is_sleep else 1):
#             input.tap(pid, w / 2, (HEIGHT - 1.0) * h / HEIGHT, gap=8)  # <= modify
#         # 3. 返回到福利页面
#         phone.go_back(pid)
#
#     # 时段奖励
#     def time_reward():
#         # 1. 点击左下角头条
#         # 有时弹出广告悬浮窗
#         input.tap(pid, 0.6 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)
#         # 2. 点击领取
#         input.tap(pid, (WIDTH - 0.6) * w / WIDTH, 1.0 * h / HEIGHT)
#         # 有时弹出广告悬浮窗
#
#     if datetime.now().minute.__lt__(SCHEDULE_TIME):
#         checkin.qutoutiao(pid)
#         app.qutoutiao_benefit_page(pid, w, h)
#
#         # [x] 睡觉赚金币
#         # 20:00-08:00为睡觉时间
#         # 12:00-14:00为午休时间
#         if datetime.now().hour.__eq__(20):
#             sleep_money(False)
#         elif datetime.now().hour.__eq__(9):
#             sleep_money(True)
#         elif datetime.now().hour.__eq__(12):
#             sleep_money(False)
#         elif datetime.now().hour.__eq__(15):
#             sleep_money(True)
#
#         # [x] 时段奖励
#         # 阶梯式时间分布
#         time_reward()
#
#         phone.stop_app(pid, packages['qutoutiao'])
#
#
#     if datetime.now().hour.__gt__(2) and datetime.now().hour.__lt__(9):
#         # 进入趣头条
#         checkin.qutoutiao(pid)
#         app.qutoutiao_benefit_page(pid, w, h)
#         # [x] 看广告视频拿金币
#         # 每天可以看6次
#         video_coin()
#         phone.stop_app(pid, packages['qutoutiao'])
#
#
#
#
# def ximalaya(pid, w, h):
#     def listen_sound():
#         # 1. 点击收听
#         input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)
#         # 2. 点击收金币
#         # 在收金币界面
#         input.tap(pid, 3.8 * w / WIDTH, 1.0 * h / HEIGHT)
#
#     def collect_coin():
#         # 1. 点击取金币
#         input.tap(pid, 0.7 * w / WIDTH, 3.5 * h / HEIGHT)
#         # 2. 看视频超级翻倍
#         input.tap(pid, w / 2, 8.9 * h / HEIGHT)
#         # 3. 播放30s
#         time.sleep(30)
#         # 4. 返回到播放收金币页面
#         # 第1次退出广告页面
#         # 第2次退出翻倍成功页面
#         phone.go_back(pid, times=2)
#
#     if datetime.now().minute.__lt__(SCHEDULE_TIME):
#         if datetime.now().hour.__eq__(12):
#             checkin.ximalaya(pid)
#             # [x] 收听喜马拉雅
#             listen_sound()
#             phone.go_home(pid)
#         elif datetime.now().hour.__gt__(12) and datetime.now().hour.__lt__(16):
#             checkin.ximalaya(pid)
#             collect_coin()
#             if datetime.now().hour.__eq__(15):
#                 # 关闭喜马拉雅
#                 phone.stop_app(pid, 'ximalaya')

# noinspection PyUnusedLocal
def douhuo(pid, w, h):
    return None


def kuge(pid, w, h):
    def share_song():
        # 1. 点击进入全屏播放页面
        input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)
        # 2. 点击右上角分享
        input.tap(pid, (WIDTH - 0.6) * w / WIDTH, 0.9 * h / HEIGHT)
        # 3. 点击微信
        input.tap(pid, w / 6, h * 6 / 7)
        # 4. 返回
        phone.go_back(pid, gap=1)

    if datetime.now().minute.__gt__(SCHEDULE_TIME) and datetime.now().hour.__eq__(22):
        checkin.kuge(pid, w, h)
        # [x] 分享歌曲
        share_song()
        # 随便关闭酷狗儿歌后台播放
        phone.stop_app(pid, packages['kuge'])


def makan(pid, w, h):
    def time_reward():
        # 1. 点击领取
        input.tap(pid, 0.8 * w / WIDTH, 1.0 * h / HEIGHT, gap=2)

    def get_coin():
        # 1. 点击点我领金币
        input.tap(pid, (WIDTH - 1.1) * w / WIDTH, 10.7 * h / HEIGHT)
        # 2. 点击免费领金币
        input.tap(pid, (WIDTH - 1.1) * w / WIDTH, 9.3 * h / HEIGHT)
        # 3. 返回到首页
        phone.go_back(pid, times=2)

    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        checkin.makan(pid, w, h)
        # 消除悬浮窗
        phone.go_back(pid)
        app.makan_benefit_page(pid, w, h)
        # [x] 领金币
        get_coin()

        # [x] 时段奖励
        time_reward()
        phone.stop_app(pid, packages['makan'])

        if datetime.now().hour.__eq__(20) or datetime.now().hour.__eq__(21):
            checkin.makan(pid, w, h)
            phone.go_back(pid, gap=2)
            # [x] 阅读蚂蚁看点文章
            app.read_makan_article(pid, w, h, num=1)
            # 解决彩蛋问题
            input.tap(pid, 1.0 * w / WIDTH, 2.3 * h / HEIGHT, gap=2)
            phone.stop_app(pid, packages['makan'])


def diandian(pid, w, h):
    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        checkin.diandian(pid, w, h)
        # [x] 阅读点点文章
        app.read_diandian_article(pid, w, h, num=1)
        phone.stop_app(pid, packages['diandian'])


# noinspection PyUnusedLocal
def moji(pid, w, h):
    return None


def qutoutiao(pid, w, h):
    # 开宝箱
    def open_treasure():
        # 1. 点击宝箱
        input.tap(pid, (WIDTH - 1.0) * w / WIDTH, (HEIGHT - 1.6) * h / HEIGHT)
        # 2. 播放广告50s
        time.sleep(50)
        # 3. 回退到播放页面
        phone.go_back(pid, times=2, gap=1)

    if ((datetime.now().hour % 3).__eq__(1) and datetime.now().minute.__lt__(SCHEDULE_TIME)) or (
            (datetime.now().hour % 3).__eq__(2) and datetime.now().minute.__ge__(SCHEDULE_TIME)):
        checkin.qutoutiao(pid)
        app.qutoutiao_benefit_page(pid, w, h)
        # [x] 开宝箱
        # 每个小时一次
        # 1, 4, 7, 10, 13, 16, 19, 22开上半时段
        # 2, 5, 8, 11, 14, 17, 20, 23开下半时段
        open_treasure()
        phone.stop_app(pid, packages['qutoutiao'])


# noinspection PyUnusedLocal
def baidu(pid, w, h):
    # 时段奖励
    def time_reward():
        # 1. 点击时段奖励
        input.tap(pid, (WIDTH - 0.9) * w / WIDTH, 0.9 * h / HEIGHT)
        # 2. 返回到程序主页
        phone.go_back(pid)

    if datetime.now().minute.__lt__(SCHEDULE_TIME) and (datetime.now().hour % 2).__eq__(0):
        checkin.baidu(pid)
        # [x] 时段奖励
        time_reward()
        phone.stop_app(pid, packages['baidu'])


# noinspection PyUnusedLocal
def weishi(pid, w, h):
    return None
