# runner
自动程序系统

### 运行程序

主做每日签到和0.01元以上的任务。

目标100个程序，平均每个0.3元，每台手机每天30元收入。

[程序排行榜](https://www.qimai.cn/rank/marketRank)

[手机屏幕尺寸](https://uiiiuiii.com/screen/)


### 技术问题

1. 安装tesseract

```
// 依赖可能存在问题
pip uninstall pyOpenSSL
pip install pyOpenSSL
// 安装识别软件
sudo apt install libleptonica-dev tesseract-ocr libtesseract-dev
pip install pytesseract
// 安装中文识别字库
sudo mv chi_sim.traineddata /usr/share/tesseract-ocr/4.00/tessdata/
```

2. 安装tkinter图形界面

```
apt install python3-tk
```

3. 切换国内源

```
sudo pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple  cairosvg
```