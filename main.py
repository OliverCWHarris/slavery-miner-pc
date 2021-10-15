import pyautogui
import time
import random
from datetime import date
import keyboard

today=date.today()
todaystr=str(today)

randomtime=random.randint(1,4)
randomtime2=random.randint(120,135)


def OD():
    time.sleep(2)
    pyautogui.moveTo(120,1040)#moves cursor to discord in tray
    pyautogui.click()#opens discord
    pyautogui.moveTo(15,350)#goes to server
    pyautogui.move(100,225)#goes to chat bar
    time.sleep(0.01)
    pyautogui.scroll(-1000)#scrolls to bottom of chat bar
    time.sleep(0.1)
    pyautogui.click()#enters chat


def CD():
    pyautogui.moveTo(120,1040)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.moveTo(825,540)


def FHS():
    pyautogui.write(';f')
    pyautogui.press('enter')
    time.sleep(randomtime)
    pyautogui.write(';h')
    pyautogui.press('enter')
    time.sleep(randomtime)
    pyautogui.write(';s')
    pyautogui.press('enter')
    time.sleep(randomtime)


def CA():
    pyautogui.write(';claimall')
    pyautogui.press('enter')







start=1
while start==1:
    menuchoice=int(input("1 for open discord\n2 for fish hunt sell\n3 for claim crate\n4 for everything\n5 for repeat sell\n: "))
    if menuchoice==1:
        OD()
        CD()
    elif menuchoice==2:
        OD()
        FHS()
        CD()
    elif menuchoice==3:
        OD()
        CA()
        CD()
    elif menuchoice==4:
        OD()
        FHS()
        CA()
        CD()
    elif menuchoice==5:
        repeat=1
        done=1
        while repeat==1:
            donestr=str(done)
            OD()
            FHS()
            CA()
            CD()
            f=open("timesdone.txt","a")
            f.write("\n")
            f.write(todaystr)
            f.write(" ")
            f.write(donestr)
            f.close()
            time.sleep(randomtime2)
            done=done+1
            if keyboard.is_pressed('0'):
                repeat=0