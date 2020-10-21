#!/usr/bin/env ipython
import requests
from bs4 import BeautifulSoup
from time import sleep
from os import system

url = "https://www.worldometers.info/coronavirus/country/nepal/"
site = requests.get(url).text
sleep(2)

soup = BeautifulSoup(site, "lxml")

cases = soup.find(class_="news_li").strong.text
system('notify-send "' + cases + '"')
