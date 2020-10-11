import time

from src import checkin, phone, input
from src.info import packages, WIDTH, HEIGHT


# noinspection PyUnusedLocal
def toutiao(pid, w, h):
    # 打开头条
    checkin.toutiao(pid)

    # [x] 开宝箱
    # 每10分钟一次
    # 1. 点击任务
    input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)
    # 2. 点击宝箱
    # 开宝箱得金币
    input.tap(pid, (WIDTH - 1.2) * w / WIDTH, (HEIGHT - 1.7) * h / HEIGHT)
    # 3. 点击看视频再领金币
    input.tap(pid, w / 2, 9.4 * h / HEIGHT)
    # 4. 播放15s
    time.sleep(15)
    # 5. 退出播放页面
    # 返回到任务页面
    phone.go_back(pid)

    # 关闭头条
    phone.stop_app(pid, packages['toutiao'])


# noinspection PyUnusedLocal
def kuaishou(pid, w, h):
    # 打开快手
    checkin.kuaishou(pid)

    # [x] 开宝箱
    # 时间跨度依次递增
    # 每天有次数限制
    # 1. 点击左上角菜单栏
    input.tap(pid, 0.6 * w / WIDTH, 0.9 * h / HEIGHT)  # <= modify
    # 2. 点击去赚钱
    input.tap(pid, w / 2, 7.2 * h / HEIGHT)
    # 3. 点击开宝箱得金币
    input.tap(pid, 5.7 * w / WIDTH, 11.5 * h / HEIGHT)  # <= modify
    # 4. 返回到上级页面
    # 是返回到播放视频的界面
    # 而不是去赚钱页面
    phone.go_back(pid)

    # 关闭快手
    phone.stop_app(pid, packages['kuaishou'])


# noinspection PyUnusedLocal
def douyin(pid, w, h):
    # 打开抖音
    checkin.douyin(pid)

    # [x] 开宝箱
    # 每20分钟一次
    # 1. 点击中间的福袋按钮
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)
    # 2. 点击开宝箱得金币
    input.tap(pid, 5.7 * w / WIDTH, (HEIGHT - 1.1) * h / HEIGHT)  # <= modify
    # 3. 点击看广告视频再赚金币
    input.tap(pid, w / 2, 8.4 * h / HEIGHT)
    # 4. 播放30s
    time.sleep(30)
    # 5. 返回上级界面
    # 是返回到任务页面
    phone.go_back(pid)

    # [x] 限时任务赚金币
    # 每20分钟完成一次广告
    # 1. 点击去领取
    input.tap(pid, (WIDTH - 1.3) * w / WIDTH, 7.4 * h / HEIGHT)
    # 2. 播放30s
    time.sleep(30)
    # 3. 返回上级页面
    # 是返回到任务页面
    phone.go_back(pid)

    # 关闭抖音
    phone.stop_app(pid, packages['douyin'])


# noinspection PyUnusedLocal
def huoshan(pid, w, h):
    # 打开火山
    checkin.huoshan(pid)

    # [x] 开宝箱
    # 每20分钟一次
    # 1. 点击红包
    input.tap(pid, 4.3 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)
    # 2. 点击开宝箱得金币
    input.tap(pid, (WIDTH - 1.0) * w / WIDTH, (HEIGHT - 2.1) * h / HEIGHT)
    # 3. 点击看视频金币翻倍按钮
    input.tap(pid, w / 2, 9.4 * h / HEIGHT)
    # 4. 播放30s
    time.sleep(30)
    # 5. 返回上级页面
    # 是返回到任务页面
    phone.go_back(pid)

    # 关闭火山
    phone.stop_app(pid, packages['huoshan'])


# noinspection PyUnusedLocal
def jingdong(pid, w, h):
    return None


# noinspection PyUnusedLocal
def fanqie(pid, w, h):
    # 打开番茄
    checkin.fanqie(pid, w, h)

    # [x] 开宝箱
    # 1. 点击中间下方的福利
    input.tap(pid, w / 2, (HEIGHT - 0.5) * h / HEIGHT)
    # 2. 点击开宝箱得金币
    input.tap(pid, (WIDTH - 1.0) * w / WIDTH, (HEIGHT - 2.3) * h / HEIGHT)
    # 3. 点击看视频在领金币
    input.tap(pid, w / 2, 8.7 * h / HEIGHT)
    # 4. 播放30s
    time.sleep(30)
    # 5. 返回上级页面
    # 无法通过回退返回
    # 返回到福利页面
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)

    # 关闭番茄
    phone.stop_app(pid, packages['fanqie'])


# noinspection PyUnusedLocal
def fanchang(pid, w, h):
    # 打开番茄畅听
    checkin.fanchang(pid, w, h)

    # [x] 开宝箱
    # 1. 点击下方的福利
    input.tap(pid, 4.8 * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT)
    # 2. 点击开宝箱得金币
    input.tap(pid, (WIDTH - 1.0) * w / WIDTH, (HEIGHT - 2.1) * h / HEIGHT)
    # 3. 点击看视频再领金币
    input.tap(pid, w / 2, 9.9 * h / HEIGHT)
    # 4. 播放30s
    time.sleep(30)
    # 5. 返回上级页面
    # 无法通过回退返回
    # 返回到福利页面
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)

    # 关闭番茄畅听
    phone.stop_app(pid, packages['fanchang'])


# noinspection PyUnusedLocal
def weishi(pid, w, h):
    return None


# noinspection PyUnusedLocal
def shuqi(pid, w, h):
    return None


# noinspection PyUnusedLocal
def yingke(pid, w, h):
    # 打开映客
    checkin.yingke(pid, w, h)

    # [x] 开宝箱领金币
    # 1. 点击下方的横幅
    input.tap(pid, w / 3, (HEIGHT - 1.8) * h / HEIGHT)
    # 2. 点击开宝箱领金币
    input.tap(pid, (WIDTH - 1.1) * w / WIDTH, 12.2 * h / HEIGHT)
    # 3. 播放视频60s
    time.sleep(60)
    # 4. 返回上级页面
    # 返回到福利页面
    phone.go_back(pid)

    # 关闭映客
    phone.stop_app(pid, packages['yingke'])


# noinspection PyUnusedLocal
def kugou(pid, w, h):
    return None


# noinspection PyUnusedLocal
def huitoutiao(pid, w, h):
    return None


# noinspection PyUnusedLocal
def zhongqing(pid, w, h):
    return None


# noinspection PyUnusedLocal
def pinduoduo(pid, w, h):
    return None


# noinspection PyUnusedLocal
def taobao(pid, w, h):
    return None


# noinspection PyUnusedLocal
def shuabao(pid, w, h):
    return None


# noinspection PyUnusedLocal
def qutoutiao(pid, w, h):
    return None


# noinspection PyUnusedLocal
def baidu(pid, w, h):
    return None


# noinspection PyUnusedLocal
def ximalaya(pid, w, h):
    return None
