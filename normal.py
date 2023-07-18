from re import S
import auto
import common
import autoFindRoad
import time
result = None
def finallFindAndAttck(skill):
    autoFindRoad.findDoor(67, False, False)
    y_distance = auto.getRoleAndMiddle()
    if abs(y_distance) >= 0.1:
        if y_distance > 0:
            common.moveFunc('top', y_distance)
        else:
            common.moveFunc('bottom', abs(y_distance) + 0.1)
    common.moveFunc('right', 1)
    common.otherKeys(skill)
def start(skills, total):
    n = 1
    count = int(total / 6) + 1
    while n <= count:
        common.otherKeys('y')
        for skill in skills:
            finallFindAndAttck(skill)
        time.sleep(7)
        common.otherKeys('`')
        time.sleep(5)
        common.otherKeys('esc')
        time.sleep(1)
        common.otherKeys('esc')
        time.sleep(2)
        common.otherKeys('R_ctrl')
        time.sleep(5)
        n+=1
# 根据角色当前位置移动到目标位置
def autoMoveRoleToGoal(goalX,goalY, speed):
    roleX,roleY = auto.getRoleCurrPosition()
    if roleX == 0:
        common.moveFunc(common.getRandomResult())
    roleY += 150
    if roleX == 0:
        common.moveFunc('left', 3) # 可能角色移动到最右边，向左移动
    else:
        distanceX = roleX - goalX
        distanceY = roleY - goalY - 100
        timeX = distanceX / 200
        timeY = distanceY / 300
        if abs(timeX) > 0.1:
            timeX = (65 / speed) * timeX
            if timeX > 0:
                common.moveFunc('left', timeX)
            else:
                common.moveFunc('right', abs(timeX))
        if abs(timeY) > 0.1:
            timeY = (65 / speed) * timeY
            if timeY > 0:
                common.moveFunc('top', timeY)
            else:
                common.moveFunc('bottom', abs(timeY))

def changePickEpic():
    time.sleep(1)
    common.otherKeys('5')
    time.sleep(1)
    common.otherKeys('capslock')
    time.sleep(5)
    common.otherKeys('x')
    time.sleep(2)
    common.otherKeys('x')
    time.sleep(2)
    common.otherKeys('x')
    time.sleep(1)
    common.otherKeys('5')

def nextAndClear(slow = False):
    time.sleep(3)
    common.otherKeys('`')
    common.otherKeys('x')
    common.otherKeys('x')
    common.otherKeys('x')
    time.sleep(3.5)
    common.otherKeys('esc')
    time.sleep(2)
    common.otherKeys('esc')
    time.sleep(1)
    common.otherKeys('R_ctrl')
    time.sleep(4)
    if autoFindRoad.checkFatigueValueisClear() is True:
        common.otherKeys('f12')
        time.sleep(5)
        if slow == True:
            common.moveFunc('left', 1)
        autoFindRoad.sealGoogsAndFix()
        return True
    return False