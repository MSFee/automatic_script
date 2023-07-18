from turtle import position
import pyautogui
import pydirectinput
import time
import random
from startgGame import getWindow
pyautogui.FAILSAFE = False 

time.sleep(1)
pyautogui.moveTo(216, 243, 0.5)
pyautogui.click()
# pyautogui.click()
# getWindow('地下城与勇士')

def moveFunc(direction, times = 0): 
    if direction == 'right':
        pydirectinput.keyDown('right')
        time.sleep(times)
        pydirectinput.keyUp('right')
    elif direction == 'left': # 左键
        pydirectinput.keyDown('left')
        time.sleep(times)
        pydirectinput.keyUp('left')
    elif direction == 'top': # 上键
        pydirectinput.keyDown('up')
        time.sleep(times)
        pydirectinput.keyUp('up')
    else: # 下键
        pydirectinput.keyDown('down')
        time.sleep(times)
        pydirectinput.keyUp('down')

# 移动方向和移动时间
def moveFunc2(direction, times = 0): 
    if direction == 'right':
        pyautogui.moveTo(756, 1020) # 右键
        pyautogui.mouseDown()
        if times != 0:
            time.sleep(times)
        pyautogui.mouseUp()
    elif direction == 'left': # 左键
        pyautogui.moveTo(650,1020)
        pyautogui.mouseDown()
        if times != 0:
            time.sleep(times)
        pyautogui.mouseUp()
    elif direction == 'top': # 上键
        pyautogui.moveTo(700,950)
        pyautogui.mouseDown()
        if times != 0:
            time.sleep(times)
        pyautogui.mouseUp()
    else: # 下键
        pyautogui.moveTo(700,1020)
        pyautogui.mouseDown()
        if times != 0:
            time.sleep(times)
        pyautogui.mouseUp()

def otherKeys(key):
    if key == 'v':
        pydirectinput.press('v')
    elif key == 'z':
        pydirectinput.press('z')
    elif key == 'x':
        pydirectinput.press('x')
    elif key == 'd':
        pydirectinput.press('d')
    elif key == 'c':
        pydirectinput.press('c')
    elif key == 'f':
        pydirectinput.press('f')
    elif key == 'r':
        pydirectinput.press('r')
    elif key == 'q':
        pydirectinput.press('q')
    elif key == 'w':
        pydirectinput.press('w')
    elif key == 'e':
        pydirectinput.press('e')
    elif key == 't':
        pydirectinput.press('t')
    elif key == 'y':
        pydirectinput.press('y')
    elif key == 'a':
        pydirectinput.press('a') 
    elif key == 's':
        pydirectinput.press('s')
    elif key == 'g':
        pydirectinput.press('g')
    elif key == 'h':
        pydirectinput.press('h')
    elif key == 'ctrl':
        pydirectinput.press('ctrlleft')
    elif key == 'R_ctrl':
        pydirectinput.press('ctrlright')
    elif key == '`':
        pydirectinput.press('`')
    elif key == '.':
        pydirectinput.press('.')
    elif key == 'esc':
        pydirectinput.press('esc')
    elif key == 'space':
        pydirectinput.press('space')
    elif key == 'alt':
        pydirectinput.press('alt')
    elif key == '5':
        pydirectinput.press('5')
    elif key == 'tab':
        pydirectinput.press('tab')
    elif key == 'capslock':
        pydirectinput.press('capslock')
    elif key == 'f12':
        pydirectinput.press('f12')
    elif key == 'left':
        pydirectinput.press('left')
    elif key == 'right':
        pydirectinput.press('right')
    else:
        pydirectinput.press(key)



# 其他按键和长按时间
def otherKeys2(key):
    if key == 'x':
        pyautogui.moveTo(222, 958) # X键
        pydirectinput.press('x')
    if key == 'd':
        pyautogui.moveTo(267, 909) # D键
        pydirectinput.press('d')
    elif key == 'c':
        pyautogui.moveTo(280, 962) # C键
        pydirectinput.press('c')
    elif key == 'f':
        pyautogui.moveTo(317, 909) # f键
        pydirectinput.press('f')
    elif key == 'r':
        pyautogui.moveTo(293, 847) # R键
        pydirectinput.press('r')
    elif key == 'q':
        pyautogui.moveTo(127, 854) # Q键
        pydirectinput.press('q')
    elif key == 'w':
        pyautogui.moveTo(171, 854) # 
        pydirectinput.press('w')
    elif key == 'e':
        pyautogui.moveTo(239, 854) 
        pydirectinput.press('e')
    elif key == 't':
        pyautogui.moveTo(322, 854) 
        pydirectinput.press('t')
    elif key == 'y':
        pyautogui.moveTo(377, 854) 
        pydirectinput.press('y')
    elif key == 'a':
        pyautogui.moveTo(157, 900)
        pydirectinput.press('a') 
    elif key == 's':
        pyautogui.moveTo(209, 900) 
        pydirectinput.press('s')
    elif key == 'g':
        pyautogui.moveTo(370, 900) 
        pydirectinput.press('g')
    elif key == 'h':
        pyautogui.moveTo(407, 900) 
        pydirectinput.press('h')
    elif key == 'ctrl':
        pyautogui.moveTo(95, 1024) # ctrl键
        pydirectinput.press('ctrlleft')
    elif key == 'R_ctrl':
        pyautogui.moveTo(600, 1024)
        pydirectinput.press('ctrlright')
    elif key == '`':
        pyautogui.moveTo(92, 768) # `键
        pydirectinput.press('`')
    elif key == '.':
        pyautogui.moveTo(606, 950) # . 键
        pydirectinput.press('.')
    elif key == 'esc':
        pyautogui.moveTo(29, 787) # ESC键
        pydirectinput.press('esc')
    elif key == 'space':
        pyautogui.moveTo(400, 1020) # 空格键
        pydirectinput.press('space')
    elif key == 'alt':
        pyautogui.moveTo(203, 1020) 
        pydirectinput.press('alt')
    pyautogui.mouseDown()
    pyautogui.mouseUp()

# 生成随机结果
def getRandomResult():
    result = random.randint(1,10)
    dir = ''
    if result >= 6:
        dir = 'left'
    else:
        dir = 'right'
    return dir, result / 10

# 添加buff，部分角色添加不上，建议使用快捷键
def addBuff(way = 'right'):
    if way == 'right':
        pydirectinput.keyDown('right')
        pydirectinput.keyUp('right')
        pydirectinput.keyDown('right')
        pydirectinput.press('space')
        pydirectinput.keyUp('right')
    else:
        pydirectinput.keyDown('up')
        pydirectinput.keyUp('up')
        pydirectinput.keyDown('down')
        pydirectinput.press('space')
        pydirectinput.keyUp('down')
# 奔跑
def run(times = 0, way = 'right'):
    pydirectinput.press(way)
    pydirectinput.keyDown(way)
    time.sleep(times)
    pydirectinput.keyUp(way)
# 奔跑
def run2(times = 0, way = 'right'):
    moveFunc(way)
    moveFunc(way, times)

# 随机移动角色位置
def ranDomMoveRole():
    resultLeftorRight = random.randint(1,10)
    resultTopOrBottom = random.randint(1,10)
    if resultLeftorRight <= 5:
        positionX = 'left'
    else:
        positionX = 'right'
    if resultTopOrBottom <= 5:
        positionY = 'top'
    else:
        positionY = 'bottom'
    moveFunc(positionX, resultLeftorRight / 5)
    moveFunc(positionY, resultTopOrBottom / 5)
