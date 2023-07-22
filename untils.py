from time import sleep
import pyautogui
import autoFindRoad
import auto
import common
from startgGame import closeWindow, getWindow
import pydirectinput


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


def loginGame(isNextRole=False):
    print('退出游戏')
    hwnd, h, w = getWindow()
    closeWindow(hwnd)
    sleep(10)
    x, y = auto.findWegameStarGameBtn()
    pydirectinput.click(x, y)
    while auto.findGameSpace() is False:
        sleep(5)
    pyautogui.moveTo(546, 241, 0.1)
    pydirectinput.click()
    if isNextRole:
        common.otherKeys('right')
        sleep(0.5)
    common.otherKeys('space')
    sleep(5)
    common.moveFunc('right', 3)
    common.otherKeys('space')
    sleep(3)
    common.moveFunc('right', 5)
    common.otherKeys('up')
    sleep(0.5)
    common.otherKeys('space')


def checkIsClear():
    common.otherKeys('R_ctrl')
    sleep(5)
    if autoFindRoad.checkFatigueValueisClear(0.8):
        return True
    return False
def nextGame(needSale=False):
    common.otherKeys('`')
    common.otherKeys('x')
    common.otherKeys('x')
    common.otherKeys('x')
    common.otherKeys('x')
    if needSale:
        sleep(8)
        common.otherKeys('a')
        sleep(0.5)
        common.otherKeys('space')
        sleep(0.5)
        common.otherKeys('left')
        sleep(0.5)
        common.otherKeys('space')
        sleep(1)
    else:
        sleep(3.5)
        common.otherKeys('3')
        sleep(6)
    common.otherKeys('a')
    common.otherKeys('space')
    common.otherKeys('left')
    common.otherKeys('space')
    sleep(2)
    common.otherKeys('esc')
    if autoFindRoad.checkFatigueValueisClear(0.8) is False: # 未符合预期
        loginGame()
        return False, 0

    if checkIsClear(): # 疲劳值清空
        loginGame(True)
        return False, 1
    return True, 0
