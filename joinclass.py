#!/bin/python3
from os import system, popen
import pyautogui as pg
from time import sleep

x = popen("pgrep zoom").read()
if len(x) > 1:
    system("killall zoom")
    sleep(2)
system("zoom &")
sleep(12)

pg.hotkey("winleft", "6")
sleep(2)


def image(x, y, z):
    i = True
    while i is True:
        w = pg.locateCenterOnScreen(x, grayscale=y, region=z)
        if w is not None:
            pg.click(w)
            i = False


image_dir = "/home/suphal/.scripts/images/"
image(image_dir + "join1.png", True, (200, 100, 1150, 600))
sleep(4)
pg.press("tab")
pg.press("tab")
pg.write("")
pg.press("return")

sleep(6)
s = pg.pixel(940, 465)
# print(s[2])
if s[0] == 14:
    pg.click(920, 465)
    sleep(2)
    pg.press("tab")
    pg.press("tab")
sleep(3)

pg.write("")
pg.press("return")
#  https://zoom.us/j/3127947004?pwd=TnFjWGMzajMvVkVWMVdsellMdTByQT0
