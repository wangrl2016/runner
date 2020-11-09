# 屏幕的实际尺寸
# 通过实际测量手机获得
# 毫米为单位
WIDTH = 6.8
HEIGHT = 14.3

phones = {
    'vivo-u3x': ['720x1544'],
    'Redmi8A': ['720x1520'],
}

numbers = ['15391503757', '15334195745', '17343162426', ]

# 低配置手机前面用##表示
high_serials = ['1fc4da61', 'ce7f96a00307', '9404d35e0307']

# 保留运行信息
contexts = {}

# 程序名
apps = ['toutiao', 'kuaishou', 'douyin', 'huoshan',
        'jingdong', 'fanqie', 'fanchang', 'kuchang',
        'shuqi', 'yingke', 'kugou', 'huitoutiao',
        'zhongqing', 'pinduoduo', 'kuaiyin', 'tangdou',
        'dongfang', 'jukandian', 'kankuai', 'douhuo',
        'kuge', 'makan', 'diandian', 'moji',
        'qutoutiao',
        ]

# 程序对应的包名
packages = {
    apps[0]: 'com.ss.android.article.lite',
    apps[1]: 'com.kuaishou.nebula',
    apps[2]: 'com.ss.android.ugc.aweme.lite',
    apps[3]: 'com.ss.android.ugc.livelite',
    apps[4]: 'com.jd.jdlite',
    apps[5]: 'com.dragon.read',
    apps[6]: 'com.xs.fm',
    apps[7]: 'com.kugou.android.douge',
    apps[8]: 'com.shuqi.controller',
    apps[9]: 'com.ingkee.lite',
    apps[10]: 'com.kugou.android.elder',
    apps[11]: 'com.cashtoutiao',
    apps[12]: 'cn.youth.news',
    apps[13]: 'com.xunmeng.pinduoduo',
    apps[14]: 'com.kuaiyin.player',
    apps[15]: 'com.bokecc.dance',
    apps[16]: 'com.songheng.eastnews',
    apps[17]: 'com.xiangzi.jukandian',
    apps[18]: 'com.tencent.reading',
    apps[19]: 'com.ss.android.ugc.live',
    apps[20]: 'com.kugou.android.child',
    apps[21]: 'com.ldzs.zhangxin',
    apps[22]: 'com.yingliang.clicknews',
    apps[23]: 'com.moji.mjweather.light',
    'weixin': 'com.tencent.mm',
    'qutoutiao': 'com.jifen.qukan',
    'baidu': 'com.baidu.searchbox.lite',
    'weishi': 'com.tencent.weishi',
    'ximalaya': 'com.ximalaya.ting.lite',
    'wuba': 'com.wuba.town.client',
    'taobao': 'com.taobao.litetao',
    'shuabao': 'com.jm.video',
    'yuetoutiao': 'com.expflow.reading',
    'midu': 'com.lechuan.mdwz',
    'qire': 'com.qixiao.qrxs',
    'quhongbao': 'com.qixiao.qrxs',
    'hongshi': 'com.jxbz.hbdsp',
    'youliao': 'com.youliao.topic',
    'wukong': 'com.yshx.wukong',
}

activities = {
    apps[0]: 'com.ss.android.article.lite/.activity.SplashActivity',
    apps[1]: 'com.kuaishou.nebula/com.yxcorp.gifshow.HomeActivity',
    apps[2]: 'com.ss.android.ugc.aweme.lite/com.ss.android.ugc.aweme.splash.SplashActivity',
    apps[3]: 'com.ss.android.ugc.livelite/com.ss.android.ugc.live.main.MainActivity',
    apps[4]: '#com.jd.jdlite/.MainFrameActivity',
    apps[5]: '#com.dragon.read/.pages.main.MainFragmentActivity',
    apps[6]: '#com.xs.fm/com.dragon.read.pages.main.MainFragmentActivity',
    apps[7]: '#com.kugou.android.douge/com.kugou.android.app.MediaActivity',
    apps[8]: '#com.shuqi.controller/com.shuqi.activity.MainActivity',
    apps[9]: '#com.ingkee.lite/com.meelive.ingkee.business.main.entry.legacy.MainActivity',
    apps[10]: '#com.kugou.android.elder/com.kugou.android.app.MediaActivity',
    apps[11]: 'com.cashtoutiao/.account.ui.main.MainTabActivity',
    apps[12]: '#cn.youth.news/.ui.splash.SplashAdActivity',
    apps[13]: '#com.xunmeng.pinduoduo/.ui.activity.HomeActivity',
    apps[14]: '#com.kuaiyin.player/.v2.ui.main.MainActivity',
    apps[15]: 'com.bokecc.dance/.activity.MainActivity',
    apps[16]: '#com.songheng.eastnews/com.songheng.eastfirst.common.view.activity.MainActivity',
    apps[17]: '#com.xiangzi.jukandian/.activity.MainActivity',
    apps[18]: 'com.tencent.reading/.activity.SplashActivity',
    apps[19]: 'com.ss.android.ugc.live/.main.MainActivity',
    apps[20]: '#com.kugou.android.child/com.kugou.android.app.MediaActivity',
    apps[21]: '#com.ldzs.zhangxin/com.weishang.wxrd.activity.MainActivity',
    apps[22]: '#com.yingliang.clicknews/.MainActivity',
    apps[23]: 'com.moji.mjweather.light/com.moji.mjweather.MainActivity',
    'weixin': 'com.tencent.mm/.ui.LauncherUI',
    'qutoutiao': 'com.jifen.qukan/com.jifen.qkbase.main.MainActivity',
    'baidu': 'com.baidu.searchbox.lite/com.baidu.searchbox.MainActivity',
    'weishi': 'com.tencent.weishi/com.tencent.oscar.module.splash.SplashActivity',
    'ximalaya': 'com.ximalaya.ting.lite/com.ximalaya.ting.android.host.activity.MainActivity',
    'wuba': 'com.wuba.town.client/com.wuba.town.TownCenterActivity',
    'taobao': 'com.taobao.litetao/com.taobao.ltao.maintab.MainFrameActivity',
    'shuabao': 'com.jm.video/.ui.main.MainActivity',
    'yuetoutiao': 'com.expflow.reading/.activity.MainActivity',
    'midu': '#com.lechuan.mdwz/.ui.activity.NovelMainActivity',
    'qire': 'com.qixiao.qrxs/.ui.activity.MainActivity',
    'quhongbao': 'com.qixiao.qrxs/.ui.activity.MainActivity',
    'hongshi': 'com.jxbz.hbdsp/com.cy.browser.BrowserActivity',
    'youliao': '#com.youliao.topic/.TrueMainActivity',
    'wukong': '#com.yshx.wukong/com.yuruisoft.desktop.mvp.view.activity.HomeActivity',
}

# 程序的定时任务为25分钟
SCHEDULE_TIME = 25
