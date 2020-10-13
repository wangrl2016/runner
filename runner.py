#!/usr/bin/env python3

import argparse
import os
from datetime import datetime
import signal
import sys
import threading
# import pytesseract
# from PIL import Image

from src import phone, checkin, sign, app, utils, info
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
            print('看快手视频 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.kuaishou(pid)
            # 2. 看快手视频
            app.watch_kuaishou_video(pid, w, h, hour)
            # 3. 关闭程序
            phone.stop_app(pid, packages['kuaishou'])

        hour = datetime.now().hour
        while run_apps.__contains__('douyin') and datetime.now().hour.__eq__(hour):
            # [x] 看抖音视频
            print('看抖音视频 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.douyin(pid)
            # 2. 看抖音视频
            app.watch_douyin_video(pid, w, h, hour)
            # 3. 关闭程序
            phone.stop_app(pid, packages['douyin'])

        hour = datetime.now().hour
        while run_apps.__contains__('huoshan') and datetime.now().hour.__eq__(hour):
            # [x] 看火山视频
            print('看火山视频 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.huoshan(pid)
            # 2. 看火山视频
            app.watch_huoshan_video(pid, w, h, hour)
            # 3. 关闭程序
            phone.stop_app(pid, packages['huoshan'])

        hour = datetime.now().hour
        while run_apps.__contains__('weishi') and datetime.now().hour.__eq__(hour):
            # [x] 看微视视频
            print('看微视视频 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.weishi(pid)
            # 2. 看微视视频
            app.watch_weishi_video(pid, w, h, hour)
            # 3. 关闭程序
            phone.stop_app(pid, packages['weishi'])

        hour = datetime.now().hour
        while run_apps.__contains__('shuabao') and datetime.now().hour.__eq__(hour):
            # [x] 看刷宝视频
            print('看刷宝视频 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.shuabao(pid)
            # 2. 看刷宝视频
            app.watch_shuabao_video(pid, w, h, hour)
            # 3. 关闭程序
            phone.stop_app(pid, packages['shuabao'])


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

    # 识别文字
    # phone_name = phone.get_page_photo(pid, output=out_dir)
    # txt = pytesseract.image_to_string(Image.open(os.path.join(out_dir, phone_name)), lang='chi_sim')

    # 获取手机的大小
    (w, h) = phone.get_size(pid)
    # 滑动手机打开屏幕
    phone.swipe_down_to_up(pid, w, h)
    # 回到手机主页面
    phone.go_home(pid)

    while True:
        while datetime.now().hour.__eq__(0):
            # [x] 所有程序的签到工作
            print('所有程序的签到工作 ' + datetime.now().__str__())
            for a in apps:
                # 1. 打开程序
                if tap_start(a):
                    getattr(checkin, a)(pid, w, h)
                else:
                    getattr(checkin, a)(pid)
                # 2. 所有程序签到工作
                getattr(sign, a)(pid, w, h)

                # 3. 关闭程序
                phone.stop_app(pid, packages[a])

            # [x] 看快手视频
            print('看快手视频 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.kuaishou(pid)
            # 2. 看快手视频
            app.watch_kuaishou_video(pid, w, h, hour=0)
            # 3. 关闭程序
            phone.stop_app(pid, packages['kuaishou'])

        while datetime.now().hour.__eq__(1):
            # 花费35分钟
            schedule_apps(pid, w, h)

            # [x] 阅读今日头条文章
            # 花费5分钟
            print('阅读头条文章 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.toutiao(pid)
            # 2. 阅读今日头条文章
            app.read_toutiao_article(pid, w, h, num=10)
            # 3. 关闭程序
            phone.stop_app(pid, packages['toutiao'])

            # [x] 看视频
            # 花费20分钟
            print('看今日头条视频 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.toutiao(pid)
            # 2. 看视频
            app.toutiao_video(pid, w, h, num=20)
            # 3. 关闭程序
            phone.stop_app(pid, packages['toutiao'])

        while datetime.now().hour.__eq__(2):
            schedule_apps(pid, w, h)

            # [x] 看快手视频
            print('看快手视频 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.kuaishou(pid)
            # 2. 看快手视频
            app.watch_kuaishou_video(pid, w, h, hour=2)
            # 3. 关闭程序
            phone.stop_app(pid, packages['kuaishou'])

            # [x] 1000金币悬赏任务
            print('快手1000金币悬赏任务 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.kuaishou(pid)
            # 2. 悬赏任务做10次
            app.kuaishou_reward_task(pid, w, h, num=10)
            # 3. 关闭程序
            phone.stop_app(pid, packages['kuaishou'])

        while datetime.now().hour.__eq__(3):
            schedule_apps(pid, w, h)

            # [x] 看抖音视频
            print('看抖音视频 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.douyin(pid)
            # 2. 看抖音视频
            app.watch_douyin_video(pid, w, h, hour=3)
            # 3. 关闭程序
            phone.stop_app(pid, packages['douyin'])

        while datetime.now().hour.__eq__(4):
            schedule_apps(pid, w, h)

            # [x] 摇钱树
            print('火山摇钱树 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.huoshan(pid)
            app.huoshan_money_tree(pid, w, h)
            # 2. 退出程序
            phone.stop_app(pid, packages['huoshan'])

            # [x] 看火山视频
            start = datetime.now()
            print('看火山视频 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.huoshan(pid)
            # 2. 看火山视频
            app.watch_huoshan_video(pid, w, h, hour=4)
            # 3. 关闭程序
            phone.stop_app(pid, packages['huoshan'])
            info.watch_huoshan_minutes += (datetime.now() - start).seconds / 60

        while datetime.now().hour.__eq__(5):
            schedule_apps(pid, w, h)

            # [x] 逛商品赚金币
            print('京东逛商品赚金币 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.jingdong(pid, w, h)
            # 2. 逛商品赚金币
            # 50次
            app.jingdong_good(pid, w, h, sec=1000)
            # 3. 关闭程序
            phone.stop_app(pid, packages['jingdong'])

            # [x] 逛活动赚金币
            print('京东逛活动赚金币 ')
            # 1. 打开程序
            checkin.jingdong(pid, w, h)
            # 2. 逛活动赚金币
            # 10次
            app.jingdong_activity(pid, w, h, sec=200)
            # 3. 关闭程序
            phone.stop_app(pid, packages['jingdong'])

            # [x] 看视频赚金币
            print('京东看视频赚金币 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.jingdong(pid, w, h)
            # 2. 看视频赚金币
            app.jingdong_video_coin(pid, w, h, hour=5)
            # 3. 关闭程序
            phone.stop_app(pid, packages['jingdong'])

        while datetime.now().hour.__eq__(6):
            schedule_apps(pid, w, h)

            # 手机休息5分钟
            phone.sleep_to_weak(pid, w, h)

            # [x] 看视频赚海量金币
            # 1. 打开程序
            checkin.fanqie(pid, w, h)
            # 2. 看视频赚海量金币
            # 10次
            # 每次30s
            app.fanqie_video_coin(pid, w, h, num=9)
            # 3. 关闭程序
            phone.stop_app(pid, packages['fanqie'])

            # [x] 阅读番茄小说
            print('阅读番茄小说 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.fanqie(pid, w, h)
            # 2. 阅读番茄小说
            app.read_fanqie_novel(pid, w, h, hour=6)
            # 3. 关闭程序
            phone.stop_app(pid, packages['fanqie'])

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

            # [x] 听番畅音频
            print('听番畅音频 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.fanchang(pid, w, h)
            # 2. 听番畅音频120s
            app.listen_fanchang_sound(pid, w, h, sec=120)
            # 3. 关闭程序
            phone.stop_app(pid, packages['fanchang'])

        while datetime.now().hour.__eq__(8):
            schedule_apps(pid, w, h)

            # [x] 看微视视频
            print('看微视视频 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.weishi(pid)
            # 2. 看微视视频
            app.watch_weishi_video(pid, w, h, hour=8)
            # 3. 关闭程序
            phone.stop_app(pid, packages['weishi'])

        while datetime.now().hour.__eq__(9):
            schedule_apps(pid, w, h)

            # [x] 看视频赚金币
            print('书旗看视频赚金币 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.shuqi(pid, w, h)
            # 2. 看视频赚金币
            app.shuqi_video_coin(pid, w, h, num=10)
            # 2. 退出程序
            phone.stop_app(pid, packages['shuqi'])

            # [x] 阅读书旗小说
            print('阅读书旗小说 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.shuqi(pid, w, h)
            # 2. 阅读书旗小说
            app.read_shuqi_novel(pid, w, h, sec=300)
            # 3. 退出程序
            phone.stop_app(pid, packages['shuqi'])

        while datetime.now().hour.__eq__(10):
            schedule_apps(pid, w, h)

            # [x] 看映客直播
            print('看映客直播 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.yingke(pid, w, h)
            # 2. 看映客直播
            app.watch_yingke_live(pid, w, h, sec=300)
            # 3. 退出程序
            phone.stop_app(pid, packages['yingke'])

        while datetime.now().hour.__eq__(11):
            schedule_apps(pid, w, h)

            # [x] 听酷狗音乐
            print('听酷狗音乐 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.kugou(pid, w, h)
            # 2. 听酷狗音乐
            app.listen_kugou_music(pid, w, h, sec=300)
            # 3. 关闭程序
            phone.stop_app(pid, packages['kugou'])

        while datetime.now().hour.__eq__(12):
            schedule_apps(pid, w, h)

            # 手机休息5分钟
            phone.sleep_to_weak(pid, w, h)

            # [x] 阅读惠头条文章
            print('阅读惠头条文章 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.huitoutiao(pid)
            # 2. 阅读惠头条文章
            app.read_huitoutiao_article(pid, w, h, num=30)
            # 3. 关闭程序
            phone.stop_app(pid, packages['huitoutiao'])

        while datetime.now().hour.__eq__(13):
            schedule_apps(pid, w, h)

            # [x] 阅读中青看点文章
            print('阅读中青看点文章 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.zhongqing(pid, w, h)
            # 2. 阅读中青看点文章
            app.read_zhongqing_article(pid, w, h, num=30)
            # 3. 关闭程序
            phone.stop_app(pid, packages['zhongqing'])

        while datetime.now().hour.__eq__(14):
            schedule_apps(pid, w, h)

            # 拼多多
            print('拼多多 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.pinduoduo(pid, w, h)
            # 2. 关闭程序
            phone.stop_app(pid, packages['pinduoduo'])

        while datetime.now().hour.__eq__(15):
            schedule_apps(pid, w, h)

            # 淘宝
            print('淘宝 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.taobao(pid)
            # 2. 关闭程序
            phone.stop_app(pid, packages['taobao'])

        while datetime.now().hour.__eq__(16):
            schedule_apps(pid, w, h)

            # [x] 看刷宝视频
            print('看刷宝视频 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.shuabao(pid)
            # 2. 看刷宝视频
            app.watch_shuabao_video(pid, w, h, hour=16)
            # 3. 关闭程序
            phone.stop_app(pid, packages['shuabao'])

        while datetime.now().hour.__eq__(17):
            schedule_apps(pid, w, h)

            # [x] 看趣头条小视频
            print('看趣头条小视频 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.qutoutiao(pid)
            # 2. 看趣头条小视频
            app.watch_qutoutiao_svideo(pid, w, h, hour=17)
            # 3. 关闭程序
            phone.stop_app(pid, packages['qutoutiao'])

        while datetime.now().hour.__eq__(18):
            schedule_apps(pid, w, h)

            # 手机休息5分钟
            phone.sleep_to_weak(pid, w, h)

            # [x] 好看视频
            print('百度好看视频 ' + datetime.now().__str__())
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

        while datetime.now().hour.__eq__(19):
            schedule_apps(pid, w, h)

            # [x] 听喜马拉雅音频
            print('听喜马拉雅音频 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.ximalaya(pid)
            # 2. 听喜马拉雅音频
            app.listen_ximalaya_sound(pid, w, h, sec=300)
            # 3. 关闭程序
            phone.stop_app(pid, packages['ximalaya'])

        while datetime.now().hour.__eq__(20):
            schedule_apps(pid, w, h)

            # [x] 看快手视频
            print('看快手视频 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.kuaishou(pid)
            # 2. 看快手视频
            app.watch_kuaishou_video(pid, w, h, hour=20)
            # 3. 关闭程序
            phone.stop_app(pid, packages['kuaishou'])

        while datetime.now().hour.__eq__(21):
            schedule_apps(pid, w, h)

            # [x] 看抖音视频
            print('看抖音视频 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.douyin(pid)
            # 2. 看抖音视频
            app.watch_douyin_video(pid, w, h, hour=21)
            # 3. 关闭程序
            phone.stop_app(pid, packages['douyin'])

        while datetime.now().hour.__eq__(22):
            schedule_apps(pid, w, h)

            # [x] 看火山视频
            print('看火山视频 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.huoshan(pid)
            # 2. 看火山视频
            app.watch_huoshan_video(pid, w, h, hour=4)
            # 3. 关闭程序
            phone.stop_app(pid, packages['huoshan'])

        while datetime.now().hour.__eq__(23):
            schedule_apps(pid, w, h)

            # 手机休息5分钟
            phone.sleep_to_weak(pid, w, h)


def main(args):
    # 获取设备号
    devices = []
    if args.serial:
        for s in args.serial.split(' '):
            devices.append(s)
    else:
        devices = phone.get_devices()
    print(devices)

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
