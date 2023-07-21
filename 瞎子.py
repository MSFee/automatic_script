from time import sleep
import common
import auto
import autoFindRoad
import pydirectinput
import startgGame
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
    common.otherKeys('esc')
    common.otherKeys('R_ctrl')
    sleep(5)

def start():

    common.otherKeys('y')
    sleep(0.5)
    common.otherKeys('ctrl')
    sleep(0.5)
    common.otherKeys('g')
    sleep(1)
    autoFindRoad.findDoorPlus(100)
    sleep(0.5)
    common.run(0.3)
    common.otherKeys('s')
    sleep(0.5)
    common.otherKeys('q')
    common.run(0.6)

    autoFindRoad.findDoorPlus(100)
    sleep(0.8)
    autoFindRoad.moveRoleToYCenter()
    common.run(0.3)
    common.otherKeys('d')
    common.run(0.7)

    autoFindRoad.findDoorPlus(100)
    sleep(0.5)
    autoFindRoad.moveRoleToYCenter()
    common.otherKeys('w')
    sleep(1)
    common.run(1.2)

    autoFindRoad.findDoorPlus(100)
    sleep(0.5)
    autoFindRoad.moveRoleToYCenter()
    common.run(0.3)
    common.otherKeys('f')
    common.run(0.5)

    autoFindRoad.findDoorPlus(100)
    common.run(0.5)
    autoFindRoad.moveRoleToYCenter()
    common.otherKeys('s')
    sleep(0.5)
    common.otherKeys('alt')
    sleep(2)
    common.otherKeys('a')
    sleep(1)
    nextGame()
    start()
# start()
