import os
import threading
import tkinter as tk
from datetime import datetime

from PIL import Image, ImageTk
from src import phone
import cairosvg
from io import BytesIO


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.image_frame = tk.Frame(self, width=w * scale, height=h * scale, bg='white')
        self.operate_frame = tk.Frame(self, width=w * scale, height=h * scale, bg='beige')

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
        self.curr_img = None

    # def destroy(self):
    #     self.master.destroy()
    #     os.remove('../out/' + self.curr_img)

    def create_widgets(self):
        self.image_frame.pack_propagate(0)  # 固定frame的大小
        self.image_frame.pack(side='left')
        self.operate_frame.pack_propagate(0)
        self.operate_frame.pack(side='left')

        self.image_label.bind('<Button-1>', self.left_click)
        self.image_label.bind('<MouseWheel>', self.vertical_swipe)
        self.image_label.pack()

        self.home.pack(side='left')
        self.back.pack(side='left')
        self.update.pack(side='left')
        self.reboot.pack(side='left')
        self.exit.pack(side='left')

        self.arrow_forward.pack(side='left')
        self.arrow_back.pack(side='left')
        self.arrow_upward.pack(side='left')
        self.arrow_downward.pack(side='left')

    @staticmethod
    def left_click(event):
        threads = []
        for pid in devices:
            t = threading.Thread(target=phone.tap, args=(pid, int(event.x / scale), int(event.y / scale)))
            threads.append(t)
            t.start()
        # 等待每个任务结束
        for t in threads:
            t.join()

    @staticmethod
    def vertical_swipe(event):
        print('上下滑动手机　' + datetime.now().time().__str__())
        for pid in devices:
            if event.delta > 0:
                # 往上滚动
                phone.swipe_down_to_up(pid, event.x, h)
            else:
                # 往下滚动
                phone.swipe_up_to_down(pid, event.x, h)

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
        print('更新页面 ' + datetime.now().time().__str__())
        file_path = phone.get_page_photo(devices[0], '../out/')
        self.curr_img = file_path
        img = Image.open('../out/' + file_path).resize((int(w * scale), int(h * scale)))
        img = ImageTk.PhotoImage(image=img)
        self.image_label.config(image=img)
        self.image_label.image = img

        if self.prev_img:
            os.remove('../out/' + file_path)

        self.prev_img = file_path

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

    (w, h) = phone.get_size(devices[0])

    scale = 0.5

    app = Application(master=root)

    root.after(1000, app.update_page)

    app.mainloop()
