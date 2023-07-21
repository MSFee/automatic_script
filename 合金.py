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

    common.otherKeys('t')
    sleep(0.5)
    common.otherKeys('alt')
    sleep(0.5)
    autoFindRoad.findDoorPlus(100)
    sleep(0.5)
    common.run(0.3)
    common.otherKeys('w')
    sleep(0.5)
    common.run(0.6)

    autoFindRoad.findDoorPlus(100)
    sleep(0.5)
    autoFindRoad.moveRoleToYCenter()
    common.run(0.5)
    common.otherKeys('d')
    sleep(0.5)
    common.run(0.7)

    autoFindRoad.findDoorPlus(100)
    sleep(0.5)
    autoFindRoad.moveRoleToYCenter()
    common.run(0.7)
    common.otherKeys('w')
    sleep(1)
    common.run(0.5)

    autoFindRoad.findDoorPlus(100)
    sleep(0.5)
    autoFindRoad.moveRoleToYCenter()
    common.run(0.7)
    common.otherKeys('e')
    sleep(0.5)
    common.run(0.5)

    autoFindRoad.findDoorPlus(100)
    common.run(0.3)
    autoFindRoad.moveRoleToYCenter()
    common.otherKeys('f')
    sleep(0.5)
    common.otherKeys('r')
    sleep(0.5)
    common.otherKeys('a')
    sleep(3)
    nextGame()
    start()
start()