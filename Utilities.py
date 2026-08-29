import pyautogui
import time
import mouse
import keyboard
import random
import pydirectinput



def FindPurpleButton():
    image = 'PurpleButton.png'

    try:
        x, y = pyautogui.locateCenterOnScreen(image, confidence=0.42)
        pydirectinput.moveTo(x, y)
        time.sleep(0.2)
        pydirectinput.moveTo(x + 1, y + 1)
        pydirectinput.click()
    except pyautogui.ImageNotFoundException:
        return


def PerfectKick():
    pydirectinput.click()
    time.sleep(0.4)
    pydirectinput.click()
    print('kicking')


def farmBrain():
    while True:
        pydirectinput.click()
        time.sleep(0.30)
        pydirectinput.click()
        time.sleep(25.5)
        print('press W')
        keyboard.press('w')
        time.sleep(38)
        keyboard.release('w')
        keyboard.press('s')
        time.sleep(5)
        keyboard.release('s')
        time.sleep(3)



def click_At(x, y):
    pydirectinput.moveTo(x, y)
    time.sleep(0.2)
    pydirectinput.moveTo(x + 1, y + 1)
    pydirectinput.click()

def Rebirth():
    click_At(120,800)
    time.sleep(0.5)
    click_At(1200, 980)
    time.sleep(0.5)
    click_At(1700, 400)

def Upgrade():
     keyboard.press_and_release('1')
     time.sleep(0.5)
     keyboard.press_and_release('space')
     click_At(1280, 700)
     click_At(1280, 700)
     click_At(1280, 700)
     time.sleep(0.5)
     keyboard.press_and_release('1')