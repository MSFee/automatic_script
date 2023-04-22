import startgGame
import auto
import pydirectinput
from time import sleep
import subprocess
import os
import datetime
pydirectinput.FAILSAFE = False
auto.saveAndCropFunc("./chuanqi/main", [0, 0, 1391, 818])


def click(x, y):
    if x != 0:
        pydirectinput.click(int(x), int(y))


def check_network_status():
    try:
        # 判断当前电脑是否联网
        subprocess.check_output(
            ['ping', 'www.baidu.com', '-n', '1', '-w', '5000'])
        return True
    except:
        return False


def connect_wifi(is5G=True):
    # # 扫描可用wifi列表
    # wifi_list = subprocess.check_output(['netsh', 'wlan', 'show', 'network'], shell=True, timeout=15, stderr=subprocess.STDOUT, encoding='gbk').split('\n')
    # # 查找指定名称的wifi
    # mr1002_5G = [line.split(':')[1][1:-1] for line in wifi_list if 'mr1002-5G' in line]
    # if len(mr1002_5G) > 0:
    #     # 连接指定的wifi

    if is5G:
        os.system('netsh wlan connect name="{}"'.format('mr1002-5G'))
    else:
        os.system('netsh wlan connect name="{}"'.format('mr1002'))


def clickPackage():
    auto.saveAndCropFunc("./chuanqi/main", [0, 0, 1391, 818])
    x, y = auto.getImg1AndImg2("./chuanqi/main.jpg", "./chuanqi/package.jpg")
    pydirectinput.moveTo(int(x), int(y) + 8)
    pydirectinput.click()
    sleep(2)


def openQuicklyBack():
    x_back, y_back = auto.getImg1AndImg2(
        "./chuanqi/main.jpg", "./chuanqi/back.jpg")
    if x_back != 0:
        pydirectinput.moveTo(int(x_back), int(y_back) + 8)
        pydirectinput.click()
    else:
        clickPackage()
        auto.saveAndCropFunc("./chuanqi/main", [0, 0, 1391, 818])
        sleep(2)
        x1, y1 = auto.getImg1AndImg2(
            "./chuanqi/main.jpg", "./chuanqi/back.jpg")
        click(x1, y1 + 8)


def clickQuicklyBack(count=0):
    auto.saveAndCropFunc("./chuanqi/main", [0, 0, 1391, 818])
    x_back, y_back = auto.getImg1AndImg2(
        "./chuanqi/main.jpg", "./chuanqi/quicklyBack.jpg")
    if x_back != 0:
        sleep(1)
        pydirectinput.moveTo(int(x_back), int(y_back) + 8)
        pydirectinput.click()
    else:
        if count >= 3:
            checkGameWindow(True)
            return
        openQuicklyBack()
        sleep(3)
        clickQuicklyBack(count + 1)


def goMonster():
    sleep(2)
    pydirectinput.moveTo(1144, 96)
    pydirectinput.click()
    pydirectinput.moveTo(295, 663)
    pydirectinput.mouseDown()
    pydirectinput.moveTo(295, 300, 2)
    sleep(2)
    pydirectinput.mouseUp()
    pydirectinput.click(290, 665)
    sleep(1)
    pydirectinput.mouseDown()
    pydirectinput.moveTo(295, 300, 2)
    sleep(2)
    pydirectinput.mouseUp()
    pydirectinput.click(290, 665)
    sleep(1)
    pydirectinput.mouseDown()
    pydirectinput.moveTo(295, 300, 2)
    sleep(2)
    pydirectinput.mouseUp()
    pydirectinput.click(290, 665)
    sleep(1)
    # 神族地牢
    click(310, 401)
    pydirectinput.click(1015, 474)
    # pydirectinput.mouseDown()
    # pydirectinput.moveTo(295, 300, 2)
    # sleep(2)
    # pydirectinput.mouseUp()
    # pydirectinput.click(300, 563)
    # pydirectinput.click(1015, 474)
    # pydirectinput.click(1015, 428)  # 霍乱
    sleep(2)
    pydirectinput.click(945, 648)
    sleep(2)
    pydirectinput.click(945, 648)


def checkIsDead():
    auto.saveAndCropFunc("./chuanqi/main", [0, 0, 1391, 818])
    x, y = auto.getImg1AndImg2("./chuanqi/main.jpg", "./chuanqi/isDead.jpg")
    if x != 0:
        click(x, y + 8)
        sleep(2)
        auto.saveAndCropFunc("./chuanqi/main", [0, 0, 1391, 818])
        x, y = auto.getImg1AndImg2(
            "./chuanqi/main.jpg", "./chuanqi/package.jpg")
        x_back, y_back = auto.getImg1AndImg2(
            "./chuanqi/main.jpg", "./chuanqi/quicklyBack.jpg")
        if x_back != 0:
            click(x, y + 8)
        goMonster()


