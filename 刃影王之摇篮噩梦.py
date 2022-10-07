from calendar import weekheader
from time import sleep
import common
import autoFindRoad
import normal
import auto


def start():
    while True:
        if autoFindRoad.checkFatigueValueisClear() is True:
            common.otherKeys('f12')
            break
        # 第一个图
        common.otherKeys('y')
        autoFindRoad.findDoorPlus(83)
        # 第二个图
        common.moveFunc('top', 1.1)
        common.otherKeys('f')
        sleep(2.5)
        common.moveFunc('right', 1)
        sleep(2)
        while (auto.judgeMap('1') or auto.judgeMap('6')) is False:
            common.run(0.2)
            common.otherKeys('s')
            sleep(5)
            common.otherKeys('w')
        autoFindRoad.findDoorPlus(83, True)
        if auto.checkHasEpic() is True:
            common.moveFunc('right', 1)
            normal.changePickEpic()
            common.moveFunc('left', 1)

        # 第三个图
        sleep(1)
        while auto.judgeMap('2', True) is False and (auto.judgeMap('1') or auto.judgeMap('6')) is True:
            common.run(0.2)
            autoFindRoad.findDoorPlus(83, True)
            sleep(2)
        common.moveFunc('left', 0.1)
        common.moveFunc('top', 0.05)
        common.otherKeys('e')
        sleep(1)
        common.moveFunc('bottom', 0.25)
        common.otherKeys('ctrl')
        sleep(1)
        common.moveFunc('right', 0.5)
        while (auto.judgeMap('2') or auto.judgeMap('7')) is False:
            common.run(0.1)
            common.otherKeys('e')
            sleep(5)
            common.otherKeys('w')
        autoFindRoad.findDoorPlus(83, True)
        if auto.checkHasEpic() is True:
            common.moveFunc('bottom', 0.5)
            normal.changePickEpic()
            common.moveFunc('top', 0.5)

        # 第四个图
        sleep(1)
        while auto.judgeMap('3', True) is False and (auto.judgeMap('2') or auto.judgeMap('7')) is True:
            common.run(0.2)
            autoFindRoad.findDoorPlus(83, True)
            sleep(2)
        common.moveFunc('top', 0.8)
        common.run(0.4)
        common.otherKeys('d')
        common.moveFunc('top', 0.8)
        sleep(2)
        common.moveFunc('bottom', 0.2)
        while (auto.judgeMap('3') or auto.judgeMap('8')) is False:
            common.moveFunc('top', 0.6)
            common.otherKeys('s')
            sleep(1)
            common.otherKeys('e')
            sleep(5)
            common.moveFunc('left', 0.1)
            common.moveFunc('top', 0.1)
            common.otherKeys('s')
            sleep(1)
            common.otherKeys('w')
        common.run(0.5)
        autoFindRoad.findDoorPlus(83)
        if auto.checkHasEpic() is True:
            common.moveFunc('left', 0.5)
            normal.changePickEpic()
            common.moveFunc('right', 0.5)

        # 第五个图
        while auto.judgeMap('4', True) is False and (auto.judgeMap('3') or auto.judgeMap('8')) is True:
            common.run(0.5, 'left')
            common.moveFunc('top', 0.1)
            autoFindRoad.findDoorPlus(83)
            sleep(2)
        normal.moveRoleToYCenter(84)
        common.run(0.6)
        common.otherKeys('g')
        sleep(2)
        common.otherKeys('r')
        sleep(2)
        common.moveFunc('bottom', 0.1)
        while (auto.judgeMap('4') or auto.judgeMap('9')) is False:
            common.moveFunc('right', 0.1)
            common.moveFunc('bottom', 0.1)
            common.otherKeys('s')
            sleep(1)
            common.otherKeys('e')
            sleep(5)
            common.moveFunc('left', 0.1)
            common.moveFunc('top', 0.1)
            common.otherKeys('s')
            sleep(1)
            common.otherKeys('w')
        autoFindRoad.findDoorPlus(83, False, True)
        if auto.checkHasEpic() is True:
            common.moveFunc('bottom', 0.5)
            normal.changePickEpic()
            common.moveFunc('top', 0.5)

        # 第六个图
        sleep(1)
        while auto.judgeMap('5', True) is False and (auto.judgeMap('4') or auto.judgeMap('9')) is True:
            common.moveFunc('bottom', 0.5)
            autoFindRoad.findDoorPlus(83)
            sleep(2)
        common.moveFunc('top', 0.5)
        common.moveFunc('right', 0.01)
        common.otherKeys('alt')
        sleep(4)
        common.run(0.6)
        while (auto.judgeMap('5') or auto.judgeMap('10')) is False:
            common.moveFunc('left', 0.1)
            common.moveFunc('top', 0.1)
            common.otherKeys('e')
            sleep(5)
            common.otherKeys('w')
        autoFindRoad.findDoorPlus(83, False, True)
        if auto.checkHasEpic() is True:
            common.moveFunc('bottom', 0.5)
            normal.changePickEpic()
            common.moveFunc('top', 0.5)
        # 第七个图
        sleep(1)
        while auto.judgeMap('6', True) is False and (auto.judgeMap('5') or auto.judgeMap('10')) is True:
            common.moveFunc('bottom', 0.5)
            common.moveFunc('left', 0.2)
            autoFindRoad.findDoorPlus(83)
            sleep(2)
        common.moveFunc('top', 0.7)
        common.otherKeys('h')
        sleep(7)
        common.otherKeys('t')
        sleep(6)
        common.otherKeys('`')
        sleep(5)
        common.otherKeys('esc')
        sleep(6)
        common.otherKeys('esc')
        sleep(3)
        common.otherKeys('R_ctrl')
        sleep(6)
start()
sleep(2)
autoFindRoad.sealGoogsAndFix()