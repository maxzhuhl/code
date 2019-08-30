import time
from selenium import webdriver

def openwed(url):
    #1.打开浏览器，获取驱动
    driver=webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver