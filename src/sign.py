import time
from random import randrange

from src import phone, app, info, checkin
from src.info import WIDTH, HEIGHT


def midu(pid, w, h):
    # 1. 消除可能的悬浮窗
    phone.go_back(pid)
    # 2. 进入福利页面
    app.midu_benefit_page(pid, w, h, gap=5)
    # 3. TODO: 点击立即签到
    # [x] 签到成功
    phone.tap(pid, (WIDTH - 1.2) * w / WIDTH, 1.2 * h / HEIGHT)
    # 4. 看视频领金币
    phone.tap(pid, w / 2, 7.5 * h / HEIGHT, gap=10)
    # 5. 播放30s
    time.sleep(30)
    # 6. 返回到福利页面
    phone.go_back(pid, times=2, gap=1)


# noinspection PyUnusedLocal
def changdou(pid, w, h):
    # 消除可能的悬浮窗
    phone.go_back(pid)
    app.changdou_benefit_page(pid, w, h, gap=5)
    # [x] 签到成功
    phone.tap(pid, w / 2, 9.8 * h / HEIGHT, gap=3)


# noinspection PyUnusedLocal
def lanmao(pid, w, h):
    # 忽略悬浮窗
    # 如果没有悬浮窗会出现问题
    phone.go_back(pid, gap=1)
    # 1. 点击我的
    phone.tap(pid, (WIDTH - 0.7) * w / WIDTH, (HEIGHT - 0.5) * h / HEIGHT, gap=3)
    # 2. 点击签到
    # TODO: 需要验证确认
    # [x] 签到成功
    phone.tap(pid, (WIDTH - 0.8) * w / WIDTH, 1.4 * h / HEIGHT)


def jingdong(pid, w, h):
    phone.go_back(pid, gap=1)
    # 1. 点击中间的现金签到
    phone.tap(pid, w / 2, 7.6 * h / HEIGHT, gap=3)  # <=== modify
    # 2. 点击立即签到
    # [x] 签到成功
    phone.tap(pid, w / 2, 5.8 * h / HEIGHT, gap=2)  # <= modify


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
    app.fanchang_benefit_page(pid, w, h, gap=5)


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
    phone.tap(pid, w / 2, 10.4 * h / HEIGHT, gap=10)  # <=== modify
    # 4. 播放30s广告
    # [x] 签到成功
    time.sleep(30)


def kugou(pid, w, h):
    phone.go_back(pid, gap=1)
    # 1. 点击右下角赚钱
    app.kugou_benefit_page(pid, w, h)
    # 2. 点击每日签到栏
    # [x] 签到成功
    phone.tap(pid, (WIDTH - 1.0) * w / WIDTH, (HEIGHT - 3.1) * h / HEIGHT, gap=2)  # <=== modify
    # 3. 返回到赚钱页面
    phone.go_back(pid, gap=1)


def qukan(pid, w, h):
    # 1. 直接点击中间的悬浮框
    phone.tap(pid, w / 2, h / 2, gap=3)
    # 2. 返回退出悬浮窗
    phone.go_back(pid)
    app.qukan_benefit_page(pid, w, h)
    # 3. 点击签到
    # [x] 签到成功
    phone.tap(pid, w / 2, 4.9 * h / HEIGHT, gap=2)


def zhongqing(pid, w, h):
    # 1. 假装想要退出关闭可能的悬浮窗
    phone.go_back(pid)
    # 2. 点击任务待签到
    app.zhongqing_benefit_page(pid, w, h)
    phone.go_back(pid, gap=1)
    # 3. 点击签到领现金
    # [x] 签到成功
    phone.tap(pid, w / 2, 4.9 * h / HEIGHT, gap=3)  # <= modify


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


def jukandian(pid, w, h):
    # 进入文章详情
    phone.tap(pid, w * 2 / 3, 8.8 * h / HEIGHT, gap=3)
    # 退出
    phone.go_back(pid)
    # [x] 签到成功
    phone.tap(pid, (WIDTH - 1.7) * w / WIDTH, 6.0 * h / HEIGHT, gap=2)


