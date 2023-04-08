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
    map1, map2, map3, map4, map5, boss = skills
    hasEmergencyMap = False # 是否遇到紧急任务
    needSale = False
    while True:
        sleep(0.5)
        auto.saveAndCropFunc('small_map', [950, 56, 1066, 110])
        question_x, y1 = auto.getImg1AndImg2('small_map.jpg', './pic/question.jpg')
        x, y = auto.getImg1AndImg2('small_map.jpg', './pic/map_role.jpg')
        boss_x, boss_y = auto.getImg1AndImg2('small_map.jpg', './pic/boss.jpg')
        emergency_map_x, emergency_map_y = auto.getImg1AndImg2('small_map.jpg', './pic/emergency_map.jpg')
        if emergency_map_x:
            if hasEmergencyMap:
                hasEmergencyMap = False
            else:
                hasEmergencyMap = True
        if x == 11.5:
            print("第一个图")
            packFully_x , packFully_y = auto.getImg1AndImg2('dnf.jpg', './pic/pack_fully.jpg')
            if packFully_x:
                needSale = True
            else:
                needSale = False
            map1()
            autoFindRoad.findDoor(speed)
        if x == 29.5:
            print("第二个图")
            if question_x == 0:
                map2()
            else:
                common.moveFunc('left', 0.5)
                normal.changePickEpic()
                common.moveFunc('right', 0.5)
            autoFindRoad.findDoor(speed)
        if x == 47.5:
            print("第三个图")
            if question_x == 0:
                map3()
            else:
                common.moveFunc('left', 0.5)
                normal.changePickEpic()
                common.moveFunc('right', 0.5)
            autoFindRoad.findDoor(speed)
        if x == 65.5:
            print("第四个图")
            if question_x == 0:
                map4()
            else:
                common.moveFunc('left', 0.5)
                normal.changePickEpic()
                common.moveFunc('right', 0.5)
            autoFindRoad.findDoor(speed, True, True, False, [600,0,1067,600])
        if x == 83.5:
            print("第五个图")
            if question_x == 0:
                map5()
            else:
                common.moveFunc('left', 0.5)
                normal.changePickEpic()
                common.moveFunc('right', 0.5)
            autoFindRoad.findDoor(speed, True, True, False, [200,0,1067,600])
        elif x == 0 and boss_x:
            print('boss图')
            boss()
            nextGame(needSale)
        else:
            if autoFindRoad.checkFatigueValueisClear() is True:
                common.otherKeys('f12')
                sleep(2)
                autoFindRoad.sealGoogsAndFix()
                break
            common.otherKeys('R_ctrl')
            sleep(0.5)
