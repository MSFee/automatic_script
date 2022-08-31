from time import sleep
import common
import autoFindRoad
import auto
import normal


def start():
    while True:
        if autoFindRoad.checkFatigueValueisClear() is True:
            common.otherKeys('f12')
            break
        common.otherKeys('y')
        autoFindRoad.findDoorPlus(85)
        common.moveFunc('top', 1.3)
        common.otherKeys('w')
        common.otherKeys('w')
        sleep(1)
        common.moveFunc('bottom', 0.2)
        common.run(2, 'left')

        # common.otherKeys('5')
        # sleep(1)
        # common.otherKeys('capslock')
        # sleep(10)
        # common.otherKeys('5')

        while (auto.judgeMap('1') or auto.judgeMap('6')) is False:
            common.moveFunc('right', 0.1)
            common.otherKeys('r')
            sleep(15)
        autoFindRoad.findDoorPlus(65, True)
        if auto.checkHasEpic() is True:
            common.moveFunc('right', 1)
            normal.changePickEpic()
            common.moveFunc('left', 1)

        # 第三个图
        common.run(0.5, 'left')
        common.otherKeys('r')
        sleep(1)
        common.run(0.5, 'left')
        while (auto.judgeMap('2') or auto.judgeMap('7')) is False:
            common.run(0.3)
            common.moveFunc('left', 0.02)
            common.otherKeys('w')
            common.otherKeys('w')
            common.run(0.3)
            sleep(16)
        autoFindRoad.findDoorPlus(65, True)
        if auto.checkHasEpic() is True:
            common.moveFunc('bottom', 0.5)
            normal.changePickEpic()
            common.moveFunc('top', 0.5)

        # 第四个图
        common.moveFunc('top', 1.2)
        common.run(0.4)
        common.otherKeys('f')
        common.moveFunc('top', 0.5)
        sleep(3)
        common.moveFunc('bottom', 0.5)
        common.run(0.5)
        while (auto.judgeMap('3') or auto.judgeMap('8')) is False:
            common.moveFunc('right', 0.1)
            common.otherKeys('r')
            sleep(15)
        autoFindRoad.findDoorPlus(85)
        if auto.checkHasEpic() is True:
            common.moveFunc('left', 0.5)
            normal.changePickEpic()
            common.moveFunc('right', 0.5)

        # 第五个图"""  """
        sleep(0.5)
        common.moveFunc('right', 0.3)
        normal.moveRoleToYCenter(80, [0,0,400,600])
        common.otherKeys('g')
        sleep(0.7)
        common.moveFunc('left', 0.05)
        common.otherKeys('d')
        sleep(1)
        common.otherKeys('e')
        common.otherKeys('e')
        sleep(1)
        common.moveFunc('bottom', 0.4)
        while (auto.judgeMap('4') or auto.judgeMap('9')) is False:
            common.moveFunc('left', 0.1)
            common.otherKeys('t')
            sleep(10)
            common.otherKeys('r')
            sleep(10)
        autoFindRoad.findDoorPlus(65, False, True)
        if auto.checkHasEpic() is True:
            common.moveFunc('bottom', 0.5)
            normal.changePickEpic()
            common.moveFunc('top', 0.5)

        # 第五个图
        common.moveFunc('top', 1.2)
        common.run(0.2, 'left')
        common.moveFunc('right', 0.1)
        common.otherKeys('w')
        common.otherKeys('w')
        sleep(2)
        common.run(0.6, 'left')
        sleep(1)
        while (auto.judgeMap('5') or auto.judgeMap('10')) is False:
            common.run(0.5, 'left')
            common.otherKeys('f')
            sleep(3)
            common.otherKeys('r')
            sleep(3)
        sleep(1)
        common.otherKeys('ctrl')
        taskx, taskYy = auto.checkHasTask()
        if taskx != 0:
            common.run(1, 'left')
            common.moveFunc('bottom', 1)
            common.run(4)
            common.moveFunc('left', 0.8)
            autoFindRoad.findDoorPlus(90)
            common.moveFunc('top', 0.5)
            sleep(3)
        else:
            autoFindRoad.findDoor(85)
            if auto.checkHasEpic() is True:
                common.moveFunc('bottom', 0.5)
                normal.changePickEpic()
                common.moveFunc('top', 0.5)

        # 第六个图
        sleep(1)
        common.moveFunc('top', 0.7)
        common.otherKeys('v')
        common.moveFunc('left', 0.5)
        common.otherKeys('alt')
        sleep(2)
        common.otherKeys('ctrl')
        sleep(5)
        common.otherKeys('r')
        sleep(6)
        common.otherKeys('`')
        common.otherKeys('x')
        common.otherKeys('x')
        common.otherKeys('x')
        sleep(3)
        common.otherKeys('x')
        common.otherKeys('x')
        common.otherKeys('esc')
        sleep(4)
        common.otherKeys('esc')
        sleep(3)
        common.otherKeys('R_ctrl')
        sleep(6)
start()
sleep(2)
autoFindRoad.sealGoogsAndFix()