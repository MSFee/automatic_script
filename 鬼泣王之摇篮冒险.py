from time import sleep
import common
import auto
import autoFindRoad
import normal


def start():
    while True:
        if autoFindRoad.checkFatigueValueisClear() is True:
            common.otherKeys('f12')
            break
        common.otherKeys('top')
        common.otherKeys('space')
        sleep(0.7)
        common.otherKeys('y')
        sleep(2)
        common.otherKeys('ctrl')
        sleep(1)
        
        autoFindRoad.findDoor(90)
        common.moveFunc('top', 1.25)
        common.run(0.55)
        common.otherKeys('w')
        common.otherKeys('w')
        sleep(3.5)

        common.run(0.48)
        sleep(0.5)
        while (auto.judgeMap('1') or auto.judgeMap('6')) is False:
            common.moveFunc('left', 0.1)
            common.otherKeys('q')
            sleep(4)

        autoFindRoad.findDoor(90)
        if auto.checkHasEpic() is True:
            common.moveFunc('left', 0.5)
            normal.changePickEpic()
            common.moveFunc('right', 0.5)
        common.run(0.48)
        normal.moveRoleToYCenter(65)
        common.otherKeys('alt')
        common.run(0.4)
        sleep(2)
        common.run(0.8)
        sleep(0.5)
        while (auto.judgeMap('2-r') or auto.judgeMap('2-r2')) is False:
            common.moveFunc('right', 0.1)
            common.otherKeys('q')
            sleep(4)
        autoFindRoad.findDoor(90)
        if auto.checkHasEpic() is True:
            common.moveFunc('bottom', 0.5)
            normal.changePickEpic()
            common.moveFunc('top', 0.5)

        common.moveFunc('top', 1)
        common.run(0.48, 'left')
        common.otherKeys('w')
        common.moveFunc('bottom', 0.2)
        common.moveFunc('right', 0.01)
        common.otherKeys('a')
        sleep(4)
        common.moveFunc('top', 0.2)
        sleep(0.5)
        while (auto.judgeMap('3-l') or auto.judgeMap('3-l2')) is False:
            common.moveFunc('left', 0.1)
            common.otherKeys('q')
            sleep(4)
        autoFindRoad.findDoorPlus(90, True)
        if auto.checkHasEpic() is True:
            common.moveFunc('right', 0.5)
            normal.changePickEpic()
            common.moveFunc('left', 0.5)
        sleep(0.5)
        common.run(0.3, 'left')
        normal.moveRoleToYCenter(90, [400,0, 800, 600])
        common.otherKeys('s')
        sleep(2)
        autoFindRoad.findDoorPlus(90, False, True)
        if auto.checkHasEpic() is True:
            common.moveFunc('bottom', 0.5)
            normal.changePickEpic()
            common.moveFunc('top', 0.5)
        common.moveFunc('top', 1.25)
        common.moveFunc('right', 0.01)
        common.otherKeys('h')
        sleep(3)

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
            common.run(0.5)
            sleep(0.5)
            while (auto.judgeMap('5-l') or auto.judgeMap('5-l2')) is False:
                common.moveFunc('right', 0.1)
                common.otherKeys('q')
                sleep(4)
            autoFindRoad.findDoor(90)
            if auto.checkHasEpic() is True:
                common.moveFunc('bottom', 0.5)
                normal.changePickEpic()
                common.moveFunc('top', 0.5)
        common.moveFunc('top', 0.8)
        common.moveFunc('left', 0.01)
        sleep(0.2)
        common.otherKeys('g')
        sleep(1)
        common.otherKeys('w')
        sleep(3)
        common.otherKeys('`')
        common.otherKeys('x')
        common.otherKeys('x')
        common.otherKeys('x')
        common.otherKeys('x')
        sleep(3.5)
        common.otherKeys('esc')
        sleep(6)
        common.otherKeys('esc')
        sleep(2)
        common.otherKeys('R_ctrl')
        sleep(5)
start()
sleep(2)
autoFindRoad.sealGoogsAndFix()