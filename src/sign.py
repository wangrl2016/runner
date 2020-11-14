import time

from src import input, phone, app
from src.info import WIDTH, HEIGHT


def midu(pid, w, h):
    # 1. 消除可能的悬浮窗
    phone.go_back(pid, gap=1)
    # 2. 进入福利页面
    app.midu_benefit_page(pid, w, h)
    # 3. 点击立即签到
    # [x] 签到成功
    input.tap(pid, (WIDTH - 1.2) * w / WIDTH, 1.3 * h / HEIGHT)


# noinspection PyUnusedLocal
def lanmao(pid, w, h):
    # [x] 签到成功
    return None


def jingdong(pid, w, h):
    # 1. 点击中间的现金签到
    input.tap(pid, w / 2, 7.6 * h / HEIGHT, gap=3)  # <=== modify
    # 2. 点击立即签到
    # [x] 签到成功
    input.tap(pid, w / 2, 5.8 * h / HEIGHT, gap=3)  # <= modify


def fanqie(pid, w, h):
    # 1. 假装退出关闭可能存在的悬浮窗
    phone.go_back(pid, gap=1)
    # 2. 点击中间下方福利签到
    # [x] 签到成功
    app.fanqie_benefit_page(pid, w, h)
    # 3. 点击看视频再领金币
    input.tap(pid, w / 2, 10.1 * h / HEIGHT)  # <== modify
    # 4. 播放视频30s
    time.sleep(30)
    # 5. 点击关闭回退到福利页面
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT, gap=2)  # <== modify


def fanchang(pid, w, h):
    # 1. 进入福利页面
    # [x] 签到成功
    app.fanchang_benefit_page(pid, w, h)
    # 2. 点击看视频再领金币
    input.tap(pid, w / 2, 10.0 * h / HEIGHT)  # <= modify
    # 3. 播放视频30s
    time.sleep(30)
    # 4. 点击关闭回退到福利页面
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT, gap=2)  # <== modify


# noinspection PyUnusedLocal
def kuchang(pid, w, h):
    # [x] 签到成功
    return None


def shuqi(pid, w, h):
    # 后退会弹出提示框
    # 不后退有时会有广告悬浮窗
    # [x] 签到成功
    app.shuqi_benefit_page(pid, w, h, gap=5)


def yingke(pid, w, h):
    # 1. 假装退出解决可能出现的悬浮窗问题
    # 2. 可能出现两次
    phone.go_back(pid, times=2)
    # 2. 点击下方红包
    app.yingke_benefit_page(pid, w, h)
    # 3. 点击立即签到
    input.tap(pid, w / 2, 10.4 * h / HEIGHT)  # <=== modify
    # 4. 播放30s广告
    # [x] 签到成功
    time.sleep(30)


def kugou(pid, w, h):
    # 1. 点击右下角赚钱
    app.kugou_benefit_page(pid, w, h)
    # 2. 点击每日签到栏
    # [x] 签到成功
    input.tap(pid, (WIDTH - 1.0) * w / WIDTH, (HEIGHT - 3.4) * h / HEIGHT, gap=3)  # <== modify
    # 3. 返回到赚钱页面
    phone.go_back(pid, gap=1)


def zhongqing(pid, w, h):
    # 1. 假装想要退出关闭可能的悬浮窗
    phone.go_back(pid)
    # 2. 点击任务待签到
    app.zhongqing_benefit_page(pid, w, h)
    phone.go_back(pid)
    # 3. 点击签到领现金
    # [x] 签到成功
    input.tap(pid, w / 2, 4.9 * h / HEIGHT)  # <= modify
    # 4. 回退到福利页面
    phone.go_back(pid, gap=1)


def pinduoduo(pid, w, h):
    # 1. 回退消除可能出现的悬浮窗
    phone.go_back(pid)
    # 2. 点击中间的现金签到
    input.tap(pid, w / 2, 5.5 * h / HEIGHT)  # <= modify
    # 3. 点击签到领现金
    # [x] 签到成功
    input.tap(pid, w / 2, 3.0 * h / HEIGHT)  # <= modify
    # 3. 返回到程序主页
    phone.go_back(pid, gap=1)


