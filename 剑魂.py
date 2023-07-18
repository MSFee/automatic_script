from time import sleep
import common
import auto
import autoFindRoad
import pydirectinput

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
        common.otherKeys('3')
        sleep(6)
    common.otherKeys('a')
    common.otherKeys('space')
    common.otherKeys('left')
    common.otherKeys('space') 
    sleep(2)
    common.otherKeys('R_ctrl')
    sleep(5)

def start():

    common.otherKeys('y')
    sleep(1)
    autoFindRoad.findDoorPlus(100)
    sleep(0.5)
    common.run(0.7)
    common.otherKeys('r')
    common.run(0.3)

    autoFindRoad.findDoorPlus(100)
    sleep(0.5)
    autoFindRoad.moveRoleToYCenter()
    common.run(0.7)
    common.otherKeys('f')
    common.run(0.3)

    autoFindRoad.findDoorPlus(100)
    sleep(0.5)
    autoFindRoad.moveRoleToYCenter()
    common.otherKeys('w')
    sleep(0.5)
    common.otherKeys('e')
    common.otherKeys('e')
    common.run(0.1)

    autoFindRoad.findDoorPlus(100)
    sleep(0.5)
    autoFindRoad.moveRoleToYCenter()
    common.run(0.5)
    common.otherKeys('g')
    common.run(0.3)

    autoFindRoad.findDoorPlus(100)
    common.run(0.5)
    autoFindRoad.moveRoleToYCenter()
    common.otherKeys('t')
    sleep(0.5)
    common.otherKeys('d')
    sleep(3)
    nextGame()
    start()
start()