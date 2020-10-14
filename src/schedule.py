import time
from datetime import datetime

from src import checkin, phone, input
from src.info import packages, WIDTH, HEIGHT, SCHEDULE_TIME


def toutiao(pid, w, h):
    # 进入福利页面
    def benefit_page():
        input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)  # <= modify

    # [x] 开宝箱
    # 每10分钟一次
    def open_treasure():
        # 1. 点击宝箱
        input.tap(pid, (WIDTH - 1.2) * w / WIDTH, (HEIGHT - 1.7) * h / HEIGHT)  # <= modify
        # 2. 点击看视频再领金币
        input.tap(pid, w / 2, 9.4 * h / HEIGHT)  # <= modify
        # 3. 播放15s
        time.sleep(15)
        # 4. 返回到任务页面
        phone.go_back(pid)

    # [x] 吃饭补贴
    # 早中晚夜宵4次
    def meal_allowance():
        # 1. 点击吃饭补贴
        input.tap(pid, w * 2 / 3, 5.8 * h / HEIGHT)  # <= modify
        # 2. 领取补贴
        input.tap(pid, w / 2, (HEIGHT - 1.3) * h / HEIGHT)  # <= modify
        # 3. 返回上级页面
        # 返回到福利页面
        phone.go_back(pid)

    # [x] 睡觉赚钱
    # 20:00-2:00为睡觉时间
    def sleep_money(is_sleep):
        # 1. 点击睡觉赚钱
        input.tap(pid, w / 3, 7.4 * h / HEIGHT)  # <= modify
        # 2. 点击我要睡了/我睡醒了
        for i in range(0, 2 if is_sleep else 1):
            input.tap(pid, w / 2, (HEIGHT - 1.0) * h / HEIGHT, 8)  # <= modify
        # 3. 返回到上级页面
        # 返回到福利页面
        phone.go_back(pid)

    # [x] 免费抽手机
    def free_phone():
        # 1. 点击免费抽手机
        input.tap(pid, w * 2 / 3, 7.4 * h / HEIGHT)  # <= modify
        # 2. 点击抽奖
        input.tap(pid, w / 2, 5.8 * h / HEIGHT, 10)  # <= modify
        # 3. 返回上级页面
        # 返回到任务页面
        phone.go_back(pid)

    # 打开头条进入福利页面
    checkin.toutiao(pid)
    benefit_page()

    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        # [x] 开宝箱
        open_treasure()

        # [x] 吃饭补贴
        hour = datetime.now().hour
        if hour.__eq__(6) or hour.__eq__(12) or hour.__eq__(18) or hour.__eq__(22):
            meal_allowance()

        # [x] 睡觉赚钱
        if hour.__eq__(20):
            sleep_money(False)
        elif hour.__eq__(3):
            sleep_money(True)

        # [x] 免费抽手机
        if hour.__eq__(6):
            free_phone()
    else:
        open_treasure()

    # 关闭头条
    phone.stop_app(pid, packages['toutiao'])


# noinspection PyUnusedLocal
def kuaishou(pid, w, h):
    def benefit_page():
        # 点击左上角菜单栏
        input.tap(pid, 0.6 * w / WIDTH, 0.9 * h / HEIGHT)  # <= modify
        # 点击去赚钱
        input.tap(pid, w / 2, 7.2 * h / HEIGHT)

    # [x] 开宝箱
    # 时间跨度依次递增
    # 每天有次数限制
    def open_treasure():
        # 1. 点击开宝箱得金币
        input.tap(pid, 5.7 * w / WIDTH, 11.5 * h / HEIGHT)  # <= modify
        # 2. 返回到上级页面
        # 是返回到播放视频的页面
        # 而不是去赚钱页面
        phone.go_back(pid)

    # [x] 看直播领金币
    def watch_live():
        # 1. 滑动页面打开看直播领金币
        phone.swipe_down_to_up(pid, w, h, 3, internal=50)
        for i in range(0, 10):
            # 2. 点击看直播
            input.tap(pid, (WIDTH - 1.0) * w / WIDTH, 8.8 * h / HEIGHT)  # <= modify
            # 3. 观看20s
            time.sleep(20)
            # 4 返回到福利页面
            phone.go_back(pid, gap=5)
        # 6. 福利页面恢复原样
        phone.swipe_up_to_down(pid, w, h, 3, internal=50)

    # 每隔一个小时开一次宝箱
    if datetime.now().minute.__lt__(SCHEDULE_TIME) and (datetime.now().hour % 2).__eq__(0):
        # 打开快手
        checkin.kuaishou(pid)
        benefit_page()

        open_treasure()

        if datetime.now().hour.__eq__(22):
            watch_live()

        # 关闭快手
        phone.stop_app(pid, packages['kuaishou'])


