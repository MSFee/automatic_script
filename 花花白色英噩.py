from time import sleep
import auto
import autoFindRoad
import common
import pydirectinput
import autoAttch2

def init():
    common.otherKeys('a')
    sleep(0.5)
    common.otherKeys('s')
    sleep(0.5)
    common.run(1.2)

def map1():
    # 第一个

    common.run(0.2)
    common.otherKeys('r')
    sleep(0.5)
    common.otherKeys('w')
    sleep(2)
    common.otherKeys('q')
    sleep(0.5)
    common.run(1.2)

# 第二个图
def map2():
    common.otherKeys('t')
    sleep(0.5)
    common.otherKeys('f')
    sleep(0.5)
    common.run(1.5)

def map3():
    common.run(0.2)
    common.otherKeys('h')
    sleep(1.5)
    common.otherKeys('y')
    sleep(2)
    common.run(1.1)

def map4():
    common.otherKeys('e')
    sleep(1)
    common.otherKeys('q')
    sleep(0.5)
    common.run(0.6)
    common.otherKeys('g')
    sleep(0.9)
    common.run(1)

def map5():
    sleep(0.5)
    common.otherKeys('f')
    sleep(1)
    common.run(1.5)

def boss():
    common.run(0.3)
    common.otherKeys('d')
    sleep(1)
    common.otherKeys('y')
    sleep(9)


autoAttch2.start([init, map1, map2, map3, map4, map5, boss])