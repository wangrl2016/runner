import time
from random import randrange

from src import input, phone, app, info, checkin
from src.info import WIDTH, HEIGHT


def midu(pid, w, h):
    # 1. 消除可能的悬浮窗
    phone.go_back(pid, gap=1)
    # 2. 进入福利页面
    app.midu_benefit_page(pid, w, h, gap=5)
    # 3. 点击立即签到
    # [x] 签到成功
    input.tap(pid, (WIDTH - 1.2) * w / WIDTH, 2.3 * h / HEIGHT, gap=2)


# noinspection PyUnusedLocal
def changdou(pid, w, h):
    # 可能存在悬浮窗
    phone.stop_app(pid, info.packages['changdou'])
    checkin.changdou(pid, w, h)
    app.changdou_benefit_page(pid, w, h, gap=5)
    # [x] 签到成功
    input.tap(pid, w / 2, 9.8 * h / HEIGHT, gap=3)


# noinspection PyUnusedLocal
def kulingyin(pid, w, h):
    phone.go_back(pid, gap=1)
    # 1. 进入福利页面
    app.kulingyin_benefit_page(pid, w, h)
    # 2. 点击签到
    # [x] 签到成功
    input.tap(pid, (WIDTH - 1.3) * w / WIDTH, 7.5 * h / HEIGHT, gap=12)


# noinspection PyUnusedLocal
def lanmao(pid, w, h):
    # 忽略悬浮窗
    # 如果没有悬浮窗会出现问题
    phone.go_back(pid, gap=1)
    # 1. 点击我的
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT, gap=3)
    # 2. 点击签到
    # TODO: 需要验证确认
    # [x] 签到成功
    input.tap(pid, (WIDTH - 0.8) * w / WIDTH, 1.4 * h / HEIGHT)


def jingdong(pid, w, h):
    phone.go_back(pid, gap=1)
    # 1. 点击中间的现金签到
    input.tap(pid, w / 2, 7.6 * h / HEIGHT, gap=3)  # <=== modify
    # 2. 点击立即签到
    # [x] 签到成功
    input.tap(pid, w / 2, 5.8 * h / HEIGHT, gap=2)  # <= modify


def fanqie(pid, w, h):
    # 1. 假装退出关闭可能存在的悬浮窗
    phone.go_back(pid, gap=1)
    # 2. 点击中间下方福利签到
    # [x] 签到成功
    app.fanqie_benefit_page(pid, w, h, gap=5)


def fanchang(pid, w, h):
    phone.go_back(pid, gap=1)
    # 1. 进入福利页面
    # [x] 签到成功
    app.fanchang_benefit_page(pid, w, h)


# noinspection PyUnusedLocal
def kuchang(pid, w, h):
    # [x] 签到成功
    return None


def shuqi(pid, w, h):
    # 后退会弹出提示框
    # 不后退有时会有广告悬浮窗
    phone.stop_app(pid, info.packages['shuqi'])
    checkin.shuqi(pid, w, h)
    # [x] 签到成功
    app.shuqi_benefit_page(pid, w, h)


def yingke(pid, w, h):
    # 1. 假装退出解决可能出现的悬浮窗问题
    # 2. 可能出现两次
    phone.go_back(pid, times=2)
    # 2. 点击下方红包
    app.yingke_benefit_page(pid, w, h)
    # 3. 点击立即签到
    input.tap(pid, w / 2, 10.4 * h / HEIGHT, gap=10)  # <=== modify
    # 4. 播放30s广告
    # [x] 签到成功
    time.sleep(30)


def kugou(pid, w, h):
    phone.go_back(pid, gap=1)
    # 1. 点击右下角赚钱
    app.kugou_benefit_page(pid, w, h)
    # 2. 点击每日签到栏
    # [x] 签到成功
    input.tap(pid, (WIDTH - 1.0) * w / WIDTH, (HEIGHT - 3.1) * h / HEIGHT, gap=2)  # <=== modify
    # 3. 返回到赚钱页面
    phone.go_back(pid, gap=1)


def qukan(pid, w, h):
    # 1. 直接点击中间的悬浮框
    input.tap(pid, w / 2, h / 2)
    # 2. 点击签到
    # [x] 签到成功
    input.tap(pid, w / 2, 5.8 * h / HEIGHT, gap=2)