# noinspection PyUnusedLocal
def douyin(pid, w, h):
    # 福利页面
    def benefit_page():
        # 进入福利页面
        input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)

    # [x] 限时任务赚金币
    # 每20分钟完成一次广告任务
    def limit_duty():
        # 1. 点击去领取
        input.tap(pid, (WIDTH - 1.3) * w / WIDTH, 11.0 * h / HEIGHT)  # <= modify
        # 2. 播放30s
        time.sleep(30)
        # 3. 返回上级页面
        # 是返回到任务页面
        phone.go_back(pid)

    # [x] 开宝箱得金币
    # 每20分钟一次
    def open_treasure():

        # 2. 点击开宝箱得金币
        input.tap(pid, 5.7 * w / WIDTH, (HEIGHT - 1.1) * h / HEIGHT)  # <= modify
        # 3. 点击看广告视频再赚金币
        input.tap(pid, w / 2, 8.4 * h / HEIGHT)  # <= modify
        # 4. 播放30s
        time.sleep(30)
        # 5. 返回上级页面
        # 是返回到任务页面
        phone.go_back(pid)

    # [x] 睡觉赚钱
    # 20:00-2:00为睡觉时间
    def sleep_money(is_sleep):
        # 1. 下滑到最下面
        phone.swipe_down_to_up(pid, w, h, internal=100)
        # 2. 点击睡觉赚金币
        input.tap(pid, (WIDTH - 1.3) * w / WIDTH, 5.5 * h / HEIGHT)
        # 3. 点击我要睡了/我睡醒了
        for i in range(0, 2 if is_sleep else 1):
            input.tap(pid, w / 2, (HEIGHT - 1.0) * h / HEIGHT, 8)  # <= modify
        # 4. 返回到回到福利页面
        phone.go_back(pid)
        # 5. 滑到最上面
        phone.swipe_up_to_down(pid, w, h, internal=100)

    def meal_allowance():
        # 1. 下滑任务页面到最下面
        phone.swipe_down_to_up(pid, w, h, internal=100)
        # 2. 点击吃饭补贴
        input.tap(pid, w * 2 / 3, 10.6 * h / HEIGHT)  # <= modify
        # 3. 领取补贴
        input.tap(pid, w / 2, (HEIGHT - 1.3) * h / HEIGHT)  # <= modify
        # 4. 返回到福利页面
        phone.go_back(pid)

    checkin.douyin(pid)
    benefit_page()

    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        # 开宝箱得金币
        open_treasure()

        # 限时任务赚金币
        limit_duty()

        # [x] 睡觉赚金币
        if datetime.now().hour.__eq__(20):
            sleep_money(False)
        elif datetime.now().hour.__eq__(3):
            sleep_money(True)

        # [x] 吃饭补贴
        # 早中晚夜宵4次
        hour = datetime.now().hour
        if hour.__eq__(6) or hour.__eq__(12) or hour.__eq__(18) or hour.__eq__(22):
            meal_allowance()
    else:
        # 开宝箱得金币
        open_treasure()

        # 限时任务赚金币
        limit_duty()

    # 关闭抖音
    phone.stop_app(pid, packages['douyin'])


# noinspection PyUnusedLocal
def huoshan(pid, w, h):
    # 打开火山
    checkin.huoshan(pid)

    # 开宝箱
    def open_treasure():
        # 1. 点击红包
        input.tap(pid, 4.3 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)  # <= modify
        # 2. 点击开宝箱得金币
        input.tap(pid, (WIDTH - 1.0) * w / WIDTH, (HEIGHT - 2.1) * h / HEIGHT)  # <= modify
        # 3. 点击看视频金币翻倍按钮
        input.tap(pid, w / 2, 9.4 * h / HEIGHT)  # <= modify
        # 4. 播放30s
        time.sleep(30)
        # 5. 返回到福利页面
        phone.go_back(pid)

    # 看视频赚海量金币
    def video_money():
        # 1. 点击看视频赚海量金币
        input.tap(pid, w / 2, 7.5 * h / HEIGHT)
        # 2. 播放30s
        time.sleep(30)
        # 3. 返回到福利页面
        phone.go_back(pid)

    # 睡觉赚金币
    def sleep_money(is_sleep):
        # 1. 点击睡觉赚金币
        input.tap(pid, w / 2, 10.0 * h / HEIGHT)  # <= modify
        # 2. 点击我要睡了/我睡醒了
        for i in range(0, 2 if is_sleep else 1):
            input.tap(pid, w / 2, (HEIGHT - 1.0) * h / HEIGHT, 8)  # <= modify
        # 3. 返回到回到福利页面
        phone.go_back(pid)

    # [x] 开宝箱
    # 每20分钟一次
    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        open_treasure()

        # [x] 看视频赚海量金币
        # 总计20次
        if datetime.now().hour.__gt__(3):
            video_money()

        # [x] 睡觉赚金币
        # 20点睡觉3点起床收金币
        if datetime.now().hour.__eq__(20):
            sleep_money(False)
        elif datetime.now().hour.__eq__(3):
            sleep_money(True)
    else:
        open_treasure()

    # 关闭火山
    phone.stop_app(pid, packages['huoshan'])


