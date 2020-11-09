import inspect

from src import phone, input
from src.info import activities, WIDTH, HEIGHT

# 对于无法通过Activity进行启动的图标需要定位
# 不同手机位置不同
# 设置成为4x6的图标布局模式
ROWS = [1.4, 3.4, 5.4, 7.4, 9.4, 11.4]
COLUMNS = [1.0, 2.6, 4.2, 5.8]


def toutiao(pid, gap=10):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    # 头条进入首页是空等时间
    # 所以设定启动程序的时间要短
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def kuaishou(pid, gap=10):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def douyin(pid, gap=10):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def huoshan(pid, gap=10):
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
    input.tap(pid, COLUMNS[0] * w / WIDTH, ROWS[1] * h / HEIGHT, gap)


def fanqie(pid, w, h, gap=10):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 模仿启动输出
    print('Staring: Intent { cmp=' + activities[inspect.getframeinfo(inspect.currentframe()).function.__str__()] + ' }')
    # 2. 启动程序
    input.tap(pid, COLUMNS[1] * w / WIDTH, ROWS[1] * h / HEIGHT, gap)


def fanchang(pid, w, h, gap=10):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 模仿启动输出
    print('Staring: Intent { cmp=' + activities[inspect.getframeinfo(inspect.currentframe()).function.__str__()] + ' }')
    # 2. 启动程序
    input.tap(pid, COLUMNS[2] * w / WIDTH, ROWS[1] * h / HEIGHT, gap)


def kuchang(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 模仿启动输出
    print('Staring: Intent { cmp=' + activities[inspect.getframeinfo(inspect.currentframe()).function.__str__()] + ' }')
    # 2. 启动程序
    input.tap(pid, COLUMNS[3] * w / WIDTH, ROWS[1] * h / HEIGHT, gap)


# def weishi(pid, gap=15):
#     # 1. 回到手机主界面
#     phone.go_home(pid)
#     # 2. 启动程序
#     phone.start_app(pid, activities[
#         inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def shuqi(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 模仿启动输出
    print('Staring: Intent { cmp=' + activities[inspect.getframeinfo(inspect.currentframe()).function.__str__()] + ' }')
    # 2. 启动程序
    input.tap(pid, COLUMNS[0] * w / WIDTH, ROWS[2] * h / HEIGHT, gap)


def yingke(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 模仿启动输出
    print('Staring: Intent { cmp=' + activities[inspect.getframeinfo(inspect.currentframe()).function.__str__()] + ' }')
    # 2. 启动程序
    input.tap(pid, COLUMNS[1] * w / WIDTH, ROWS[2] * h / HEIGHT, gap)


def kugou(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 模仿启动输出
    print('Staring: Intent { cmp=' + activities[inspect.getframeinfo(inspect.currentframe()).function.__str__()] + ' }')
    # 2. 启动程序
    input.tap(pid, COLUMNS[2] * w / WIDTH, ROWS[2] * h / HEIGHT, gap)


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
    input.tap(pid, COLUMNS[0] * w / WIDTH, ROWS[3] * h / HEIGHT, gap)


def pinduoduo(pid, w, h, gap=10):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 模仿启动输出
    print('Staring: Intent { cmp=' + activities[inspect.getframeinfo(inspect.currentframe()).function.__str__()] + ' }')
    # 2. 启动程序
    input.tap(pid, COLUMNS[1] * w / WIDTH, ROWS[3] * h / HEIGHT, gap)


def kuaiyin(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 模仿启动输出
    print('Staring: Intent { cmp=' + activities[inspect.getframeinfo(inspect.currentframe()).function.__str__()] + ' }')
    # 2. 启动程序
    input.tap(pid, COLUMNS[2] * w / WIDTH, ROWS[3] * h / HEIGHT, gap)


def tangdou(pid, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


# def taobao(pid, gap=10):
#     # 1. 回到手机主界面
#     phone.go_home(pid)
#     # 2. 启动程序
#     phone.start_app(pid, activities[
#         inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)
#
#
# def shuabao(pid, gap=15):
#     # 1. 回到手机主界面
#     phone.go_home(pid)
#     # 2. 启动程序
#     phone.start_app(pid, activities[
#         inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)
#
#

#
#
# def ximalaya(pid, gap=15):
#     # 1. 回到手机主界面
#     phone.go_home(pid)
#     # 2. 启动程序
#     phone.start_app(pid, activities[
#         inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)

def dongfang(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 模仿启动输出
    print('Staring: Intent { cmp=' + activities[inspect.getframeinfo(inspect.currentframe()).function.__str__()] + ' }')
    # 2. 启动程序
    input.tap(pid, COLUMNS[0] * w / WIDTH, ROWS[4] * h / HEIGHT, gap)


def jukandian(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 模仿启动输出
    print('Staring: Intent { cmp=' + activities[inspect.getframeinfo(inspect.currentframe()).function.__str__()] + ' }')
    # 2. 启动程序
    input.tap(pid, COLUMNS[1] * w / WIDTH, ROWS[4] * h / HEIGHT, gap)


def kankuai(pid, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def douhuo(pid, gap=10):
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
    input.tap(pid, COLUMNS[0] * w / WIDTH, ROWS[5] * h / HEIGHT, gap)


def makan(pid, w, h, gap=20):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 模仿启动输出
    print('Staring: Intent { cmp=' + activities[inspect.getframeinfo(inspect.currentframe()).function.__str__()] + ' }')
    # 2. 启动程序
    input.tap(pid, COLUMNS[1] * w / WIDTH, ROWS[5] * h / HEIGHT, gap)


def diandian(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    print('Staring: Intent { cmp=' + activities[inspect.getframeinfo(inspect.currentframe()).function.__str__()] + ' }')
    # 2. 启动程序
    input.tap(pid, COLUMNS[2] * w / WIDTH, ROWS[5] * h / HEIGHT, gap)


def moji(pid, gap=10):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def weixin(pid, gap=10):
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
