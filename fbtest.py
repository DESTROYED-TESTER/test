import random
import re
import sys
import time
import hashlib
import uuid
import urllib.request
import requests
import string
import os
import time,subprocess,platform,uuid,json
import random
import base64
import string
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
uid = input("Enter UID / Email: ").strip()
pw = input("Enter Password: ").strip()
enpass = "#PWD_BROWSER:0:{}:{}".format(int(time.time()), pw)
session = requests.Session()
url1 = "https://mbasic.facebook.com/"
head = {"authority": "m.prod.facebook.com",
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
"cache-control": "max-age=0",
"dpr": "3",
"sec-ch-prefers-color-scheme": "light",
"sec-fetch-dest": "document",
"sec-fetch-mode": "navigate",
"sec-fetch-site": "none",
"sec-fetch-user": "?1",
"upgrade-insecure-requests": "1",
"user-agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Mobile Safari/537.36',
"viewport-width": "980"}
requu1 = session.get(url1,headers=head)

cookies = {
    'datr': 'cBNEaQDmgPScqxAEzMAVJz2c',
    'locale': 'en_US',
    'wd': '1160x773',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,bn;q=0.6',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.messenger.com',
    'priority': 'u=0, i',
    'referer': 'https://www.messenger.com/?locale=en_US',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    # 'cookie': 'datr=cBNEaQDmgPScqxAEzMAVJz2c; locale=en_US; wd=1160x773',
}

data = {
    'jazoest': '2860',
    'lsd': 'AdHIJjGJEKQ',
    'initial_request_id': 'AjNT6s4V9aYDxWY1xquwbZF',
    'timezone': '-330',
    'lgndim': 'eyJ3IjoxNDQwLCJoIjo5MDAsImF3IjoxNDQwLCJhaCI6ODYwLCJjIjoyNH0=',
    'lgnrnd': '064512_QZiY',
    'lgnjs': 'n',
    'email': '8101729293',
    'pass': '#PWD_BROWSER:5:1766069581:Ab1QAHJ8IWa7REAjnsTK6FtwMIvRPk3eykctwMku5firfVEhbm4YwYJNfcx7x3Dp5mb5GPA3VLrXKyVvLTzXGnAT8on/nlAun+JgYEa88qyaXq4Gz5Iu46EbLpxT03UFYtK89F4KB/vYFEzW',
    'default_persistent': '',
}

response = session.post('https://www.messenger.com/login/password/', cookies=cookies, headers=headers, data=data)
session_cookies = session.cookies
if response.status_code == 200:
   if 'login' not in response.url.lower():
       print("✅ VERIFIED: Can access messenger without redirect")
       cookies_dict = requests.utils.dict_from_cookiejar(session_cookies)
       curl_cookies = "; ".join([f"{k}={v}" for k, v in cookies_dict.items()])
       print(curl_cookies)
       print(cookies_dict)
   else:
       print("❌ FAILED: Redirected to login page")
else:
    print(f"❌ ERROR: HTTP {response.status_code}")



