from time import sleep
import common
import autoFindRoad

def start():

    common.otherKeys('y')
    sleep(1)
    autoFindRoad.findDoorPlus(100)
    sleep(0.5)
    common.run(0.7)
    common.otherKeys('f')
    common.run(0.3)

    autoFindRoad.findDoorPlus(100)
    sleep(0.5)
    autoFindRoad.moveRoleToYCenter()
    common.run(0.7)
    common.otherKeys('r')
    common.run(0.3)

    autoFindRoad.findDoorPlus(100)
    sleep(0.5)
    autoFindRoad.moveRoleToYCenter()
    common.run(0.5)
    common.otherKeys('g')
    common.run(0.3)

    autoFindRoad.findDoorPlus(100)
    sleep(0.5)
    autoFindRoad.moveRoleToYCenter()
    common.otherKeys('w')
    sleep(0.5)
    common.otherKeys('e')
    common.otherKeys('e')
    common.run(0.1)


    autoFindRoad.findDoorPlus(100)
    common.run(0.5)
    autoFindRoad.moveRoleToYCenter()
    common.otherKeys('t')
    sleep(0.5)
    common.otherKeys('d')
    sleep(3)