#!/bin/python
import os
from rofi import Rofi

r = Rofi()

script = "/home/suphal/.scripts/"
ls = os.listdir(script)

result = r.select("Which script would you like to run?", ls)
j = 0
dist = {}
for i in ls:
    dist[(j, 0)] = i
    j += 1

for i in dist:
    if str(i) == str(result):
        path = "/bin/python " + script + dist[i]
        os.system(path)
