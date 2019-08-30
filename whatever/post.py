import requests,json
#import urllib3
#http = urllib3.PoolManager(maxsize=10)
#http = urllib3.HTTPConnectionPool('google.com', maxsize=10)
import ssl #
ssl._create_default_https_context = ssl._create_unverified_context
url ="https://passport.csdn.net/v1/api/app/scan/createAppScan"
headers = {"Content-Type": "application/json;charset=utf-8"}
data={
    "userCode":"15573706812",
    "password":""
}
requests = requests.post(url=url, headers=headers, data=json.dumps(data))
print(requests.text)
print(requests.headers)



