import os
from datetime import datetime
from random import randrange

from src import schedule, checkin, phone, app, info
from src.info import activities, SCHEDULE_TIME

import pytesseract
from PIL import Image
from pytesseract import Output


def is_coordinate_checkin(a):
    """
    :return: 程序是否需要点击桌面图标启动
    """
    return activities[a].__contains__('#')


def get_packages_dict(activities_dict):
    """
    通过activity的名字获取package的名字
    """
    packages_dict = activities_dict.copy()
    for key in packages_dict:
        packages_dict[key] = packages_dict[key][1 if packages_dict[key].__contains__('#') else 0:
                                                packages_dict[key].index('/')]
    return packages_dict


def schedule_apps(pid, w, h):
    """
    做两次程序的定时任务
    第1次半个小时，其余的时间用来看视频
    第2次做重要的任务
    """

    def watch_kuaishou_video():
        print('看快手视频 ' + datetime.now().__str__())
        checkin.kuaishou(pid)
        # 从下往上翻页
        while datetime.now().minute < SCHEDULE_TIME:
            phone.swipe_down_to_up(pid, w / 2, h, randrange(5, 16))
        phone.stop_app(pid, info.packages['kuaishou'])

    if datetime.now().minute.__lt__(SCHEDULE_TIME):
        print('第1次定时任务 ' + datetime.now().__str__())
        for a in info.apps:
            getattr(schedule, a)(pid, w, h)

        if (datetime.now().hour % 4).__eq__(1):
            # 手机休息180s
            phone.sleep_to_weak(pid, w, h, gap=180)

        # [x] 看快手视频
        if datetime.now().minute < SCHEDULE_TIME:
            watch_kuaishou_video()

    print('第2次定时任务 ' + datetime.now().__str__())
    for a in info.apps:
        getattr(schedule, a)(pid, w, h)


# 每个小时的收尾工作
def tail_work(pid, w, h, hour):
    if datetime.now().hour.__lt__(12):
        checkin.jingdong(pid, w, h)
        app.jingdong_benefit_page(pid, w, h)
        # [x] 京东看视频赚金币
        app.jingdong_video_coin(pid, w, h, hour=14)
        phone.stop_app(pid, info.packages['jingdong'])
    else:
        checkin.kuaishou(pid)
        # [x] 看快手视频
        app.watch_kuaishou_video(pid, w, h, hour)
        phone.stop_app(pid, info.packages['kuaishou'])


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
    if photo_name is None:
        return None
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
