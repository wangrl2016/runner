import os
import subprocess
import time
from datetime import datetime


def go_home(pid, gap=1):
    """
    回到手机主页
    """
    subprocess.run(['adb', '-s', pid, 'shell', 'input', 'keyevent', 'KEYCODE_HOME'])
    time.sleep(gap)


def go_back(pid, times=1, gap=3):
    """
    回退到上级页面
    """
    for i in range(0, times):
        subprocess.run(['adb', '-s', pid, 'shell', 'input', 'keyevent', 'KEYCODE_BACK'])
        time.sleep(gap)


def swipe_down_to_up(pid, w, h, gap=3, internal=200):
    """
    从下往上滑动屏幕
    """
    subprocess.run(['adb', '-s', pid, 'shell', 'input', 'swipe',
                    str(int(w / 2)), str(int(h * 3 / 4)),
                    str(int(w / 2)), str(int(h * 1 / 4)),
                    str(internal)])
    time.sleep(gap)


def swipe_up_to_down(pid, w, h, gap=3, internal=200):
    """
    从上往下滑动屏幕
    """
    subprocess.call(['adb', '-s', pid, 'shell', 'input', 'swipe',
                     str(int(w / 2)), str(int(h * 1 / 4)),
                     str(int(w / 2)), str(int(h * 3 / 4)),
                     str(internal)])
    time.sleep(gap)


def swipe_right_to_left(pid, w, h, gap=3, internal=200):
    """
    从右往左滑动屏幕
    """
    subprocess.call(['adb', '-s', pid, 'shell', 'input', 'swipe',
                     str(int(w * 3 / 4)), str(int(h / 2)),
                     str(int(w * 1 / 4)), str(int(h / 2)),
                     str(internal)])
    time.sleep(gap)


def swipe_left_to_right(pid, w, h, gap=3, internal=200):
    """
    从右往左滑动屏幕
    """
    subprocess.call(['adb', '-s', pid, 'shell', 'input', 'swipe',
                     str(int(w * 1 / 4)), str(int(h / 2)),
                     str(int(w * 3 / 4)), str(int(h / 2)),
                     str(internal)])
    time.sleep(gap)


def screenshot(pid, gap=1):
    """
    截取手机屏幕
    :return:截取图片文件名称
    """
    filename = '/sdcard/' + datetime.now().__str__() + '.png'
    subprocess.run(['adb', '-s', pid, 'shell', 'screencap', '-p', filename])
    time.sleep(gap)
    return filename


def get_screenshot(pid, filename, output=".", gap=1):
    """
    获取手机上的截图
    """
    subprocess.run(['adb', '-s', pid, 'pull', filename, output])
    time.sleep(gap)


def remove_screenshot(pid, filename, gap=1):
    """
    删除手机上的截图
    """
    subprocess.run(['adb', '-s', pid, 'shell', 'rm', filename])
    time.sleep(gap)


def get_page_photo(pid, output, gap=1):
    """
    获取手机的页面
    """
    filename = datetime.now().date().__str__() + '_' + datetime.now().time().__str__() + '.png'
    path = os.path.join('/sdcard', filename)
    subprocess.run(['adb', '-s', pid, 'shell', 'screencap', '-p', path])
    time.sleep(gap)
    subprocess.run(['adb', '-s', pid, 'pull', path, output],
                   check=True, stdout=subprocess.PIPE,
                   stderr=subprocess.STDOUT, universal_newlines=True)
    time.sleep(gap)
    subprocess.run(['adb', '-s', pid, 'shell', 'rm', path])
    time.sleep(gap)
    return filename


def stop_app(pid, package, gap=1):
    """
    关闭程序
    """
    subprocess.run(['adb', '-s', pid, 'shell', 'am', 'force-stop', package])
    time.sleep(gap)


def start_app(pid, activity, gap=15):
    """
    启动程序
    """
    subprocess.run(['adb', '-s', pid, 'shell', 'am', 'start', '-n', activity])
    time.sleep(gap)


def list_packages(pid, gap=1):
    """
    获取程序包名
    :return: 包含包名的字符串
    """
    p = subprocess.run(['adb', '-s', pid, 'shell', 'pm', 'list', 'package'],
                       check=True, stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT, universal_newlines=True)
    time.sleep(gap)
    return p.stdout


def power(pid, gap=3):
    """
    关闭或者点亮屏幕
    """
    subprocess.run(['adb', '-s', pid, 'shell', 'input', 'keyevent', 'KEYCODE_POWER'])
    time.sleep(gap)


def get_top_activities(pid, gap=1):
    """
    获取最上面的activity名称
    :return: activity名称
    """
    p = subprocess.run(['adb', '-s', pid, 'shell', 'dumpsys', 'activity', 'top'],
                       check=True, stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT, universal_newlines=True)
    time.sleep(gap)

    return p.stdout


def sleep_to_weak(pid, w, h, gap=300):
    """
    手机休息到唤醒
    """
    print('手机休息时间 ' + datetime.now().__str__())
    power(pid)
    time.sleep(gap)
    power(pid)
    swipe_down_to_up(pid, w, h)


def get_size(pid):
    """
    获取手机的像素点大小
    """
    p = subprocess.run(['adb', '-s', pid, 'shell', 'wm', 'size'], check=True, stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT, universal_newlines=True)
    time.sleep(2)
    size_str = p.stdout.strip('\n')
    print(size_str)
    for s in size_str.split(' '):
        if s.rfind('x') > 0:
            return int(s.split('x')[0]), int(s.split('x')[1])


def get_devices():
    """
    获取连接上电脑的设备
    """
    p = subprocess.run(['adb', 'devices'], check=True, stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT, universal_newlines=True)
    time.sleep(1)
    devices = []
    for line in p.stdout.split('\n'):
        line = line.strip('\n')
        if len(line) == 0 or line.__contains__('List') or line.__contains__('*'):
            continue
        # 以whitespace分开
        devices.append(line.split()[0].strip('\\s+'))
    return devices


def reboot(devices):
    """
    重启设备
    """
    for pid in devices:
        subprocess.run(['adb', '-s', pid, 'reboot'])
        time.sleep(120)


def get_device_properties(pid):
    """
    获取手机的属性
    """
    properties = []
    p = subprocess.run(['adb', '-s', pid, 'shell', 'getprop'], check=True, stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT, universal_newlines=True)
    for line in p.stdout.split('\n'):
        line.strip('\n')
        properties.append(line)
    return properties