# noinspection PyUnusedLocal
def kuaiyin(pid, w, h):
    # 进入福利页面
    # [x] 签到成功
    app.kuaiyin_benefit_page(pid, w, h)


# noinspection PyUnusedLocal
def quhongbao(pid, w, h):
    # 进入福利页面
    # [x] 签到成功
    app.quhongbao_benefit_page(pid, w, h)


# noinspection PyUnusedLocal
def dongfang(pid, w, h):
    phone.go_back(pid)
    app.dongfang_benefit_page(pid, w, h)
    # [x] 签到成功
    input.tap(pid, w / 2, 3.7 * h / HEIGHT)


def jukandian(pid, w, h):
    # [x] 签到成功
    input.tap(pid, (WIDTH - 1.7) * w / WIDTH, 6.0 * h / HEIGHT, gap=2)


def kuge(pid, w, h):
    # 1. 点击右上方赚钱
    input.tap(pid, 4.8 * w / WIDTH, 1.2 * h / HEIGHT)
    # 点击签到
    # 位置未知
    # [x] 签到成功
    for i in range(0, 7):
        input.tap(pid, (1.0 + 0.8 * i) * w / WIDTH, 6.9 * h / HEIGHT, gap=1)


def makan(pid, w, h):
    # 1. 回退关闭可能的悬浮窗
    phone.go_back(pid, gap=1)
    # 2. 点击任务
    # [x] 签到成功
    app.makan_benefit_page(pid, w, h)
    # 3. 返回到主页
    phone.go_back(pid)
    # 4. 获取时段奖励
    input.tap(pid, 0.8 * w / WIDTH, 1.0 * h / HEIGHT)  # <= modify


# noinspection PyUnusedLocal
def diandian(pid, w, h):
    # 1. 回退关闭可能的悬浮窗
    phone.go_back(pid, gap=1)
    # 2. 点击任务
    # [x] 签到成功
    app.diandian_benefit_page(pid, w, h)


# 25-28

def toutiao(pid, w, h):
    # 1. 点击右下方任务栏目
    # 显示签到界面
    # [x] 签到成功
    app.toutiao_benefit_page(pid, w, h)
    # 2. 点击看视频再领金币
    input.tap(pid, w / 2, 9.1 * h / HEIGHT)  # <== modify
    # 3. 播放15s
    time.sleep(15)
    # 4. 返回到任务页面
    phone.go_back(pid, gap=1)


def kuaishou(pid, w, h):
    # 1. 假装后退解决弹出青少年模式悬浮窗的问题
    phone.go_back(pid)
    # 2. 进入快手福利页面
    app.kuaishou_benefit_page(pid, w, h)
    # 3. 显示签到页面点击立即签到
    # [x] 签到成功
    input.tap(pid, w / 2, 10.4 * h / HEIGHT)  # <=== modify
    # 4. 回退到播放界面
    phone.go_back(pid)


def douyin(pid, w, h):
    # 1. 假装退出解决弹出的青少年模式悬浮窗问题
    phone.go_back(pid)
    # 2. 点击下方的福袋
    # 等待10s签到界面出现
    app.douyin_benefit_page(pid, w, h, gap=10)
    # 3. 点击立即签到领金币
    # 4. 看视频再赚金币
    # [x] 签到成功
    for i in range(0, 2):
        input.tap(pid, w / 2, 9.7 * h / HEIGHT)  # <=== modify
    # 5. 播放30s
    time.sleep(30)
    # 6. 退出到播放页面
    phone.go_back(pid, gap=1)


def huoshan(pid, w, h):
    # 1. 假装想要退出解决弹出青少年模式悬浮窗的问题
    phone.go_back(pid)
    # 2. 进入福利页面
    # [x] 签到成功
    app.huoshan_benefit_page(pid, w, h)
    # 3. 看广告再领金币
    input.tap(pid, w / 2, 9.5 * h / HEIGHT)
    # 4. 播放30s
    time.sleep(30)
    # 5. 返回到福利页面
    phone.go_back(pid)


