from time import sleep
import common

while True:
    common.otherKeys('ctrl')
    sleep(1)
    common.otherKeys('alt')
    sleep(1)

    common.run(2.2)
    common.otherKeys('f')
    sleep(1)


    common.run(4)
    common.otherKeys('w')
    sleep(1)
    common.moveFunc('bottom', 0.3)
    common.run(3.5)
    common.otherKeys('r')
    sleep(2)

    common.moveFunc('top', 2)

    common.otherKeys('g')
    sleep(1)

    common.run(3)
    common.otherKeys('e')
    sleep(2)

    common.run(3)
    common.moveFunc('left', 0.3)

    common.moveFunc('top', 1.4)
    common.moveFunc('right', 1)
    common.otherKeys('y')
    sleep(3)
    common.run(0.6)

    common.moveFunc('top', 0.7)
    common.moveFunc('right', 2.5)
    common.moveFunc('top', 0.7)
    common.otherKeys('t')

    sleep(3)
    common.otherKeys('`')
    common.otherKeys('x')
    common.otherKeys('x')
    common.otherKeys('x')
    sleep(5)
    common.otherKeys('esc')
    sleep(1)
    common.otherKeys('esc')
    sleep(1)
    common.otherKeys('R_ctrl')
    sleep(4)