def checkArea():
    auto.saveAndCropFunc("./chuanqi/main", [0, 0, 1391, 818])
    x_monster, y3 = auto.getImg1AndImg2(
        "./chuanqi/main.jpg", "./chuanqi/monster.jpg", 0.9)
    x_monster1, y3 = auto.getImg1AndImg2(
        "./chuanqi/main.jpg", "./chuanqi/monster1.jpg", 0.9)
    x_monster2, y3 = auto.getImg1AndImg2(
        "./chuanqi/main.jpg", "./chuanqi/monster2.jpg", 0.9)
    if x_monster != 0 or x_monster1 != 0 or x_monster2 != 0:
        checkIsDead()
        return
    x, y = auto.getImg1AndImg2("./chuanqi/main.jpg", "./chuanqi/package.jpg")
    if x != 0:
        pydirectinput.moveTo(int(x), int(y) + 8)
        pydirectinput.click()
    goMonster()


def resolve():
    clickPackage()
    auto.saveAndCropFunc("./chuanqi/main", [0, 0, 1391, 818])
    x, y = auto.getImg1AndImg2("./chuanqi/main.jpg", "./chuanqi/compile.jpg")
    if x == 0 or y == 0:
        pydirectinput.rightClick(1338, 360)
        sleep(2)
        resolve()
        return
    pydirectinput.moveTo(int(x), int(y) + 8)
    pydirectinput.click()
    sleep(2)
    pydirectinput.moveTo(1151, 317)
    pydirectinput.click()
    sleep(1)
    pydirectinput.moveTo(919, 664)
    pydirectinput.click()
    sleep(1)
    pydirectinput.moveTo(427, 195)
    pydirectinput.click()
    sleep(1)
    pydirectinput.moveTo(919, 664)
    pydirectinput.click()
    sleep(1)
    pydirectinput.moveTo(1150, 142)
    pydirectinput.click()


def checkHasEquip():
    x, y = auto.getImg1AndImg2(
        "./chuanqi/main.jpg", "./chuanqi/quicklyEquip.jpg")
    if x != 0:
        pydirectinput.moveTo(int(x), int(y) + 8)
        pydirectinput.click()


def clickWeChantLogo():
    leftPostion = 1931
    topPosition = 1392
    auto.saveAndCropFunc("./chuanqi/wechatMain",
                         [leftPostion, topPosition, 2533, 1439])
    x, y = auto.getImg1AndImg2(
        "./chuanqi/wechatMain.jpg", "./chuanqi/wechatLogo.jpg", 0.8)
    if x != 0:
        click(leftPostion + x, topPosition + y)
    else:
        pydirectinput.click(2327, 1414)


def outGameAndLoginGame():
    sleep(1)
    pydirectinput.click(1346, 21)
    clickWeChantLogo()
    sleep(2)
    hwnd, left, top, width, height = startgGame.getWindowAndSetMoveRightBottom(
        "微信", "WeChatMainWndForPC")
    auto.saveAndCropFunc("./chuanqi/wechatMain",
                         [left, top, left + width, top + height])
    x, y = auto.getImg1AndImg2(
        "./chuanqi/wechatMain.jpg", "./chuanqi/gameBtn.jpg")
    click(left + x, top + y)
    sleep(1)
    auto.saveAndCropFunc("./chuanqi/wechatMain",
                         [left, top, left + width, top + height])
    x_logo, y_logo = auto.getImg1AndImg2(
        "./chuanqi/wechatMain.jpg", "./chuanqi/gameLogo.jpg", 0.8)
    click(left + x_logo, top + y_logo)
    sleep(3)
    pydirectinput.click(1347, 863)
    sleep(2)
    pydirectinput.click(1378, 873)
    sleep(2)
    pydirectinput.click(1271, 932)
    sleep(5)
    # pydirectinput.click(2542, 763)
    startgGame.closeWindow(hwnd)
    sleep(5)


def getCanLogin():
    while True:
        auto.saveAndCropFunc("./chuanqi/wechat", [0, 950, 550, 1390])
        x, y = auto.getImg1AndImg2(
            "./chuanqi/wechat.jpg", "./chuanqi/wechatLogin.jpg", 0.8)
        if x != 0:
            print('开始登陆')
            deleteMsg()
            outGameAndLoginGame()
            startgGame.getWindow("雷霆传说")
            autoScreensHot()
            break
        sleep(60)


