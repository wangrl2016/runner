import time
from datetime import datetime

from src import checkin, phone, input, app
from src.info import packages, WIDTH, HEIGHT, SCHEDULE_TIME


def toutiao_open_treasure(pid, w, h, gap=15):
    """
    今日头条开宝箱
    """
    # 1. 点击宝箱
    input.tap(pid, (WIDTH - 1.2) * w / WIDTH, (HEIGHT - 1.7) * h / HEIGHT)  # <= modify
    # 2. 点击看视频再领金币
    input.tap(pid, w / 2, 9.4 * h / HEIGHT)  # <= modify
    # 3. 默认播放15s
    time.sleep(gap)
    # 4. 返回到任务页面
    phone.go_back(pid)


def toutiao(pid, w, h):
    # 吃饭补贴
    def meal_allowance():
        # 1. 点击吃饭补贴
        input.tap(pid, w * 2 / 3, 5.8 * h / HEIGHT)  # <= modify
        # 2. 领取补贴
        input.tap(pid, w / 2, (HEIGHT - 1.3) * h / HEIGHT)  # <= modify
        # 3. 返回到福利页面
        phone.go_back(pid)

    # 睡觉赚钱
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
        # 3. 返回到福利页面
        phone.go_back(pid)

    # 种菜赚金币
    def grow_vegetables(is_first):
        # 1. 点击种菜赚金币
        input.tap(pid, w / 2, (HEIGHT - 1.1) * h / HEIGHT)  # <== modify
        # 2. 弹出离线产量悬浮窗
        # 第2次解决签到礼包悬浮窗
        # 点击看视频获取
        input.tap(pid, w / 2, 8.4 * h / HEIGHT)  # <= modify
        # 3. 播放15s
        time.sleep(15)
        # 5. 如果是第1次会返回到签到礼包页面
        phone.go_back(pid)
        if is_first:
            # 6. 点击领取奖励
            input.tap(pid, w / 3, (HEIGHT - 3.5) * h / HEIGHT)
            # 7. 点击确定
            input.tap(pid, w / 2, 8.4 * h / HEIGHT)
            # 8. 关闭签到礼包
            input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 2.8 * h / HEIGHT)
        # 9. 点击浇水
        input.tap(pid, (WIDTH - 0.9) * w / WIDTH, (HEIGHT - 1.0) * h / HEIGHT)
        # 10. 领取奖励
        # 点击宝箱
        input.tap(pid, (WIDTH - 0.9) * w / WIDTH, 1.7 * h / HEIGHT)
        # 11. 点击看视频再领金币
        input.tap(pid, w / 2, 8.4 * h / HEIGHT)
        # 12. 播放15s
        phone.go_back(pid)
        # 13. 点击确定
        input.tap(pid, w / 2, 8.4 * h / HEIGHT)
        # 14. 返回到福利页面
        phone.go_back(pid)

    # 打开头条
    checkin.toutiao(pid)
    app.toutiao_benefit_page(pid, w, h)

    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        # [x] 吃饭补贴
        # 早中晚夜宵4次
        hour = datetime.now().hour
        if hour.__eq__(6) or hour.__eq__(12) or hour.__eq__(18) or hour.__eq__(22):
            meal_allowance()

        # [x] 睡觉赚钱
        # 20:00-2:00
        if hour.__eq__(20):
            sleep_money(False)
        elif hour.__eq__(6):
            sleep_money(True)

        # [x] 免费抽手机
        if hour.__eq__(6):
            free_phone()
            grow_vegetables(True)

        if hour.__gt__(6) and hour.__le__(11):
            # [x] 种菜赚金币
            grow_vegetables(False)

    # [x] 开宝箱
    # 每10分钟一次
    toutiao_open_treasure(pid, w, h)

    # 关闭头条
    phone.stop_app(pid, packages['toutiao'])


