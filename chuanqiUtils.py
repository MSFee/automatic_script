import subprocess
import os
import startgGame
import pydirectinput
import auto
import datetime
from time import sleep

def click(x, y):
    if x != 0:
        pydirectinput.click(int(x), int(y))


def check_network_status():
    try:
        # 判断当前电脑是否联网
        subprocess.check_output(
            ['ping', 'www.baidu.com', '-n', '1', '-w', '5000'])
        return True
    except:
        return False

def connect_wifi(is5G=True):
    # # 扫描可用wifi列表
    # wifi_list = subprocess.check_output(['netsh', 'wlan', 'show', 'network'], shell=True, timeout=15, stderr=subprocess.STDOUT, encoding='gbk').split('\n')
    # # 查找指定名称的wifi
    # mr1002_5G = [line.split(':')[1][1:-1] for line in wifi_list if 'mr1002-5G' in line]
    # if len(mr1002_5G) > 0:
    #     # 连接指定的wifi

    if is5G:
        os.system('netsh wlan connect name="{}"'.format('mr1002-5G'))
    else:
        os.system('netsh wlan connect name="{}"'.format('mr1002'))

# 检查电脑网络链接
def checkISNotNetWork(isNeedLogin=False, is5G=True, count=0):
    if not check_network_status():
        if count > 10:
            sleep(300)
        connect_wifi(is5G)
        sleep(10)
        is5G = not is5G
        checkISNotNetWork(True, is5G, count + 1)
        return
    elif isNeedLogin:
        print('开始登陆')
        outGameAndLoginGame()
        sleep(5)
        startgGame.getWindow("雷霆传说")
        return
    else:
        return

def clickWeChantLogo():
    leftPostion = 1931
    topPosition = 1392
    auto.saveAndCropFunc("./chuanqi/wechatMain",
                         [leftPostion, topPosition, 2533, 1439])
    x, y = auto.getImg1AndImg2(
        "./chuanqi/wechatMain.jpg", "./chuanqi/wechatLogo.jpg", 0.8)
    if x != 0:
        click(leftPostion + x, topPosition + y)
    else:
        pydirectinput.click(2327, 1414)


def outGameAndLoginGame():
    sleep(2)
    click(690, 481)
    sleep(2)
    pydirectinput.click(1346, 21)
    clickWeChantLogo()
    sleep(2)
    hwnd, left, top, width, height = startgGame.getWindowAndSetMoveRightBottom(
        "微信", "WeChatMainWndForPC")
    auto.saveAndCropFunc("./chuanqi/wechatMain",
                         [left, top, left + width, top + height])
    x, y = auto.getImg1AndImg2(
        "./chuanqi/wechatMain.jpg", "./chuanqi/gameBtn.jpg")
    click(left + x, top + y)
    sleep(1)
    auto.saveAndCropFunc("./chuanqi/wechatMain",
                         [left, top, left + width, top + height])
    x_logo, y_logo = auto.getImg1AndImg2(
        "./chuanqi/wechatMain.jpg", "./chuanqi/gameLogo.jpg", 0.8)
    click(left + x_logo, top + y_logo)
    sleep(3)
    pydirectinput.click(1347, 863)
    sleep(2)
    pydirectinput.click(1378, 873)
    sleep(2)
    pydirectinput.click(1271, 932)
    sleep(5)
    # pydirectinput.click(2542, 763)
    startgGame.closeWindow(hwnd)
    sleep(5)

def checkGameisError():
    auto.saveAndCropFunc("./chuanqi/main", [0, 0, 1391, 818])
    x, y = auto.getImg1AndImg2(
            "./chuanqi/main.jpg", "./chuanqi/errorImg/1.jpg", 0.8)
    x1, y1 = auto.getImg1AndImg2(
            "./chuanqi/main.jpg", "./chuanqi/errorImg/2.jpg", 0.8)
    x2, y2 = auto.getImg1AndImg2(
            "./chuanqi/main.jpg", "./chuanqi/errorImg/3.jpg", 0.8)
    if x != 0 :
        click(x, y)
        sleep(1)
        click(x, y)
        sleep(1)
        checkISNotNetWork(True)
    elif x1 != 0 :
        click(x1, y1)
        sleep(1)
        click(x1, y1)
        sleep(1)
        checkISNotNetWork(True)
    elif x2 != 0 :
        click(x2, y2)   
        sleep(1) 
        click(x2, y2)   
        sleep(1) 
        checkISNotNetWork(True)

# 自动截图并发送微信
def autoScreensHot(isFull=False):
    pydirectinput.keyDown('alt')
    pydirectinput.press('a')
    pydirectinput.keyUp('alt')
    sleep(1)
    if not isFull:
        pydirectinput.click(500, 400)
        sleep(1)
        pydirectinput.click(1333, 847)
        sleep(1)
    else:
        pydirectinput.click(900, 1115)
        sleep(1)
        pydirectinput.click(2511, 1412)
        sleep(1)
    pydirectinput.click(40, 1370)
    sleep(1)
    pydirectinput.keyDown('ctrl')
    pydirectinput.press('v')
    pydirectinput.keyUp('ctrl')
    sleep(1)
    pydirectinput.press('enter')
    sleep(1)

def desert_treasure():
    target_time = datetime.datetime.now().replace(hour=13, minute=0, second=0, microsecond=0)
    delta = (target_time - datetime.datetime.now()).total_seconds()
    if delta >= 300 or delta < 0:  # 300秒等于5分钟，如果还没到13:00，则等待
        return False
    sleep(1)
    click(631, 683)
    count = 0
    autoScreensHot()
    while count < 32:
        count += 1
        auto.saveAndCropFunc("./chuanqi/main", [0, 0, 1391, 818])
        sleep(0.5)
        go_to_img_x, go_to_img_y = auto.getImg1AndImg2(
            "./chuanqi/main.jpg", "./chuanqi/go_to.jpg", 0.8)
        if go_to_img_x != 0:
            autoScreensHot()
            click(go_to_img_x, go_to_img_y + 9)
            sleep(1)
            click(177, 244)
            sleep(1)
            click(1258, 362)
            sleep(15 * 60)
            autoScreensHot()
            break
        sleep(10)
    return True