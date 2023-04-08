import common
from time import sleep
import autoAttch2

def map1():
    common.otherKeys('y')
    sleep(1.5)
    common.run(1)


def map2():
    common.run(0.8)
    common.otherKeys('r')
    sleep(2)
    common.run(1.2)

def map3():
    common.otherKeys('w')
    sleep(0.6)
    common.otherKeys('e')
    common.otherKeys('e')
    sleep(1)

def map4():
    common.run(0.6)
    common.otherKeys('g')
    sleep(1.5)


def map5():
    common.moveFunc('top', 0.3)
    common.run(0.3)
    common.otherKeys('f')
    sleep(1)


def map6():
    common.moveFunc('top', 0.5)
    common.otherKeys('f')
    common.moveFunc('top', 0.5)
    common.run(1.5)
    common.moveFunc('bottom', 0.3)

def map7():
    common.moveFunc('top', 0.7)
    common.otherKeys('t')
    sleep(0.5)
    common.otherKeys('d')
    sleep(3)
    common.moveFunc('right', 0.2)
    common.moveFunc('right', 0.2)

def map8():
    common.moveFunc('top', 0.4)
    common.otherKeys('w')
    sleep(0.5)
    common.otherKeys('e')
    common.otherKeys('e')
    sleep(1)

def boss():
    common.run(0.35)
    common.otherKeys('t')
    sleep(0.5)
    common.otherKeys('alt')
    sleep(2.5)
    common.otherKeys('ctrl')
    sleep(6)
    sleep(2)


autoAttch2.start([map1, map2, map3, map4, map5, map6, map7, map8, boss], 100)


