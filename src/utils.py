from datetime import datetime

from src import schedule
from src.info import packages, apps


def tap_start(a):
    """
    程序需要点击桌面图标启动
    """
    return packages[a].__contains__('#')


def schedule_apps(p_id, w, h):
    """
    程序的定时任务
    """
    print('做程序的定时任务 ' + datetime.now().__str__())
    for a in apps:
        getattr(schedule, a)(p_id, w, h)
