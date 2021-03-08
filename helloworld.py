import requests


url = 'https://exmartapi.sdycsdyc.cn/api/inform'
body = {"informType": 0}
res = requests.post(url=url,json=body)
print(res.headers)