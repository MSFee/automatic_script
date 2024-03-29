from time import sleep
import pyautogui
import autoFindRoad
import auto
import common
from startgGame import closeWindow, getWindow
import pydirectinput
import otherUntils
import datetime

def getCurrSmallMap(callback1, callback2, callback3, callback4, callback5, callback6, callback7, callback8, callback9):
    auto.saveAndCropFunc('small_map', [737, 47, 794, 139])
    x, y = auto.getImg1AndImg2('small_map1.jpg', './pic/map_role.jpg')
    if x == 0:
        sleep(0.5)
        getCurrSmallMap(callback1, callback2, callback3, callback4,
                        callback5, callback6, callback7, callback8, callback9)
        return
    x1, y1 = auto.getImg1AndImg2('small_map.jpg', './pic/question.jpg')
    flag = x1 != 0  # true表示图已经打完
    if x == 29.5 and y == 76:
        # 第一个图
        callback1()
        autoFindRoad.findDoorPlus()
    elif x == 11.5 and y == 58:
        # 第二个图 （左边）
        if flag is True:
            autoFindRoad.findDoorPlus()
        else:
            callback2()
    elif x == 29.5 and y == 58:
        # 第二个图 （中间）
        if flag is True:
            autoFindRoad.findDoorPlus()
        else:
            callback3()
    elif x == 47.5 and y == 58:
        # 第二个图 （右边）
        if flag is True:
            autoFindRoad.findDoorPlus()
        else:
            callback4()
    elif x == 11.5 and y == 40:
        # 第三个图 （左边）
        if flag is True:
            autoFindRoad.findDoorPlus()
        else:
            callback5()
    elif x == 29.5 and y == 40:
        # 第三个图 （中间）
        if flag is True:
            autoFindRoad.findDoorPlus()
        else:
            callback6()
    elif x == 47.5 and y == 40:
        # 第三个图 （右边）
        if flag is True:
            autoFindRoad.findDoorPlus()
        else:
            callback7()
    elif x == 29.5 and y == 22:
        # 第四个图 （中间）
        if flag is True:
            autoFindRoad.findDoorPlus()
        else:
            callback8()
    else:
        # boss图 # 29.5  4
        callback9()
    getCurrSmallMap(callback1, callback2, callback3, callback4,
                    callback5, callback6, callback7, callback8, callback9)

# 判断刚进入游戏，赛利亚房间，是否有弹窗
def checkHasCloseBtn():
   sleep(30)
   auto.saveAndCropFunc()
   x, y = auto.getImg1AndImg2('./dnf.jpg', './others_pic/close_btn.jpg')
   if x != 0:
    common.clickPosition(x, y)
    sleep(3)


def goToMonster(needUp = True):
    common.otherKeys('space')
    sleep(5)
    checkHasCloseBtn()
    common.moveFunc('right', 3)
    common.otherKeys('space')
    sleep(3)
    common.moveFunc('right', 5)
    sleep(3)
    if needUp:
        common.otherKeys('up')
    sleep(0.5)
    common.otherKeys('space')

def findStartGameBtn():
    count = 0
    while auto.findGameSpace() is False:
        count += 1
        sleep(5)
        if count > 50:
            x, y = auto.getImg1AndImg2('./dnf.jpg', './others_pic/go_home.jpg')
            if x and y:
                common.clickPosition(x, y+20)
                sleep(5)
                changeRole()
            else:
                otherUntils.chatWithweixin("findStartGameBtn 死循环了")
                otherUntils.shutdown()
def changeRole():
    checkHasCloseBtn()
    common.otherKeys('esc')
    auto.saveAndCropFunc()
    x, y = auto.getImg1AndImg2('./dnf.jpg', './others_pic/choise_role.jpg')
    sleep(2)
    common.clickPosition(x, y)
    findStartGameBtn()
    common.otherKeys('right')
    sleep(3)
    goToMonster(False)

def startGame():
    x, y = auto.findWegameStarGameBtn()
    pydirectinput.click(x, y)
    findStartGameBtn()
    pyautogui.moveTo(546, 241, 0.1)
    pydirectinput.click()
    goToMonster()

def logoutGame():
    hwnd, h, w = getWindow()
    closeWindow(hwnd)
    sleep(10)
    startGame()



def checkIsClear():
    common.otherKeys('R_ctrl')
    sleep(5)
    if autoFindRoad.checkFatigueValueisClear(0.8):
        return True
    return False
def nextGame():
    common.otherKeys('`')
    common.otherKeys('x')
    common.otherKeys('x')
    common.otherKeys('x')
    common.otherKeys('x')
    sleep(3.5)
    common.otherKeys('3')
    sleep(6)
    common.otherKeys('a')
    common.otherKeys('space')
    common.otherKeys('left')
    common.otherKeys('space')
    sleep(2)
    common.otherKeys('esc')
    if otherUntils.check_network_status() is False:
        otherUntils.checkISNotNetWork()
        logoutGame()
        return False, 0
    if autoFindRoad.checkFatigueValueisClear(0.8) is False: # 未符合预期
        otherUntils.autoScreensHot()
        logoutGame()
        return False, 0

    if checkIsClear(): # 疲劳值清空
        otherUntils.autoScreensHot()
        common.otherKeys('shiftright')
        sleep(5)
        changeRole()
        return False, 1
    return True, 0

# 判断刚进入地图，是否命中安全模式
def checkisSafe():
   common.otherKeys('z')
   sleep(1)
   auto.saveAndCropFunc()
   x, y = auto.getImg1AndImg2('./dnf.jpg', './others_pic/60s_safe.jpg')
   if x != 0:
       common.otherKeys('esc')
   sleep(0.5)

def checkTime():
    now = datetime.datetime.now()
    if now.hour >= 13 and now.hour <= 18:
        return True
    return False