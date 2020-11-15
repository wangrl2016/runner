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

# 所有程序名
apps = []

# 所有程序对应的包名
packages = {}

activities = {
    # 1-4
    'toutiao': 'com.ss.android.article.lite/.activity.SplashActivity',
    'kuaishou': 'com.kuaishou.nebula/com.yxcorp.gifshow.HomeActivity',
    'douyin': 'com.ss.android.ugc.aweme.lite/com.ss.android.ugc.aweme.splash.SplashActivity',
    'huoshan': 'com.ss.android.ugc.livelite/com.ss.android.ugc.live.main.MainActivity',

    # 5-8
    'jingdong': '#com.jd.jdlite/.MainFrameActivity',
    'fanqie': '#com.dragon.read/.pages.main.MainFragmentActivity',
    'fanchang': '#com.xs.fm/com.dragon.read.pages.main.MainFragmentActivity',
    'kuchang': '#com.kugou.android.douge/com.kugou.android.app.MediaActivity',

    # 9-12
    'shuqi': '#com.shuqi.controller/com.shuqi.activity.MainActivity',
    'yingke': '#com.ingkee.lite/com.meelive.ingkee.business.main.entry.legacy.MainActivity',
    'kugou': '#com.kugou.android.elder/com.kugou.android.app.MediaActivity',
    'youliao': '#com.youliao.topic/.TrueMainActivity',

    # 13-16
    'zhongqing': '#cn.youth.news/.ui.splash.SplashAdActivity',
    'pinduoduo': '#com.xunmeng.pinduoduo/.ui.activity.HomeActivity',
    'kuaiyin': '#com.kuaiyin.player/.v2.ui.main.MainActivity',
    'quhongbao': '#com.chenglie.hongbao/com.bytedance.sdk.openadsdk.activity.base.TTDelegateActivity',

    # 17-20
    'dongfang': '#com.songheng.eastnews/com.songheng.eastfirst.common.view.activity.MainActivity',
    'jukandian': '#com.xiangzi.jukandian/.activity.MainActivity',
    'qukankan': '#com.popnews2345/.main.activity.MainActivity',
    'miaokan': '#com.taige.mygold/.MainActivityV2',

    # 21-24
    'kuge': '#com.kugou.android.child/com.kugou.android.app.MediaActivity',
    'makan': '#com.ldzs.zhangxin/com.weishang.wxrd.activity.MainActivity',
    'diandian': '#com.yingliang.clicknews/.MainActivity',
    'xingqiu': '#com.planet.light2345/.main.activity.MainActivity',

    # 25-28
    'midu': '#com.lechuan.mdwz/.ui.activity.NovelMainActivity',
    'changdou': '#com.zf.shuashua/.MainActivity',
    'kulingyin': '#com.hot.war/.MainActivity',
    'lanmao': '#com.yuri.lazycat/com.yuruisoft.desktop.mvp.view.activity.HomeActivity',

    # 29-32
    'qutoutiao': 'com.jifen.qukan/com.jifen.qkbase.main.MainActivity',
    'baidu': 'com.baidu.searchbox.lite/com.baidu.searchbox.MainActivity',
    'weishi': 'com.tencent.weishi/com.tencent.oscar.module.splash.SplashActivity',
    'ximalaya': 'com.ximalaya.ting.lite/com.ximalaya.ting.android.host.activity.MainActivity',

    # 33-36
    'wuba': 'com.wuba.town.client/com.wuba.town.TownCenterActivity',
    'taobao': 'com.taobao.litetao/com.taobao.ltao.maintab.MainFrameActivity',
    'shuabao': 'com.jm.video/.ui.main.MainActivity',
    'qqyuedu': 'com.qq.reader/.activity.MainActivity',

    # 37-40
    'chejia': 'com.autohome.speed/com.cubic.autohome.MainActivity',
    'uc': 'com.UCMobile/com.uc.browser.InnerUCMobile',
    'kuaikandian': 'com.yuncheapp.android.pearl/com.kuaishou.athena.MainActivity',
    'hongshi': 'com.jxbz.hbdsp/com.cy.browser.BrowserActivity',

    # 41-44
    'doudou': 'com.kanshu.ksgb.fastread.doudou/com.kanshu.home.fastread.doudou.module.activity.AdSplashActivity',
    'qimao': 'com.kmxs.reader/.home.ui.HomeActivity',
    'kankuai': 'com.tencent.reading/.activity.SplashActivity',
    'douhuo': 'com.ss.android.ugc.live/.main.MainActivity',

    # 45-48
    'moji': 'com.moji.mjweather.light/com.moji.mjweather.MainActivity',
    'ersansi': 'com.browser2345/.BrowserActivity',
    'tangdou': 'com.bokecc.dance/.activity.MainActivity',
    'yangchong': 'com.bikann.mfxssk/com.lwby.breader.view.BKHomeActivity',

    # 49-52
    'weixin': 'com.tencent.mm/.ui.LauncherUI',
    'sougou': 'sogou.mobile.explorer.speed/sogou.mobile.explorer.BrowserActivity',
    'zhuanshi': 'com.sljh.zqxsp/com.cy.browser.BrowserActivity',
    'qizhu': 'com.wetimetech.pig/net.guangying.pig.MainActivity',

    # 'zqya': 'com.xuniu.zqya/.ui.MainActivity',
    # 'zhuanbao':'com.yujin.zhuanbao/.activity.ZbMainActivity',
}

# 程序的定时任务为30分钟
SCHEDULE_TIME = 30
