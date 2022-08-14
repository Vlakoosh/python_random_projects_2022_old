from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# X:  624 Y:  600 RGB: (  0,   0,   0)
# X:  712 Y:  600 RGB: (  0,   0,   0)
# X:  792 Y:  600 RGB: (  0,   0,   0)
# X:  881 Y:  600 RGB: (  0,   0,   0)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(624, 600)[0] == 0:
        click(624, 600)
    if pyautogui.pixel(712, 600)[0] == 0:
        click(712, 600)
    if pyautogui.pixel(792, 600)[0] == 0:
        click(792, 600)
    if pyautogui.pixel(881, 600)[0] == 0:
        click(881, 600)

