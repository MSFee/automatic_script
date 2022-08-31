from time import sleep
import common
import normal


def callBack1():
    common.otherKeys('y')
    sleep(1)
    common.otherKeys('ctrl')
    sleep()


def callBack2():
    common.moveFunc('top', 1.4)
    common.run(0.7)
    common.otherKeys('w')
    common.otherKeys('w')
    sleep(3.5)
    common.run(0.6)


def callBack3():
    common.run(0.6)
    normal.moveRoleToYCenter(65)
    common.otherKeys('alt')
    common.run(0.5)
    sleep(2)
    common.run(1)


def callBack4():
    common.moveFunc('top', 1.4)
    common.run(0.6, 'left')
    common.otherKeys('w')
    common.moveFunc('bottom', 0.5)
    common.moveFunc('right', 0.01)
    common.otherKeys('a')
    sleep(2)
    common.moveFunc('top', 0.5)
    common.run(0.5, 'left')

def callBack5():
    common.run(0.7, 'left')
    normal.moveRoleToYCenter(65, [0,0, 400, 600])
    common.otherKeys('s')
    sleep(2)

def callBack6():
    common.moveFunc('top', 1.4)
    common.moveFunc('right', 0.01)
    common.otherKeys('h')
    sleep(3)

def callBack9():
    common.moveFunc('top', 1)
    common.moveFunc('left', 0.01)
    sleep(0.2)
    common.otherKeys('g')