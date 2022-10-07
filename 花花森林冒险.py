from time import sleep
import autoFindRoad
import normal
import auto
import common

def addBuff():
        common.otherKeys('a')
        sleep(0.5)
        common.otherKeys('s')
        sleep(0.5)
def map1():
    sleep(0.5)
    common.moveFunc('top', 1)
    common.run(0.5)
    common.otherKeys('w')
    common.run(0.6)
def map2():
    if auto.checkHasEpic() is True:
        common.moveFunc('left', 0.5)
        normal.changePickEpic()
        common.moveFunc('right', 0.5)
    sleep(0.5)
    normal.moveRoleToYCenter(77)
    common.run(0.3)
    common.otherKeys('f')
    sleep(0.5)
    common.run(1.3)
def map3():
    if auto.checkHasEpic() is True:
        common.moveFunc('bottom', 0.5)
        normal.changePickEpic()
        common.moveFunc('top', 0.5)
    sleep(0.5)
    common.moveFunc('top', 1)
    common.moveFunc('left', 0.5)
    common.otherKeys('r')
    sleep(1.5)
    common.moveFunc('top', 0.3)
    sleep(1)
    common.moveFunc('bottom', 0.3)
    common.run(0.3, 'left')
def map4():
    if auto.checkHasEpic() is True:
        common.moveFunc('right', 0.5)
        normal.changePickEpic()
        common.moveFunc('left', 0.5)
    sleep(0.5)
    normal.moveRoleToYCenter(77)
    common.run(0.5, 'left')
    common.otherKeys('w')
    sleep(1)
def map5():
    if auto.checkHasEpic() is True:
        common.moveFunc('bottom', 0.5)
        normal.changePickEpic()
        common.moveFunc('top', 0.5)
    sleep(0.5)
    common.moveFunc('top', 1)
    common.run(0.35)
    common.otherKeys('g')
    sleep(1)
    taskx, taskYy = auto.checkHasTask()
    autoFindRoad.findDoorPlus(77)
    if taskx != 0:
       sleep(3)
def map6():
    if auto.checkHasEpic() is True:
        common.moveFunc('bottom', 0.5)
        normal.changePickEpic()
        common.moveFunc('top', 0.5)
    sleep(0.5)
    common.moveFunc('top', 0.7)
    common.run(0.3, 'left')
    sleep(0.1)
    common.otherKeys('alt')
    sleep(1)
def start():
    while True:
        addBuff()
        autoFindRoad.findDoorPlus(77)
        map1()
        autoFindRoad.findDoorPlus(77)
        map2()
        autoFindRoad.findDoorPlus(77)
        map3()
        autoFindRoad.findDoorPlus(77, True)
        map4()
        autoFindRoad.findDoorPlus(77, False, True)
        map5()
        map6()
        if normal.nextAndClear(True):
            break
start()