def checkIsOutLogin():
    auto.saveAndCropFunc("./chuanqi/main", [0, 0, 1391, 818])
    x, y = auto.getImg1AndImg2("./chuanqi/main.jpg", "./chuanqi/outlogin.jpg")
    if x != 0:
        getCanLogin()
        return
    x1, y = auto.getImg1AndImg2(
        "./chuanqi/main.jpg", "./chuanqi/notNetwork.jpg")
    if x1 != 0:
        outGameAndLoginGame()

# 删除信息


def deleteMsg(imgName='wechatLogin'):
    hwndHeight, width, height = startgGame.getWindowAndSetMoveBottom("文件传输助手")
    auto.saveAndCropFunc("./chuanqi/wechat", [0, hwndHeight, width, height])
    x, y = auto.getImg1AndImg2(
        "./chuanqi/wechat.jpg", "./chuanqi/" + imgName + ".jpg", 0.8)
    if x != 0:
        pydirectinput.rightClick(int(x), int(hwndHeight + y))
        sleep(1)
        auto.saveAndCropFunc("./chuanqi/wechat",
                             [0, hwndHeight, width, height])
        x1, y1 = auto.getImg1AndImg2(
            "./chuanqi/wechat.jpg", "./chuanqi/deleteBtn.jpg", 0.8)
        pydirectinput.click(int(x1), int(hwndHeight + y1))
        sleep(1)
        auto.saveAndCropFunc("./chuanqi/wechat",
                             [0, hwndHeight, width, height])
        x2, y2 = auto.getImg1AndImg2(
            "./chuanqi/wechat.jpg", "./chuanqi/sureBtn.jpg", 0.8)
        pydirectinput.click(int(x2), int(hwndHeight + y2))
        sleep(1)

# 自动截图并发送微信

def autoScreensHot(isFull=False):
    pydirectinput.keyDown('alt')
    pydirectinput.press('a')
    pydirectinput.keyUp('alt')
    sleep(1)
    if not isFull:
        pydirectinput.click(500, 400)
        sleep(1)
        pydirectinput.click(1333, 847)
        sleep(1)
    else:
        pydirectinput.click(900, 1115)
        sleep(1)
        pydirectinput.click(2511, 1412)
        sleep(1)
    pydirectinput.click(40, 1370)
    sleep(1)
    pydirectinput.keyDown('ctrl')
    pydirectinput.press('v')
    pydirectinput.keyUp('ctrl')
    sleep(1)
    pydirectinput.press('enter')
    sleep(1)

# 检查电脑网络链接


def checkISNotNetWork(isNeedLogin=False, is5G=True, count=0):
    if not check_network_status():
        if count > 10:
            sleep(300)
        connect_wifi(is5G)
        sleep(10)
        is5G = not is5G
        checkISNotNetWork(True, is5G, count + 1)
        return
    elif isNeedLogin:
        print('开始登陆')
        outGameAndLoginGame()
        sleep(5)
        startgGame.getWindow("雷霆传说")
        return
    else:
        print('开始登陆')
        outGameAndLoginGame()
        sleep(5)
        startgGame.getWindow("雷霆传说")


def checkGameWindow(isClose=False):
    try:
        hwnd, width, height = startgGame.getWindow("雷霆传说")
        if isClose:
            startgGame.closeWindow(hwnd)
            sleep(5)
            checkISNotNetWork()
    except:
        checkISNotNetWork()


def toBossAndAttch(position):
    sleep(3)
    # 点击进入地图按钮
    click(946, 650)
    click(946, 650)
    sleep(1)
    # 点击右上角地图
    click(1304, 145)
    sleep(3)
    # 700级斗笠boss地图坐标
    click(position[0], position[1])
    sleep(15)
    # 关闭地图
    click(1151, 142)
    sleep(1)
    auto.saveAndCropFunc("./chuanqi/main", [0, 0, 1391, 818])
    x, y = auto.getImg1AndImg2("./chuanqi/main.jpg", "./chuanqi/fight.jpg")
    if x == 0:
        x_close, y_close = auto.getImg1AndImg2("./chuanqi/main.jpg", "./chuanqi/closeBtn.jpg", 0.9)
        click(x_close, y_close)
    sleep(1)
    click(1258, 362)
    sleep(160)


