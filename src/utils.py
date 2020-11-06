import os
from datetime import datetime
from random import randrange

from src import schedule, checkin, phone, app
from src.info import apps, activities, packages, SCHEDULE_TIME

import pytesseract
from PIL import Image
from pytesseract import Output


def tap_start(a):
    """
    程序需要点击桌面图标启动
    """
    return activities[a].__contains__('#')


def set_home_page(pid, w, h, a):
    """
    通过app的位置设置当前页面
    """
    if apps.__len__().__gt__(24) and apps.index(a).__eq__(0):
        # 滑动到首页
        phone.go_home(pid)
        for i in range(0, int(apps.__len__() / 25)):
            phone.swipe_left_to_right(pid, w, h, gap=1)
    elif apps.index(a).__eq__(24):
        # 滑动到第2页
        phone.go_home(pid)
        phone.swipe_right_to_left(pid, w, h)


def schedule_apps(pid, w, h):
    """
    做两次程序的定时任务
    第1次半个小时，其余的时间用来看视频
    第2次做重要的任务
    """
    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        print('第1次定时任务 ' + datetime.now().__str__())
        for a in apps:
            set_home_page(pid, w, h, a)
            getattr(schedule, a)(pid, w, h)

        if (datetime.now().hour % 4).__eq__(1):
            # 手机休息5分钟
            phone.sleep_to_weak(pid, w, h, gap=180)

        def watch_kuaishou_video():
            print('看快手视频 ' + datetime.now().__str__())
            checkin.kuaishou(pid)
            # 从下往上翻页
            while datetime.now().minute < SCHEDULE_TIME:
                phone.swipe_down_to_up(pid, w, h, randrange(5, 16))
            phone.stop_app(pid, packages['kuaishou'])

        # [x] 看快手视频
        if datetime.now().minute < SCHEDULE_TIME:
            watch_kuaishou_video()

    print('第2次定时任务 ' + datetime.now().__str__())
    for a in apps:
        set_home_page(pid, w, h, a)
        getattr(schedule, a)(pid, w, h)


# 每个小时的收尾工作
def tail_work(pid, w, h, hour):
    if hour.__lt__(4):
        while datetime.now().hour.__eq__(hour):
            # [x] 看快手视频
            app.full_watch_kuaishou_video(pid, w, h, hour)
    elif hour.__lt__(8):
        while datetime.now().hour.__eq__(hour):
            # [x] 看抖音视频
            app.full_watch_douyin_video(pid, w, h, hour)
    elif hour.__lt__(12):
        while datetime.now().hour.__eq__(hour):
            # [x] 看火山视频
            app.full_watch_huoshan_video(pid, w, h, hour)
    elif hour.__lt__(16):
        while datetime.now().hour.__eq__(hour):
            # [x] 看快手视频
            app.full_watch_kuaishou_video(pid, w, h, hour)
        # while datetime.now().hour.__eq__(hour):
        #     # [x] 看微视视频
        #     app.full_watch_weishi_video(pid, w, h, hour)
    elif hour.__lt__(20):
        while datetime.now().hour.__eq__(hour):
            # [x] 看快手视频
            app.full_watch_kuaishou_video(pid, w, h, hour)
    elif hour.__lt__(24):
        while datetime.now().hour.__eq__(hour):
            # [x] 看快手视频
            app.full_watch_kuaishou_video(pid, w, h, hour)


def get_photos(path):
    photos = []
    for root, dirs, filenames in os.walk(path):
        for file in filenames:
            if os.path.splitext(file)[1].__eq__('.png'):
                photos.append(os.path.join(root, file))
    return photos


def current_words_location(pid, words, output_dir='out'):
    """
    获取当前页面上文字的位置
    """
    # 1. 获取到手机截图
    photo_name = phone.get_page_photo(pid, output_dir)
    # 2. 对截图进行识别
    data = pytesseract.image_to_data(Image.open(os.path.join(output_dir, photo_name)),
                                     output_type=Output.DICT, lang='chi_sim')
    # 3. 截图信息对比
    for i in range(0, len(data['text'])):
        if data['text'][i].__eq__(words[0]):
            is_found = True
            for j, word in enumerate(words):
                if not word.__eq__(data['text'][i + j]):
                    is_found = False
                    break
            if is_found:
                # 4. 返回处理结果
                os.remove(os.path.join(output_dir, photo_name))
                return {'x': data['left'][i], 'y': data['top'][i],
                        'w': data['width'][i], 'h': data['height'][i]}
    os.remove(os.path.join(output_dir, photo_name))
    return None


def print_current_location(pid, out_dir='out'):
    """
    打印当前页面文字的位置
    调试使用的函数
    """
    photo_name = phone.get_page_photo(pid, output=out_dir)
    data = pytesseract.image_to_data(Image.open(os.path.join(out_dir, photo_name)),
                                     output_type=Output.DICT, lang='chi_sim')
    for i in range(0, len(data['text'])):
        print(data['text'][i], data['left'][i], data['top'][i], data['width'][i], data['height'][i])
    os.remove(os.path.join(out_dir, photo_name))
