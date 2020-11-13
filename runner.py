#!/usr/bin/env python3

import argparse
import os
import signal
import sys
import threading
from datetime import datetime

from src import phone, checkin, sign, app, utils, info
from src.info import high_serials, activities
from src.utils import schedule_apps

MAX_PHOTOS_STORE = 50


def cycle(pid):
    # 需要保持手机处于亮屏状态
    # 不能有密码
    # 手机初始化工作
    # 获取手机的大小
    (w, h) = phone.get_size(pid)
    # 滑动手机打开屏幕
    phone.swipe_down_to_up(pid, w / 2, h)
    # 回到手机主页面
    phone.go_home(pid)

    # 检测有哪些程序可以在手机上运行
    phone_packages = phone.list_packages(pid)
    run_apps = []
    for p in info.packages:
        if phone_packages.__contains__(info.packages[p]):
            run_apps.append(p)

    # 执行相关任务


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
                        info.contexts[pid]['phone_name'] = 'vivo'
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
    phone.swipe_down_to_up(pid, w / 2, h)
    # 回到手机主页面
    phone.go_home(pid)

    # 代码测试位置

    while True:
        while datetime.now().hour.__eq__(0):
            print('所有程序的签到工作 ' + datetime.now().__str__())
            for a in info.apps:
                if utils.is_coordinate_checkin(a):
                    getattr(checkin, a)(pid, w, h)
                else:
                    getattr(checkin, a)(pid)
                # [x] 所有程序的签到工作
                getattr(sign, a)(pid, w, h)
                phone.stop_app(pid, info.packages[a])

            utils.tail_work(pid, w, h, hour=0)

        while datetime.now().hour.__eq__(1):
            schedule_apps(pid, w, h)

            checkin.midu(pid, w, h)
            app.midu_benefit_page(pid, w, h)
            # [x] 阅读米读小说
            app.read_midu_novel(pid, w, h, sec=300)
            phone.stop_app(pid, info.packages['midu'])

            checkin.toutiao(pid)
            # [x] 阅读今日头条文章
            app.read_toutiao_article(pid, w, h, num=5)
            phone.stop_app(pid, info.packages['toutiao'])

            checkin.toutiao(pid)
            # [x] 看今日头条视频
            app.toutiao_video(pid, w, h, num=5)
            phone.stop_app(pid, info.packages['toutiao'])

            utils.tail_work(pid, w, h, hour=1)

        while datetime.now().hour.__eq__(2):
            schedule_apps(pid, w, h)

            for i in range(0, 2):
                checkin.kuaishou(pid)
                phone.go_back(pid)
                app.kuaishou_benefit_page(pid, w, h)
                # [x] 快手1000金币悬赏任务
                app.kuaishou_reward_task(pid, w, h, num=5)
                phone.stop_app(pid, info.packages['kuaishou'])

            utils.tail_work(pid, w, h, hour=2)

        while datetime.now().hour.__eq__(3):
            schedule_apps(pid, w, h)

            checkin.douyin(pid)
            phone.go_back(pid)
            # [x] 看抖音视频
            app.watch_douyin_video(pid, w, h, hour=3)
            phone.stop_app(pid, info.packages['douyin'])

            utils.tail_work(pid, w, h, hour=3)

        while datetime.now().hour.__eq__(4):
            schedule_apps(pid, w, h)

            checkin.huoshan(pid)
            phone.go_back(pid)
            # [x] 看火山视频
            app.watch_huoshan_video(pid, w, h, hour=4)
            phone.stop_app(pid, info.packages['huoshan'])

            utils.tail_work(pid, w, h, hour=4)

        while datetime.now().hour.__eq__(5):
            schedule_apps(pid, w, h)

            checkin.jingdong(pid, w, h)
            app.jingdong_benefit_page(pid, w, h)
            # [x] 京东看视频赚金币
            app.jingdong_video_coin(pid, w, h, hour=5)
            phone.stop_app(pid, info.packages['jingdong'])

            utils.tail_work(pid, w, h, hour=5)

        # 番茄免费小说
        while datetime.now().hour.__eq__(6):
            schedule_apps(pid, w, h)

            checkin.jingdong(pid, w, h)
            app.jingdong_benefit_page(pid, w, h)
            # [x] 京东看视频赚金币
            app.jingdong_video_coin(pid, w, h, hour=6)
            phone.stop_app(pid, info.packages['jingdong'])

            utils.tail_work(pid, w, h, hour=6)

        # 番茄畅听
        while datetime.now().hour.__eq__(7):
            schedule_apps(pid, w, h)

            checkin.jingdong(pid, w, h)
            app.jingdong_benefit_page(pid, w, h)
            # [x] 京东看视频赚金币
            app.jingdong_video_coin(pid, w, h, hour=7)
            phone.stop_app(pid, info.packages['jingdong'])

            utils.tail_work(pid, w, h, hour=7)

        # 酷狗唱唱斗歌版
        # 微视视频
        while datetime.now().hour.__eq__(8):
            schedule_apps(pid, w, h)

            checkin.weishi(pid)
            # [x] 看微视视频
            app.watch_weishi_video(pid, w, h, sec=180)
            phone.stop_app(pid, info.packages['weishi'])

            utils.tail_work(pid, w, h, hour=8)

        # 书旗小说
        # 五八同城
        while datetime.now().hour.__eq__(9):
            schedule_apps(pid, w, h)

            # 无法确定关闭的位置所以强制关闭
            for i in range(0, 10):
                checkin.shuqi(pid, w, h, gap=12)
                app.shuqi_benefit_page(pid, w, h)
                # [x] 书旗小说看视频赚金币
                # 10min赚0.3元
                app.shuqi_video_coin(pid, w, h)
                phone.stop_app(pid, info.packages['shuqi'])

            for i in range(0, 2):
                checkin.wuba(pid)
                app.wuba_benefit_page(pid, w, h)
                # [x] 五八同城看视频赚金币
                app.watch_wuba_video(pid, w, h, num=4)
                phone.stop_app(pid, info.packages['wuba'])

            checkin.shuqi(pid, w, h)
            # [x] 阅读书旗小说
            app.read_shuqi_novel(pid, w, h, sec=400)
            phone.stop_app(pid, info.packages['shuqi'])

            utils.tail_work(pid, w, h, hour=9)

        # 映客直播
        while datetime.now().hour.__eq__(10):
            schedule_apps(pid, w, h)

            checkin.yingke(pid, w, h)
            app.yingke_benefit_page(pid, w, h)
            # [x] 分享映客极速版
            app.share_yingke_live(pid, w, h, times=3)
            phone.stop_app(pid, info.packages['yingke'])

            checkin.yingke(pid, w, h)
            # [x] 看映客直播
            app.watch_yingke_live(pid, w, h, sec=600)
            phone.stop_app(pid, info.packages['yingke'])

            utils.tail_work(pid, w, h, hour=10)

        # 酷狗大字版
        # 刷宝短视频
        while datetime.now().hour.__eq__(11):
            schedule_apps(pid, w, h)

            checkin.kugou(pid, w, h)
            # [x] 酷狗背景音乐
            # 下次进入的时候关闭
            app.kugou_background_music(pid, w, h)

            checkin.shuabao(pid)
            # [x] 看刷宝视频
            app.watch_shuabao_video(pid, w, h, num=30)
            phone.stop_app(pid, info.packages['shuabao'])

            utils.tail_work(pid, w, h, hour=11)

        # 惠头条
        while datetime.now().hour.__eq__(12):
            schedule_apps(pid, w, h)

            checkin.huitoutiao(pid)
            # [x] 阅读惠头条文章
            app.read_huitoutiao_article(pid, w, h, num=10)
            phone.stop_app(pid, info.packages['huitoutiao'])

            checkin.huitoutiao(pid)
            # [x] 看惠头条视频
            app.watch_huitoutiao_video(pid, w, h, sec=180)
            phone.stop_app(pid, info.packages['huitoutiao'])

            checkin.hongshi(pid)
            # [x] 看红包短视频
            app.watch_hongbao_video(pid, w, h, sec=180)
            phone.stop_app(pid, info.packages['hongshi'])

            utils.tail_work(pid, w, h, hour=12)

        # 中青看点
        # 汽车之家
        while datetime.now().hour.__eq__(13):
            schedule_apps(pid, w, h)

            for i in range(0, 2):
                checkin.chejia(pid)
                app.chejia_benefit_page(pid, w, h)
                # [x] 看汽车之家福利视频
                app.chejia_benefit_video(pid, w, h, num=5)
                phone.stop_app(pid, info.packages['chejia'])

            checkin.zhongqing(pid, w, h)
            # [x] 阅读中青看点文章
            app.read_zhongqing_article(pid, w, h, num=5)
            phone.stop_app(pid, info.packages['zhongqing'])

            checkin.zhongqing(pid, w, h)
            # [x] 看中青看点视频
            app.watch_zhongqing_video(pid, w, h, num=5)
            phone.stop_app(pid, info.packages['zhongqing'])

            utils.tail_work(pid, w, h, hour=13)

        while datetime.now().hour.__eq__(14):
            schedule_apps(pid, w, h)

            checkin.jingdong(pid, w, h)
            app.jingdong_benefit_page(pid, w, h)
            # [x] 京东看视频赚金币
            app.jingdong_video_coin(pid, w, h, hour=14)
            phone.stop_app(pid, info.packages['jingdong'])

            utils.tail_work(pid, w, h, hour=14)

        # 快音
        while datetime.now().hour.__eq__(15):
            schedule_apps(pid, w, h)

            for i in range(0, 5):
                checkin.kuaiyin(pid, w, h)
                app.kuaiyin_benefit_page(pid, w, h)
                # [x] 快音看视频赚钱
                app.watch_kuaiyin_video(pid, w, h)
                phone.stop_app(pid, info.packages['kuaiyin'])

            utils.tail_work(pid, w, h, hour=15)

        # 糖豆
        while datetime.now().hour.__eq__(16):
            schedule_apps(pid, w, h)

            checkin.tangdou(pid)
            app.tangdou_benefit_page(pid, w, h)
            app.tangdou_funny_video(pid, w, h, num=30)
            phone.stop_app(pid, info.packages['tangdou'])

            utils.tail_work(pid, w, h, hour=16)

        # 东方头条
        while datetime.now().hour.__eq__(17):
            schedule_apps(pid, w, h)

            # # [x] 看头条文章
            # checkin.qutoutiao(pid)
            # app.read_qutoutiao_article(pid, w, h, num=10)
            # phone.stop_app(pid, info.packages['qutoutiao'])
            #
            # # [x] 看头条视频
            # checkin.qutoutiao(pid)
            # app.watch_qutoutiao_video(pid, w, h, num=10)
            # phone.stop_app(pid, info.packages['qutoutiao'])
            #
            # # [x] 看趣头条小视频
            # app.full_watch_qutoutiao_svideo(pid, w, h, hour=17)

            utils.tail_work(pid, w, h, hour=17)

        # 聚看点
        # 百度极速版
        while datetime.now().hour.__eq__(18):
            schedule_apps(pid, w, h)

            checkin.baidu(pid)
            # [x] 百度看好看视频
            app.baidu_haokan_video(pid, w, h, num=10)
            phone.stop_app(pid, info.packages['baidu'])

            checkin.jukandian(pid, w, h)
            # [x] 聚看点阅读文章
            app.read_jukandian_article(pid, w, h, num=5)
            phone.stop_app(pid, info.packages['jukandian'])

            checkin.jukandian(pid, w, h)
            # [x] 聚看点视频
            app.watch_jukandian_video(pid, w, h, num=5)
            phone.stop_app(pid, info.packages['jukandian'])

            checkin.jukandian(pid, w, h)
            # [x] 聚看点小视频
            app.watch_jukandian_svideo(pid, w, h, num=5)
            phone.stop_app(pid, info.packages['jukandian'])

            checkin.baidu(pid)
            # [x] 看百度小视频
            app.watch_baidu_svideo(pid, w, h, hour=18)
            phone.stop_app(pid, info.packages['baidu'])

            utils.tail_work(pid, w, h, hour=18)

        # 看点快报
        while datetime.now().hour.__eq__(19):
            schedule_apps(pid, w, h)

            for i in range(0, 3):
                checkin.kankuai(pid)
                app.kankuai_benefit_page(pid, w, h)
                # [x] 看广告领金币
                app.watch_kankuai_advert(pid, w, h, num=10)
                phone.stop_app(pid, info.packages['kankuai'])

            utils.tail_work(pid, w, h, hour=19)

        # 抖音火山
        while datetime.now().hour.__eq__(20):
            schedule_apps(pid, w, h)

            checkin.douhuo(pid)
            # [x] 看抖音火山视频
            # 中途可能存在广告导致无法播放
            app.watch_douhuo_video(pid, w, h, sec=300)
            phone.stop_app(pid, info.packages['douhuo'])

            utils.tail_work(pid, w, h, hour=20)

        # 酷狗儿歌
        while datetime.now().hour.__eq__(21):
            checkin.kuge(pid, w, h)
            # [x] 后台播放酷狗儿歌
            # 在定时任务中关闭儿歌
            app.kuge_play_background(pid, w, h)

            schedule_apps(pid, w, h)

            utils.tail_work(pid, w, h, hour=21)

        # 蚂蚁看点
        while datetime.now().hour.__eq__(22):
            schedule_apps(pid, w, h)

            checkin.makan(pid, w, h)
            phone.go_back(pid, gap=2)
            # [x] 阅读蚂蚁看点文章
            # 需要提前解决彩蛋问题
            app.read_makan_article(pid, w, h, num=5)
            phone.stop_app(pid, info.packages['makan'])

            checkin.makan(pid, w, h)
            phone.go_back(pid)
            app.makan_benefit_page(pid, w, h)
            # [x] 蚂蚁看点搜索赚钱
            app.makan_search_coin(pid, w, h, num=12)
            phone.stop_app(pid, info.packages['makan'])

            utils.tail_work(pid, w, h, hour=22)

        # 点点新闻
        while datetime.now().hour.__eq__(23):
            schedule_apps(pid, w, h)

            for i in range(0, 10):
                checkin.diandian(pid, w, h)
                # [x] 天天领红包
                app.diandian_daily_packet(pid, w, h)
                phone.stop_app(pid, info.packages['diandian'])

            checkin.diandian(pid, w, h)
            # [x] 看新闻
            # 看完十几篇以后有倒计时
            app.read_diandian_article(pid, w, h, num=10)
            phone.stop_app(pid, info.packages['diandian'])

            utils.tail_work(pid, w, h, hour=23)


def main(args):
    # 获取设备号
    devices = []
    if args.serial:
        devices.append(args.serial)
    else:
        devices = phone.get_devices()
    print(devices)

    # 创建图像界面

    # 为每部设备创建单独的线程运行
    threads = []
    # 设备号对应的线程号
    pts = {}
    for pid in devices:
        info.contexts.update({pid: {}})
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
            if ats is None:
                sys.exit(0)
            for a in info.apps:
                if ats.__contains__(info.packages[a]):
                    print('关闭运行的程序 ' + info.packages[a])
                    phone.stop_app(d, info.packages[a], 0.2)
        sys.exit(0)

    # 处理中断情况
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()

    # 等待所有线程退出
    for t in threads:
        t.join()


def init():
    # 初始化out目录
    out_dir = 'out'
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    photos = utils.get_photos(out_dir)
    if len(photos).__gt__(MAX_PHOTOS_STORE):
        for photo in photos:
            os.remove(photo)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='PROG', conflict_handler='resolve')
    parser.add_argument('-s', '--serial', help='phone serial number')

    init()

    # 初始化全局变量
    info.apps = list(activities.keys())
    info.packages = utils.get_packages_dict(activities)

    main(parser.parse_args())