def kuge(pid, w, h):
    phone.go_back(pid, gap=1)
    # 1. 点击右上方赚钱
    phone.tap(pid, 4.8 * w / WIDTH, 1.2 * h / HEIGHT, gap=10)
    # 点击签到
    # 位置未知
    # [x] 签到成功
    for i in range(0, 7):
        phone.tap(pid, (1.0 + 0.8 * i) * w / WIDTH, 6.9 * h / HEIGHT, gap=(3 if (i == 6) else 1))


def makan(pid, w, h):
    # 1. 回退关闭可能的悬浮窗
    phone.go_back(pid, gap=1)
    # 2. 点击任务
    # [x] 签到成功
    app.makan_benefit_page(pid, w, h)
    # 3. 返回到主页
    phone.go_back(pid)
    # 4. 获取时段奖励
    phone.tap(pid, 0.8 * w / WIDTH, 1.0 * h / HEIGHT, gap=2)  # <= modify


# noinspection PyUnusedLocal
def diandian(pid, w, h):
    # 1. 回退关闭可能的悬浮窗
    phone.go_back(pid, gap=1)
    # 2. 点击任务
    # [x] 签到成功
    app.diandian_benefit_page(pid, w, h)


# noinspection PyUnusedLocal
def tengtu(pid, w, h):
    # 1. 点击活动专区
    phone.tap(pid, w / 2, (HEIGHT - 2.8) * h / HEIGHT)
    # 2. 点击天天领现金
    phone.tap(pid, w / 2, h / 5)
    # 3. 马上签到领现金
    # TODO
    phone.tap(pid, w / 2, 9.0 * h / HEIGHT, gap=3)


# noinspection PyUnusedLocal
def momo(pid, w, h):
    # 1. 点击红包
    phone.tap(pid, (WIDTH - 0.8) * w / WIDTH, (HEIGHT - 2.4) * h / HEIGHT, gap=8)
    # 2. 点击签到
    # [x] 签到成功
    phone.tap(pid, w / 2, 9.1 * h / HEIGHT, gap=3)


# noinspection PyUnusedLocal
def jitou(pid, w, h):
    app.jitou_benefit_page(pid, w, h)
    # [x] 签到成功
    phone.tap(pid, 5.1 * w / WIDTH, 5.8 * h / HEIGHT, gap=3)


# noinspection PyUnusedLocal
def sanliuling(pid, w, h):
    return None


# noinspection PyUnusedLocal
def yunshanfu(pid, w, h):
    # 1. 点击签到
    phone.tap(pid, (WIDTH - 0.5) * w / WIDTH, 11.4 * h / HEIGHT)
    # 2. 点击签到
    # [x] 云闪付签到
    phone.tap(pid, w / 2, 11.0 * h / HEIGHT, gap=2)


# noinspection PyUnusedLocal
def shengqian(pid, w, h):
    return None


# noinspection PyUnusedLocal
def qingtuanshe(pid, w, h):
    return None


# noinspection PyUnusedLocal
def aijian(pid, w, h):
    return None


# noinspection PyUnusedLocal
def eleme(pid, w, h):
    return None


# noinspection PyUnusedLocal
def zhebabai(pid, w, h):
    return None


# noinspection PyUnusedLocal
def rong(pid, w, h):
    return None


def toutiao(pid, w, h):
    # 1. 点击右下方任务栏目
    # 显示签到界面
    # [x] 签到成功
    app.toutiao_benefit_page(pid, w, h)
    # 2. 点击看视频再领金币
    phone.tap(pid, w / 2, 9.1 * h / HEIGHT)  # <== modify
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
    phone.tap(pid, w / 2, 10.4 * h / HEIGHT)  # <=== modify
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
        phone.tap(pid, w / 2, 9.7 * h / HEIGHT)  # <=== modify
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
    phone.tap(pid, w / 2, 9.5 * h / HEIGHT)
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
    app.wuba_benefit_page(pid, w, h, gap=5)
    # 2. 看视频
    phone.tap(pid, w / 2, 8.3 * h / HEIGHT, gap=8)
    # 3. 返回到签到页面
    # [x] 签到成功
    phone.go_back(pid)


