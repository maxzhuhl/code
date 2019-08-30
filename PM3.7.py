# def openweb(driver,url):
#     driver.get(url)
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     return  driver
import time
def search(driver,search):
    driver.find_element_by_id("kw").send_keys(search)
    time.sleep(5)
    driver.find_element_by_id("su").click()
    return driver