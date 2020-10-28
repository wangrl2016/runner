#!/usr/bin/env python3

import argparse
import os
import signal
import sys
import threading
from datetime import datetime

from src import phone, checkin, sign, app, utils
from src.info import packages, apps, high_serials
from src.utils import tap_start, schedule_apps

MAX_PHOTOS_STORE = 50


def cycle(pid):
    # 需要保持手机处于亮屏状态
    # 不能有密码
    # 手机初始化工作
    # 获取手机的大小
    (w, h) = phone.get_size(pid)
    # 滑动手机打开屏幕
    phone.swipe_down_to_up(pid, w, h)
    # 回到手机主页面
    phone.go_home(pid)

    # 检测有哪些程序可以在手机上运行
    phone_packages = phone.list_packages(pid)
    run_apps = []
    for p in packages:
        if phone_packages.__contains__(packages[p]):
            run_apps.append(p)

    while True:
        hour = datetime.now().hour
        while run_apps.__contains__('kuaishou') and datetime.now().hour.__eq__(hour):
            # [x] 看快手视频
            app.full_watch_kuaishou_video(pid, w, h, hour)

        hour = datetime.now().hour
        while run_apps.__contains__('douyin') and datetime.now().hour.__eq__(hour):
            # [x] 看抖音视频
            app.full_watch_kuaishou_video(pid, w, h, hour)

        hour = datetime.now().hour
        while run_apps.__contains__('huoshan') and datetime.now().hour.__eq__(hour):
            # [x] 看火山视频
            app.full_watch_huoshan_video(pid, w, h, hour)

        hour = datetime.now().hour
        while run_apps.__contains__('weishi') and datetime.now().hour.__eq__(hour):
            # [x] 看微视视频
            app.full_watch_weishi_video(pid, w, h, hour)


