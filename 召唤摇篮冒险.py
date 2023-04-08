from time import sleep
import common

import autoAttch


keysBorad = ['s', 'e', 'f', 'g', 'h', 't', 'r', 'd', 'a']

def keyPressBorad(keys):
    for key in keys:
        common.otherKeys(key)
        sleep(1)

def addBuff():
    keyPressBorad(keysBorad)
    sleep(1)

def attch1():
    common.moveFunc('top', 2)
    common.run(2)
    sleep(1.5)

def attch2():
    common.run(3)
    sleep(0.5)

def attch3():
    sleep(3.5)
    common.moveFunc('top', 3)
    common.run(1.7, 'left')
    common.moveFunc('bottom', 0.6)

def attch4():
    sleep(3.5)
    common.run(0.7, 'left')
    sleep(1)

def attch5():
    common.run(1, 'left')
    sleep(2)
    common.moveFunc('top', 1)
    common.run(1.5)
    common.otherKeys('y')
    sleep(2)

def acctch_boss():
    common.otherKeys('a')
    sleep(13)


autoAttch.start([addBuff, attch1, attch2, attch3, attch4, attch5, acctch_boss], 50)