from time import sleep
from tkinter import Y
import auto
import common

#   将角色移动到y轴中间
def moveRoleToYCenter(speed = 122, cropPosition = [0,0,450,600]):
    y_distance = auto.getRoleAndMiddle(cropPosition)
    y_distance = y_distance * (122 / speed)
    y_distance /= 320
    if abs(y_distance) >= 0.02:
        if y_distance < 0:
            common.moveFunc('top', abs(y_distance))
        else:
            common.moveFunc('bottom', abs(y_distance))
def findDoorPlus(speed = 100):
    sleep(0.5)
    total = 1
    while total <= 10:
        timeX, timeY = auto.getRoleAndDoor()
        if timeX is None or timeX is False or timeX < 0:
            common.moveFunc('right', 0.2) 
            total += 1
            continue
        timeX = (65 / speed) * timeX
        common.moveFunc('right', timeX)
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

# 判断当前疲劳值是否清空 或者判断当前是否打死BOSS准备重新进入地图
def checkFatigueValueisClear(num):
    auto.saveAndCropFunc()
    img,img_size = auto.getImgInfo('./dnf.jpg')
    over,over_size = auto.getImgInfo('./others_pic/over.jpg')
    system, system_size = auto.getImgInfo('./others_pic/system_menu.jpg')
    s_curr, s_x, s_y = auto.search_returnPoint(img,system,system_size, 0.8)
    if s_x != None:
        common.otherKeys('esc')
        auto.saveAndCropFunc()
        img,img_size = auto.getImgInfo('./dnf.jpg')
    curr, x, y = auto.search_returnPoint(img,over,over_size, num)
    if x is None:
        return False
    else:
        return True

# 自动出售物品并维修装备
def sealGoogsAndFix():
    common.moveFunc('left', 0.85)
    common.moveFunc('top', 2)
    
    while auto.checkHasMachine() is False:
        common.moveFunc('left', 0.02)
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

    # # 维修装备
    # common.otherKeys('s')
    # sleep(1)
    # common.otherKeys('space')

    common.otherKeys('esc')