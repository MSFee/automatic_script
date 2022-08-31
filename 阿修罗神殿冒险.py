from time import sleep
import common

while True:
    common.otherKeys('t')
    sleep(2)
    common.otherKeys('y')
    sleep(1)
    common.otherKeys('g')
    sleep(1)

    common.run(2)
    common.moveFunc('bottom', 0.5)
    common.otherKeys('s')

    common.run(3)

    common.otherKeys('q')

    common.run(4)

    # common.moveFunc('top', 0.6)
    common.otherKeys('w')
    sleep(0.5)
    common.run(4)

    common.otherKeys('s')

    common.run(5)

    common.otherKeys('alt')
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