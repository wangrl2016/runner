import argparse
import ctypes
import inspect
import os
import subprocess
import threading
import tkinter as tk
from datetime import datetime
from random import randrange

from PIL import Image, ImageTk

import runner
from src import phone, info, utils
from src import input
import cairosvg
from io import BytesIO
import shutil

from src.info import activities


def _async_raise(tid, exctype):
    if not inspect.isclass(exctype):
        raise TypeError("Only types can be raised (not instances)")
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid), ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


def close_top_app():
    print('关闭当前程序 ' + datetime.now().time().__str__())
    for pid in devices:
        top_activities = phone.get_top_activities(pid)
        if top_activities is None:
            return
        for a in info.apps:
            if top_activities.__contains__(info.packages[a]):
                phone.stop_app(pid, info.packages[a], 0.1)


def start_auto_running():
    pts = {}
    runner_threads.clear()
    for pid in devices:
        info.contexts.update({pid: {}})
        t = threading.Thread(target=runner.run, args=(pid,), daemon=True)
        runner_threads.append(t)
        pts[pid] = t.ident
        t.start()


def stop_auto_running():
    for t in runner_threads:
        if t.is_alive():
            stop_thread(t)


class Point(object):
    """
    Creates a point on a coordinate with values x and y.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.continue_update_image = True
        self.auto_system_start = True

        self.point0 = Point(0, 0)
        self.point1 = Point(0, 0)

        self.image_frame = tk.Frame(self, width=w * scale, height=h * scale, bg='white')
        self.operate_frame = tk.Frame(self, width=w * scale, height=h * scale, bg='beige')

        self.button_frame = tk.Frame(self.operate_frame)

        self.phone_list = tk.Listbox(self.operate_frame)

        for pid in devices:
            self.phone_list.insert(tk.END, pid)

        img = Image.new(mode='RGB', size=(int(w * scale), int(h * scale)), color='white')
        img = ImageTk.PhotoImage(image=img)

        self.image_label = tk.Label(self.image_frame)

        self.image_label.config(image=img)
        self.image_label.image = img

        self.home = tk.Button(self.button_frame, text='回到主页', command=self.go_home)
        self.reboot = tk.Button(self.button_frame, text='重启手机', command=self.reboot)
        self.update = tk.Button(self.button_frame, text='更新代码', command=self.update_code)
        self.close_top_app = tk.Button(self.button_frame, text='关闭当前程序', command=close_top_app)
        self.hand_system = tk.Button(self.button_frame, text='手动系统已开启', bg='green', command=self.hand_system)
        self.auto_system = tk.Button(self.button_frame, text='自动系统已开启', bg='green', command=self.auto_system)

        img = cairosvg.svg2png(url='res/arrow_forward.svg')
        img = Image.open(BytesIO(img))
        img = ImageTk.PhotoImage(image=img)
        self.arrow_forward = tk.Label(self.operate_frame)
        self.arrow_forward.config(image=img)
        self.arrow_forward.image = img

        img = cairosvg.svg2png(url='res/arrow_back.svg')
        img = Image.open(BytesIO(img))
        img = ImageTk.PhotoImage(image=img)
        self.arrow_back = tk.Label(self.operate_frame)
        self.arrow_back.config(image=img)
        self.arrow_back.image = img

        img = cairosvg.svg2png(url='res/arrow_upward.svg')
        img = Image.open(BytesIO(img))
        img = ImageTk.PhotoImage(image=img)
        self.arrow_upward = tk.Label(self.operate_frame)
        self.arrow_upward.config(image=img)
        self.arrow_upward.image = img

        img = cairosvg.svg2png(url='res/arrow_downward.svg')
        img = Image.open(BytesIO(img))
        img = ImageTk.PhotoImage(image=img)
        self.arrow_downward = tk.Label(self.operate_frame)
        self.arrow_downward.config(image=img)
        self.arrow_downward.image = img

        self.master = master
        self.pack()

        self.create_widgets()

        self.prev_img = None

    def exit_system(self):
        print('退出程序 ' + datetime.now().__str__())
        if self.auto_system_start:
            stop_auto_running()
        self.master.destroy()

    def hand_system(self):
        # 是否停止更新图片
        self.continue_update_image = not self.continue_update_image
        if self.continue_update_image:
            self.hand_system['text'] = '手动系统已开启'
            self.hand_system['bg'] = 'green'
            self.update_page()
        else:
            self.hand_system['text'] = '开启手动已关闭'
            self.hand_system['bg'] = 'red'

    def auto_system(self):
        print(('关闭' if self.auto_system_start else '开启') + '自动系统 ' + datetime.now().__str__())
        if self.auto_system_start:
            stop_auto_running()
            self.auto_system['text'] = '自动系统已关闭'
            self.auto_system['bg'] = 'red'
        else:
            start_auto_running()
            self.auto_system['text'] = '自动系统已开启'
            self.auto_system['bg'] = 'green'
        self.auto_system_start = not self.auto_system_start

    def create_widgets(self):
        self.image_frame.pack_propagate(0)  # 固定frame的大小
        self.image_frame.pack(side='left')
        self.operate_frame.pack_propagate(0)
        self.operate_frame.pack(side='left')

        self.button_frame.pack(side='top')

        self.image_label.bind('<Button-1>', self.mouse_left_click)  # 鼠标左键单击
        self.image_label.bind('<Button-2>', self.mouse_center_click)  # 鼠标中键单击
        self.image_label.bind('<Button-3>', self.mouse_right_click)  # 鼠标右键单击
        self.image_label.bind('<ButtonRelease-1>', self.mouse_left_release)  # 鼠标左键释放
        self.image_label.bind('<ButtonRelease-2>', self.mouse_center_release)  # 鼠标中键释放
        # self.image_label.bind('<B1-Motion>', self.mouse_left_drag)
        # self.image_label.bind('<B3-Motion>', self.mouse_right_drag)

        # self.image_label.bind('<MouseWheel>', self.vertical_swipe)  # 鼠标滚轮上下滚动
        self.image_label.bind('<KeyPress>', self.keyboard_press)

        self.image_label.focus_set()
        self.image_label.pack()

        self.phone_list.pack(side='top')

        # 第0排按钮
        self.close_top_app.grid(row=0, column=0)
        self.hand_system.grid(row=0, column=1)
        self.auto_system.grid(row=0, column=2)

        # 第1排按钮
        self.home.grid(row=1, column=0)
        self.update.grid(row=1, column=1)
        self.reboot.grid(row=1, column=2)

        self.arrow_forward.pack(side='left')
        self.arrow_back.pack(side='left')
        self.arrow_upward.pack(side='left')
        self.arrow_downward.pack(side='left')

    @staticmethod
    def mouse_left_click(event):
        print('点击鼠标左键 (' + str(event.x) + ', ' + str(event.y) + ')')
        threads = []
        for pid in devices:
            tid = threading.Thread(target=phone.tap, args=(pid, int(event.x / scale), int(event.y / scale)))
            threads.append(tid)
            tid.start()
        # 等待每个任务结束
        # for tid in threads:
        #     tid.join()

    def mouse_center_click(self, event):
        print('点击鼠标中键 (' + str(event.x) + ', ' + str(event.y) + ')')
        self.point0.set_x(event.x)
        self.point0.set_y(event.y)

    @staticmethod
    def mouse_right_click(event):
        print('点击鼠标右键 (' + str(event.x) + ', ' + str(event.y) + ')')
        threads = []
        for pid in devices:
            tid = threading.Thread(target=phone.go_back, args=(pid,))
            threads.append(tid)
            tid.start()
        #
        # for tid in threads:
        #     tid.join()

    @staticmethod
    def mouse_left_release(event):
        print('mouse left release ' + str(event.x) + ', ' + str(event.y))
        return None

    def mouse_center_release(self, event):
        # print('mouse center release (' + str(event.x) + ', ' + str(event.y) + ')')
        self.point1.set_x(event.x)
        self.point1.set_y(event.y)
        self.hand_swipe()

    def hand_swipe(self):
        threads = []
        for pid in devices:
            tid = threading.Thread(target=input.swipe,
                                   args=(pid, self.point0.get_x() / scale,
                                         self.point0.get_y() / scale,
                                         self.point1.get_x() / scale,
                                         self.point1.get_y() / scale,
                                         randrange(190, 230)))
            threads.append(tid)
            tid.start()

        # for tid in threads:
        #     tid.join()

    @staticmethod
    def mouse_left_drag(event):
        print('mouse left drag ' + str(event.x) + ', ' + str(event.y))

    @staticmethod
    def mouse_right_drag(event):
        print('mouse right drag ' + str(event.x) + ', ' + str(event.y))

    @staticmethod
    def keyboard_press(event):
        print('按键事件 ' + event.keysym)

    @staticmethod
    def reboot():
        print('手机重启 ' + datetime.now().time().__str__())
        threads = []
        for pid in devices:
            tid = threading.Thread(target=phone.reboot, args=(pid,))
            threads.append(tid)
            tid.start()

    @staticmethod
    def go_home():
        print('回到主页 ' + datetime.now().time().__str__())
        threads = []
        for pid in devices:
            tid = threading.Thread(target=phone.go_home, args=(pid,))
            threads.append(tid)
            tid.start()

    @staticmethod
    def go_back():
        print('返回上级页面 ' + datetime.now().time().__str__())
        threads = []
        for pid in devices:
            tid = threading.Thread(target=phone.go_back, args=(pid,))
            threads.append(tid)
            tid.start()

    def update_page(self):
        # print('update page start ' + datetime.now().time().__str__())
        update_page_thread = UpdatePageThread(devices[0], out_dir)
        update_page_thread.start()
        update_page_thread.join()

        file_path = update_page_thread.get_file_path()
        try:
            # 可能中途拔掉手机
            img = Image.open(out_dir + file_path).resize((int(w * scale), int(h * scale)))
        except Exception as e:
            print(e)
            return None

        img = ImageTk.PhotoImage(image=img)
        self.image_label.config(image=img)
        self.image_label.image = img

        if self.prev_img:
            os.remove(out_dir + file_path)

        self.prev_img = file_path

        # print('update page end ' + datetime.now().time().__str__())
        if self.continue_update_image:
            root.after(50, self.update_page)

    @staticmethod
    def update_code():
        print('更新代码 ' + datetime.now().time().__str__())
        subprocess.run(['git', 'checkout', 'https://username:password@github.com/wangrl2016/runner'])


class UpdatePageThread(threading.Thread):
    def __init__(self, pid, od):
        threading.Thread.__init__(self)
        self.pid = pid
        self.out_dir = od
        self.file_path = ''

    def run(self):
        self.file_path = phone.get_page_photo(devices[0], out_dir)

    def get_file_path(self):
        return self.file_path


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='PROG', conflict_handler='resolve')
    parser.add_argument('-s', '--serial', help='phone serial number')

    runner_threads = []

    # 初始化全局变量
    info.apps = list(activities.keys())
    info.packages = utils.get_packages_dict(activities)

    root = tk.Tk()

    root.title('手机手动控制系统')

    devices = phone.get_devices()
    if devices.__contains__('13bfd6e6'):
        devices.remove('13bfd6e6')
    if devices.__contains__('8aa89ae87d94'):
        devices.remove('8aa89ae87d94')
    if not devices:
        print('没有发现手机设备')
        exit(0)

    start_auto_running()

    out_dir = 'out/'

    (w, h) = phone.get_size(devices[0])

    scale = 0.5

    app = Application(master=root)

    hand_thread = threading.Thread(target=root.after, args=(50, app.update_page), daemon=True)
    hand_thread.start()

    app.mainloop()

    shutil.rmtree(out_dir)
    os.mkdir(out_dir)
