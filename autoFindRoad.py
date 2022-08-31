from time import sleep
from tkinter import Y
import auto
import common
def findDoor(speed = 65, isNeedColumn = True, isNeedToLeft = True, isTaskDoor = False):
    total = 1
    flag = False
    while total <= 10:
        sleep(1)
        timeX, timeY = auto.getRoleAndDoor(isTaskDoor)
        if timeX is False:
            common.ranDomMoveRole() 
            total += 1
        if timeX is None:
            common.moveFunc('right', 0.2) 
            total += 1
            continue
        if abs(timeX) > 0.1:
            timeX = (65 / speed) * timeX
            if timeX < 0 and isNeedToLeft is False:
                common.moveFunc('right', 1)
                continue
            if timeX > 0:
                common.moveFunc('right', timeX)
            else:
                common.moveFunc('left', abs(timeX))
        if isNeedColumn is False:
            return
        if abs(timeY) > 0.1:
            print(timeY)
            # timeY = (65 / speed) * timeY
            if timeY > 0:
                common.moveFunc('bottom', timeY)
            else:
                common.moveFunc('top', abs(timeY))
        break
def findDoorPlus(speed = 65, limitLeft = False, limitTop = False):
    total = 1
    while total <= 10:
        if total > 4:
            common.otherKeys('.')
        sleep(1)
        timeX, timeY = auto.getRoleAndDoor()
        if total > 4:
            common.otherKeys('.')
        if timeX is None:
            if limitLeft is True:
                common.moveFunc('left', 0.2)
            else:
                common.moveFunc('right', 0.2) 
            total += 1
            continue
        if timeX is False:
            if limitLeft is True:
                common.moveFunc('right', 0.2)
            else:
                common.moveFunc('left', 0.2) 
            # findRolePositionAndMoveCenter()
            total -= 1
            continue
        if limitTop is True:
            if abs(timeY) < 0.4:
                if timeX > 0:
                    common.moveFunc('left', 0.3)
                else:
                    common.moveFunc('right', 0.3)
                continue
            else:
                if abs(timeX) > 1:
                    common.moveFunc('right', 0.3)
                    continue
        if abs(timeX) > 0.1:
            timeX = (65 / speed) * timeX
            # 只往右走
            # if timeX < 0:
            #     common.moveFunc('right', 1)
            #     continue
            if timeX > 0:
                if limitLeft is True and abs(timeY) < 0.2:
                    common.moveFunc('left', 1)
                    continue
                else:
                    common.moveFunc('right', timeX)
            else:
                common.moveFunc('left', abs(timeX))
        if abs(timeY) > 0.1:
            timeY = (65 / speed) * timeY
            if timeY > 0:
                common.moveFunc('bottom', timeY)
            else:
                common.moveFunc('top', abs(timeY))
        break
# 寻找角色位置，将角色位置移动到地图正中间
def findRolePositionAndMoveCenter(count = 0):
    if count > 5:
        return
    flag = True
    x,y = auto.getRoleCurrPosition()
    while x == 0:
        common.ranDomMoveRole()
        x,y = auto.getRoleCurrPosition()
    if abs(y - 400) > 20:
        if y > 400:
            common.moveFunc('top', (y - 400) / 230)
        else:
            common.moveFunc('bottom', (400 - abs(y)) / 150)
        flag = False
    if abs(x - 400) > 50:
        if x > 400:
            common.moveFunc('left', (x - 400) / 200)
        else:
            common.moveFunc('right', abs((x - 400) / 200))
        flag = False
    if flag == False:
        findRolePositionAndMoveCenter(count + 1)
# 自动寻找紧急任务门
def findTaskDoor(speed = 65):
    common.otherKeys('.')
    x,y = auto.checkHasTask()
    print(x,y)
    if x == 0:
        findRolePositionAndMoveCenter()
    flag = False
    while x == 0:
        x,y = auto.checkHasTask()
        if flag is False:
            common.run(0.5, 'left')
            x,y = auto.checkHasTask()
            if x != 0:
                break
            common.run(0.5, 'left')
            x,y = auto.checkHasTask()
            if x != 0:
                break
            common.run(0.5, 'left')
            x,y = auto.checkHasTask()
            if x != 0:
                break
            flag = True
        else:
            common.run(0.5, 'right')
            x,y = auto.checkHasTask()
            if x != 0:
                break
            common.run(0.5, 'right')
            x,y = auto.checkHasTask()
            if x != 0:
                break
            common.run(0.5, 'right')
            x,y = auto.checkHasTask()
            if x != 0:
                break
            flag = False
    findDoor(speed, True, True, True)
    common.otherKeys('.')

# 判断当前疲劳值是否清空
def checkFatigueValueisClear():
    auto.saveAndCropFunc()
    img,img_size = auto.getImgInfo('./dnf.jpg')
    over,over_size = auto.getImgInfo('./others_pic/over.jpg')
    system, system_size = auto.getImgInfo('./others_pic/system_menu.jpg')
    s_curr, s_x, s_y = auto.search_returnPoint(img,system,system_size, 0.8)
    if s_x != None:
        common.otherKeys('esc')
        auto.saveAndCropFunc()
        img,img_size = auto.getImgInfo('./dnf.jpg')
    curr, x, y = auto.search_returnPoint(img,over,over_size, 0.9)
    if x is None:
        return False
    else:
        return True

# 自动出售物品并维修装备
def sealGoogsAndFix():
    common.moveFunc('left', 0.85)
    common.moveFunc('top', 2)
    
    while auto.checkHasMachine() is False:
        common.moveFunc('right', 0.02)
        sleep(1.5)

    # 出售装备
    common.otherKeys('space')
    sleep(1)
    common.otherKeys('space')
    sleep(1)
    common.otherKeys('a')
    sleep(1)
    common.otherKeys('space')
    sleep(1)
    common.otherKeys('left')
    sleep(1)
    common.otherKeys('space')
    sleep(1)

    # 维修装备
    common.otherKeys('s')
    sleep(1)
    common.otherKeys('space')

    common.otherKeys('esc')