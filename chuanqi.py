import chuanqiUtils
import startgGame
import auto
import pydirectinput
from time import sleep
pydirectinput.FAILSAFE = False
auto.saveAndCropFunc("./chuanqi/main", [0, 0, 1391, 818])


def click(x, y):
    if x != 0:
        pydirectinput.click(int(x), int(y))


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


def findMonster(count):
    while count != 0:
        count = count - 1
        pydirectinput.moveTo(295, 663)
        pydirectinput.mouseDown()
        sleep(0.5)
        pydirectinput.moveTo(295, 300, 2)
        sleep(0.5)
        pydirectinput.mouseUp()


def goMonster():
    sleep(2)
    click(1144, 96)
    sleep(2)
    findMonster(6)
    sleep(1)
    # 神族地牢
    # click(310, 401)
    # pydirectinput.click(1015, 474)
    pydirectinput.click(293, 593)
    # pydirectinput.click(1015, 474)
    pydirectinput.click(1027, 430)  # 血龙秘境
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

def needLogin():
    auto.saveAndCropFunc("./chuanqi/wechat", [0, 950, 550, 1390])
    x, y = auto.getImg1AndImg2(
           "./chuanqi/wechat.jpg", "./chuanqi/wechatLogin.jpg", 0.8)
    if x != 0:
        print('重新登陆')
        deleteMsg()
        chuanqiUtils.outGameAndLoginGame()
        startgGame.getWindow("雷霆传说")
        autoScreensHot()

def getCanLogin():
    while True:
        auto.saveAndCropFunc("./chuanqi/wechat", [0, 950, 550, 1390])
        x, y = auto.getImg1AndImg2(
            "./chuanqi/wechat.jpg", "./chuanqi/wechatLogin.jpg", 0.8)
        if x != 0:
            print('开始登陆')
            deleteMsg()
            chuanqiUtils.outGameAndLoginGame()
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
        chuanqiUtils.outGameAndLoginGame()

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


def checkGameWindow(isClose=False):
    try:
        hwnd, width, height = startgGame.getWindow("雷霆传说")
        chuanqiUtils.checkGameisError()
        if isClose:
            startgGame.closeWindow(hwnd)
            sleep(5)
            chuanqiUtils.checkISNotNetWork()
    except:
        chuanqiUtils.checkISNotNetWork()


def toBossAndAttch(position, time=80):
    sleep(3)
    # 点击进入地图按钮
    click(946, 650)
    click(946, 650)
    sleep(1)
    checkIsError()
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
        x_close, y_close = auto.getImg1AndImg2(
            "./chuanqi/main.jpg", "./chuanqi/closeBtn.jpg", 0.9)
        click(x_close, y_close)
    sleep(1)
    click(1258, 362)
    sleep(2)
    autoScreensHot()
    sleep(time)


def attch800Boss(bossIndex):
    boss6 = [[585, 278], [], [479, 391]]
    boss7 = [[584, 354], [], [479, 390]]
    boss8 = [[710, 510], [], [512, 325]]
    boss14 = [[398, 500], [], [897, 393]]
    boss17 = [[736, 651], [], [432, 632]]
    xBoss, yBoss = auto.getImg1AndImg2(
        "./chuanqi/main.jpg", "./chuanqi/boss800Area/6.jpg", 0.97)
    if xBoss != 0:
        click(xBoss, yBoss + 25)
        position = boss6[bossIndex]
        toBossAndAttch(position)
        return True

    xBoss, yBoss = auto.getImg1AndImg2(
        "./chuanqi/main.jpg", "./chuanqi/boss800Area/7.jpg", 0.97)
    if xBoss != 0:
        click(xBoss, yBoss + 25)
        position = boss7[bossIndex]
        toBossAndAttch(position)
        return True

    xBoss, yBoss = auto.getImg1AndImg2(
        "./chuanqi/main.jpg", "./chuanqi/boss800Area/8.jpg", 0.97)
    if xBoss != 0:
        click(xBoss, yBoss + 25)
        position = boss8[bossIndex]
        toBossAndAttch(position)
        return True

    xBoss, yBoss = auto.getImg1AndImg2(
        "./chuanqi/main.jpg", "./chuanqi/boss800Area/14.jpg", 0.97)
    if xBoss != 0:
        click(xBoss, yBoss + 25)
        position = boss14[bossIndex]
        toBossAndAttch(position)
        return True

    xBoss1, yBoss1 = auto.getImg1AndImg2(
        "./chuanqi/main.jpg", "./chuanqi/boss800Area/15.jpg", 0.97)
    if xBoss1 != 0:
        click(xBoss1, yBoss1 + 25)
        position = boss14[bossIndex]
        toBossAndAttch(position)
        return True

    xBoss, yBoss = auto.getImg1AndImg2(
        "./chuanqi/main.jpg", "./chuanqi/boss800Area/17.jpg", 0.97)
    if xBoss != 0:
        click(xBoss, yBoss + 25)
        position = boss17[bossIndex]
        toBossAndAttch(position)
        return True

    return False