# noinspection PyUnusedLocal
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
        phone.swipe_down_to_up(pid, w, h, gap=3, internal=100)
        # 2. 点击看直播按钮
        # 位置不定
        input.tap(pid, (WIDTH - 1.0) * w / WIDTH, 8.8 * h / HEIGHT)  # <== modify
        for i in range(0, 10):
            # 3. 观看20s
            time.sleep(20)
            # 4. 上滑出现下一个
            phone.swipe_down_to_up(pid, w, h / 2, internal=100, gap=5)
        # 5. 返回到福利页面
        phone.go_back(pid, gap=8)
        # 6. 福利页面恢复原样
        phone.swipe_up_to_down(pid, w, h, 3, internal=100)

    # 每隔一个小时开一次宝箱
    if datetime.now().minute.__lt__(SCHEDULE_TIME) and (datetime.now().hour % 2).__eq__(0):
        # 打开快手
        checkin.kuaishou(pid)
        app.kuaishou_benefit_page(pid, w, h)

        # [x] 看直播
        # 21:00-24:00
        if datetime.now().hour.__eq__(22):
            watch_live()

        # [x] 开宝箱
        open_treasure()

        # 关闭快手
        phone.stop_app(pid, packages['kuaishou'])


# noinspection PyUnusedLocal
def douyin(pid, w, h):
    # 福利页面
    def benefit_page():
        # 进入福利页面
        input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)

    # 限时任务赚金币
    def limit_duty():
        # 1. 点击去领取
        input.tap(pid, (WIDTH - 1.3) * w / WIDTH, 9.5 * h / HEIGHT)  # <= modify
        # 2. 播放30s
        time.sleep(30)
        # 3. 返回福利页面
        phone.go_back(pid)

    # 开宝箱得金币
    def open_treasure():
        # 1. 点击开宝箱得金币
        input.tap(pid, (WIDTH - 1.1) * w / WIDTH, (HEIGHT - 1.1) * h / HEIGHT)  # <= modify
        # 2. 点击看广告视频再赚金币
        input.tap(pid, w / 2, 8.4 * h / HEIGHT)  # <= modify
        # 3. 播放30s
        time.sleep(30)
        # 4. 返回福利页面
        # 存在超过30s的广告需要返回两次
        phone.go_back(pid, times=2)

    # 睡觉赚钱
    def sleep_money(is_sleep):
        # 1. 下滑到最下面
        phone.swipe_down_to_up(pid, w, h, internal=100)
        # 2. 点击睡觉赚金币
        input.tap(pid, w / 2, 5.5 * h / HEIGHT)  # <== modify
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
        phone.swipe_down_to_up(pid, w, h, internal=100)
        # 2. 点击吃饭补贴
        input.tap(pid, w / 2, 10.6 * h / HEIGHT)  # <== modify
        # 3. 领取补贴
        input.tap(pid, w / 2, (HEIGHT - 1.3) * h / HEIGHT)  # <= modify
        # 4. 返回到福利页面
        phone.go_back(pid)
        # 5. 滑到最上面
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
    benefit_page()

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

    # [x] 限时任务赚金币
    # 每20分钟一次
    limit_duty()
    # [x] 开宝箱得金币
    # 每20分钟一次
    open_treasure()

    # 关闭抖音
    phone.stop_app(pid, packages['douyin'])


# 火山开宝箱
def huoshan_open_treasure(pid, w, h):
    # 2. 点击开宝箱得金币
    input.tap(pid, (WIDTH - 1.0) * w / WIDTH, (HEIGHT - 2.1) * h / HEIGHT)  # <= modify
    # 3. 点击看视频金币翻倍按钮
    input.tap(pid, w / 2, 9.4 * h / HEIGHT)  # <= modify
    # 4. 播放30s
    time.sleep(30)
    # 5. 返回到福利页面
    phone.go_back(pid)


