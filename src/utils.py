import os
from datetime import datetime
from random import randrange

from src import schedule, checkin, phone, app
from src.info import apps, activities, packages, SCHEDULE_TIME


def tap_start(a):
    """
    程序需要点击桌面图标启动
    """
    return activities[a].__contains__('#')


def schedule_apps(pid, w, h):
    """
    做两次程序的定时任务
    第1次半个小时，其余的时间用来看视频
    第2次做重要的任务
    """
    minute = datetime.now().minute
    if minute < SCHEDULE_TIME:
        print('第1次做程序的定时任务 ' + datetime.now().__str__())
        for a in apps:
            getattr(schedule, a)(pid, w, h)

        # 1. 打开程序
        checkin.kuaishou(pid)

        # 2. 不停地从下往上翻页
        while datetime.now().minute < SCHEDULE_TIME:
            phone.swipe_down_to_up(pid, w, h, randrange(9, 16))

        # 3. 关闭程序
        phone.stop_app(pid, packages['kuaishou'])

    print('第2次做程序的定时任务 ' + datetime.now().__str__())
    for a in apps:
        getattr(schedule, a)(pid, w, h)


# 每个小时的收尾工作
def tail_work(pid, w, h, hour):
    if hour.__lt__(4):
        while datetime.now().hour.__eq__(hour):
            # [x] 看快手视频
            app.full_watch_kuaishou_video(pid, w, h, hour)

    elif hour.__lt__(8):
        while datetime.now().hour.__eq__(hour):
            # [x] 看抖音视频
            print('看抖音视频 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.douyin(pid)
            # 2. 看抖音视频
            app.watch_douyin_video(pid, w, h, hour)
            # 3. 关闭程序
            phone.stop_app(pid, packages['douyin'])
    elif hour.__lt__(12):
        while datetime.now().hour.__eq__(hour):
            # [x] 看火山视频
            print('看火山视频 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.huoshan(pid)
            # 2. 看火山视频
            app.watch_huoshan_video(pid, w, h, hour)
            # 3. 关闭程序
            phone.stop_app(pid, packages['huoshan'])
    elif hour.__lt__(16):
        while datetime.now().hour.__eq__(hour):
            # [x] 看微视视频
            print('看微视视频 ' + datetime.now().__str__())
            # 1. 打开程序
            checkin.weishi(pid)
            # 2. 看微视视频
            app.watch_weishi_video(pid, w, h, hour)
            # 3. 关闭程序
            phone.stop_app(pid, packages['weishi'])
    elif hour.__lt__(20):
        while datetime.now().hour.__eq__(hour):
            # [x] 看快手视频
            app.full_watch_kuaishou_video(pid, w, h, hour)
    elif hour.__lt__(24):
        while datetime.now().hour.__eq__(hour):
            # [x] 看快手视频
            app.full_watch_kuaishou_video(pid, w, h, hour)


def get_photos(path):
    photos = []
    for root, dirs, filenames in os.walk(path):
        for file in filenames:
            if os.path.splitext(file)[1].__eq__('.png'):
                photos.append(os.path.join(root, file))
    return photos
