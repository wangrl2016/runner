import inspect

from src import phone
from src.info import activities


def toutiao(pid):
    # 1. 回到手机主页
    phone.go_home(pid)
    # 2. 启动程序
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()])


def kuaishou(pid):
    # 1. 回到手机主页
    phone.go_home(pid)
    # 2. 启动程序
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()])


def douyin(pid):
    # 1. 回到手机主页
    phone.go_home(pid)
    # 2. 启动程序
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()])


def huoshan(pid):
    # 1. 回到手机主页
    phone.go_home(pid)
    # 2. 启动程序
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()])
