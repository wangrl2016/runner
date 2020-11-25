import tkinter as tk

from PIL import Image, ImageTk

from src import phone


def go_home():
    print('回到主页')


def callback(event):
    print('当前位置 ' + str(event.x) + 'x' + str(event.y))


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.frame = tk.Frame(self, width=w * scale, height=h * scale, bg='white')

        img = Image.open('../out/2020-11-12_15:38:48.630062.png') \
            .resize((int(w * scale), int(h * scale)))
        img = ImageTk.PhotoImage(image=img)

        self.label = tk.Label(self.frame)

        self.label.config(image=img)
        self.label.image = img

        self.home = tk.Button(self, text='主页')
        self.change = tk.Button(self, text='更换', command=self.change_image)
        self.back = tk.Button(self, text='返回')
        self.reboot = tk.Button(self, text='重启')
        self.exit = tk.Button(self, text='退出', command=self.master.destroy)

        self.master = master
        self.pack()

        self.create_widgets()

    def create_widgets(self):
        self.home['command'] = go_home

        self.frame.pack()

        self.label.bind('<Button-1>', callback)
        self.label.pack()

        self.home.pack(side='left')
        self.change.pack(side='left')
        self.back.pack(side='left')
        self.reboot.pack(side='left')
        self.exit.pack(side='right')

    def change_image(self):
        print('更换图片')

        img = Image.open('../out/2020-10-26_17:02:55.074631.png') \
            .resize((int(w * scale), int(h * scale)))
        img = ImageTk.PhotoImage(image=img)
        self.label.config(image=img)
        self.label.image = img


if __name__ == '__main__':
    root = tk.Tk()

    root.title('手机手动控制系统')

    devices = phone.get_devices()
    if not devices:
        exit(0)

    (w, h) = phone.get_size(devices[0])

    scale = 0.5

    app = Application(master=root)
    app.mainloop()
