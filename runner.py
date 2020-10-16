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

# import pytesseract
# from PIL import Image
# from pytesseract import Output

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
            if p.__contains__('Xiaomi'):
                for line in properties:
                    if line.__contains__('ro.product.model'):
                        print(line)

    # 文字识别
    # photo_name = phone.get_page_photo(pid, output=out_dir)
    # text = pytesseract.image_to_string(Image.open(os.path.join(out_dir, photo_name)), lang='chi_sim')
    # print(text)
    # data = pytesseract.image_to_data(Image.open(os.path.join(out_dir, photo_name)),
    #                                  output_type=Output.DICT, lang='chi_sim')
    # for i in range(0, len(data['text'])):
    #     print(data['text'][i], data['left'][i], data['top'][i], data['width'][i], data['height'][i])

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

        while datetime.now().hour.__eq__(1):
            # 花费35分钟
            schedule_apps(pid, w, h)

            # [x] 阅读今日头条文章
            # 花费5分钟
            # 1. 打开程序
            checkin.toutiao(pid)
            # 2. 阅读今日头条文章
            app.read_toutiao_article(pid, w, h, num=10)
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

        while datetime.now().hour.__eq__(2):
            schedule_apps(pid, w, h)

            app.full_watch_kuaishou_video(pid, w, h, hour=2)

            # [x] 1000金币悬赏任务
            # 1. 打开程序
            checkin.kuaishou(pid)
            # 2. 悬赏任务做9次
            # 不然完成后会放置最下面
            # 打乱原本的顺序
            app.kuaishou_reward_task(pid, w, h, num=9)
            # 3. 关闭程序
            phone.stop_app(pid, packages['kuaishou'])

            utils.tail_work(pid, w, h, hour=2)

        while datetime.now().hour.__eq__(3):
            schedule_apps(pid, w, h)

            # [x] 看抖音视频
            app.full_watch_douyin_video(pid, w, h, hour=3)

            utils.tail_work(pid, w, h, hour=3)

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

        while datetime.now().hour.__eq__(5):
            schedule_apps(pid, w, h)

            # [x] 逛商品赚金币
            # 1. 打开程序
            checkin.jingdong(pid, w, h)
            # 2. 逛商品赚金币
            # 50次
            app.jingdong_good(pid, w, h, sec=1000)
            # 3. 关闭程序
            phone.stop_app(pid, packages['jingdong'])

            # [x] 逛活动赚金币
            # 1. 打开程序
            checkin.jingdong(pid, w, h)
            # 2. 逛活动赚金币
            # 10次
            app.jingdong_activity(pid, w, h, sec=200)
            # 3. 关闭程序
            phone.stop_app(pid, packages['jingdong'])

            # [x] 看视频赚金币
            app.full_jingdong_video_coin(pid, w, h, hour=5)

            utils.tail_work(pid, w, h, hour=5)

        while datetime.now().hour.__eq__(6):
            schedule_apps(pid, w, h)

            # [x] 看视频赚海量金币
            # 1. 打开程序
            checkin.fanqie(pid, w, h)
            # 2. 看视频赚海量金币
            # 10次
            # 每次30s
            # 如果全部做完会打乱顺序
            app.fanqie_video_coin(pid, w, h, num=9)
            # 3. 关闭程序
            phone.stop_app(pid, packages['fanqie'])

            # [x] 阅读番茄小说
            # 1. 打开程序
            checkin.fanqie(pid, w, h)
            # 2. 阅读番茄小说
            app.read_fanqie_novel(pid, w, h, hour=6)
            # 3. 关闭程序
            phone.stop_app(pid, packages['fanqie'])

            utils.tail_work(pid, w, h, hour=6)

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
            # 1. 打开程序
            checkin.fanchang(pid, w, h)
            # 2. 听番畅音频120s
            app.listen_fanchang_sound(pid, w, h, sec=120)
            # 3. 关闭程序
            phone.stop_app(pid, packages['fanchang'])

            utils.tail_work(pid, w, h, hour=7)

        while datetime.now().hour.__eq__(8):
            schedule_apps(pid, w, h)

            # [x] 看微视视频
            app.full_watch_weishi_video(pid, w, h, hour=8)

            utils.tail_work(pid, w, h, hour=8)

        while datetime.now().hour.__eq__(9):
            schedule_apps(pid, w, h)

            # [x] 看视频赚金币
            # 1. 打开程序
            checkin.shuqi(pid, w, h)
            # 2. 看视频赚金币
            app.shuqi_video_coin(pid, w, h, num=10)
            # 3. 邀请书友
            app.shuqi_invent_friend(pid, w, h)
            # 4. 退出程序
            phone.stop_app(pid, packages['shuqi'])

            # [x] 阅读书旗小说
            # 1. 打开程序
            checkin.shuqi(pid, w, h)
            # 2. 阅读书旗小说
            app.read_shuqi_novel(pid, w, h, sec=300)
            # 3. 退出程序
            phone.stop_app(pid, packages['shuqi'])

            utils.tail_work(pid, w, h, hour=9)

        while datetime.now().hour.__eq__(10):
            schedule_apps(pid, w, h)

            # [x] 看映客直播
            # 1. 打开程序
            checkin.yingke(pid, w, h)
            # 2. 看映客直播
            app.watch_yingke_live(pid, w, h, sec=600)
            # 3. 退出程序
            phone.stop_app(pid, packages['yingke'])

            utils.tail_work(pid, w, h, hour=10)

        while datetime.now().hour.__eq__(11):
            schedule_apps(pid, w, h)

            # [x] 听酷狗音乐
            # 1. 打开程序
            checkin.kugou(pid, w, h)
            # 2. 听酷狗音乐
            app.listen_kugou_music(pid, w, h, sec=600)
            # 3. 关闭程序
            phone.stop_app(pid, packages['kugou'])

            utils.tail_work(pid, w, h, hour=11)

        while datetime.now().hour.__eq__(12):
            schedule_apps(pid, w, h)

            # [x] 阅读惠头条文章
            # 1. 打开程序
            checkin.huitoutiao(pid)
            # 2. 阅读惠头条文章
            app.read_huitoutiao_article(pid, w, h, num=30)
            # 3. 关闭程序
            phone.stop_app(pid, packages['huitoutiao'])

            utils.tail_work(pid, w, h, hour=12)

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

        while datetime.now().hour.__eq__(17):
            schedule_apps(pid, w, h)

            # [x] 看趣头条小视频
            app.full_watch_qutoutiao_svideo(pid, w, h, hour=17)

            utils.tail_work(pid, w, h, hour=17)

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

        while datetime.now().hour.__eq__(19):
            schedule_apps(pid, w, h)

            # [x] 听喜马拉雅音频
            # 1. 打开程序
            checkin.ximalaya(pid)
            # 2. 听喜马拉雅音频
            app.listen_ximalaya_sound(pid, w, h, sec=300)
            # 3. 关闭程序
            phone.stop_app(pid, packages['ximalaya'])

            utils.tail_work(pid, w, h, hour=19)

        while datetime.now().hour.__eq__(20):
            schedule_apps(pid, w, h)

            # [x] 看抖音火山视频
            # 1. 打开程序
            checkin.douhuo(pid)
            app.watch_douhuo_video(pid, w, h, sec=300)
            # 3. 关闭程序
            phone.stop_app(pid, packages['douhuo'])

            utils.tail_work(pid, w, h, hour=20)

        while datetime.now().hour.__eq__(21):
            schedule_apps(pid, w, h)

            utils.tail_work(pid, w, h, hour=21)

        while datetime.now().hour.__eq__(22):
            schedule_apps(pid, w, h)

            utils.tail_work(pid, w, h, hour=22)

        while datetime.now().hour.__eq__(23):
            schedule_apps(pid, w, h)

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
    #

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
