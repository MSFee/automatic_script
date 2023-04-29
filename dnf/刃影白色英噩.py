import common
from time import sleep
import autoAttch2

def map1():
    common.otherKeys('y')
    sleep(1.5)
    common.run(1)


def map2():
    common.otherKeys('ctrl')
    sleep(1.5)
    common.run(0.45)


def map3():
    common.run(0.4)
    common.otherKeys('w')
    sleep(0.6)
    common.otherKeys('e')
    sleep(1)
    common.otherKeys('s')
    sleep(1)
    common.run(0.6)

def map4():
    common.run(0.5)
    common.otherKeys('d')
    sleep(1.5)
    common.moveFunc('top', 0.3)

def map5():
    common.otherKeys('ctrl')
    common.run(0.2)


def map6():
    common.moveFunc('top', 0.4)
    common.otherKeys('g')
    sleep(1.5)
    common.moveFunc('top', 0.4)
    common.run(1)
    common.moveFunc('bottom', 0.2)
    sleep(0.5)

def map7():
    common.run(0.3)
    common.otherKeys('r')
    sleep(1)
    common.run(0.6)

def map8():
    common.moveFunc('top', 0.4)
    common.run(0.2)
    common.otherKeys('f')
    sleep(2)
    common.run(0.3)
    common.moveFunc('top', 0.4)
    common.run(0.2)


def boss():
    common.moveFunc('top', 0.4)
    common.run(0.4)
    common.otherKeys('ctrl')
    sleep(1)
    common.otherKeys('h')
    sleep(8)


autoAttch2.start([map1, map2, map3, map4, map5, map6, map7, map8, boss], 110)