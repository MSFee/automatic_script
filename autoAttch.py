import auto
from autoFindRoad import findDoor, findDoorPlus
from time import sleep
import normal
import common


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

def start(skillArr, ROLESPEED = 65, needRunTask = True):
    hasEmergencyMap = False # 是否遇到紧急任务
    addBuff, attch1, attch2, attch3, attch4, acctch5, acctch_boss = skillArr
    while True:
        sleep(0.5)
        auto.saveAndCropFunc('small_map', [737, 47, 794, 139])
        auto.saveAndCropFunc()
        x1, y1 = auto.getImg1AndImg2('small_map.jpg', './pic/question.jpg')
        x, y = auto.getImg1AndImg2('small_map.jpg', './pic/map_role.jpg')
        boss_x, boss_y = auto.getImg1AndImg2('small_map.jpg', './pic/boss.jpg')
        emergency_map_x, emergency_map_y = auto.getImg1AndImg2('small_map.jpg', './pic/emergency_map.jpg')
        if emergency_map_x:
            if hasEmergencyMap:
                hasEmergencyMap = False
            else:
                hasEmergencyMap = True
        packFully_x, packFully_y = auto.getImg1AndImg2('dnf.jpg', './pic/pack_fully.jpg')
        flag = x1 != 0  # true表示图已经打完
        if x == 29.5 and y == 76:
            # 第一个图
            print('第一个图')
            addBuff()
            findDoor(ROLESPEED)
        elif x == 11.5 and y == 58:
            print("倒数第二排，左边图")
        elif x == 29.5 and y == 58:
            # 第二个图 （中间）
            print("倒数第二排，中间图")
            attch1()
            findDoor(ROLESPEED)
            if auto.checkHasEpic() is True:
                common.moveFunc('left', 0.5)
                normal.changePickEpic()
                common.moveFunc('right', 0.5)
        elif x == 47.5 and y == 58:
            # 第二个图 （右边）
            print("倒数第二排，右边图")
            attch2()
            findDoor(ROLESPEED)
            if auto.checkHasEpic() is True:
                common.moveFunc('bottom', 0.5)
                normal.changePickEpic()
                common.moveFunc('top', 0.5)
        elif x == 11.5 and y == 40:
            print("倒数第三排，左边图")
        elif x == 47.5 and y == 40:
            # 第三个图 （右边）
            print("倒数第三排，右边图")
            attch3()
            findDoorPlus(ROLESPEED, True)
            if auto.checkHasEpic() is True:
                common.moveFunc('right', 0.5)
                normal.changePickEpic()
                common.moveFunc('left', 0.5)
        elif x == 29.5 and y == 40:
            # 第三个图 （中间）
            print("倒数第三排，中间图")
            attch4()
            findDoorPlus(ROLESPEED, False, True)
            common.moveFunc('top', 0.3)
            if auto.checkHasEpic() is True:
                common.moveFunc('bottom', 0.5)
                normal.changePickEpic()
                common.moveFunc('top', 0.5)
        elif (emergency_map_x and hasEmergencyMap) or (x == 29.5 and y == 22):
            print("倒数第四排，中间图")
            acctch5()
            if emergency_map_x != 0 and needRunTask:
                common.run(0.8, 'left')
                common.moveFunc('bottom', 1)
                common.run(3)
                common.moveFunc('left', 0.6)
            else:
                common.run(0.5)
                sleep(0.5)
            findDoor(ROLESPEED)
            if auto.checkHasEpic() is True:
                common.moveFunc('bottom', 0.5)
                normal.changePickEpic()
                common.moveFunc('top', 0.5)
            if emergency_map_x:
                sleep(3)
        else:
            if boss_x:
                acctch_boss()
                sleep(2)
                nextGame(packFully_x != 0)
            else:
                print('未知图')