# noinspection PyUnusedLocal
def jingdong(pid, w, h):
    if datetime.now().minute > SCHEDULE_TIME:
        return None


# noinspection PyUnusedLocal
def fanqie(pid, w, h):
    def benefit_page():
        # 1. 点击中间下方的福利
        input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)

    def open_treasure():
        # 1. 点击开宝箱得金币
        input.tap(pid, (WIDTH - 1.0) * w / WIDTH, (HEIGHT - 2.3) * h / HEIGHT)  # <= modify
        # 2. 点击看视频在领金币
        input.tap(pid, w / 2, 8.7 * h / HEIGHT)
        # 3. 播放30s
        time.sleep(30)
        # 4. 返回到福利页面
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)  # <= modify

    # 打开番茄
    checkin.fanqie(pid, w, h)
    benefit_page()

    # [x] 开宝箱
    # 每20分钟一次开宝箱任务
    open_treasure()

    # 关闭番茄
    phone.stop_app(pid, packages['fanqie'])


# noinspection PyUnusedLocal
def fanchang(pid, w, h):
    # 进入福利页面
    def benefit_page():
        # 1. 点击下方的福利
        input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)  # <= modify

    # 开宝箱
    def open_treasure():
        # 1. 点击开宝箱得金币
        input.tap(pid, (WIDTH - 1.0) * w / WIDTH, (HEIGHT - 2.1) * h / HEIGHT)  # <= modify
        # 2. 点击看视频再领金币
        input.tap(pid, w / 2, 9.9 * h / HEIGHT)  # <= modify
        # 3. 播放30s
        time.sleep(30)
        # 4. 返回到福利页面
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)  # <= modify

    # 完整的开宝箱流程
    def full_open_treasure():
        checkin.fanchang(pid, w, h)
        benefit_page()
        open_treasure()
        phone.stop_app(pid, packages['fanchang'])

    # [x] 开宝箱
    # 每个小时一次
    # 1, 4, 7开上半时段
    # 2, 5, 8开下半时段
    if (datetime.now().hour % 3).__eq__(1) and datetime.now().minute.__lt__(SCHEDULE_TIME):
        full_open_treasure()
    elif (datetime.now().hour % 3).__eq__(2) and datetime.now().minute.__ge__(SCHEDULE_TIME):
        full_open_treasure()


# noinspection PyUnusedLocal
def weishi(pid, w, h):
    if datetime.now().minute > SCHEDULE_TIME:
        return None


# noinspection PyUnusedLocal
def shuqi(pid, w, h):
    if datetime.now().minute > SCHEDULE_TIME:
        return None


# noinspection PyUnusedLocal
def yingke(pid, w, h):
    if datetime.now().minute > SCHEDULE_TIME:
        return None

    def benefit_page():
        # 1. 点击下面的横幅
        input.tap(pid, w / 3, (HEIGHT - 1.8) * h / HEIGHT)

    # 看福利视频
    def benefit_video():
        # 1. 点击领金币
        input.tap(pid, (WIDTH - 1.2) * w / WIDTH, 4.7 * h / HEIGHT)
        # 2. 播放30s
        time.sleep(30)
        # 3. 点击返回到福利页面
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)

    # 开宝箱
    def open_treasure():
        # 1. 点击开宝箱领金币
        input.tap(pid, (WIDTH - 1.1) * w / WIDTH, 12.2 * h / HEIGHT)
        # 2. 播放视频30s
        time.sleep(30)
        # 3. 返回到福利页面
        phone.go_back(pid)

    # [x] 看福利视频
    # 可以看10次
    # [x] 开宝箱
    # 次数未知
    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        # 进入福利页面
        checkin.yingke(pid, w, h)
        benefit_page()

        if datetime.now().hour.__lt__(11):
            benefit_video()
        if datetime.now().hour.__ge__(11):
            open_treasure()
        # 关闭映客
        phone.stop_app(pid, packages['yingke'])


