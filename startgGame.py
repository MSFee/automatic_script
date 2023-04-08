from time import sleep
import pyautogui
import win32gui
import win32api
import auto
pyautogui.FAILSAFE = False
import win32con
def getWindow(windowName = '', windowClassName = None):
    hwnd = win32gui.FindWindow(windowClassName, windowName)
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
    height = bottom- top
    if left != 0 or top != 0:
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, width, height, win32con.SWP_SHOWWINDOW)
    return hwnd, width, height    

def closeWindow(hwnd):
    win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

def getWindowAndSetMoveRightBottom(windowName = '', windowClassName = None):
    hwnd = win32gui.FindWindow(windowClassName, windowName)
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    width = right - left
    height = bottom- top
    hwndHeight = win32api.GetSystemMetrics(1) 
    hwndWidth = win32api.GetSystemMetrics(0)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, hwndWidth - width, hwndHeight - height - 48, width, height, win32con.SWP_SHOWWINDOW)
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    return hwnd, left, top, width, height

def getWindowAndSetMoveBottom(windowName):
    hwnd = win32gui.FindWindow(None, windowName)
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    width = right - left
    height = bottom- top
    hwndHeight = win32api.GetSystemMetrics(1) - height
    if left != 0 or bottom != 0:
    #  print('设置游戏窗口到左下角')
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, hwndHeight, width, height, win32con.SWP_SHOWWINDOW)
        return hwndHeight, width, win32api.GetSystemMetrics(1)