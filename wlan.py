#!/usr/bin/env ipython

from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://192.168.1.1")
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("superadmin")
driver.find_element_by_id("psd").send_keys("")
log_in = driver.find_element_by_xpath(
    "/html/body/form/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/input[1]"
)
log_in.click()
sleep(5)
# on login
driver.get("http://192.168.1.1/wlvap.asp")

try:
    driver.find_element_by_xpath(
        "/html/body/blockquote/div/form/table/tbody/tr[5]/td[2]/input"
    ).click()
except:
    driver.find_element_by_xpath(
        "/html/body/blockquote/div/form/table/tbody/tr[5]/td[2]/input"
    )
driver.find_element_by_xpath("/html/body/blockquote/div/form/input[3]").click()

# Exit login
driver.get("http://192.168.1.1")
sleep(5)
driver.find_element_by_xpath(
    "/html/body/form/table[2]/tbody/tr[1]/td[2]/font[2]/input"
).click()
driver.quit()
