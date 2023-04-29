import auto
import autoFindRoad
from time import sleep
import common

import autoAttch

def addBuff():
    common.otherKeys('ctrl')
    sleep(1)

def attch1():
    common.otherKeys('alt')
    common.moveFunc('top', 1)
    common.run(0.5)
    common.otherKeys('a')
    sleep(1)
    common.run(0.5)

def attch2():
    common.run(0.5)
    common.otherKeys('e')
    sleep(1)
    common.run(1.2)

def attch3():
    common.moveFunc('top', 1)
    common.run(0.7, 'left')
    common.otherKeys('r')
    sleep(1)
    common.moveFunc('top', 0.5)
    sleep(2)
    common.moveFunc('bottom', 0.5)

def attch4():
    common.run(0.5, 'left')
    common.otherKeys('f')
    sleep(1)
    common.otherKeys('alt')
    common.moveFunc('bottom', 0.3)

def attch5():
    common.moveFunc('top', 1.2)
    common.moveFunc('right', 0.01)
    common.otherKeys('g')
    sleep(1)

def acctch_boss():
    common.moveFunc('top', 0.8)
    common.moveFunc('left', 0.4)
    common.otherKeys('r')

autoAttch.start([addBuff, attch1, attch2, attch3, attch4, attch5, acctch_boss], 80)