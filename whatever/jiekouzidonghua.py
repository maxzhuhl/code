import requests
url = "http://www.baidu.com"

headers ={"Content-Type": "text/html;charset=utf-8"}
requests = requests.get(url=url,headers=headers)
print(requests.text)
print(requests.headers)


