from time import sleep
import pyautogui
import win32gui
import win32ui
import auto
pyautogui.FAILSAFE = False
import win32con
def getWindow(windowName):
    hwnd = win32gui.FindWindow(None, windowName)
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    # hwndDC = win32gui.GetWindowDC(hwnd)
    win32gui.SetForegroundWindow(hwnd)
    # # 根据窗口的DC获取mfcDC
    # mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # # mfcDC创建可兼容的DC
    # saveDC = mfcDC.CreateCompatibleDC()
    # # 创建bigmap准备保存图片
    # saveBitMap = win32ui.CreateBitmap()
    #     # 获取监控器信息
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    width = right - left
    height = bottom - top
    if left != 0 or top != 0:
    #     print('设置游戏窗口到左上角')
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, width, height, win32con.SWP_SHOWWINDOW)
    # saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    # # 高度saveDC，将截图保存到saveBitmap中
    # saveDC.SelectObject(saveBitMap)
    # saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)
    # saveBitMap.SaveBitmapFile(saveDC, './wegame.jpg')
    # # # 截取从左上角（0，0）长宽为（w，h）的图片
    # # if flag==0:
    # #     saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)
    # #     saveBitMap.SaveBitmapFile(saveDC, filename)
    # # else:
    # #     saveDC.BitBlt((720, 795), (75, 60), mfcDC, (0, 0), win32con.SRCCOPY)
    # #     saveBitMap.SaveBitmapFile(saveDC, './pos.png')

