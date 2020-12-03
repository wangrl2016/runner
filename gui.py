import os
import threading
import tkinter as tk
from datetime import datetime

from PIL import Image, ImageTk
from src import phone
import cairosvg
from io import BytesIO
import shutil


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.continue_update_image = False

        self.image_frame = tk.Frame(self, width=w * scale, height=h * scale, bg='white')
        self.operate_frame = tk.Frame(self, width=w * scale, height=h * scale, bg='beige')

        self.phone_list = tk.Listbox(self.operate_frame)

        for i in range(0, 10):
            self.phone_list.insert(tk.END, i)

        img = Image.new(mode='RGB', size=(int(w * scale), int(h * scale)), color='white')
        img = ImageTk.PhotoImage(image=img)

        self.image_label = tk.Label(self.image_frame)

        self.image_label.config(image=img)
        self.image_label.image = img

        self.home = tk.Button(self.operate_frame, text='主页', command=self.go_home)
        self.back = tk.Button(self.operate_frame, text='返回', command=self.go_back)
        self.reboot = tk.Button(self.operate_frame, text='重启', command=self.reboot)
        self.update = tk.Button(self.operate_frame, text='更新', command=self.update_code)
        self.exit = tk.Button(self.operate_frame, text='退出', command=self.master.destroy)
        self.close_top_app = tk.Button(self.operate_frame, text='关闭当前程序')

        self.hand_system = tk.Button(self.operate_frame, text='开启手动系统', command=self.hand_system)

        self.start_auto_system = tk.Button(self.operate_frame, text='开启自动系统')
        self.stop_auto_system = tk.Button(self.operate_frame, text='停止自动系统')

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

    def hand_system(self):
        # 是否停止更新图片
        self.continue_update_image = not self.continue_update_image
        if self.continue_update_image:
            self.hand_system['text'] = '关闭手动系统'
            self.update_page()
        else:
            self.hand_system['text'] = '开启手动系统'

    def create_widgets(self):
        self.image_frame.pack_propagate(0)  # 固定frame的大小
        self.image_frame.pack(side='left')
        self.operate_frame.pack_propagate(0)
        self.operate_frame.pack(side='left')

        self.image_label.bind('<Button-1>', self.mouse_left_click)  # 鼠标左键单击
        self.image_label.bind('<Button-2>', self.mouse_center_click)  # 鼠标中键单击
        self.image_label.bind('<Button-3>', self.mouse_right_click)  # 鼠标右键单击
        self.image_label.bind('<B1-Motion>', self.mouse_left_drag)
        self.image_label.bind('<B2-Motion>', self.mouse_center_drag)
        self.image_label.bind('<B3-Motion>', self.mouse_right_drag)

        self.image_label.bind('<MouseWheel>', self.vertical_swipe)  # 鼠标滚轮上下滚动
        self.image_label.bind('<Key>', self.keyboard_press)  # 键盘事件

        self.image_label.pack()

        self.phone_list.pack(side='left')

        self.home.pack(side='bottom')
        self.back.pack(side='bottom')
        self.update.pack(side='bottom')
        self.reboot.pack(side='bottom')
        self.exit.pack(side='bottom')
        self.close_top_app.pack(side='bottom')
        self.hand_system.pack(side='bottom')
        self.start_auto_system.pack(side='bottom')
        self.stop_auto_system.pack(side='bottom')

        self.arrow_forward.pack(side='left')
        self.arrow_back.pack(side='left')
        self.arrow_upward.pack(side='left')
        self.arrow_downward.pack(side='left')

    @staticmethod
    def mouse_left_click(event):
        print('点击鼠标左键 (' + str(event.x) + ', ' + str(event.y) + ')')
        threads = []
        for pid in devices:
            t = threading.Thread(target=phone.tap, args=(pid, int(event.x / scale), int(event.y / scale)))
            threads.append(t)
            t.start()
        # 等待每个任务结束
        for t in threads:
            t.join()

    @staticmethod
    def mouse_center_click(event):
        print('点击鼠标中键 (' + str(event.x) + ', ' + str(event.y) + ')')
        return None

    @staticmethod
    def mouse_right_click(event):
        print('点击鼠标右键 (' + str(event.x) + ', ' + str(event.y) + ')')
        return None

    @staticmethod
    def mouse_left_drag(event):
        return None

    @staticmethod
    def mouse_center_drag(event):
        return None

    @staticmethod
    def mouse_right_drag(event):
        return None

    @staticmethod
    def vertical_swipe(event):
        print('上下滑动手机　' + datetime.now().time().__str__())
        for pid in devices:
            if event.delta > 0:
                # 往上滚动
                phone.swipe_down_to_up(pid, event.x, h, event.delta)
            else:
                # 往下滚动
                phone.swipe_up_to_down(pid, event.x, h, -event.delta)

    @staticmethod
    def keyboard_press(event):
        print('键盘事件 ' + event.char)

    @staticmethod
    def reboot():
        print('手机重启 ' + datetime.now().time().__str__())
        phone.reboot(devices)

    @staticmethod
    def go_home():
        print('回到主页 ' + datetime.now().time().__str__())
        for pid in devices:
            phone.go_home(pid)

    @staticmethod
    def go_back():
        print('返回上级页面 ' + datetime.now().time().__str__())
        for pid in devices:
            phone.go_back(pid)

    def update_page(self):
        file_path = phone.get_page_photo(devices[0], out_dir)
        img = Image.open(out_dir + file_path).resize((int(w * scale), int(h * scale)))
        img = ImageTk.PhotoImage(image=img)
        self.image_label.config(image=img)
        self.image_label.image = img

        if self.prev_img:
            os.remove(out_dir + file_path)

        self.prev_img = file_path

        if self.continue_update_image:
            root.after(1000, self.update_page)

    @staticmethod
    def update_code():
        print('更新代码 ' + datetime.now().time().__str__())


if __name__ == '__main__':
    root = tk.Tk()

    root.title('手机手动控制系统')

    devices = phone.get_devices()
    if not devices:
        print('没有发现手机设备')
        exit(0)

    out_dir = 'out/'

    (w, h) = phone.get_size(devices[0])

    scale = 0.5

    app = Application(master=root)

    root.after(1000, app.update_page)

    app.mainloop()

    shutil.rmtree(out_dir)
    os.mkdir(out_dir)
