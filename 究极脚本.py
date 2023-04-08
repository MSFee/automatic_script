import auto
from autoFindRoad import findDoor, findDoorPlus
from time import sleep
import normal
import common

ROLESPEED = 94.5  # 角色初速度

hasEmergencyMap = False # 是否遇到紧急任务

#   9
#   8
#  567
#  234
#   1

def guiqi_addBuff():
    common.otherKeys('y')
    sleep(2)
    common.otherKeys('ctrl')
    sleep(1)

# 倒数第二排，中间图


def guiqi_attch1():
    common.moveFunc('top', 1)
    common.run(0.55)
    common.otherKeys('w')
    common.otherKeys('w')
    sleep(3.5)
    common.run(0.48)
    sleep(0.5)

# 倒数第二排，右边图


def guiqi_attch2():
    common.run(0.48)
    normal.moveRoleToYCenter(ROLESPEED)
    common.otherKeys('alt')
    common.run(0.4)
    sleep(2)
    common.run(0.8)
    sleep(0.5)

# 倒数第三排，右边图


def guiqi_attch3():
    common.moveFunc('top', 1)
    common.run(0.48, 'left')
    common.otherKeys('w')
    common.moveFunc('bottom', 0.2)
    common.moveFunc('right', 0.01)
    common.otherKeys('a')
    sleep(4)

# 倒数第三排，中间图


def guiqi_attch4():
    sleep(0.5)
    common.run(0.3, 'left')
    normal.moveRoleToYCenter(ROLESPEED, [300, 0, 800, 600])
    common.otherKeys('s')
    sleep(2)


def guiqi_acctch5(needRun = True):
    common.moveFunc('top', 1.2)
    common.moveFunc('right', 0.01)
    common.otherKeys('h')
    sleep(3)
    if needRun:
        common.run(0.5)
        sleep(0.5)
    else:
        common.run(0.5, 'left')
        common.moveFunc('bottom', 1)
        common.run(4)
        common.moveFunc('top', 2)


def guiqi_acctch_boss():
    common.moveFunc('top', 0.8)
    common.moveFunc('left', 0.01)
    sleep(0.2)
    common.otherKeys('g')
    sleep(1)
    common.otherKeys('w')
    sleep(3)


def nextGame(needSale = False):
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
        common.otherKeys('esc')
        sleep(6)
    common.otherKeys('esc')
    sleep(2)
    common.otherKeys('R_ctrl')
    sleep(5)

while True:
    sleep(0.5)
    auto.saveAndCropFunc('small_map', [737, 47, 794, 139])
    auto.saveAndCropFunc()
    x1, y1 = auto.getImg1AndImg2('small_map.jpg', './pic/question.jpg')
    x, y = auto.getImg1AndImg2('small_map.jpg', './pic/map_role.jpg')
    boss_x, boss_y = auto.getImg1AndImg2('small_map.jpg', './pic/boss.jpg')
    emergency_map_x, emergency_map_y = auto.getImg1AndImg2('small_map.jpg', './pic/emergency_map.jpg')
    if emergency_map_x:
        hasEmergencyMap = not hasEmergencyMap
    packFully_x, packFully_y = auto.getImg1AndImg2('dnf.jpg', './pic/pack_fully.jpg')
    print(packFully_x)
    flag = x1 != 0  # true表示图已经打完
    if x == 29.5 and y == 76:
        # 第一个图
        print('第一个图')
        guiqi_addBuff()
        findDoor(ROLESPEED)
    elif x == 11.5 and y == 58:
        print("倒数第二排，左边图")
    elif x == 29.5 and y == 58:
        # 第二个图 （中间）
        print("倒数第二排，中间图")
        guiqi_attch1()
        findDoor(ROLESPEED)

    elif x == 47.5 and y == 58:
        # 第二个图 （右边）
        print("倒数第二排，右边图")
        guiqi_attch2()
        findDoor(ROLESPEED)
    elif x == 11.5 and y == 40:
        print("倒数第三排，左边图")
    elif x == 29.5 and y == 40:
        # 第三个图 （中间）
        print("倒数第三排，中间图")
        guiqi_attch4()
        findDoorPlus(ROLESPEED, False, True)
        common.moveFunc('top', 0.3)
    elif x == 47.5 and y == 40:
        # 第三个图 （右边）
        print("倒数第三排，右边图")
        guiqi_attch3()
        findDoorPlus(ROLESPEED, True)
    elif (emergency_map_x and hasEmergencyMap) or (x == 29.5 and y == 22):
        print("倒数第四排，中间图")
        guiqi_acctch5(emergency_map_x == 0)
        findDoor(ROLESPEED)
        if emergency_map_x:
            sleep(3)
    else:
        if boss_x:
            guiqi_acctch_boss()
            nextGame(packFully_x != 0)
        else:
            print('未知图')