def zhongqing(pid, w, h):
    # 1. 假装想要退出关闭可能的悬浮窗
    phone.go_back(pid)
    # 2. 点击任务待签到
    app.zhongqing_benefit_page(pid, w, h)
    phone.go_back(pid, gap=1)
    # 3. 点击签到领现金
    # [x] 签到成功
    input.tap(pid, w / 2, 4.9 * h / HEIGHT, gap=3)  # <= modify


def pinduoduo(pid, w, h):
    # 1. 回退消除可能出现的悬浮窗
    phone.go_back(pid)
    # 2. 点击中间的现金签到
    input.tap(pid, w / 2, 5.5 * h / HEIGHT)  # <= modify
    # 3. 点击签到领现金
    # [x] 签到成功
    input.tap(pid, w / 2, 3.0 * h / HEIGHT, gap=2)  # <= modify
    # 3. 返回到程序主页
    phone.go_back(pid, gap=1)


# noinspection PyUnusedLocal
def kuaiyin(pid, w, h):
    # 进入福利页面
    # [x] 签到成功
    app.kuaiyin_benefit_page(pid, w, h)


# noinspection PyUnusedLocal
def quhongbao(pid, w, h):
    phone.stop_app(pid, info.packages['quhongbao'])
    checkin.quhongbao(pid, w, h)
    # [x] 签到成功
    app.quhongbao_benefit_page(pid, w, h, gap=5)
    # 签到翻倍
    input.tap(pid, w / 2, 7.7 * h / HEIGHT, gap=10)
    # 播放30s
    time.sleep(30)


def jukandian(pid, w, h):
    time.sleep(3)
    # [x] 签到成功
    input.tap(pid, (WIDTH - 1.7) * w / WIDTH, 6.0 * h / HEIGHT, gap=2)


# noinspection PyUnusedLocal
def miaokan(pid, w, h):
    app.miaokan_benefit_page(pid, w, h)
    # 点击签到
    # [x] 签到成功
    input.tap(pid, (WIDTH - 1.3) * w / WIDTH, 4.6 * h / HEIGHT, gap=2)


def kuge(pid, w, h):
    phone.go_back(pid, gap=1)
    # 1. 点击右上方赚钱
    input.tap(pid, 4.8 * w / WIDTH, 1.2 * h / HEIGHT, gap=10)
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
    input.tap(pid, 0.8 * w / WIDTH, 1.0 * h / HEIGHT, gap=2)  # <= modify


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
    # 1. 解决弹出青少年模式悬浮窗的问题
    for i in range(0, 6):
        phone.swipe_down_to_up(pid, w / 2, h, randrange(4, 9))
        phone.go_back(pid, gap=1)
    # 2. 进入快手福利页面
    app.kuaishou_benefit_page(pid, w, h)
    # 3. 显示签到页面点击立即签到
    # [x] 签到成功
    input.tap(pid, w / 2, 10.4 * h / HEIGHT)  # <=== modify
    # 4. 回退到播放界面
    phone.go_back(pid)


def douyin(pid, w, h):
    # 1. 解决弹出青少年模式悬浮窗的问题
    for i in range(0, 6):
        phone.swipe_down_to_up(pid, w / 2, h, randrange(4, 9))
        phone.go_back(pid, gap=1)
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
    # 1. 解决弹出青少年模式悬浮窗的问题
    for i in range(0, 6):
        phone.swipe_down_to_up(pid, w / 2, h, randrange(4, 9))
        phone.go_back(pid, gap=1)
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


def baidu(pid, w, h):
    # 1. 点击右下方去签到
    app.baidu_benefit_page(pid, w, h)
    # 2. 回退悬浮窗然签到界面显示
    # [x] 签到成功
    phone.go_back(pid, gap=2)


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
    # 2. 看视频
    input.tap(pid, w / 2, 8.3 * h / HEIGHT, gap=10)
    # 3. 返回到签到页面
    # [x] 签到成功
    phone.go_back(pid)


# noinspection PyUnusedLocal
def taobao(pid, w, h):
    # 1. 消除可能存在的悬浮窗
    phone.go_back(pid)
    # 2. 点击签到
    input.tap(pid, 0.7 * w / WIDTH, 2.6 * h / HEIGHT)
    # 3. 点击视频
    input.tap(pid, w / 2, 6.7 * h / HEIGHT)
    # 4. 播放30s
    # [x] 签到成功
    time.sleep(30)


