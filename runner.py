import argparse
from datetime import datetime
import signal
import sys
import threading

from src import phone, checkin, sign, app
from src.info import packages, apps, high_serials
from src.utils import tap_start, schedule_apps


def run(pid):
    # 需要保持手机处于亮屏状态
    # 不能有密码
    # 手机初始化工作
    # 获取手机的大小
    (w, h) = phone.get_size(pid)
    # 滑动手机打开屏幕
    phone.swipe_down_to_up(pid, w, h)
    # 回到手机主界面
    phone.go_home(pid)

    while True:
        while datetime.now().hour.__eq__(0):
            # 所有程序的签到工作
            print('所有程序的签到工作 ' + datetime.now().__str__())
            for a in apps:
                # 1. 打开程序
                if tap_start(a):
                    getattr(checkin, a)(pid, w, h)
                else:
                    getattr(checkin, a)(pid)
                # 2. 签到
                getattr(sign, a)(pid, w, h)
                # 3. 关闭程序
                phone.stop_app(pid, packages[a])

        while datetime.now().hour.__eq__(1):
            schedule_apps(pid, w, h)

            # [ ] 阅读头条文章
            print('阅读头条文章 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.toutiao(pid)
            # 2. 阅读头条文章
            app.read_toutiao_articles(pid, w, h, 30)
            # 3. 关闭程序
            phone.stop_app(pid, packages['toutiao'])

        while datetime.now().hour.__eq__(2):
            schedule_apps(pid, w, h)

            # [x] 看快手视频
            print('看快手视频 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.kuaishou(pid)
            # 2. 看快手视频
            app.watch_kuaishou_video(pid, w, h, 2)
            # 3. 关闭程序
            phone.stop_app(pid, packages['kuaishou'])

        while datetime.now().hour.__eq__(3):
            schedule_apps(pid, w, h)

            # [x] 看抖音视频
            print('看抖音视频 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.douyin(pid)
            # 2. 看抖音视频
            app.watch_douyin_video(pid, w, h, 3)
            # 3. 关闭程序
            phone.stop_app(pid, packages['douyin'])

        while datetime.now().hour.__eq__(4):
            schedule_apps(pid, w, h)

            # [x] 看火山视频
            print('看火山视频 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.huoshan(pid)
            # 2. 看火山视频
            app.watch_huoshan_video(pid, w, h, 4)
            # 3. 关闭程序
            phone.stop_app(pid, packages['huoshan'])


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
            return None

    # noinspection PyUnusedLocal
    def signal_handler(sig, frame):
        # 结束前关闭所有程序
        for d in devices:
            activities = phone.get_top_activities(d)
            for a in apps:
                if activities.__contains__(packages[a]):
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
    main(parser.parse_args())
