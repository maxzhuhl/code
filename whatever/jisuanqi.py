from appium import webdriver
import time
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'platformVersion': '5.0.2',
    'appPackage': 'com.android.calculator2',
    'appActivity': 'com.android.calculator2.Calculator'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.find_element_by_id("com.android.calculator2:id/digit_3").click()
driver.find_element_by_id("com.android.calculator2:id/op_add").click()
driver.find_element_by_id("com.android.calculator2:id/digit_9").click()
driver.find_element_by_id("com.android.calculator2:id/eq").click()
time.sleep(2)
driver.find_element_by_id("com.android.calculator2:id/op_mul").click()
driver.find_element_by_id("com.android.calculator2:id/digit_8").click()
driver.find_element_by_id("com.android.calculator2:id/digit_0").click()
driver.find_element_by_id("com.android.calculator2:id/digit_0").click()
driver.find_element_by_id("com.android.calculator2:id/eq").click()
driver.quit()
