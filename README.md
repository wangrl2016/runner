# runner
自动程序系统

### 运行程序

1. 今日头条极速版

- [x] 签到
- [x] 阅读今日头条文章 (app)
- [x] 看视频 (app)
- [x] 开宝箱
- [x] 吃饭补贴
- [x] 睡觉赚钱
- [x] 免费抽手机
- [x] 种菜赚金币
- [x] ~~看小说赚金币~~
- [x] 模拟开店赚钱

2. 快手极速版

- [x] 签到
- [x] 看快手视频
- [x] 开宝箱
- [x] 1000金币悬赏任务 (app)
- [x] 看直播领金币

3. 抖音极速版

- [x] 签到
- [x] 看抖音视频
- [x] 开宝箱
- [x] 限时任务赚金币
- [x] 游戏抽奖
- [x] 吃饭补贴
- [x] 睡觉赚金币

4. 火山极速版

- [x] 签到
- [x] 看火山视频
- [x] 开宝箱
- [x] 摇钱树
- [x] 睡觉赚金币
- [x] 看视频赚海量金币
- [x] 晒收入


5. 京东极速版

- [x] 现金签到
- [x] 逛商品赚金币
- [x] 逛活动赚金币
- [x] 看视频赚金币

6. 番茄免费小说

- [x] 签到
- [x] 阅读番茄小说 (app)
- [x] 开宝箱
- [x] 看视频赚海量金币 (app)
- [x] 分享好书给好友
- [x] 加入书架

7. 番茄畅听

- [x] 签到
- [x] 听番畅音频
- [x] 开宝箱
- [x] 看视频赚海量金币 (app)

8. 微视

- [x] ~~签到~~
- [x] 看微视视频

9. 书旗小说

- [x] 签到
- [x] 阅读书旗小说
- [x] 看视频赚金币
- [x] 邀请书友

10. 映客直播

- [x] 签到
- [x] 看映客直播
- [x] 开宝箱领金币
- [x] 看福利视频
- [ ] 分享映客极速版
- [ ] 好友点击你的分享
- [x] 分享直播间

11. 酷狗大字版

- [x] 签到
- [x] 听酷狗音乐
- [x] 刷创意视频
- [ ] 玩游戏获金币
- [ ] 资讯赚
- [ ] 分享歌曲
- [ ] 分享视频

12. 惠头条

- [x] 签到
- [x] 阅读惠头条文章
- [x] 时段奖励
- [x] 看惠头条视频

13. 中青看点

- [x] 签到
- [x] 阅读中青看点文章
- [ ] 观看视频
- [ ] 分享领青豆

14. 拼多多

- [x] 现金签到
- [x] 逛街得现金

15. 淘宝特价版

- [x] 签到领红包
- [x] 天天赚特币

16. 刷宝短视频

- [x] 签到
- [x] 看刷宝视频
- [x] 看福利视频

17. 趣头条

- [x] 看趣头条小视频
- [x] 开宝箱
- [x] ~~摇钱树赚金币~~
- [x] 睡觉赚金币
- [x] 看广告视频拿金币
- [x] 时段奖励
 

18. 百度极速版

- [x] 看百度小视频
- [x] 好看视频
- [x] 开宝箱
- [x] 时段奖励

19. 喜马拉雅极速版

- [x] 签到
- [x] 听喜马拉雅音频
- [ ] 观看趣味视频

20. 抖音火山

- [ ] 签到
- [x] 看视频

21. 酷狗儿歌

- [x] 签到
- [x] 收听酷狗儿歌
- [ ] 分享

22. 蚂蚁看点

- [ ] 签到

23. 点点新闻

- [ ] 签到

24. 墨迹天气极速版

- [ ] 签到

25. 酷狗唱唱斗歌版

- [ ] 签到

26. 快音

- [ ] 签到

27. 七猫免费小说

- [ ] 签到



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