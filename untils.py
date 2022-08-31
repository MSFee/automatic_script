from sys import flags
from time import sleep
import autoFindRoad
import auto

def getCurrSmallMap(callback1, callback2, callback3, callback4, callback5, callback6, callback7, callback8, callback9):
    auto.saveAndCropFunc('small_map', [737, 47, 794, 139])
    x, y = auto.getImg1AndImg2('small_map1.jpg', './pic/map_role.jpg')
    if x == 0:
       sleep(0.5)
       getCurrSmallMap(callback1, callback2, callback3, callback4, callback5, callback6, callback7, callback8, callback9)
       return
    x1, y1 = auto.getImg1AndImg2('small_map.jpg', './pic/question.jpg')
    flag = x1 != 0 # true表示图已经打完
    if x == 29.5 and y == 76:
        # 第一个图
        callback1()
        autoFindRoad.findDoorPlus()
    elif x == 11.5 and y == 58:
        # 第二个图 （左边）
        if flag is True:
            autoFindRoad.findDoorPlus()
        else:
            callback2()
    elif x == 29.5 and y == 58:
        # 第二个图 （中间）
        if flag is True:
            autoFindRoad.findDoorPlus()
        else:
            callback3()
    elif x == 47.5 and y == 58:
        # 第二个图 （右边）
        if flag is True:
            autoFindRoad.findDoorPlus()
        else:
            callback4()
    elif x == 11.5 and y == 40:
        # 第三个图 （左边）
        if flag is True:
            autoFindRoad.findDoorPlus()
        else:
            callback5()
    elif x == 29.5 and y == 40:
        # 第三个图 （中间）
        if flag is True:
            autoFindRoad.findDoorPlus()
        else:
            callback6()
    elif x == 47.5 and y == 40:
        # 第三个图 （右边）
        if flag is True:
            autoFindRoad.findDoorPlus()
        else:
            callback7()
    elif x == 29.5 and y == 22:
        # 第四个图 （中间）
        if flag is True:
            autoFindRoad.findDoorPlus()
        else:
            callback8()
    else: 
        # boss图 # 29.5  4
        callback9()
    getCurrSmallMap(callback1, callback2, callback3, callback4, callback5, callback6, callback7, callback8, callback9)
#auto.getRoleCurrPosition()