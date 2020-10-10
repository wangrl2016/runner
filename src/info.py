# 屏幕的实际尺寸
# 通过实际测量手机获得
WIDTH = 0.0
HEIGHT = 0.0

phones = {
    'vivo-u3x': ['720x1544']
}

# 程序名
apps = ['toutiao', 'kuaishou', 'douyin', 'huoshan',
        'jingdong', 'fanqie', 'fanchang', 'weishi',
        'shuqi', 'yingke', 'kugou', 'huitoutiao',
        'zhongqing', 'pinduoduo', 'taobao', 'shuabao']

# 程序对应的包名
packages = {
    apps[0]: 'com.ss.android.article.lite',
    apps[1]: 'com.kuaishou.nebula',
    apps[2]: 'com.ss.android.ugc.aweme.lite',
    apps[3]: 'com.ss.android.ugc.livelite',
    apps[4]: 'com.jd.jdlite',
    apps[5]: 'com.dragon.read',
    apps[6]: 'com.xs.fm',
    apps[7]: 'com.tencent.weishi',
    apps[8]: 'com.shuqi.controller',
    apps[9]: 'com.ingkee.lite',
    apps[10]: 'com.kugou.android.elder',
    apps[11]: 'com.cashtoutiao',
    apps[12]: 'cn.youth.news',
    apps[13]: 'com.xunmeng.pinduoduo',
    apps[14]: 'com.taobao.litetao',
    apps[15]: 'com.jm.video'
}

activities = {
    apps[0]: 'com.ss.android.article.lite/.activity.SplashActivity',
    apps[1]: 'com.kuaishou.nebula/com.yxcorp.gifshow.HomeActivity',
    apps[2]: 'com.ss.android.ugc.aweme.lite/com.ss.android.ugc.aweme.splash.SplashActivity',
    apps[3]: 'com.ss.android.ugc.livelite/com.ss.android.ugc.live.main.MainActivity',
    apps[4]: '#com.jd.jdlite/.MainFrameActivity',
    apps[5]: '#com.dragon.read/.pages.main.MainFragmentActivity',
    apps[6]: 'com.xs.fm/com.dragon.read.pages.main.MainFragmentActivity',
    apps[7]: 'com.tencent.weishi/com.tencent.oscar.module.splash.SplashActivity',
    apps[8]: '#com.shuqi.controller/com.shuqi.activity.MainActivity',
    apps[9]: '#com.ingkee.lite/com.meelive.ingkee.business.main.entry.legacy.MainActivity',
    apps[10]: '#com.kugou.android.elder/com.kugou.android.app.MediaActivity',
    apps[11]: 'com.cashtoutiao/.account.ui.main.MainTabActivity',
    apps[12]: '#cn.youth.news/.ui.splash.SplashAdActivity',
    apps[13]: '#com.xunmeng.pinduoduo/.ui.activity.HomeActivity',
    apps[14]: 'com.taobao.litetao/com.taobao.ltao.maintab.MainFrameActivity',
    apps[15]: 'com.jm.video/.ui.main.MainActivity'
}

numbers = ['15391503757', '17343162426', '15334195745']

# 高配置和低配置手机
high_serials = ['1fc4da61']
low_serials = []
