#!/usr/bin/env ipython
from re import match
from time import sleep

from selenium import webdriver

path = ""
htmlp = (
    "/home/suphal/Data/web/freecodingcamp/responsive-web-design/tribute-page/index.html"
)
html = input("Please enter the path to your project or website folder =  ")
css = input(
    "if the name of the css file is not style.css than enter its name =  ")
if len(css) < 2:
    if html[len(html) - 1] == "/":
        for i in range(len(html)):
            path = path + html[i]
    css = path + "/style.css"
cssf = open(css, "r").read()

htmlp = path + "index.html"

x = match("(.*).html", htmlp)
if x:
    html = "file://" + htmlp
else:
    html = "file://" + htmlp + "index.html"

driver = webdriver.Firefox()
driver.get(html)

hfile = open(htmlp, "r").read()
while True:
    cssn = open(css, "r").read()
    hfilen = open(htmlp, "r").read()
    if hfile != hfilen or cssf != cssn:
        cssf = cssn
        hfile = hfilen
        driver.refresh()
        print("refreshed")
    sleep(2)