# noinspection PyUnusedLocal
def taobao(pid, w, h):
    # 1. 消除可能存在的悬浮窗
    phone.go_back(pid)
    # 2. 点击签到
    # [x] 签到成功
    phone.tap(pid, 0.7 * w / WIDTH, 2.6 * h / HEIGHT, gap=3)


def shuabao(pid, w, h):
    # 1. 刷宝福利页面
    app.shuabao_benefit_page(pid, w, h)
    # 2.点击签到
    phone.tap(pid, (WIDTH - 1.0) * w / WIDTH, 3.4 * h / HEIGHT, gap=3)
    # 3. 看视频签到
    phone.tap(pid, w * 2 / 3, 9.5 * h / HEIGHT)
    # 4. 播放30s
    time.sleep(30)
    # 5. 返回到福利页面
    # [x] 签到成功
    phone.tap(pid, (WIDTH - 0.7) * w / WIDTH, 1.2 * h / HEIGHT)


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
    app.kuaikandian_benefit_page(pid, w, h, gap=5)
    # 2. 看视频再领金币
    phone.tap(pid, w / 2, 9.8 * h / HEIGHT)
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
        phone.tap(pid, (0.8 + i * 0.9) * w / WIDTH, 3.4 * h / HEIGHT, gap=0.5)


# noinspection PyUnusedLocal
def qimao(pid, w, h):
    # [x] 签到成功
    phone.tap(pid, (WIDTH - 1.1) * w / WIDTH, 2.9 * h / HEIGHT, gap=2)


def douhuo(pid, w, h):
    # 1. 假装回退关闭可能的悬浮窗
    time.sleep(5)
    phone.go_back(pid, gap=1)
    # 2. 点击个人中心图标
    phone.tap(pid, 0.5 * w / WIDTH, 0.9 * h / HEIGHT, gap=3)
    # 3. 点击火苗管理
    # [x] 签到成功
    phone.tap(pid, w / 2, 7.9 * h / HEIGHT)


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
    phone.tap(pid, w / 2, 5.8 * h / HEIGHT, gap=3)
    # 3. 看视频
    phone.tap(pid, w / 2, 10.6 * h / HEIGHT, gap=10)
    # 4. 播放30s
    time.sleep(30)


# noinspection PyUnusedLocal
def yangcong(pid, w, h):
    # [x] 签到成功
    app.yangcong_benefit_page(pid, w, h, gap=5)


# 73-96


# noinspection PyUnusedLocal
def qqliulan(pid, w, h):
    app.qqliulan_benefit_page(pid, w, h)
    # 点击福利中心
    # [x] 签到成功
    phone.tap(pid, w / 3, h * 11 / 14)
    return None


# noinspection PyUnusedLocal
def lingshenghui(pid, w, h):
    app.lingshenghui_benefit_page(pid, w, h)


# noinspection PyUnusedLocal
def zhuanshi(pid, w, h):
    return None


# noinspection PyUnusedLocal
def tengzhi(pid, w, h):
    phone.tap(pid, (WIDTH - 0.6) * w / WIDTH, h / 2)
    return None


# noinspection PyUnusedLocal
def zhaoshang(pid, w, h):
    return None


# noinspection PyUnusedLocal
def gudong(pid, w, h):
    return None


# noinspection PyUnusedLocal
def xiongmao(pid, w, h):
    return None


# noinspection PyUnusedLocal
def buduoduo(pid, w, h):
    return None


# noinspection PyUnusedLocal
def duokan(pid, w, h):
    return None


# noinspection PyUnusedLocal
def shandian(pid, w, h):
    return None


# noinspection PyUnusedLocal
def taozhi(pid, w, h):
    return None


# noinspection PyUnusedLocal
def cainiao(pid, w, h):
    return None


# noinspection PyUnusedLocal
def weixin(pid, w, h):
    return None