def shuabao(pid, w, h):
    # 1. 刷宝福利页面
    app.shuabao_benefit_page(pid, w, h)
    # 2.点击签到
    input.tap(pid, (WIDTH - 1.0) * w / WIDTH, 3.4 * h / HEIGHT, gap=3)
    # 3. 看视频签到
    input.tap(pid, w * 2 / 3, 9.5 * h / HEIGHT)
    # 4. 播放30s
    time.sleep(30)
    # 5. 返回到福利页面
    # [x] 签到成功
    input.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)


# noinspection PyUnusedLocal
def qqyuedu(pid, w, h):
    # [x] 签到成功
    app.qqyuedu_benefit_page(pid, w, h, gap=5)


def chejia(pid, w, h):
    # [x] 签到成功
    app.chejia_benefit_page(pid, w, h)


# noinspection PyUnusedLocal
def uc(pid, w, h):
    # 没有签到
    return None


# noinspection PyUnusedLocal
def kuaikandian(pid, w, h):
    # 1. 进入福利页面
    # [x] 签到成功
    app.kuaikandian_benefit_page(pid, w, h)
    # 2. 看视频再领金币
    input.tap(pid, w / 2, 9.8 * h / HEIGHT)
    # 3. 播放30s
    time.sleep(30)


# noinspection PyUnusedLocal
def hongshi(pid, w, h):
    # 没有签到
    return None


# noinspection PyUnusedLocal
def doudou(pid, w, h):
    app.doudou_benefit_page(pid, w, h)
    for i in range(0, 7):
        # [x] 签到成功
        input.tap(pid, (0.8 + i * 0.9) * w / WIDTH, 3.4 * h / HEIGHT, gap=0.5)


# noinspection PyUnusedLocal
def qimao(pid, w, h):
    input.tap(pid, (WIDTH - 1.1) * w / WIDTH, 2.9 * h / HEIGHT, gap=2)
    return None


# noinspection PyUnusedLocal
def kankuai(pid, w, h):
    # 进入福利中心
    app.kankuai_benefit_page(pid, w, h)
    # 点击立即签到
    # [x] 签到成功
    input.tap(pid, w / 2, 8.5 * h / HEIGHT, gap=2)


def douhuo(pid, w, h):
    # 1. 假装回退关闭可能的悬浮窗
    time.sleep(5)
    phone.go_back(pid, gap=1)
    # 2. 点击个人中心图标
    input.tap(pid, 0.5 * w / WIDTH, 0.9 * h / HEIGHT, gap=3)
    # 3. 点击火苗管理
    # [x] 签到成功
    input.tap(pid, w / 2, 7.9 * h / HEIGHT, gap=2)


# noinspection PyUnusedLocal
def moji(pid, w, h):
    # [x] 签到成功
    app.moji_benefit_page(pid, w, h)


# noinspection PyUnusedLocal
def tangdou(pid, w, h):
    # 1. 进入福利页面
    app.tangdou_benefit_page(pid, w, h)
    # 2. 点击签到领现金
    # [x] 签到成功
    input.tap(pid, w / 2, 5.8 * h / HEIGHT, gap=3)
    # 3. 看视频
    input.tap(pid, w / 2, 10.6 * h / HEIGHT, gap=10)
    # 4. 播放30s
    time.sleep(30)


# noinspection PyUnusedLocal
def yangcong(pid, w, h):
    # [x] 签到成功
    app.yangcong_benefit_page(pid, w, h)


# 49 - 72


# noinspection PyUnusedLocal
def sougou(pid, w, h):
    app.sougou_benefit_page(pid, w, h)
    for i in range(0, 4):
        input.tap(pid, (1.2 + i * 1.5) * w / WIDTH, 3.5 * h / HEIGHT, gap=1)
    for i in range(0, 3):
        input.tap(pid, (1.2 + i * 1.5) * w / WIDTH, 5.5 * h / HEIGHT, gap=1)


# noinspection PyUnusedLocal
def zhuanshi(pid, w, h):
    # 没有签到
    return None


# noinspection PyUnusedLocal
def qizhu(pid, w, h):
    return None


# noinspection PyUnusedLocal
def weixin(pid, w, h):
    return None
