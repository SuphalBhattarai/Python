#!/bin/python3
from datetime import datetime
from email import emails
from os import listdir, system
from time import sleep

from pyautogui import hotkey, press, write
from rofi import Rofi


def new_page():
    hotkey("alt", "p")
    sleep(1)
    press("n")
    sleep(2)


def insert_image(x):
    hotkey("alt", "i")
    sleep(1)
    press("return")
    sleep(5)
    write(x)
    sleep(4)
    press("return")
    sleep(1)
    press("return")
    sleep(6)
    hotkey("alt", "n")
    sleep(5)


def make_img(num):
    sleep(2)
    press("f4")
    sleep(2)
    if num != 0:
        press("right")
    hotkey("alt", "a")
    write("270")
    press("return")
    sleep(3)
    press("f4")
    sleep(2)
    press("left")
    sleep(1)
    hotkey("alt", "x")
    write("-0.4")
    hotkey("alt", "y")
    write("-0.4")
    hotkey("alt", "d")
    write("8.5")
    hotkey("alt", "e")
    write("11")
    press("return")
    sleep(5)


system("libreoffice -o /home/suphal/Documents/draft.odg & ")
hotkey("winleft", "9")
sleep(25)

downloads = listdir("/home/suphal/Downloads/")

num = 0
for x in downloads:
    if x[len(x) - 3] + x[len(x) - 2] + x[len(x) - 1] == "jpg":
        y = x
        new_page()
        insert_image(y)
        make_img(num)
        num += 1

r = Rofi().text_entry("Whose homework is this ?")
name = r + "Homework" + str(datetime.now().date())

sleep(1)
hotkey("alt", "f")
sleep(1)
press("e")
press("d")
sleep(3)
write(name)
sleep(1)
press("return")
hotkey("winleft", "7")
sleep(120)

o = 0
while o < 3:
    e = Rofi().select(
        "Would you like to send the email ?",
        ["yes", "no"],
        lines=2,
        width=25,
        key1=("y", "yes"),
        key2=("n", "no"),
    )
    o += 1
    sleep(30)

if e == (0, 1):
    hotkey("winleft", "5")
    system(
        "thunderbird --compose to="
        + emails[r]
        + ",subject=Homework,attachment=/home/suphal/Documents/"
        + name
        + ".pdf"
    )
    sleep(3)
    write("Suphal Bhattarai (D6 Bio)")
    system("mv /home/suphal/Downloads/*.jpg /home/suphal/for_deletion/")
