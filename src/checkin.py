import inspect

from src import phone, input
from src.info import activities, WIDTH, HEIGHT


def toutiao(pid):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()])


def kuaishou(pid):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()])


def douyin(pid):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()])


def huoshan(pid):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()])


def jingdong(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 模仿启动输出
    print('Staring: Intent { cmp=' + activities[inspect.getframeinfo(inspect.currentframe()).function.__str__()] + ' }')
    # 2. 启动程序
    input.tap(pid, 1.0 * w / WIDTH, 3.7 * h / HEIGHT, gap)  # <= modify


def fanqie(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 模仿启动输出
    print('Staring: Intent { cmp=' + activities[inspect.getframeinfo(inspect.currentframe()).function.__str__()] + ' }')
    # 2. 启动程序
    input.tap(pid, 2.6 * w / WIDTH, 3.7 * h / HEIGHT, gap)  # <= modify


def fanchang(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 模仿启动输出
    print('Staring: Intent { cmp=' + activities[inspect.getframeinfo(inspect.currentframe()).function.__str__()] + ' }')
    # 2. 启动程序
    input.tap(pid, 4.2 * w / WIDTH, 3.7 * h / HEIGHT, gap)  # <= modify
