from src import checkin, phone
from src.info import packages


# noinspection PyUnusedLocal
def toutiao(pid, w, h):
    # 打开头条
    checkin.toutiao(pid)

    # 关闭头条
    phone.stop_app(pid, packages['toutiao'])


# noinspection PyUnusedLocal
def kuaishou(pid, w, h):
    return None


# noinspection PyUnusedLocal
def douyin(pid, w, h):
    return None


# noinspection PyUnusedLocal
def huoshan(pid, w, h):
    return None


# noinspection PyUnusedLocal
def jingdong(pid, w, h):
    return None


# noinspection PyUnusedLocal
def fanqie(pid, w, h):
    return None


# noinspection PyUnusedLocal
def fanchang(pid, w, h):
    return None


# noinspection PyUnusedLocal
def weishi(pid, w, h):
    return None


# noinspection PyUnusedLocal
def shuqi(pid, w, h):
    return None


# noinspection PyUnusedLocal
def yingke(pid, w, h):
    return None


# noinspection PyUnusedLocal
def kugou(pid, w, h):
    return None


# noinspection PyUnusedLocal
def huitoutiao(pid, w, h):
    return None


# noinspection PyUnusedLocal
def zhongqing(pid, w, h):
    return None


# noinspection PyUnusedLocal
def pinduoduo(pid, w, h):
    return None


# noinspection PyUnusedLocal
def taobao(pid, w, h):
    return None


# noinspection PyUnusedLocal
def shuabao(pid, w, h):
    return None


# noinspection PyUnusedLocal
def qutoutiao(pid, w, h):
    return None


# noinspection PyUnusedLocal
def baidu(pid, w, h):
    return None