def run(pid):
    # 需要保持手机处于亮屏状态
    # 不能有密码
    # 手机初始化工作

    # 获取手机的属性
    properties = phone.get_device_properties(pid)
    for p in properties:
        if p.__contains__('ro.product.brand'):
            if p.__contains__('vivo'):
                for line in properties:
                    if line.__contains__('ro.vivo.market.name'):
                        print(line)
            if p.__contains__('Xiaomi'):
                for line in properties:
                    if line.__contains__('ro.product.model'):
                        print(line)

    # 文字识别
    # utils.print_current_location(pid)

    # 获取手机的大小
    (w, h) = phone.get_size(pid)
    # 滑动手机打开屏幕
    phone.swipe_down_to_up(pid, w, h)
    # 回到手机主页面
    phone.go_home(pid)

    # 代码测试位置

    while True:
        while datetime.now().hour.__eq__(0):
            # [x] 所有程序的签到工作
            print('所有程序的签到工作 ' + datetime.now().__str__())
            for a in apps:
                utils.set_home_page(pid, w, h, a)
                # 1. 打开程序
                if tap_start(a):
                    getattr(checkin, a)(pid, w, h)
                else:
                    getattr(checkin, a)(pid)
                # 2. 所有程序签到工作
                getattr(sign, a)(pid, w, h)

                # 3. 关闭程序
                phone.stop_app(pid, packages[a])

            utils.tail_work(pid, w, h, hour=0)

        # 今日头条
        while datetime.now().hour.__eq__(1):
            # 花费35分钟
            schedule_apps(pid, w, h)

            # [x] 阅读今日头条文章
            # 花费5分钟
            # 1. 打开程序
            checkin.toutiao(pid)
            # 2. 阅读今日头条文章
            app.read_toutiao_article(pid, w, h, num=15)
            # 3. 关闭程序
            phone.stop_app(pid, packages['toutiao'])

            # [x] 看视频
            # 1. 打开程序
            checkin.toutiao(pid)
            # 2. 看视频
            app.toutiao_video(pid, w, h, num=10)
            # 3. 关闭程序
            phone.stop_app(pid, packages['toutiao'])

            utils.tail_work(pid, w, h, hour=1)

        # 快手
        while datetime.now().hour.__eq__(2):
            schedule_apps(pid, w, h)

            checkin.kuaishou(pid)
            app.kuaishou_benefit_page(pid, w, h)
            # [x] 1000金币悬赏任务
            # 10次
            # 6min赚0.1元
            # 做完之后放置在最下面
            app.kuaishou_reward_task(pid, w, h, num=10)
            phone.stop_app(pid, packages['kuaishou'])

            app.full_watch_kuaishou_video(pid, w, h, hour=2)

            utils.tail_work(pid, w, h, hour=2)

        # 抖音
        while datetime.now().hour.__eq__(3):
            schedule_apps(pid, w, h)

            # [x] 看抖音视频
            app.full_watch_douyin_video(pid, w, h, hour=3)

            utils.tail_work(pid, w, h, hour=3)

        # 火山小视频
        while datetime.now().hour.__eq__(4):
            schedule_apps(pid, w, h)

            # [x] 摇钱树
            # 1. 打开程序
            checkin.huoshan(pid)
            app.huoshan_money_tree(pid, w, h)
            # 2. 退出程序
            phone.stop_app(pid, packages['huoshan'])

            # [x] 看火山视频
            app.full_watch_huoshan_video(pid, w, h, hour=4)

            utils.tail_work(pid, w, h, hour=4)

        # 京东
        while datetime.now().hour.__eq__(5):
            schedule_apps(pid, w, h)

            # [x] 逛商品赚金币
            # 1. 打开程序
            checkin.jingdong(pid, w, h)
            # 2. 逛商品赚金币
            # 50次
            app.jingdong_good(pid, w, h, num=50)
            # 3. 关闭程序
            phone.stop_app(pid, packages['jingdong'])

            # [x] 逛活动赚金币
            # 1. 打开程序
            checkin.jingdong(pid, w, h)
            # 2. 逛活动赚金币
            app.jingdong_activity(pid, w, h, num=3)
            # 3. 关闭程序
            phone.stop_app(pid, packages['jingdong'])

            # [x] 看视频赚金币
            app.full_jingdong_video_coin(pid, w, h, hour=5)

            utils.tail_work(pid, w, h, hour=5)

        # 番茄免费小说
        while datetime.now().hour.__eq__(6):
            schedule_apps(pid, w, h)

            # 打开程序
            checkin.fanqie(pid, w, h)
            # [x] 看视频赚海量金币
            # 10次
            # 做完任务后放置到最底下
            app.fanqie_video_coin(pid, w, h, num=10)
            # 关闭程序
            phone.stop_app(pid, packages['fanqie'])

            # 打开程序
            checkin.fanqie(pid, w, h)
            # [x] 阅读番茄小说
            # 6min赚0.007元
            app.read_fanqie_novel(pid, w, h, sec=360)
            # 关闭程序
            phone.stop_app(pid, packages['fanqie'])

            utils.tail_work(pid, w, h, hour=6)

        # 番茄畅听
        while datetime.now().hour.__eq__(7):
            schedule_apps(pid, w, h)

            # [x] 看视频赚海量金币
            # 1. 打开程序
            checkin.fanchang(pid, w, h)
            # 2. 看视频赚海量金币
            # 10次
            # 每次30s
            # 如果全部做完会打乱顺序
            app.fanchang_video_coin(pid, w, h, num=9)
            # 3. 关闭程序
            phone.stop_app(pid, packages['fanchang'])

            utils.tail_work(pid, w, h, hour=7)

        # 微视
        while datetime.now().hour.__eq__(8):
            schedule_apps(pid, w, h)

            # [x] 看微视视频
            app.full_watch_weishi_video(pid, w, h, hour=8)

            utils.tail_work(pid, w, h, hour=8)

        # 书旗小说
        while datetime.now().hour.__eq__(9):
            schedule_apps(pid, w, h)

            # 无法确定关闭的位置所以强制关闭
            for i in range(0, 10):
                # 有广告稍微延长时间
                checkin.shuqi(pid, w, h, gap=12)
                # [x] 看视频赚金币
                # 10个视频
                # 10min赚0.3元
                app.shuqi_video_coin(pid, w, h)
                phone.stop_app(pid, packages['shuqi'])

            # 打开程序
            checkin.shuqi(pid, w, h)
            # [x] 阅读书旗小说
            # 5min赚0.005元
            app.read_shuqi_novel(pid, w, h, sec=300)
            # 退出程序
            phone.stop_app(pid, packages['shuqi'])

            utils.tail_work(pid, w, h, hour=9)

        # 映客直播
        while datetime.now().hour.__eq__(10):
            schedule_apps(pid, w, h)

            checkin.yingke(pid, w, h)
            # [x] 分享映客极速版
            # 分享3次
            # 也可以在直播间分享
            # 1min赚0.045元
            app.share_yingke(pid, w, h, times=3)
            phone.stop_app(pid, packages['yingke'])

            checkin.yingke(pid, w, h)
            # [x] 看映客直播
            # 20min赚0.25元
            app.watch_yingke_live(pid, w, h, sec=1200)
            phone.stop_app(pid, packages['yingke'])

            utils.tail_work(pid, w, h, hour=10)

        # 酷狗大字版
        while datetime.now().hour.__eq__(11):
            schedule_apps(pid, w, h)

            utils.tail_work(pid, w, h, hour=11)

        # 惠头条
        while datetime.now().hour.__eq__(12):
            schedule_apps(pid, w, h)

            # [x] 阅读惠头条文章
            # 1. 打开程序
            checkin.huitoutiao(pid)
            # 2. 阅读惠头条文章
            app.read_huitoutiao_article(pid, w, h, num=30)
            # 3. 关闭程序
            phone.stop_app(pid, packages['huitoutiao'])

            checkin.huitoutiao(pid)
            # [x] 看惠头条视频
            app.watch_huitoutiao_video(pid, w, h, sec=180)
            phone.stop_app(pid, packages['huitoutiao'])

            utils.tail_work(pid, w, h, hour=12)

        # 中青看点
        while datetime.now().hour.__eq__(13):
            schedule_apps(pid, w, h)

            # [x] 阅读中青看点文章
            # 1. 打开程序
            checkin.zhongqing(pid, w, h)
            # 2. 阅读中青看点文章
            app.read_zhongqing_article(pid, w, h, num=30)
            # 3. 关闭程序
            phone.stop_app(pid, packages['zhongqing'])

            utils.tail_work(pid, w, h, hour=13)

        # 拼多多
        while datetime.now().hour.__eq__(14):
            schedule_apps(pid, w, h)

            # [x] 逛街得现金
            # 1. 打开程序
            checkin.pinduoduo(pid, w, h)
            # 2. 逛街得现金
            app.pinduoduo_street_money(pid, w, h)
            # 3. 关闭程序
            phone.stop_app(pid, packages['pinduoduo'])

            # [x] 京东看视频赚金币
            app.full_jingdong_video_coin(pid, w, h, hour=14)

            utils.tail_work(pid, w, h, hour=14)

        # 淘宝
        while datetime.now().hour.__eq__(15):
            schedule_apps(pid, w, h)

            # 淘宝
            # 1. 打开程序
            checkin.taobao(pid)
            # 2. 关闭程序
            phone.stop_app(pid, packages['taobao'])

            # [x] 京东看视频赚金币
            app.full_jingdong_video_coin(pid, w, h, hour=15)

            utils.tail_work(pid, w, h, hour=15)

        # 刷宝
        while datetime.now().hour.__eq__(16):
            schedule_apps(pid, w, h)

            # [x] 看刷宝视频
            # 1. 打开程序
            checkin.shuabao(pid)
            # 2. 看刷宝视频
            app.shuabao_video(pid, w, h, num=50)
            # 3. 关闭程序
            phone.stop_app(pid, packages['shuabao'])

            utils.tail_work(pid, w, h, hour=16)

        # 趣头条
        while datetime.now().hour.__eq__(17):
            schedule_apps(pid, w, h)

            # [x] 看头条文章
            checkin.qutoutiao(pid)
            app.read_qutoutiao_article(pid, w, h, num=10)
            phone.stop_app(pid, packages['qutoutiao'])

            # [x] 看头条视频
            checkin.qutoutiao(pid)
            app.watch_qutoutiao_video(pid, w, h, num=10)
            phone.stop_app(pid, packages['qutoutiao'])

            # [x] 看趣头条小视频
            app.full_watch_qutoutiao_svideo(pid, w, h, hour=17)

            utils.tail_work(pid, w, h, hour=17)

        # 百度极速版
        while datetime.now().hour.__eq__(18):
            schedule_apps(pid, w, h)

            # [x] 好看视频
            # 花费8分钟
            # 1. 打开程序
            checkin.baidu(pid)
            # 2. 看好看视频
            app.baidu_haokan_video(pid, w, h, num=10)
            # 3. 关闭程序
            phone.stop_app(pid, packages['baidu'])

            # [x] 看百度小视频
            # 十分钟左右
            print('看百度小视频 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.baidu(pid)
            # 2. 看百度小视频
            app.watch_baidu_svideo(pid, w, h, hour=18)
            # 3. 关闭程序
            phone.stop_app(pid, packages['baidu'])

            utils.tail_work(pid, w, h, hour=18)

        # 喜马拉雅
        while datetime.now().hour.__eq__(19):
            schedule_apps(pid, w, h)

            utils.tail_work(pid, w, h, hour=19)

        # 抖音火山
        while datetime.now().hour.__eq__(20):
            schedule_apps(pid, w, h)

            # [x] 看抖音火山视频
            # 1. 打开程序
            checkin.douhuo(pid)
            app.watch_douhuo_video(pid, w, h, sec=1200)
            # 3. 关闭程序
            phone.stop_app(pid, packages['douhuo'])

            utils.tail_work(pid, w, h, hour=20)

        # 酷狗儿歌
        while datetime.now().hour.__eq__(21):
            schedule_apps(pid, w, h)

            utils.tail_work(pid, w, h, hour=21)

        # 蚂蚁看点
        while datetime.now().hour.__eq__(22):
            schedule_apps(pid, w, h)

            checkin.makan(pid, w, h)
            phone.go_back(pid, gap=2)
            app.read_makan_article(pid, w, h, num=20)
            phone.stop_app(pid, packages['makan'])

            utils.tail_work(pid, w, h, hour=22)

        # 点点新闻
        while datetime.now().hour.__eq__(23):
            schedule_apps(pid, w, h)

            for i in range(0, 10):
                checkin.diandian(pid, w, h)
                # [x] 天天领红包
                app.daily_packet(pid, w, h)
                phone.stop_app(pid, packages['diandian'])

            checkin.diandian(pid, w, h)
            # [x] 看新闻
            app.read_diandian_article(pid, w, h, num=20)
            phone.stop_app(pid, packages['diandian'])

            checkin.diandian(pid, w, h)
            # [x] 看视频
            app.watch_diandian_video(pid, w, h, num=10)
            phone.stop_app(pid, packages['diandian'])

            utils.tail_work(pid, w, h, hour=23)


def main(args):
    # 获取设备号
    devices = []
    if args.serial:
        for s in args.serial.split(' '):
            devices.append(s)
    else:
        devices = phone.get_devices()
    print(devices)

    # 创建图像界面

    # 为每部设备创建单独的线程运行
    threads = []
    # 设备号对应的线程号
    pts = {}
    for pid in devices:
        if high_serials.__contains__(pid):
            t = threading.Thread(target=run, args=(pid,), daemon=True)
            threads.append(t)
            pts[pid] = t.ident
            t.start()
        else:
            # 跑低配置的手机
            t = threading.Thread(target=cycle, args=(pid,), daemon=True)
            threads.append(t)
            pts[pid] = t.ident
            t.start()

    # noinspection PyUnusedLocal
    def signal_handler(sig, frame):
        # 结束前关闭所有程序
        for d in devices:
            ats = phone.get_top_activities(d)
            for a in apps:
                if ats.__contains__(packages[a]):
                    print('关闭运行的程序 ' + packages[a])
                    phone.stop_app(d, packages[a], 0.2)
        sys.exit(0)

    # 处理中断情况
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()

    # 等待所有线程退出
    for t in threads:
        t.join()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='PROG', conflict_handler='resolve')
    parser.add_argument('-s', '--serial', help='phone serial number')
    out_dir = 'out'
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    photos = utils.get_photos(out_dir)
    if len(photos).__gt__(MAX_PHOTOS_STORE):
        for photo in photos:
            os.remove(photo)

    main(parser.parse_args())