def checkBossMap(bossIndex):
    # 放逐魔域7层，斗笠boss坐标 特戒boss坐标 盾牌boss坐标
    bossFive = [[592, 352], [816, 458], [479, 387]]
    # 放逐魔域6层，斗笠boss坐标 特戒boss坐标 盾牌boss坐标
    bossSix = [[589, 280], [516, 324], [483, 391]]
    # 混乱神域14层，斗笠boss坐标 特戒boss坐标 盾牌boss坐标
    bossEle = [[398, 498], [710, 446], [896, 391]]
    # # 混乱神域14层，斗笠boss坐标 特戒boss坐标 盾牌boss坐标
    # bossFifthteen = [[398, 498], [710, 446], [896, 391]]
    auto.saveAndCropFunc("./chuanqi/main", [0, 0, 1391, 818])
    # 放逐魔域5层
    xBoss, yBoss = auto.getImg1AndImg2(
        "./chuanqi/main.jpg", "./chuanqi/boss/boss.jpg", 0.97)
    if xBoss != 0:
        click(xBoss, yBoss + 25)
        position = bossFive[bossIndex]
        toBossAndAttch(position)
        return True

    # 放逐魔域6层
    xBoss1, yBoss1 = auto.getImg1AndImg2(
        "./chuanqi/main.jpg", "./chuanqi/boss/boss1.jpg", 0.97)
    if xBoss1 != 0:
        click(xBoss1, yBoss1 + 25)
        position = bossSix[bossIndex]
        toBossAndAttch(position)
        return True

    # 放逐魔域14层
    xBoss2, yBoss2 = auto.getImg1AndImg2(
        "./chuanqi/main.jpg", "./chuanqi/boss/boss2.jpg", 0.97)
    if xBoss2 != 0:
        click(xBoss2, yBoss2 + 25)
        position = bossEle[bossIndex]
        toBossAndAttch(position)
        return True
    
    # 放逐魔域15层
    xBoss3, yBoss3 = auto.getImg1AndImg2(
        "./chuanqi/main.jpg", "./chuanqi/boss/boss3.jpg", 0.97)
    if xBoss3 != 0:
        click(xBoss3, yBoss3 + 25)
        position = bossEle[bossIndex]
        toBossAndAttch(position)
        return True
    return False

def toLuckyBoss():
    click(1144, 96)
    sleep(1)
    click(1152, 483)
    sleep(2)
    auto.saveAndCropFunc("./chuanqi/main", [0, 0, 1391, 818])
    xBoss1, yBoss1 = auto.getImg1AndImg2(
        "./chuanqi/main.jpg", "./chuanqi/boss/luckBoss.jpg", 0.97)
    if xBoss1 != 0:
        return True
    else:
        click(1151, 143)
        sleep(1)
        return False

def toBoss():
    click(1144, 96)
    sleep(1)
    click(1150, 305)
    sleep(1)

    # 斗笠BOSS
    click(664, 192)
    sleep(1)
    result = checkBossMap(0)
    if result:
        toBoss()
        return

    # 特戒
    click(421, 192)
    sleep(1)
    result = checkBossMap(1)
    if result:
        toBoss()
        return

    # 盾牌
    click(544, 192)
    sleep(1)
    result = checkBossMap(2)
    if result:
        toBoss()
        return
    sleep(1)
    click(1150, 142)
    sleep(1)


def checkIsError():
    auto.saveAndCropFunc("./chuanqi/main", [0, 0, 1391, 818])
    x, y = auto.getImg1AndImg2("./chuanqi/main.jpg", "./chuanqi/error.jpg")
    if x != 0:
        click(1085, 256)

def isBoss_800():
    auto.saveAndCropFunc("./chuanqi/main", [0, 0, 1391, 818])
    x, y = auto.getImg1AndImg2("./chuanqi/main.jpg", "./chuanqi/boss800.jpg", 0.9)
    if x != 0:
        click(551, 682)

def is_past_midnight():
    now = datetime.datetime.now()  # 获取当前时间
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)  # 获取今天的凌晨时间
    end_of_day = midnight + datetime.timedelta(days=1) - datetime.timedelta(seconds=1)  # 获取今天的结束时间

    if now >= end_of_day:
        return True
    else:
        return False

def start(attchBoss=False):
    count = 1
    luckBossCount = 1
    while True:
        checkGameWindow()
        checkIsOutLogin()
        checkIsDead()
        # isBoss_800()
        if is_past_midnight():
            luckBossCount = 0
        if count % 30 == 0:
            checkIsError()
            sleep(2)
        if luckBossCount < 3 and count % 15 == 0 and toLuckyBoss() :
            luckBossCount = luckBossCount + 1
            # 前往挑战
            click(960, 531)
            sleep(240)
        if attchBoss:
            toBoss()
        checkArea()
        sleep(3)
        if count % 200 == 0:
            clickQuicklyBack()
        if count % 20 == 0:
            autoScreensHot()
        sleep(50)
        count = count + 1

start(True)