# noinspection PyUnusedLocal
def kugou(pid, w, h):
    if datetime.now().minute > SCHEDULE_TIME:
        return None

    def benefit_page():
        # 1. 点击赚钱
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, (HEIGHT - 0.7) * h / HEIGHT)

    # 刷创意视频
    def creative_video():
        # 1. 点击去赚钱
        input.tap(pid, (WIDTH - 1.0) * w / WIDTH, (HEIGHT - 2.1) * h / HEIGHT)
        # 2. 播放35s
        # 包含等待弹出关闭界面
        time.sleep(35)
        # 3. 点击返回到福利页面
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)
        # 4. 再次回退消除奖励页面
        phone.go_back(pid)

    # [x] 刷创意视频
    # 定时任务
    if datetime.now().hour.__gt__(3):
        # 进入程序
        checkin.kugou(pid, w, h)
        benefit_page()

        creative_video()

        # 关闭程序
        phone.stop_app(pid, packages['kugou'])


# noinspection PyUnusedLocal
def huitoutiao(pid, w, h):
    if datetime.now().minute > SCHEDULE_TIME:
        return None

    def time_reward():
        # 1. 点击领取
        input.tap(pid, (WIDTH - 1.3) * w / WIDTH, 1.0 * h / HEIGHT, 2)

    def full_time_reward():
        # 1.打开惠头条
        checkin.huitoutiao(pid)
        time_reward()
        # 3. 关闭惠头条
        phone.stop_app(pid, packages['huitoutiao'])

    # [x] 时段奖励
    # 每个小时一次
    # 1, 4, 7开上半时段
    # 2, 5, 8开下半时段
    if (datetime.now().hour % 3).__eq__(1) and datetime.now().minute.__lt__(SCHEDULE_TIME):
        full_time_reward()
    elif (datetime.now().hour % 3).__eq__(2) and datetime.now().minute.__ge__(SCHEDULE_TIME):
        full_time_reward()


# noinspection PyUnusedLocal
def zhongqing(pid, w, h):
    if datetime.now().minute > SCHEDULE_TIME:
        return None


# noinspection PyUnusedLocal
def pinduoduo(pid, w, h):
    if datetime.now().minute > SCHEDULE_TIME:
        return None


# noinspection PyUnusedLocal
def taobao(pid, w, h):
    if datetime.now().minute > SCHEDULE_TIME:
        return None
    # 天天赚特币
    if datetime.now().hour % 4 == 0:
        # 1. 打开淘宝
        checkin.toutiao(pid)
        # 2. 点击天天赚特币
        input.tap(pid, w / 2, 2.4 * h / HEIGHT, 10)
        # 3. 收取特币
        input.tap(pid, 4.3 * w / WIDTH, 6.9 * h / HEIGHT)
        # 4. 关闭淘宝
        phone.stop_app(pid, packages['taobao'])


# noinspection PyUnusedLocal
def shuabao(pid, w, h):
    if datetime.now().minute > SCHEDULE_TIME:
        return None
    # [x] 看福利视频
    if datetime.now().hour > 13:
        # 1. 打开刷宝
        checkin.shuqi(pid, w, h)
        # 2. 点击福利
        input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 1.6) * h / HEIGHT)  # <= modify
        # 3. 播放30s
        time.sleep(30)
        # 4. 点击关闭按钮
        # 返回的页面未知
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)

        # 2. 关闭刷宝
        phone.stop_app(pid, packages['shuabao'])


# noinspection PyUnusedLocal
def qutoutiao(pid, w, h):
    if datetime.now().minute > SCHEDULE_TIME:
        return None

    # 进入任务页面
    def benefit_page():
        # 2. 点击任务
        input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)

    # 开宝箱
    def open_treasure():
        # 1. 点击宝箱
        input.tap(pid, (WIDTH - 1.0) * w / WIDTH, (HEIGHT - 1.6) * h / HEIGHT)
        # 2. 播放广告30s
        time.sleep(30)
        # 3. 关闭趣头条
        phone.stop_app(pid, packages['qutoutiao'])

    # [x] 开宝箱
    if datetime.now().hour % 2 == 0:
        # 打开趣头条
        checkin.qutoutiao(pid)
        benefit_page()
        open_treasure()
        # 关闭趣头条
        phone.stop_app(pid, packages['qutoutiao'])


# noinspection PyUnusedLocal
def baidu(pid, w, h):
    if datetime.now().minute > SCHEDULE_TIME:
        return None


# noinspection PyUnusedLocal
def ximalaya(pid, w, h):
    if datetime.now().minute > SCHEDULE_TIME:
        return None
