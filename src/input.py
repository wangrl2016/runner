import subprocess
import time

"""
The commands and default sources are:
    text <string> (Default: touchscreen)
    keyevent [--longpress] <key code number or name> ... (Default: keyboard)
    tap <x> <y> (Default: touchscreen)
    swipe <x1> <y1> <x2> <y2> [duration(ms)] (Default: touchscreen)
    draganddrop <x1> <y1> <x2> <y2> [duration(ms)] (Default: touchscreen)
"""


def text(p_id, txt):
    """
    输入文字
    :param p_id: 手机标识符
    :param txt: 想要输入的文本
    """
    subprocess.run(['adb', '-s', p_id, 'shell', 'input', 'text', txt])
    time.sleep(3)


def keyevent(p_id, code, gap=3):
    """
    按键事件
    """
    subprocess.run(['adb', '-s', p_id, 'shell', 'input', 'keyevent', code])
    time.sleep(gap)


def tap(p_id, w, h, gap=5):
    """
    以像素点点击屏幕坐标为(px, py)的位置
    """
    subprocess.run(['adb', '-s', p_id, 'shell', 'input', 'tap', str(int(w)), str(int(h))])
    time.sleep(gap)


def swipe(p_id, w1, h1, w2, h2, internal=200, gap=3):
    """
    滑动事件
    """
    subprocess.run(['adb', '-s', p_id, 'shell', 'input', 'swipe',
                    str(int(w1)), str(int(h1)),
                    str(int(w2)), str(int(h2)), str(internal)])
    time.sleep(gap)
