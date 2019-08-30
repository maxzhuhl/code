from appium import webdriver
import time
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'platformVersion': '5.0.2',
    'appPackage': 'com.android.settings',
    'appActivity': 'com.android.server.am.ActivityManagerService$Lifecycle'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.find_elements_by_link_text("蓝牙").click()
