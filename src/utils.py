import os
from datetime import datetime

from src import schedule
from src.info import apps, activities


def tap_start(a):
    """
    程序需要点击桌面图标启动
    """
    return activities[a].__contains__('#')


def schedule_apps(p_id, w, h):
    """
    程序的定时任务
    """
    print('做程序的定时任务 ' + datetime.now().__str__())
    for a in apps:
        getattr(schedule, a)(p_id, w, h)


def get_photos(path):
    photos = []
    for root, dirs, filenames in os.walk(path):
        for file in filenames:
            if os.path.splitext(file)[1].__eq__('.png'):
                photos.append(os.path.join(root, file))
    return photos
