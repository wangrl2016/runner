import time

from src import input, phone, schedule, app
from src.info import WIDTH, HEIGHT


def toutiao(pid, w, h):
    # 1. 点击右下方任务栏目
    # 显示签到界面
    # [x] 签到成功
    app.toutiao_benefit_page(pid, w, h)
    # 2. 点击看视频再领金币
    input.tap(pid, w / 2, 9.0 * h / HEIGHT)  # <== modify
    # 3. 播放15s
    time.sleep(15)
    # 4. 返回到任务页面
    phone.go_back(pid)

    # [x] 开宝箱
    schedule.toutiao_open_treasure(pid, w, h)


def kuaishou(pid, w, h):
    # 1. 假装后退解决弹出青少年模式悬浮窗的问题
    phone.go_back(pid)
    # 2. 进入快手福利页面
    app.kuaishou_benefit_page(pid, w, h, gap=5)
    # 3. 显示签到页面点击立即签到
    # [x] 签到成功
    input.tap(pid, w / 2, 10.4 * h / HEIGHT)  # <=== modify
    # 4. 回退到播放界面
    phone.go_back(pid)


def douyin(pid, w, h):
    # 1. 假装退出弹出青少年模式悬浮窗的问题
    phone.go_back(pid)
    # 2. 点击下方的福袋
    # 等待10s签到界面出现
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT, 10)
    # 3. 点击立即签到领金币
    # 签到成功
    # 4. 看视频再赚金币
    for i in range(0, 2):
        input.tap(pid, w / 2, 9.7 * h / HEIGHT)
    # 5. 播放30s
    time.sleep(30)
    # 6. 退出播放页面
    phone.go_back(pid)

    # [x] 顺便开宝箱
    schedule.douyin_open_treasure(pid, w, h)


def huoshan(pid, w, h):
    # 1. 假装想要退出解决弹出青少年模式悬浮窗的问题
    phone.go_back(pid)
    # 2. 点击右下方红包宝箱
    # 显示签到成功
    input.tap(pid, 4.3 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)  # <= modify
    # 3. 看广告再领金币
    input.tap(pid, w / 2, 9.5 * h / HEIGHT)
    # 4. 播放30s
    time.sleep(30)
    # 5. 返回到福利页面
    phone.go_back(pid)

    # [x] 顺便开宝箱
    schedule.huoshan_open_treasure(pid, w, h)


def jingdong(pid, w, h):
    # 1. 点击中间的现金签到
    input.tap(pid, w / 2, 6.8 * h / HEIGHT)  # <= modify
    # 2. 点击立即签到
    # 显示签到成功
    input.tap(pid, w / 2, 5.8 * h / HEIGHT)  # <= modify
    # 3. 关闭成功界面
    phone.go_back(pid)


def fanqie(pid, w, h):
    # 1. 点击中间下方福利签到
    # 签到成功
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)
    # 2. 点击看视频再领金币
    input.tap(pid, w / 2, 10.1 * h / HEIGHT)  # <= modify
    # 3. 播放视频30s
    time.sleep(30)
    # 4. 点击关闭回退到福利页面
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)  # <== modify
    # 5. 顺便开宝箱
    # 完成之后返回到福利页面

    # [x] 开宝箱
    schedule.fanqie_open_treasure(pid, w, h)


def fanchang(pid, w, h):
    # 1. 点击福利
    # 显示签到成功
    input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)  # <= modify
    # 2. 点击看视频再领金币
    input.tap(pid, w / 2, 10.0 * h / HEIGHT)  # <= modify
    # 3. 播放视频30s
    time.sleep(30)
    # 4. 点击关闭回退到福利页面
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)  # <== modify
    # 5. 顺便开宝箱
    # 完成之后返回到福利页面

    # [x] 开宝箱
    schedule.fanchang_open_treasure(pid, w, h)


# noinspection PyUnusedLocal
def weishi(pid, w, h):
    # 没有签到窗口
    return None


def shuqi(pid, w, h):
    # 后退会弹出提示框
    # 不后退有时会有悬浮窗
    phone.swipe_up_to_down(pid, w, h / 2, gap=2, internal=100)
    # 1. 点击中间下方的福利
    # 显示签到成功
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT, gap=2)


def yingke(pid, w, h):
    # 1. 假装退出可能出现的悬浮窗问题
    # 2. 可能出现两次
    phone.go_back(pid, times=2)
    # 2. 点击右下角打开红包
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, (HEIGHT - 1.9) * h / HEIGHT)  # <= modify
    # 3. 点击立即签到
    input.tap(pid, w / 2, 10.4 * h / HEIGHT)  # <=== modify
    # 4. 播放30s广告
    time.sleep(30)
    # 5. 点击关闭
    # 弹出悬浮窗显示签到成功
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)  # <= modify
    # 6. 回到程序主页
    phone.go_back(pid)


