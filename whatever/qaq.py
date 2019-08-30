import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://183.136.146.130:10998/#!/Home")
driver.find_element_by_id("id-tf-login-username").send_keys("zhangyuye")