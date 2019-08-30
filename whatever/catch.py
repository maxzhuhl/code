import time

from selenium import webdriver
from lxml import html

etree = html.etree
# 创建对象
Browner = webdriver.Chrome()
Browner.get('https://www.jd.com/')
# 输入搜索内容
kw = Browner.find_element_by_id("key")
kw.send_keys('华为手机')

# 点击
iconfont =Browner.find_element_by_class_name('button')
iconfont.click()


# 滑动至浏览器下端
Browner.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(4)
# 获取网页源码
html = Browner.page_source

# 解析获取数据
h = etree.HTML(html)
l = h.xpath('//ul[@class="gl-warp clearfix"]/li')
# 循环获取各个对象的数据
for k in l:
    price = k.xpath('./div/div[@class="p-price"]//i/text()')
    name = k.xpath('./div/div[@class="p-name p-name-type-2"]/a/@title')
    #获取到的名字和价格，打印出来
    print(name,price)

