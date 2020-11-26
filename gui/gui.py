import os
import tkinter as tk
from datetime import datetime

from PIL import Image, ImageTk

from src import phone


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.frame = tk.Frame(self, width=w * scale, height=h * scale, bg='white')

        img = Image.new(mode='RGB', size=(int(w * scale), int(h * scale)), color='yellow')
        img = ImageTk.PhotoImage(image=img)

        self.label = tk.Label(self.frame)

        self.label.config(image=img)
        self.label.image = img

        self.home = tk.Button(self, text='主页', command=self.go_home)
        self.back = tk.Button(self, text='返回', command=self.go_back)
        self.reboot = tk.Button(self, text='重启', command=self.reboot)
        self.update = tk.Button(self, text='更新', command=self.update_code)
        self.exit = tk.Button(self, text='退出', command=self.destroy)

        self.master = master
        self.pack()

        self.create_widgets()

        self.prev_img = None
        self.curr_img = None

    def destroy(self):
        self.master.destroy()
        os.remove('../out/' + self.curr_img)

    def create_widgets(self):
        self.frame.pack()

        self.label.bind('<Button-1>', self.left_click)
        self.label.bind('<MouseWheel>', self.vertical_swipe)
        self.label.pack()

        self.home.pack(side='left')
        self.back.pack(side='left')
        self.reboot.pack(side='left')
        self.exit.pack(side='right')

    @staticmethod
    def left_click(event):
        for pid in devices:
            phone.tap(pid, int(event.x / scale), int(event.y / scale))

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
        for pid in devices:
            phone.reboot(pid)

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
        self.label.config(image=img)
        self.label.image = img

        if self.prev_img:
            os.remove('../out/' + file_path)

        self.prev_img = file_path

        root.after(3000, self.update_page)

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

    root.after(3000, app.update_page)

    app.mainloop()
