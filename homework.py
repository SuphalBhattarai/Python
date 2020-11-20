#!/usr/bin/env ipython

from re import match
from fpdf import FPDF
import os
from rofi import Rofi
from datetime import date
from time import sleep
import email_list
import multiprocessing

documents = "/home/suphal/Documents/"
downloads = "/home/suphal/Downloads/"


def insert_img(x):
    global downloads
    image_location = downloads + x
    pdf.image(image_location, x=0, y=0, w=8.27, h=11.69)


ls = os.listdir(downloads)
pdf = FPDF("P", "in", "A4")


def first_page():
    global pdf
    pdf.add_page()
    pdf.set_font("Arial", "B", 32)
    pdf.set_author("")
    pdf.set_creator("")
    pdf.set_title("Homework")
    pdf.set_fill_color(0, 0, 0)
    pdf.set_text_color(255, 255, 255)
    pdf.rect(0, 0, 8.27, 11.69, "FD")
    pdf.set_xy(1.5, 4)
    pdf.multi_cell(
        0, 0.5, "", 0, 2, "C"
    )


result = ""
results = ""


def get_input():
    global result
    global results
    results = str(Rofi().text_entry("Whose homeowrk is this?")).upper()
    result = results + "Homework" + str(date.today()) + ".pdf"


p1 = multiprocessing.Process(target=first_page)
p1.start()
p2 = multiprocessing.Process(target=get_input)
p2.start()

for x in ls:
    if match(".*.jpg", x):
        p1.join()
        pdf.add_page()
        insert_img(x)

p2.join()
pdf.output(documents + result, "F")
os.system("xdg-open " + documents + result + " &")

mail = email_list.emails[results]

sleep(10)
os.system(
    "thunderbird -compose \"to='"
    + mail
    + "',subject="
    + result
    + "',body=''\" "
)
