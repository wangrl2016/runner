import tkinter as tk

from PIL import Image, ImageTk

from src import phone


def go_home():
    print('回到主页')


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.home = tk.Button(self, text='主页')
        self.back = tk.Button(self, text='返回')
        self.reboot = tk.Button(self, text='重启')
        self.exit = tk.Button(self, text='退出', command=self.master.destroy)

        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.home['command'] = go_home
        self.home.pack(side='left')
        self.back.pack(side='left')
        self.reboot.pack(side='left')
        self.exit.pack(side='right')


if __name__ == '__main__':
    root = tk.Tk()

    root.title('手机手动控制系统')

    devices = phone.get_devices()
    if not devices:
        exit(0)

    (w, h) = phone.get_size(devices[0])

    scale = 0.5

    # frame = tk.Frame(root, width=w * scale, height=h * scale, bg='white')
    # frame.pack()

    image = Image.open('../out/2020-11-12_15:38:48.630062.png') \
        .resize((int(w * scale), int(h * scale)))
    image = ImageTk.PhotoImage(image=image)
    label = tk.Label(root, image=image)
    label.pack()

    app = Application(master=root)
    app.mainloop()