def kugou(pid, w, h):
    # 1. 点击右下角赚钱
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, (HEIGHT - 0.7) * h / HEIGHT)  # <= modify
    # 2. 点击每日签到栏
    # 显示签到成功
    input.tap(pid, (WIDTH - 1.0) * w / WIDTH, (HEIGHT - 3.4) * h / HEIGHT)  # <= modify
    # 3. 返回到赚钱页面
    phone.go_back(pid)


def huitoutiao(pid, w, h):
    # 1. 假装想要退出关闭可能的悬浮窗
    phone.go_back(pid)
    # 2. 点击下方右侧任务中心
    input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)  # <= modify
    # 3. 点击今日签到
    # 显示签到成功
    input.tap(pid, w / 2, 2.4 * h / HEIGHT)  # <= modify


def zhongqing(pid, w, h):
    # 1. 假装想要退出关闭可能的悬浮窗
    phone.go_back(pid)
    # 2. 点击任务待签到
    input.tap(pid, 4.3 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)  # <= modify
    # 3. 点击签到领现金
    # 签到成功
    input.tap(pid, w / 2, 4.9 * h / HEIGHT)  # <= modify
    # 4. 回退到福利页面
    phone.go_back(pid)


def pinduoduo(pid, w, h):
    # 1. 回退消除可能出现的悬浮窗
    phone.go_back(pid)
    # 2. 点击中间的现金签到
    input.tap(pid, w / 2, 5.4 * h / HEIGHT)  # <= modify
    # 3. 点击签到领现金
    # 签到成功
    input.tap(pid, w / 2, 3.0 * h / HEIGHT)  # <= modify
    # 3. 返回到程序主页
    phone.go_back(pid)


# noinspection PyUnusedLocal
def taobao(pid, w, h):
    # 红包很难提现
    return None


def shuabao(pid, w, h):
    # 1. 假装回退关闭可能的悬浮窗
    phone.go_back(pid)
    # 2. 点击下方福利
    input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)  # <= modify
    # 3. 假装想要退出关闭可能的悬浮窗
    phone.go_back(pid)
    # 4. 点击立即签到
    input.tap(pid, (WIDTH - 1.1) * w / WIDTH, 1.9 * h / HEIGHT)  # <= modify
    # 5. 点击看视频签到
    input.tap(pid, w * 3 / 4, 9.7 * h / HEIGHT)  # <= modify
    # 6. 播放30s
    time.sleep(30)
    # 7. 点击关闭
    # 显示签到成功页面
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)  # <= modify
    # 8. 回退显示获取元宝页面
    phone.go_back(pid)


# noinspection PyUnusedLocal
def qutoutiao(pid, w, h):
    # 1. 点击右下方任务
    # 显示签到成功
    input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)
    # 2. 点击看视频再领金币
    input.tap(pid, w / 2, 6.8 * h / HEIGHT)
    # 3. 播放50s
    time.sleep(50)
    # 4. 回退到福利页面
    phone.go_back(pid)


# noinspection PyUnusedLocal
def baidu(pid, w, h):
    # 1. 点击右下方去签到
    # 显示签到成功
    input.tap(pid, 4.7 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)
    for i in range(0, 5):
        # 2. 看视频再领金币
        input.tap(pid, w / 2, 5.6 * h / HEIGHT)  # <== modify
        # 3. 播放30s
        time.sleep(30)
        # 回退到悬浮窗页面
        phone.go_back(pid, gap=4)


def ximalaya(pid, w, h):
    # 1. 点击右下方福利
    # 显示签到成功
    input.tap(pid, 4.3 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)
    # 2. 看视频再领金币
    input.tap(pid, w / 2, 9.5 * h / HEIGHT)
    # 3. 播放30s
    time.sleep(30)
    # 4. 关闭返回广告页面
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)
    # 5. 返回到福利页面
    phone.go_back(pid)


def douhuo(pid, w, h):
    # 1. 假装回退关闭可能的悬浮窗
    phone.go_back(pid)
    # 2. 点击个人中心图标
    input.tap(pid, 0.5 * w / WIDTH, 0.9 * h / HEIGHT)
    # 3. 点击火苗管理
    # 显示签到成功
    input.tap(pid, w / 2, 8.0 * h / HEIGHT)


# noinspection PyUnusedLocal
def kuge(pid, w, h):
    # 1. 点击右上方赚钱
    input.tap(pid, 4.8 * w / WIDTH, 1.2 * h / HEIGHT)
    # 点击签到
    # 位置未知
    # 签到成功
    for i in range(0, 7):
        input.tap(pid, (1.0 + 0.8 * i) * w / WIDTH, 6.9 * h / HEIGHT, gap=1)
    # 2. 回退到福利页面
    phone.go_back(pid, gap=2)
    # 3. 必须回到儿歌页面
    input.tap(pid, 2.0 * w / WIDTH, 1.2 * h / HEIGHT, gap=2)


# noinspection PyUnusedLocal
def makan(pid, w, h):
    return None


# noinspection PyUnusedLocal
def diandian(pid, w, h):
    return None
