import os
from datetime import datetime
from random import randrange

from src import schedule, checkin, phone
from src.info import apps, activities, packages

# 程序的定时任务为30分钟
SCHEDULE_TIME = 30


def tap_start(a):
    """
    程序需要点击桌面图标启动
    """
    return activities[a].__contains__('#')


def schedule_apps(pid, w, h):
    """
    程序的定时任务
    时间不够通过看视频来凑
    """
    print('做程序的定时任务 ' + datetime.now().__str__())
    for a in apps:
        getattr(schedule, a)(pid, w, h)

    minute = datetime.now().minute
    # 1. 打开程序
    if minute < SCHEDULE_TIME:
        checkin.kuaishou(pid)

    # 2. 不停地从下往上翻页
    while datetime.now().minute < SCHEDULE_TIME:
        phone.swipe_down_to_up(pid, w, h, randrange(9, 16))

    # 3. 关闭程序
    if minute < SCHEDULE_TIME:
        phone.stop_app(pid, packages['kuaishou'])


def get_photos(path):
    photos = []
    for root, dirs, filenames in os.walk(path):
        for file in filenames:
            if os.path.splitext(file)[1].__eq__('.png'):
                photos.append(os.path.join(root, file))
    return photos
