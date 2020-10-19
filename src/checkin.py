import inspect

from src import phone, input
from src.info import activities, WIDTH, HEIGHT


def toutiao(pid, gap=10):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    # 头条进入首页是空等时间
    # 所以设定启动程序的时间要短
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def kuaishou(pid, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def douyin(pid, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def huoshan(pid, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def jingdong(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 模仿启动输出
    print('Staring: Intent { cmp=' + activities[inspect.getframeinfo(inspect.currentframe()).function.__str__()] + ' }')
    # 2. 启动程序
    input.tap(pid, 1.0 * w / WIDTH, 3.4 * h / HEIGHT, gap)  # <= modify


def fanqie(pid, w, h, gap=10):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 模仿启动输出
    print('Staring: Intent { cmp=' + activities[inspect.getframeinfo(inspect.currentframe()).function.__str__()] + ' }')
    # 2. 启动程序
    input.tap(pid, 2.6 * w / WIDTH, 3.4 * h / HEIGHT, gap)  # <= modify


def fanchang(pid, w, h, gap=10):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 模仿启动输出
    print('Staring: Intent { cmp=' + activities[inspect.getframeinfo(inspect.currentframe()).function.__str__()] + ' }')
    # 2. 启动程序
    input.tap(pid, 4.2 * w / WIDTH, 3.4 * h / HEIGHT, gap)  # <= modify


def weishi(pid, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def shuqi(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 模仿启动输出
    print('Staring: Intent { cmp=' + activities[inspect.getframeinfo(inspect.currentframe()).function.__str__()] + ' }')
    # 2. 启动程序
    input.tap(pid, 1.0 * w / WIDTH, 5.4 * h / HEIGHT, gap)  # <= modify


def yingke(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 模仿启动输出
    print('Staring: Intent { cmp=' + activities[inspect.getframeinfo(inspect.currentframe()).function.__str__()] + ' }')
    # 2. 启动程序
    input.tap(pid, 2.6 * w / WIDTH, 5.4 * h / HEIGHT, gap)  # <= modify


def kugou(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 模仿启动输出
    print('Staring: Intent { cmp=' + activities[inspect.getframeinfo(inspect.currentframe()).function.__str__()] + ' }')
    # 2. 启动程序
    input.tap(pid, 4.2 * w / WIDTH, 5.4 * h / HEIGHT, gap)  # <= modify


def huitoutiao(pid, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def zhongqing(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 模仿启动输出
    print('Staring: Intent { cmp=' + activities[inspect.getframeinfo(inspect.currentframe()).function.__str__()] + ' }')
    # 2. 启动程序
    input.tap(pid, 1.0 * w / WIDTH, 7.4 * h / HEIGHT, gap)  # <= modify


def pinduoduo(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 模仿启动输出
    print('Staring: Intent { cmp=' + activities[inspect.getframeinfo(inspect.currentframe()).function.__str__()] + ' }')
    # 2. 启动程序
    input.tap(pid, 2.6 * w / WIDTH, 7.4 * h / HEIGHT, gap)  # <= modify


def taobao(pid, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def shuabao(pid, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def qutoutiao(pid, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def baidu(pid, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def ximalaya(pid, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def douhuo(pid, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def kuge(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 模仿启动输出
    print('Staring: Intent { cmp=' + activities[inspect.getframeinfo(inspect.currentframe()).function.__str__()] + ' }')
    # 2. 启动程序
    input.tap(pid, 1.0 * w / WIDTH, (HEIGHT - 3.5) * h / HEIGHT, gap)  # <= modify
    return None