# noinspection PyUnusedLocal
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

    # 睡觉赚金币
    def sleep_money(is_sleep):
        # 1. 点击睡觉赚金币
        input.tap(pid, w / 2, 10.0 * h / HEIGHT)  # <= modify
        # 2. 点击我要睡了/我睡醒了
        for i in range(0, 2 if is_sleep else 1):
            input.tap(pid, w / 2, (HEIGHT - 1.0) * h / HEIGHT, 8)  # <= modify
        # 3. 返回到回到福利页面
        phone.go_back(pid)

    # 晒收入
    def show_income():
        # 1. 点击晒收入
        input.tap(pid, w / 2, (HEIGHT - 3.3) * h / HEIGHT)
        # 2. 点击微信
        input.tap(pid, w / 2, 8.3 * h / HEIGHT)
        for i in range(0, 3):
            # 3. 点击去粘贴
            # 进入微信页面
            input.tap(pid, w / 2, 9.2 * h / HEIGHT, 8)
            # 4. 返回到火山微信悬浮窗
            phone.go_back(pid)
        # 5. 返回到福利页面
        phone.go_back(pid)

    # 打开火山
    checkin.huoshan(pid)
    benefit_page()

    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        # [x] 开宝箱
        # 每20分钟一次
        huoshan_open_treasure(pid, w, h)

        # [x] 看视频赚海量金币
        # 总计20次
        if datetime.now().hour.__gt__(3):
            video_money()

        # [x] 睡觉赚金币
        # 20点睡觉3点起床收金币
        if datetime.now().hour.__eq__(20):
            sleep_money(False)

            # [x] 晒收入
            show_income()
        elif datetime.now().hour.__eq__(3):
            sleep_money(True)
    else:
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
    # 2. 点击看视频在领金币
    input.tap(pid, w / 2, 8.7 * h / HEIGHT)
    # 3. 播放30s
    time.sleep(30)
    # 4. 返回到福利页面
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)  # <= modify


# noinspection PyUnusedLocal
def fanqie(pid, w, h):
    def benefit_page():
        # 1. 点击中间下方的福利
        input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)

    # 分享好书给好友
    def book_share():
        # 1. 点击分享好书给好友
        input.tap(pid, w / 2, 10.1 * h / HEIGHT)
        # 2. 点击任意一本书
        input.tap(pid, w / 2, h / 3)
        # 3. 点击分享
        input.tap(pid, (WIDTH - 0.6) * w / WIDTH, 0.9 * h / HEIGHT)
        # 4. 点击微信
        input.tap(pid, 1.0 * w / WIDTH, 9.5 * h / HEIGHT)

    # 可能存在重复加入
    def add_bookshelf():
        return None

    # 打开番茄
    checkin.fanqie(pid, w, h)
    benefit_page()

    # [x] 开宝箱
    # 每20分钟一次开宝箱任务
    fanqie_open_treasure(pid, w, h)

    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        if datetime.now().hour.__eq__(21):
            add_bookshelf()
        elif datetime.now().hour.__eq__(22):
            # [x] 分享好书给好友
            book_share()

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
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)  # <== modify


