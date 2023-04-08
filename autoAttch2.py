import auto
import autoFindRoad
import normal
import common
from time import sleep



def nextGame(needSale = False):
    common.otherKeys('`')
    common.otherKeys('x')
    common.otherKeys('x')
    common.otherKeys('x')
    common.otherKeys('x')
    if needSale:
        sleep(8)
        common.otherKeys('a')
        sleep(0.5)
        common.otherKeys('space')
        sleep(0.5)
        common.otherKeys('left')
        sleep(0.5)
        common.otherKeys('space')
        sleep(1)
    else:
        sleep(3.5)
        common.otherKeys('3')
        sleep(6)
    common.otherKeys('esc')
    sleep(2)
    common.otherKeys('R_ctrl')
    sleep(5)




def start(skills, speed):
    map1, map2, map3, map4, map5, map6, map7, map8, boss = skills
    hasEmergencyMap = False # 是否遇到紧急任务
    needSale = False
    while True:
        sleep(0.5)
        auto.saveAndCropFunc('small_map', [969, 45, 1061, 121])
        x, y = auto.getImg1AndImg2('small_map.jpg', './pic/map_role.jpg')
        boss_x, boss_y = auto.getImg1AndImg2('small_map.jpg', './pic/boss.jpg')
        emergency_map_x, emergency_map_y = auto.getImg1AndImg2('small_map.jpg', './pic/emergency_map.jpg')
        if emergency_map_x:
            if hasEmergencyMap:
                hasEmergencyMap = False
            else:
                hasEmergencyMap = True
        # y == 23
        if x == 10.5 and y == 60:
            print('第一个图')
            packFully_x , packFully_y = auto.getImg1AndImg2('dnf.jpg', './pic/pack_fully.jpg')
            if packFully_x:
                needSale = True
            else:
                needSale = False
            map1()
            sleep(0.5)
        elif x == 28.5 and y == 60:
            print('第二个图')
            map2()
            sleep(0.5)
        elif x == 46.5 and y == 60:
            print('第三个图')
            map3()
            autoFindRoad.findDoor(speed)
            sleep(0.5)
        elif (x == 64.5 and y == 60) or hasEmergencyMap:
            print('第四个图')
            map4()
            autoFindRoad.findDoor(speed)
            if hasEmergencyMap:
                sleep(2.5)
        elif x == 82.5 and y == 60:
            print('第五个图')
            sleep(0.5)
            map5()
            autoFindRoad.findDoor(speed)
            sleep(0.5)
        elif x == 64.5 and y == 42:
            print('第六个图')
            sleep(0.5)
            map6()
        elif x == 82.5 and y == 42:
            print('第七个图')
            map7()
            autoFindRoad.findDoor(speed)
            sleep(0.5)
        elif x == 82.5 and y == 24:
            print('第八个图')
            map8()
            sleep(0.5)
        elif x == 0 and boss_x:
            print('boss图')
            boss()
            nextGame(needSale)
        else:
            print(autoFindRoad.checkFatigueValueisClear())
            if autoFindRoad.checkFatigueValueisClear() is True:
                common.otherKeys('f12')
                sleep(2)
                autoFindRoad.sealGoogsAndFix()
                break
            common.otherKeys('R_ctrl')
            sleep(0.5)
