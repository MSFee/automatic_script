import keyboard
import pydirectinput
pydirectinput.PAUSE = 0.01
from time import sleep 


def skill4(arrs1, arrs2, arrs3, arrs4):
    arrs = [arrs1, arrs2, arrs3, arrs4]
    for key in arrs:
        pydirectinput.keyDown(key)
        pydirectinput.keyUp(key)

def skill3(arrs1, arrs2, arrs3):
    arrs = [arrs1, arrs2, arrs3]
    for key in arrs:
        pydirectinput.keyDown(key)
        pydirectinput.keyUp(key)

def skill2(arrs1, arrs2):
    arrs = [arrs1, arrs2]
    for key in arrs:
        pydirectinput.keyDown(key)
        pydirectinput.keyUp(key)

keyboard.add_hotkey('q', skill4, args=(['down', 'down','down','c']))
keyboard.add_hotkey('a', skill4, args=(['up', 'up','up', 'x']))
keyboard.add_hotkey('w', skill4, args=(['up', 'up', 'up', 'c']))
keyboard.add_hotkey('s', skill4, args=(['down', 'down','down', 'x']))
keyboard.add_hotkey('e', skill4, args=(['up','up','down', 'c']))
keyboard.add_hotkey('d', skill4, args=(['down','down','up', 'c']))


# keyboard.add_hotkey('y', skill3, args=(['down', 'down', 'z']))
# keyboard.add_hotkey('h', skill3, args=(['down', 'down', 'x']))

keyboard.wait('p')
