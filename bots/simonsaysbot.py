from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)
print("start")
#yellow X:  589 Y:  610 RGB: (173, 166,  33) 1
#red    X:  589 Y:  808 RGB: (168,  28,  28) 2
#green  X:  409 Y:  615 RGB: ( 30, 101,  30) 3
#blue   X:  410 Y:  805 RGB: ( 29,  29, 169) 4

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def colorcheck(x,listen):
    if pyautogui.pixel(589,610)[0] != 173:
        while pyautogui.pixel(589,610)[0] != 173:
            time.sleep(0.05)
        print("yellow")
        x+=1
        if x > len(colors):
            colors.append(1)
            listen = False
                
    if pyautogui.pixel(589,808)[0] != 168:
        while pyautogui.pixel(589,808)[0] != 168:
            time.sleep(0.05)
        print("red")
        x+=1
        if x > len(colors):
            colors.append(2)
            listen = False

    if pyautogui.pixel(409,615)[0] != 30:
        while pyautogui.pixel(409,615)[0] != 30:
            time.sleep(0.05)
        print("green")
        x+=1
        if x > len(colors):
            colors.append(3)
            listen = False
                
    if pyautogui.pixel(410,805)[0] != 29:
        while pyautogui.pixel(410,805)[0] != 29:
            time.sleep(0.05)
        print("blue")
        x+=1
        if x > len(colors):
            colors.append(4)
            listen = False
    return x,listen
            

colors = []

x = 0
listen = True

while keyboard.is_pressed('q') == False:
    
    if listen:
        x, listen = colorcheck(x, listen)
    else:
        for number in colors:
            if number == 1:     #yellow
                click(589,610)
            if number == 1:     #red
                click(589,808)
            if number == 1:     #green
                click(409,615)
            if number == 1:     #blue
                click(410,805)
        time.sleep(0.3)
        listen = True
        x = 0
        
        
