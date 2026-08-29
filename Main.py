import keyboard
import time
import threading
import sys
import pyautogui
import array
from Utilities import PerfectKick, FindPurpleButton, click_At, Rebirth, Upgrade, farmBrain

image = 'PurpleButton.png'

stop_event = threading.Event()


def ClickPur():
    while True:
        FindPurpleButton()
        time.sleep(0.5)


def Quit():
    print('Quit')
    sys.exit(0)


def AutoFarm():
    keyboard.add_hotkey('t', Quit)


    while True:
        for i in range(60):
            FindPurpleButton()
            time.sleep(1)
        Rebirth()
        Upgrade()





keyboard.add_hotkey('f6', AutoFarm)

keyboard.add_hotkey('c', ClickPur)

keyboard.add_hotkey('k', PerfectKick)

keyboard.add_hotkey('f1', farmBrain)

keyboard.wait()


#PerfectKick()



