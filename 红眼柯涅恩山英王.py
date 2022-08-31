from time import sleep
import auto
import autoFindRoad
import common
import pydirectinput


def init():
    common.addBuff()
    sleep(1)
    common.otherKeys('space')
    sleep(1)
    common.otherKeys('t')
    sleep(1)
    pydirectinput.keyDown('right')
    pydirectinput.press('a')
    pydirectinput.keyUp('right')
    sleep(2)
    autoFindRoad.findDoor()
# autoFindRoad.findDoor(119)
# sleep(2)

def map1():
    # 第一个
    common.run(1.4)
    common.moveFunc('bottom', 0.3)
    common.otherKeys('d')
    sleep(1)
    common.moveFunc('top', 0.6)
    common.otherKeys('q')
    sleep(2)
    common.run(0.5, 'left')
    autoFindRoad.findDoor()

# 第二个图
def map2():
    sleep(3)
    common.moveFunc('top', 0.3)
    common.moveFunc('right', 0.01)
    common.otherKeys('e')
    sleep(4)
    pydirectinput.press('2')
    common.moveFunc('right', 0.5)
    autoFindRoad.findDoor()

def map3():
    sleep(1)
    common.otherKeys('g')
    sleep(1)
    common.otherKeys('w')
    sleep(10)
    common.run(0.5)
    common.moveFunc('left', 0.01)
    common.otherKeys('f')
    common.run(1)
    autoFindRoad.findDoor()

def map4():
    common.moveFunc('bottom', 0.1)
    common.run(0.5)
    common.otherKeys('h')
    sleep(1.5)
    common.run(4)
    common.moveFunc('bottom', 2)
    common.moveFunc('left', 0.4)

def map5():
    common.moveFunc('bottom', 0.6)
    common.moveFunc('right', 0.01)
    common.otherKeys('e')
    sleep(0.5)
    common.otherKeys('d')
    sleep(0.5)
    common.otherKeys('f')
    sleep(1)
    common.otherKeys('w')

def map6():
    common.run(0.3)
    common.otherKeys('g')
    sleep(1.5)
    common.otherKeys('q')
    sleep(1)
    common.otherKeys('w')
    sleep(3)
    common.moveFunc('right', 0.5)
    autoFindRoad.findDoor()

def map7():
    sleep(1)
    common.otherKeys('ctrl')
    common.run(0.8)
    common.moveFunc('bottom', 0.3)
    common.otherKeys('d')
    sleep(0.5)
    common.otherKeys('a')
    sleep(0.5)
    common.otherKeys('r')
    sleep(0.5)
    common.otherKeys('e')
    sleep(0.5)
    common.otherKeys('f')
    common.run(0.2, 'left')
    common.moveFunc('right', 0.01)
    common.otherKeys('alt')
    sleep(1.5)
    common.otherKeys('y')
    sleep(5)
    common.otherKeys('q')
autoFindRoad.findDoor(115)
# init()
# map1()
# map2()
map3()
# map4()
# map5()
# map6()
# map7()