def checkBossMap(bossIndex, is900= False):
    # 850级
    # 混乱神域17层 斗笠boss坐标 特戒boss坐标 盾牌boss坐标
    bossFive = [[400, 500], [711, 454], [900, 397]]
    # 混乱神域18层，斗笠boss坐标 特戒boss坐标 盾牌boss坐标
    bossSix = [[507, 448], [484, 335], [734, 345]]
    # 混乱神域19层，斗笠boss坐标 特戒boss坐标 盾牌boss坐标
    bossNice = [[739, 652], [581, 588], [434, 633]]

    bossNight = [[812, 362], [787, 563], [821, 465]]

    auto.saveAndCropFunc("./chuanqi/main", [0, 0, 1391, 818])

    if bossIndex != 1 and is900 == False:
        return attch800Boss(bossIndex)

    xBoss3, yBoss3 = auto.getImg1AndImg2(
        "./chuanqi/main.jpg", "./chuanqi/boss/boss3.jpg", 0.97)
    if xBoss3 != 0:
        click(xBoss3, yBoss3 + 25)
        position = bossNight[bossIndex]
        toBossAndAttch(position, 850)
        return True


    xBoss, yBoss = auto.getImg1AndImg2(
        "./chuanqi/main.jpg", "./chuanqi/boss/boss.jpg", 0.97)
    if xBoss != 0:
        click(xBoss, yBoss + 25)
        position = bossFive[bossIndex]
        toBossAndAttch(position, 850)
        return True

    xBoss1, yBoss1 = auto.getImg1AndImg2(
        "./chuanqi/main.jpg", "./chuanqi/boss/boss1.jpg", 0.97)
    if xBoss1 != 0:
        click(xBoss1, yBoss1 + 25)
        position = bossSix[bossIndex]
        toBossAndAttch(position, 850)
        return True

    xBoss2, yBoss2 = auto.getImg1AndImg2(
        "./chuanqi/main.jpg", "./chuanqi/boss/boss2.jpg", 0.97)
    if xBoss2 != 0:
        click(xBoss2, yBoss2 + 25)
        position = bossNice[bossIndex]
        toBossAndAttch(position, 850)
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
    xHasBoss, yHasBoss = auto.getImg1AndImg2(
        "./chuanqi/main.jpg", "./chuanqi/boss/hasLuckBossCount.jpg", 0.99)
    if xBoss1 != 0 and xHasBoss == 0:
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
    result = checkBossMap(0, True)
    if result:
        toBoss()
        return

    # sleep(1)
    # click(377, 398)
    # sleep(1)
    # # 斗笠BOSS 900
    # result = checkBossMap(0, True)
    # if result:
    #     toBoss()
    #     return

    # 盾牌
    click(544, 192)
    sleep(1)
    result = checkBossMap(2, True)
    if result:
        toBoss()
        return

    # sleep(1)
    # click(377, 398)
    # sleep(1)
    # # 盾牌BOSS 900
    # result = checkBossMap(2, True)
    # if result:
    #     toBoss()
    #     return

    # 特戒
    click(421, 192)
    sleep(1)
    result = checkBossMap(1, True)
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
    x, y = auto.getImg1AndImg2(
        "./chuanqi/main.jpg", "./chuanqi/boss800.jpg", 0.9)
    if x != 0:
        click(551, 682)


def start(attchBoss=False):
    count = 1
    while True:
        checkGameWindow()
        checkIsOutLogin()
        checkIsDead()
        # isBoss_800()
        if count % 30 == 0:
            checkIsError()
            sleep(2)
        if count % 20 == 0 and toLuckyBoss():
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