# noinspection PyUnusedLocal
def fanchang(pid, w, h):
    # 进入福利页面
    def benefit_page():
        # 1. 点击下方的福利
        input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)  # <= modify

    # 完整的开宝箱流程
    def full_open_treasure():
        checkin.fanchang(pid, w, h)
        benefit_page()
        fanchang_open_treasure(pid, w, h)
        # 收听番唱音频时不能退出程序
        if datetime.now().hour.__gt__(7) and datetime.now().hour.__lt__(12):
            phone.go_home(pid)
        else:
            phone.stop_app(pid, packages['fanchang'])

    # 收听音频
    def listen_sound():
        # 1. 点击中间下方的播放界面
        input.tap(pid, w / 2, (HEIGHT - 0.6) * h / HEIGHT)

    def collect_listen_coin():
        # 1. 点击中间下方的播放界面
        listen_sound()
        # 2. 点击立即领取
        input.tap(pid, (WIDTH - 1.0) * w / WIDTH, 10.0 * h / HEIGHT)
        for i in range(0, 9):
            # 3. 点击领红包
            input.tap(pid, w / 2, (HEIGHT - 0.9) * h / HEIGHT)
            # 4. 点击看视频再领金币
            input.tap(pid, w / 2, 8.3 * h / HEIGHT)
            # 5. 播放30s
            time.sleep(30)
            # 返回到领取界面
            input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)

    # [x] 听番畅音频
    # 08:00-09:00-10:00-11:00-12:00
    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        if datetime.now().hour.__eq__(8):
            checkin.fanchang(pid, w, h)
            # [x] 收听番唱音频
            listen_sound()
            # 回退到程序主页
            phone.go_back(pid)
            # 后台播放
            phone.go_home(pid)
        elif datetime.now().hour.__eq__(9):
            # 解锁广告
            # 1. 进入番畅音频
            checkin.fanchang(pid, w, h)
            listen_sound()
            # 2. 点击看小视频免费听
            input.tap(pid, 4.7 * w / WIDTH, 0.9 * h / HEIGHT)
            # 3. 播放45s
            time.sleep(45)
            # 4. 点击关闭
            # 播放页面
            input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)
            # 5. 回退到主页
            phone.go_back(pid)
            # ６．后台播放
            phone.go_home(pid)
        elif datetime.now().hour.__eq__(12):
            checkin.fanchang(pid, w, h)
            collect_listen_coin()
            phone.stop_app(pid, packages['fanchang'])

    # [x] 开宝箱
    # 每个小时一次
    # 1, 4, 7, 10, 13, 16, 19, 22开上半时段
    # 2, 5, 8, 11, 14, 17, 20, 23开下半时段
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
    # 进入福利页面
    def benefit_page():
        # 1. 点击下面的横幅
        input.tap(pid, w / 3, (HEIGHT - 1.8) * h / HEIGHT)  # <= modify

    # 看福利视频
    def benefit_video():
        # 1. 点击领金币
        input.tap(pid, (WIDTH - 1.2) * w / WIDTH, 4.7 * h / HEIGHT)  # <== modify
        # 2. 播放30s
        time.sleep(30)
        # 3. 点击返回到福利页面
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)  # <== modify

    # 开宝箱
    def open_treasure():
        # 1. 点击开宝箱领金币
        input.tap(pid, (WIDTH - 1.1) * w / WIDTH, (HEIGHT - 2.5) * h / HEIGHT)  # <= modify
        # 2. 播放视频30s
        time.sleep(30)
        # 3. 返回到福利页面
        phone.go_back(pid)

    if datetime.now().minute.__lt__(SCHEDULE_TIME) and datetime.now().hour.__gt__(12):
        # 进入福利页面
        checkin.yingke(pid, w, h)
        benefit_page()

        # [x] 看福利视频
        # 可以看10次
        # 后续奖励金更多
        benefit_video()
        # [x] 开宝箱
        # 次数未知
        open_treasure()

        # 关闭映客
        phone.stop_app(pid, packages['yingke'])


def kugou_background_music(pid, w, h):
    # 1. 点击下方图标进入播放页面
    input.tap(pid, w / 2, (HEIGHT - 0.7) * h / HEIGHT)
    # 2. 点击播放
    input.tap(pid, w / 2, (HEIGHT - 1.4) * h / HEIGHT)
    # 3. 回到主页
    phone.go_back(pid)
    # 4. 后台播放
    phone.go_home(pid)


# noinspection PyUnusedLocal
def kugou(pid, w, h):
    # 进入福利页面
    def benefit_page():
        # 1. 点击赚钱
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, (HEIGHT - 0.7) * h / HEIGHT)  # <= modify

    # 刷创意视频
    def creative_video():
        # 1. 点击去赚钱
        input.tap(pid, (WIDTH - 1.0) * w / WIDTH, (HEIGHT - 2.1) * h / HEIGHT)  # <= modify
        # 2. 播放35s
        # 包含等待弹出关闭界面
        time.sleep(35)
        # 3. 点击返回到福利页面
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)  # <= modify
        # 4. 再次回退消除奖励页面
        phone.go_back(pid)

    if datetime.now().minute.__lt__(SCHEDULE_TIME) and datetime.now().hour.__gt__(3):
        # 进入程序
        checkin.kugou(pid, w, h)
        benefit_page()

        # [x] 刷创意视频
        # 总共20次定时任务
        creative_video()

        # 关闭程序
        phone.stop_app(pid, packages['kugou'])

        # [x] 播放酷狗音乐
        if datetime.now().hour.__eq__(18):
            checkin.kugou(pid, w, h)
            kugou_background_music(pid, w, h)


def huitoutiao(pid, w, h):
    def time_reward():
        # 1. 点击领取
        # 有时候没有广告视频
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


