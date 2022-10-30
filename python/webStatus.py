# pip install requests#method 1
import urllib.requestfrom urllib.request import Request, urlopenreq = Request('https://medium.com/@codedev101', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).getcode()
print(webpage) # 200# method 2import requests
r = requests.get("https://medium.com/@codedev101")
print(r.status_code) # 200
