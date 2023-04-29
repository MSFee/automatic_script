from time import sleep
import auto
import autoFindRoad
import common
import pydirectinput
import autoAttch2

def init():
    common.otherKeys('t')
    sleep(0.5)
    common.otherKeys('ctrl')
    sleep(0.5)
    common.run(1.5)

def map1():
    # 第一个
    sleep(0.5)
    common.run(0.2)
    common.otherKeys('g')
    sleep(4)
    common.run(1.3)

# 第二个图
def map2():
    common.run(0.1)
    pydirectinput.keyDown('right')
    common.otherKeys('f')
    sleep(1)
    pydirectinput.keyUp('right')
    sleep(2.5)
    common.run(1)

def map3():
    common.run(0.35)
    pydirectinput.keyDown('q')
    sleep(2)
    pydirectinput.keyUp('q')
    sleep(0.5)
    common.otherKeys('e')
    sleep(1)
    common.run(1.4)

def map4():
    common.run(0.2)
    common.otherKeys('h')
    sleep(2)
    common.run(1.5)

def map5():
    sleep(0.5)
    common.run(0.05)
    common.otherKeys('g')
    sleep(1)
    common.moveFunc('left', 0.01)
    common.otherKeys('w')
    sleep(2)
    common.run(1.3)

def boss():
    common.run(0.3)
    common.otherKeys('d')
    sleep(1)
    common.otherKeys('y')
    sleep(9)


autoAttch2.start([init, map1, map2, map3, map4, map5, boss])