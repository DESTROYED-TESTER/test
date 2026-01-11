import random
import sys
import time
import hashlib
import uuid
import urllib.request
import requests
import string
import os
import time,subprocess,platform,uuid
import random
import base64
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime 
time_now = int(datetime.now().timestamp())
enc_password = f"#PWD_INSTAGRAM_BROWSER:0:{time_now}:{'891816'}"
user = '8918168736'
session = requests.Session()
response = session.get('https://www.instagram.com/accounts/login/')
csrftoken = response.cookies.get('csrftoken')
cookies = {
'csrftoken': csrftoken,
'datr': 'SehHaXwOCk9GiWPH3fNZWglz',
'ig_did': str(uuid.uuid4()).upper(),
'mid': 'aUfoSwALAAG_fJ1ItrV9b-sb7DCg',
'ig_nrcb': '1',
'wd': '1136x773',}
headers = {
    'accept': '*/*',
    'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7,hi;q=0.6,gu;q=0.5,bn;q=0.4',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.instagram.com',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/accounts/login/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="143.0.7499.170", "Chromium";v="143.0.7499.170", "Not A(Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'x-asbd-id': '359341',
    'x-csrftoken': '0flYJ11PP9lomxiSgLG0yUvWZzX0gT8w',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1031856633',
    'x-requested-with': 'XMLHttpRequest',
    'x-web-session-id': 'k0xmay:8ozsyz:oh7p68',
    # 'cookie': 'datr=wDF1aOt9UdNuCskTeplHs7Yx; ig_did=534026BE-B655-4318-AB86-5CFD617D4D50; mid=aHUxwQALAAEhOjO5lKEpzt85Xu9g; ig_nrcb=1; ps_l=1; ps_n=1; csrftoken=0flYJ11PP9lomxiSgLG0yUvWZzX0gT8w; ig_lang=en; wd=1189x773',
}

data = {
    'enc_password': enc_password,
    'caaF2DebugGroup': '0',
    'isPrivacyPortalReq': 'false',
    'loginAttemptSubmissionCount': '0',
    'optIntoOneTap': 'false',
    'queryParams': '{}',
    'trustedDeviceRecords': '{}',
    'username': user,
    'jazoest': '22791',
}

response = session.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', cookies=cookies, headers=headers, data=data)# cookies=cookies,
wanted = ["ds_user_id", "sessionid"]
all_cookies = session.cookies.get_dict()
extracted = {k: all_cookies[k] for k in wanted if k in all_cookies}
# Check response
if 'sessionid' in extracted:
   cookie_str = "; ".join(f"{k}={v}" for k, v in extracted.items())
   print("Cookies:", cookie_str)
