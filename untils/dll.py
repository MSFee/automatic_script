import time
import pywinio
import atexit

KBC_KEY_CMD = 0x64
__winio = None
KBC_KEY_DATA = 0x60

def __get_winio():
    global __winio

    if __winio is None:
            __winio = pywinio.WinIO()
            def __clear_winio():
                    global __winio
                    __winio = None
            atexit.register(__clear_winio)

    return __winio

def wait_for_buffer_empty():
    '''
    Wait keyboard buffer empty
    '''

    winio = __get_winio()

    dwRegVal = 0x02
    while (dwRegVal & 0x02):
            dwRegVal = winio.get_port_byte(KBC_KEY_CMD)

def key_down(scancode):
    winio = __get_winio()

    wait_for_buffer_empty();
    winio.set_port_byte(KBC_KEY_CMD, 0xd2);
    wait_for_buffer_empty();
    winio.set_port_byte(KBC_KEY_DATA, scancode)

def key_up(scancode):
    winio = __get_winio()

    wait_for_buffer_empty();
    winio.set_port_byte( KBC_KEY_CMD, 0xd2);
    wait_for_buffer_empty();
    winio.set_port_byte( KBC_KEY_DATA, scancode | 0x80);

def key_press(scancode, press_time = 0.2):
    key_down( scancode )
    time.sleep( press_time )
    key_up( scancode )

def mouse_down():
    winio = __get_winio()
 
    wait_for_buffer_empty();
    winio.set_port_byte(KBC_KEY_CMD, 0xd3);
    wait_for_buffer_empty();
    winio.set_port_dword(KBC_KEY_DATA, 0x09)
 
def mouse_up():
    winio = __get_winio()
 
    wait_for_buffer_empty();
    winio.set_port_byte(KBC_KEY_CMD, 0xd3);
    wait_for_buffer_empty();
    winio.set_port_dword(KBC_KEY_DATA, 0x08)

# Press 'A' key
# Scancodes references : https://www.win.tue.nl/~aeb/linux/kbd/scancodes-1.html
# key_press(0xe9)
# pyautogui.moveTo(568,45)
# time.sleep(2)
# mouse_down()
# time.sleep(1)
# mouse_up()
key_press(0xe9)