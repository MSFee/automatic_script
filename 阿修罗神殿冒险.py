from time import sleep
import common
import auto
import normal
import autoFindRoad

def addBuff():
    common.otherKeys('t')
    sleep(2)
    common.otherKeys('y')
    sleep(1)
    common.otherKeys('g')
    sleep(1)


def map1():
    sleep(0.5)
    common.moveFunc('top', 1.2)
    common.otherKeys('s')
    sleep(0.5)
    common.run(1.3)


def map2():
    if auto.checkHasEpic() is True:
        common.moveFunc('left', 0.5)
        normal.changePickEpic()
        common.moveFunc('right', 0.5)
    sleep(0.5)
    normal.moveRoleToYCenter()
    common.run(0.7)
    common.otherKeys('w')
    sleep(0.5)
    common.run(1)


def map3():
    if auto.checkHasEpic() is True:
        common.moveFunc('bottom', 0.5)
        normal.changePickEpic()
        common.moveFunc('top', 0.5)
    sleep(0.5)
    common.moveFunc('top', 1.2)
    common.run(0.5, 'left')
    common.otherKeys('q')
    sleep(1)
    common.moveFunc('top', 0.5)
    sleep(1)
    common.moveFunc('bottom', 0.3)
    common.run(0.3, 'left')

def map4():
    if auto.checkHasEpic() is True:
        common.moveFunc('right', 0.5)
        normal.changePickEpic()
        common.moveFunc('left', 0.5)
    sleep(0.5)
    normal.moveRoleToYCenter(65, [500, 0, 800, 600])
    common.otherKeys('s')
    common.run(0.5, 'left')
    common.otherKeys('a')
    sleep(0.5)


def map5():
    if auto.checkHasEpic() is True:
        common.moveFunc('bottom', 0.5)
        normal.changePickEpic()
        common.moveFunc('top', 0.5)
    sleep(0.5)
    common.moveFunc('top', 1)
    common.moveFunc('right', 0.01)
    common.otherKeys('d')
    sleep(1)
    taskx, taskYy = auto.checkHasTask()
    if taskx != 0:
        common.run(1, 'left')
        common.moveFunc('bottom', 1)
        common.run(4)
        common.moveFunc('left', 0.8)
        autoFindRoad.findDoorPlus()
        common.moveFunc('top', 0.5)
    else:
        common.run(0.8)
        common.moveFunc('top', 0.5)

def map6():
    if auto.checkHasEpic() is True:
        common.moveFunc('bottom', 0.5)
        normal.changePickEpic()
        common.moveFunc('top', 0.5)
    common.moveFunc('top', 0.6)
    common.run(0.2, 'left')
    common.otherKeys('alt')

def start():
    while True:
        addBuff()
        autoFindRoad.findDoor()
        map1()
        autoFindRoad.findDoor()
        map2()
        autoFindRoad.findDoor()
        map3()
        autoFindRoad.findDoorPlus(65, True)
        map4()
        autoFindRoad.findDoorPlus(65, False, True)
        map5()
        autoFindRoad.findDoor()
        map6()
        if normal.nextAndClear(True):
            break
start()
