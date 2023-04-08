import autoAttch3
import common
from time import sleep

def map1():
    common.otherKeys('y')
    sleep(1)
    common.run(1.3)

def map2():
    common.run(1.3)
    common.otherKeys('e')
    common.otherKeys('e')
    sleep(1.5)

def map3():
    common.run(0.7)
    common.otherKeys('f')
    sleep(3)
    common.otherKeys('e')
    sleep(0.5)
    common.run(0.5)

def map4():
    common.run(0.6)
    common.otherKeys('t')
    sleep(0.5)
    common.otherKeys('g')
    sleep(2)

def map5():
    common.run(0.2)
    common.otherKeys('r')
    sleep(0.5)
    common.run(0.5)
    common.otherKeys('e')
    common.otherKeys('e')
    sleep(2)
    common.otherKeys('ctrl')

def boss():
    common.otherKeys('w')
    sleep(0.5)
    common.otherKeys('d')
    sleep(1.3)
    common.otherKeys('alt')
    sleep(0.6)
    common.otherKeys('ctrl')
    sleep(8)

autoAttch3.start([map1, map2, map3, map4, map5, boss], 100)