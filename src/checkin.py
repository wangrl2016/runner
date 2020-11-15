import inspect

from src import phone, input
from src.info import activities, WIDTH, HEIGHT

# 对于无法通过Activity进行启动的图标需要定位
# 不同手机位置不同
# 设置成为4x6的图标布局模式
ROWS = [1.4, 3.4, 5.4, 7.4, 9.4, 11.4]
COLUMNS = [1.0, 2.6, 4.2, 5.8]


def midu(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    input.tap(pid, COLUMNS[0] * w / WIDTH, ROWS[0] * h / HEIGHT, gap)


def changdou(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    input.tap(pid, COLUMNS[1] * w / WIDTH, ROWS[0] * h / HEIGHT, gap)


def kulingyin(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    input.tap(pid, COLUMNS[2] * w / WIDTH, ROWS[0] * h / HEIGHT, gap)


def lanmao(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    input.tap(pid, COLUMNS[3] * w / WIDTH, ROWS[0] * h / HEIGHT, gap)


def jingdong(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    input.tap(pid, COLUMNS[0] * w / WIDTH, ROWS[1] * h / HEIGHT, gap)


def fanqie(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    input.tap(pid, COLUMNS[1] * w / WIDTH, ROWS[1] * h / HEIGHT, gap)


def fanchang(pid, w, h, gap=10):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    input.tap(pid, COLUMNS[2] * w / WIDTH, ROWS[1] * h / HEIGHT, gap)


def kuchang(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    input.tap(pid, COLUMNS[3] * w / WIDTH, ROWS[1] * h / HEIGHT, gap)


def shuqi(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    input.tap(pid, COLUMNS[0] * w / WIDTH, ROWS[2] * h / HEIGHT, gap)


def yingke(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    input.tap(pid, COLUMNS[1] * w / WIDTH, ROWS[2] * h / HEIGHT, gap)


def kugou(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    input.tap(pid, COLUMNS[2] * w / WIDTH, ROWS[2] * h / HEIGHT, gap)


def youliao(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    input.tap(pid, COLUMNS[3] * w / WIDTH, ROWS[2] * h / HEIGHT, gap)


def zhongqing(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    input.tap(pid, COLUMNS[0] * w / WIDTH, ROWS[3] * h / HEIGHT, gap)


def pinduoduo(pid, w, h, gap=10):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    input.tap(pid, COLUMNS[1] * w / WIDTH, ROWS[3] * h / HEIGHT, gap)


def kuaiyin(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    input.tap(pid, COLUMNS[2] * w / WIDTH, ROWS[3] * h / HEIGHT, gap)


def quhongbao(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    input.tap(pid, COLUMNS[3] * w / WIDTH, ROWS[3] * h / HEIGHT, gap)


def dongfang(pid, w, h, gap=10):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    input.tap(pid, COLUMNS[0] * w / WIDTH, ROWS[4] * h / HEIGHT, gap)


def jukandian(pid, w, h, gap=20):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    input.tap(pid, COLUMNS[1] * w / WIDTH, ROWS[4] * h / HEIGHT, gap)


def qukankan(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    input.tap(pid, COLUMNS[2] * w / WIDTH, ROWS[4] * h / HEIGHT, gap)


def miaokan(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    input.tap(pid, COLUMNS[3] * w / WIDTH, ROWS[4] * h / HEIGHT, gap)


def kuge(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    input.tap(pid, COLUMNS[0] * w / WIDTH, ROWS[5] * h / HEIGHT, gap)


def makan(pid, w, h, gap=18):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    input.tap(pid, COLUMNS[1] * w / WIDTH, ROWS[5] * h / HEIGHT, gap)


def diandian(pid, w, h, gap=18):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    input.tap(pid, COLUMNS[2] * w / WIDTH, ROWS[5] * h / HEIGHT, gap)


def xiuqiu(pid, w, h, gap=15):
    # 1. 回到手机主界面
    phone.go_home(pid)
    # 2. 启动程序
    input.tap(pid, COLUMNS[3] * w / WIDTH, ROWS[5] * h / HEIGHT, gap)


# 25-48

def toutiao(pid, gap=10):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def kuaishou(pid, gap=10):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def douyin(pid, gap=10):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def huoshan(pid, gap=10):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def qutoutiao(pid, gap=15):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def baidu(pid, gap=15):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def weishi(pid, gap=15):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def ximalaya(pid, gap=15):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def wuba(pid, gap=10):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def taobao(pid, gap=10):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def shuabao(pid, gap=10):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def qqyuedu(pid, gap=10):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def chejia(pid, gap=10):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def uc(pid, gap=10):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def kuaikandian(pid, gap=10):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def hongshi(pid, gap=15):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def doudou(pid, gap=15):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def qimao(pid, gap=15):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def kankuai(pid, gap=10):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def douhuo(pid, gap=10):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def moji(pid, gap=10):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def ersansi(pid, gap=15):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def tangdou(pid, gap=15):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def yangchong(pid, gap=15):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


# 49-72

def weixin(pid, gap=10):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def sougou(pid, gap=10):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def zhuanshi(pid, gap=10):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)


def qizhu(pid, gap=10):
    phone.start_app(pid, activities[
        inspect.getframeinfo(inspect.currentframe()).function.__str__()], gap)
