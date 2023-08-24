from time import sleep
import common
import autoFindRoad
import untils

def start():
    common.otherKeys('t')
    sleep(0.5)
    common.otherKeys('y')
    sleep(0.5)
    autoFindRoad.findDoorPlus(100)
    sleep(0.5)
    autoFindRoad.moveRoleToYCenter()
    common.run(0.5)
    common.otherKeys('h')
    sleep(0.5)
    common.run(0.2)

    autoFindRoad.findDoorPlus(100)
    sleep(0.8)
    autoFindRoad.moveRoleToYCenter()
    common.run(0.5)
    common.otherKeys('e')
    sleep(0.5)
    common.run(0.2)

    autoFindRoad.findDoorPlus(100)
    sleep(0.5)
    autoFindRoad.moveRoleToYCenter()
    common.run(0.35)
    common.otherKeys('w')
    sleep(1)
    common.run(0.3)

    autoFindRoad.findDoorPlus(100)
    sleep(0.5)
    autoFindRoad.moveRoleToYCenter()
    common.run(0.3)
    common.otherKeys('g')
    sleep(1)
    common.run(0.4)

    autoFindRoad.findDoorPlus(100)
    common.run(0.3)
    autoFindRoad.moveRoleToYCenter()
    common.otherKeys('f')
    sleep(0.5)
    common.otherKeys('w')
    sleep(3)