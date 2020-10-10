import argparse
import signal
import sys
import threading

from src import phone
from src.info import packages, apps, high_serials


def run(pid):
    print(pid)


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

    # 等待所有线程退出
    for t in threads:
        t.join()

    # 处理中断情况
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='PROG', conflict_handler='resolve')
    parser.add_argument('-s', '--serial', help='phone serial number')
    main(parser.parse_args())