def zhongqing(pid, w, h):
    # 时段奖励
    def time_reward():
        # 1. 点击领取
        for i in range(0, 2):
            # 等待8s悬浮窗消失
            # 点击看视频奖励
            input.tap(pid, (WIDTH - 0.9) * w / WIDTH, 1.0 * h / HEIGHT, 8)
        # 2. 播放30s
        time.sleep(30)
        # 3. 返回程序主页
        # 必须关闭才有奖励
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)

    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        checkin.zhongqing(pid, w, h)
        # [x] 时段奖励
        time_reward()
        phone.stop_app(pid, packages['zhongqing'])


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


def taobao(pid, w, h):
    # [x] 天天赚特币
    if datetime.now().minute.__lt__(SCHEDULE_TIME) and (datetime.now().hour % 4).__eq__(0):
        # 1. 打开淘宝
        checkin.taobao(pid)
        # 2. 点击天天赚特币
        input.tap(pid, w / 2, 2.4 * h / HEIGHT, gap=10)  # <= modify
        # 3. 收取特币
        input.tap(pid, 4.3 * w / WIDTH, 6.9 * h / HEIGHT)  # <= modify
        # 4. 关闭淘宝
        phone.stop_app(pid, packages['taobao'])


def shuabao(pid, w, h):
    def benefit_page():
        # 1. 点击福利
        input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)  # <= modify
        # 2. 回退关闭悬浮窗
        phone.go_back(pid)

    # 看福利视频
    def benefit_video():
        # 1. 点击去观看
        input.tap(pid, (WIDTH - 1.0) * w / WIDTH, (HEIGHT - 1.6) * h / HEIGHT)  # <== modify
        # 2. 播放30s
        time.sleep(30)
        # 3. 点击关闭
        input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)

    if datetime.now().minute < SCHEDULE_TIME and datetime.now().hour.__gt__(13):
        # 1. 打开刷宝
        checkin.shuabao(pid)
        benefit_page()
        # [x] 看福利视频
        benefit_video()
        # 3. 关闭刷宝
        phone.stop_app(pid, packages['shuabao'])


# 趣头条开宝箱
def qutoutiao_open_treasure(pid, w, h):
    # 1. 点击宝箱
    input.tap(pid, (WIDTH - 1.0) * w / WIDTH, (HEIGHT - 1.6) * h / HEIGHT)
    # 2. 播放广告50s
    time.sleep(50)
    # 3. 回退到福利页面
    # 第1次退出广告界面
    # 第2次退出金币提示界面
    phone.go_back(pid, times=2)


def qutoutiao(pid, w, h):
    # 进入任务页面
    def benefit_page():
        # 2. 点击任务
        input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)

    # 看广告视频拿金币
    def video_coin():
        # 1. 点击看广告视频拿金币
        input.tap(pid, w / 2, (HEIGHT - 1.2) * h / HEIGHT)  # <=== modify
        # 2. 播放45s
        time.sleep(45)
        # 3. 回退到福利页面
        phone.go_back(pid)

    # 时段奖励
    def time_reward():
        return None

    # 开宝箱
    def full_open_treasure():
        # 打开趣头条
        checkin.qutoutiao(pid)
        benefit_page()
        # [x] 开宝箱
        qutoutiao_open_treasure(pid, w, h)
        # 关闭趣头条
        phone.stop_app(pid, packages['qutoutiao'])

    # 睡觉赚钱
    def sleep_money(is_sleep):
        # 1. 下滑到最底下
        phone.swipe_down_to_up(pid, w, h, internal=100)
        # 2. 点击睡觉赚金币
        input.tap(pid, w / 2, 4.2 * h / HEIGHT)  # <=== modify
        # 3. 点击我要睡了/我睡醒了
        for i in range(0, 2 if is_sleep else 1):
            input.tap(pid, w / 2, (HEIGHT - 1.0) * h / HEIGHT, gap=8)  # <= modify
        # 4. 返回到回到福利页面
        phone.go_back(pid)

        # [x] 摇钱树领金币
        if datetime.now().hour.__eq__(15):
            money_tree()

        # 5. 福利页面恢复原样
        phone.swipe_up_to_down(pid, w, h, internal=100)

    def full_sleep_money(is_sleep):
        checkin.qutoutiao(pid)
        benefit_page()
        sleep_money(is_sleep)
        phone.stop_app(pid, packages['qutoutiao'])

    def money_tree():
        # 1. 点击摇钱树领金币
        input.tap(pid, w / 2, 5.4 * h / HEIGHT)  # <=== modify
        # 2. 摇5次
        for i in range(0, 5):
            # 领金币
            input.tap(pid, w / 2, 10.6 * h / HEIGHT)
            # 播放45s
            time.sleep(45)
            # 回退到摇钱树页面
            phone.go_back(pid)

    # [x] 开宝箱
    # 每个小时一次
    # 1, 4, 7开上半时段
    # 2, 5, 8开下半时段
    if (datetime.now().hour % 3).__eq__(1) and datetime.now().minute.__lt__(SCHEDULE_TIME):
        checkin.qutoutiao(pid)
        benefit_page()
        qutoutiao_open_treasure(pid, w, h)

        # [x] 看广告视频拿金币
        # 每天可以看六次
        if datetime.now().hour.__gt__(6):
            # 进入趣头条
            checkin.qutoutiao(pid)
            benefit_page()
            # [x] 看趣头条拿金币
            video_coin()

        # 退出趣头条
        phone.stop_app(pid, packages['qutoutiao'])

    elif (datetime.now().hour % 3).__eq__(2) and datetime.now().minute.__ge__(SCHEDULE_TIME):
        full_open_treasure()

    # [x] 睡觉赚金币
    # 20:00-08:00为睡觉时间
    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        if datetime.now().hour.__eq__(20):
            full_sleep_money(False)
        elif datetime.now().hour.__eq__(9):
            full_sleep_money(True)
        elif datetime.now().hour.__eq__(12):
            full_sleep_money(False)
        elif datetime.now().hour.__eq__(15):
            full_sleep_money(True)


