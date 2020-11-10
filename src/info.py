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
        'qutoutiao', 'baidu', 'weishi', 'ximalaya',
        'wuba', 'taobao', 'shuabao', 'yuetoutiao',
        'midu',
        ]

# 程序对应的包名
packages = {
    'toutiao': 'com.ss.android.article.lite',
    'kuaishou': 'com.kuaishou.nebula',
    'douyin': 'com.ss.android.ugc.aweme.lite',
    'huoshan': 'com.ss.android.ugc.livelite',
    'jingdong': 'com.jd.jdlite',
    'fanqie': 'com.dragon.read',
    'fanchang': 'com.xs.fm',
    'kuchang': 'com.kugou.android.douge',
    'shuqi': 'com.shuqi.controller',
    'yingke': 'com.ingkee.lite',
    'kugou': 'com.kugou.android.elder',
    'huitoutiao': 'com.cashtoutiao',
    'zhongqing': 'cn.youth.news',
    'pinduoduo': 'com.xunmeng.pinduoduo',
    'kuaiyin': 'com.kuaiyin.player',
    'tangdou': 'com.bokecc.dance',
    'dongfang': 'com.songheng.eastnews',
    'jukandian': 'com.xiangzi.jukandian',
    'kankuai': 'com.tencent.reading',
    'douhuo': 'com.ss.android.ugc.live',
    'kuge': 'com.kugou.android.child',
    'makan': 'com.ldzs.zhangxin',
    'diandian': 'com.yingliang.clicknews',
    'moji': 'com.moji.mjweather.light',
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
    'chejia': 'com.autohome.speed',
    'doudou': 'com.kanshu.ksgb.fastread.doudou',
    'weixin': 'com.tencent.mm',
}

activities = {
    'toutiao': 'com.ss.android.article.lite/.activity.SplashActivity',
    'kuaishou': 'com.kuaishou.nebula/com.yxcorp.gifshow.HomeActivity',
    'douyin': 'com.ss.android.ugc.aweme.lite/com.ss.android.ugc.aweme.splash.SplashActivity',
    'huoshan': 'com.ss.android.ugc.livelite/com.ss.android.ugc.live.main.MainActivity',
    'jingdong': '#com.jd.jdlite/.MainFrameActivity',
    'fanqie': '#com.dragon.read/.pages.main.MainFragmentActivity',
    'fanchang': '#com.xs.fm/com.dragon.read.pages.main.MainFragmentActivity',
    'kuchang': '#com.kugou.android.douge/com.kugou.android.app.MediaActivity',
    'shuqi': '#com.shuqi.controller/com.shuqi.activity.MainActivity',
    'yingke': '# com.ingkee.lite/com.meelive.ingkee.business.main.entry.legacy.MainActivity',
    'kugou': '#com.kugou.android.elder/com.kugou.android.app.MediaActivity',
    'huitoutiao': 'com.cashtoutiao/.account.ui.main.MainTabActivity',
    'zhongqing': '#cn.youth.news/.ui.splash.SplashAdActivity',
    'pinduoduo': '#com.xunmeng.pinduoduo/.ui.activity.HomeActivity',
    'kuaiyin': '#com.kuaiyin.player/.v2.ui.main.MainActivity',
    'tangdou': 'com.bokecc.dance/.activity.MainActivity',
    'dongfang': '#com.songheng.eastnews/com.songheng.eastfirst.common.view.activity.MainActivity',
    'jukandian': '#com.xiangzi.jukandian/.activity.MainActivity',
    'kankuai': 'com.tencent.reading/.activity.SplashActivity',
    'douhuo': 'com.ss.android.ugc.live/.main.MainActivity',
    'kuge': '#com.kugou.android.child/com.kugou.android.app.MediaActivity',
    'makan': '#com.ldzs.zhangxin/com.weishang.wxrd.activity.MainActivity',
    'diandian': '#com.yingliang.clicknews/.MainActivity',
    'moji': 'com.moji.mjweather.light/com.moji.mjweather.MainActivity',
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
    'chejia': 'com.autohome.speed/com.cubic.autohome.MainActivity',
    'doudou': 'com.kanshu.ksgb.fastread.doudou/com.kanshu.home.fastread.doudou.module.activity.AdSplashActivity',
    'weixin': 'com.tencent.mm/.ui.LauncherUI',
}

# 程序的定时任务为25分钟
SCHEDULE_TIME = 25
