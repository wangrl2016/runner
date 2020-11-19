import tkinter as tk
from src import phone


def go_home():
    print("回到主页")


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.back = tk.Button(self, text="返回", command=self.master.destroy)
        self.home = tk.Button(self)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.home["text"] = "主页"
        self.home["command"] = go_home
        self.home.pack(side="left")
        self.back.pack(side="right")


if __name__ == '__main__':
    root = tk.Tk()

    devices = phone.get_devices()
    if not devices:
        exit(0)

    (w, h) = phone.get_size(devices[0])

    scale = 0.5

    frame = tk.Frame(root, width=w * scale, height=h * scale, bg='white')
    frame.pack()

    app = Application(master=root)
    app.mainloop()