def qutoutiao(pid, w, h):
    # 1. 点击右下方任务
    # [x] 签到成功
    app.qutoutiao_benefit_page(pid, w, h)
    # 2. 点击看视频再领金币
    input.tap(pid, w / 2, 6.8 * h / HEIGHT, gap=8)
    # 3. 播放40s
    # TODO: 播放时长
    time.sleep(40)
    # 4. 回退到未知页面
    phone.go_back(pid, gap=1)


def baidu(pid, w, h):
    # 1. 点击右下方去签到
    # [x] 签到成功
    app.baidu_benefit_page(pid, w, h)


# noinspection PyUnusedLocal
def weishi(pid, w, h):
    return None


def ximalaya(pid, w, h):
    # 1. 点击右下方福利
    # [x] 签到成功
    app.ximalaya_benefit_page(pid, w, h)


def wuba(pid, w, h):
    # 1. 点击福利页面
    app.wuba_benefit_page(pid, w, h)
    # 2. 分享到朋友圈
    input.tap(pid, w / 2, 8.3 * h / HEIGHT, gap=10)
    # 3. 返回到主页
    # [x] 签到成功
    phone.go_back(pid, gap=1)


# noinspection PyUnusedLocal
def taobao(pid, w, h):
    # 有现金红包
    return None


# noinspection PyUnusedLocal
def shuabao(pid, w, h):
    return None


def huitoutiao(pid, w, h):
    # 1. 假装想要退出关闭可能的悬浮窗
    phone.go_back(pid)
    # 2. 进入福利页面
    app.huitoutiao_benefit_page(pid, w, h)
    # 3. 点击今日签到
    # [x] 签到成功
    input.tap(pid, w / 2, 2.4 * h / HEIGHT, gap=2)  # <= modify


def chejia(pid, w, h):
    # [x] 签到成功
    app.chejia_benefit_page(pid, w, h)


# noinspection PyUnusedLocal
def uc(pid, w, h):
    # 没有签到
    return None


# noinspection PyUnusedLocal
def hongshi(pid, w, h):
    return None


# noinspection PyUnusedLocal
def doudou(pid, w, h):
    app.doudou_benefit_page(pid, w, h)
    for i in range(0, 7):
        # [x] 签到成功
        input.tap(pid, (0.8 + i * 0.9) * w / WIDTH, 3.4 * h / HEIGHT, gap=0.5)


# noinspection PyUnusedLocal
def kankuai(pid, w, h):
    # 进入福利中心
    app.kankuai_benefit_page(pid, w, h)
    # 点击立即签到
    # [x] 签到成功
    input.tap(pid, w / 2, 8.5 * h / HEIGHT, gap=2)


def douhuo(pid, w, h):
    # 1. 假装回退关闭可能的悬浮窗
    phone.go_back(pid, times=1, gap=1)
    # 2. 点击个人中心图标
    input.tap(pid, 0.5 * w / WIDTH, 0.9 * h / HEIGHT)
    # 3. 点击火苗管理
    # [x] 签到成功
    input.tap(pid, w / 2, 7.9 * h / HEIGHT)


# noinspection PyUnusedLocal
def moji(pid, w, h):
    # [x] 签到成功
    app.moji_benefit_page(pid, w, h)


# noinspection PyUnusedLocal
def ersansi(pid, w, h):
    phone.go_back(pid)
    app.ersansi_benefit_page(pid, w, h)
    # 点击签到
    # [x] 签到成功
    input.tap(pid, (WIDTH - 1.2) * w / WIDTH, 3.0 * h / HEIGHT)


# noinspection PyUnusedLocal
def tangdou(pid, w, h):
    # 1. 进入福利页面
    app.tangdou_benefit_page(pid, w, h)
    # 2. 点击签到领现金
    # [x] 签到成功
    input.tap(pid, w / 2, 5.8 * h / HEIGHT, gap=3)
    # 3. 看视频
    input.tap(pid, w / 2, 9.6 * h / HEIGHT)
    # 4. 播放30s
    time.sleep(30)


# noinspection PyUnusedLocal
def weixin(pid, w, h):
    return None
