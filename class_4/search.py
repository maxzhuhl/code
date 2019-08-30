import  time
from selenium import webdriver
def search(driver,search):
    driver.find_element_by_css_selector("input#kw").send_keys(search)
    driver.find_element_by_css_selector("input#su").click()
    time.sleep(2)
    return driver