def baidu(pid, w, h):
    def benefit_page():
        input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)

    def open_treasure():
        # 1. 打开宝箱
        input.tap(pid, (WIDTH - 1.3) * w / WIDTH, 10.1 * h / HEIGHT)  # <= modify

    # [x] 开宝箱
    # 金银铜三种宝箱
    # 金宝箱需要3个小时
    if datetime.now().minute.__lt__(SCHEDULE_TIME) and (datetime.now().hour % 4).__eq__(0):
        checkin.baidu(pid)
        benefit_page()
        open_treasure()
        phone.stop_app(pid, packages['baidu'])


def ximalaya(pid, w, h):
    def listen_sound():
        # 1. 点击收听
        input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)
        # 2. 点击收金币
        # 在收金币界面
        input.tap(pid, 3.8 * w / WIDTH, 1.0 * h / HEIGHT)

    def collect_coin():
        # 1. 点击取金币
        input.tap(pid, 0.7 * w / WIDTH, 3.5 * h / HEIGHT)
        # 2. 看视频超级翻倍
        input.tap(pid, w / 2, 8.9 * h / HEIGHT)
        # 3. 播放30s
        time.sleep(30)
        # 4. 返回到播放收金币页面
        # 第1次退出广告页面
        # 第2次退出翻倍成功页面
        phone.go_back(pid, times=2)

    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        if datetime.now().hour.__eq__(12):
            checkin.ximalaya(pid)
            # [x] 收听喜马拉雅
            listen_sound()
            phone.go_home(pid)
        elif datetime.now().hour.__gt__(12) and datetime.now().hour.__lt__(16):
            checkin.ximalaya(pid)
            collect_coin()
            if datetime.now().hour.__eq__(15):
                # 关闭喜马拉雅
                phone.stop_app(pid, 'ximalaya')


# noinspection PyUnusedLocal
def douhuo(pid, w, h):
    return None


def kuge(pid, w, h):
    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        # [x] 收听酷狗儿歌
        if datetime.now().hour.__eq__(16):
            # 1. 进入酷狗儿歌
            checkin.kuge(pid, w, h)
            # 2. 播放
            input.tap(pid, 4.2 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)
            # 3. 回到后台
            phone.go_home(pid)
        elif datetime.now().hour.__eq__(17):
            # 1. 关闭酷狗儿歌
            phone.stop_app(pid, packages['kuge'])


# noinspection PyUnusedLocal
def makan(pid, w, h):
    return None


# noinspection PyUnusedLocal
def diandian(pid, w, h):
    return None
