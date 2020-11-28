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
    'qukan': '#com.yanhui.qktx/.activity.NewSplashActivity',

    # 13-16
    'zhongqing': '#cn.youth.news/.ui.splash.SplashAdActivity',
    'kuaiyin': '#com.kuaiyin.player/.v2.ui.main.MainActivity',
    'quhongbao': '#com.chenglie.hongbao/com.bytedance.sdk.openadsdk.activity.base.TTDelegateActivity',

    # 17-20
    'jukandian': '#com.xiangzi.jukandian/.activity.MainActivity',
    'miaokan': '#com.taige.mygold/.MainActivityV2',

    # 21-24
    'kuge': '#com.kugou.android.child/com.kugou.android.app.MediaActivity',
    'makan': '#com.ldzs.zhangxin/com.weishang.wxrd.activity.MainActivity',
    'diandian': '#com.yingliang.clicknews/.MainActivity',

    # 25-28
    'tengtu': '#com.tencent.map/.framework.launch.MapActivityReal',
    'momo': '#com.immomo.young/com.immomo.momo.maintab.MaintabActivity',
    'jitou': '#com.sanmiao.news/.activity.MainActivity',
    'sanliuling': '#com.qihoo.browser/.BrowserActivity',

    # 29-32
    'yunshanfu': '#com.unionpay/.activity.UPActivityMain',
    'xijian': '#com.watermelon.more/com.qts.customer.MainFragmentActivity',

    # 49-52
    'midu': '#com.lechuan.mdwz/.ui.activity.NovelMainActivity',
    'changdou': '#com.zf.shuashua/.MainActivity',
    'kulingyin': '#com.hot.war/.MainActivity',
    'lanmao': '#com.yuri.lazycat/com.yuruisoft.desktop.mvp.view.activity.HomeActivity',

    # 53-56
    'qutoutiao': 'com.jifen.qukan/com.jifen.qkbase.main.MainActivity',
    'baidu': 'com.baidu.searchbox.lite/com.baidu.searchbox.MainActivity',
    'weishi': 'com.tencent.weishi/com.tencent.oscar.module.splash.SplashActivity',
    'ximalaya': 'com.ximalaya.ting.lite/com.ximalaya.ting.android.host.activity.MainActivity',

    # 57-60
    'wuba': 'com.wuba.town.client/com.wuba.town.TownCenterActivity',
    'taobao': 'com.taobao.litetao/com.taobao.ltao.maintab.MainFrameActivity',
    'shuabao': 'com.jm.video/.ui.main.MainActivity',
    'qqyuedu': 'com.qq.reader/.activity.MainActivity',

    # 61-64
    'chejia': 'com.autohome.speed/com.cubic.autohome.MainActivity',
    'uc': 'com.UCMobile/com.uc.browser.InnerUCMobile',
    'kuaikandian': 'com.yuncheapp.android.pearl/com.kuaishou.athena.MainActivity',
    'hongshi': 'com.jxbz.hbdsp/com.cy.browser.BrowserActivity',

    # 65-68
    'doudou': 'com.kanshu.ksgb.fastread.doudou/com.kanshu.home.fastread.doudou.module.activity.AdSplashActivity',
    'qimao': 'com.kmxs.reader/.home.ui.HomeActivity',
    'douhuo': 'com.ss.android.ugc.live/.main.MainActivity',

    # 69-72
    'moji': 'com.moji.mjweather.light/com.moji.mjweather.MainActivity',
    'tangdou': 'com.bokecc.dance/.activity.MainActivity',
    'yangcong': 'com.bikann.mfxssk/com.lwby.breader.view.BKHomeActivity',

    # 73-76
    'qqliulan': 'com.tencent.mtt/.MainActivity',
    'lingshenghui': 'com.mars.ring.caller.show/com.play.music.moudle.home.MainActivity',
    'zhuanshi': 'com.sljh.zqxsp/com.cy.browser.BrowserActivity',
    'tengzhi': 'com.tencent.now/.mainpage.activity.LiveMainActivity',

    # 77-80
    'zhaoshang': 'cmb.pb/.app.mainframe.container.PBMainActivity',
    'gudong': 'com.codoon.gps/.ui.SlideActivity',
    'xiongmao': 'com.nd.android.pandareader/com.baidu.shucheng.ui.main.MainActivity',
    'buduoduo': 'com.qsmy.walkmonkey/com.qsmy.busniess.welcome.WelcomeActivity',

    # 81-84
    'duokan': 'com.tengu.duokan/com.tengu.duoduo.main.MainActivity',
    'shandian': 'c.l.a/.views.AppBoxHomeActivity',
    'taozhi': 'com.taobao.live/.home.activity.TaoLiveHomeActivity',

    # last
    'weixin': 'com.tencent.mm/.ui.LauncherUI',
}

# 程序的定时任务为30分钟
SCHEDULE_TIME = 30
