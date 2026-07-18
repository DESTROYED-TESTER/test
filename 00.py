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
import time,subprocess,platform,uuid
import random
import base64
import string
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
uid = "9907854044"
pw = "990785"
Session = requests.Session()
#head = {"authority":"m.prod.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","accept-language":"en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7","cache-control":"max-age=0","dpr":"3","sec-ch-prefers-color-scheme":"light","sec-fetch-dest":"document","sec-fetch-mode":"navigate","sec-fetch-site":"none","sec-fetch-user":"?1","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0","viewport-width":"980"}
#requu12 = Session.get('https://www.facebook.com/',headers=head)
requu1 = Session.get('https://touch.facebook.com/')
#datr = requu12.cookies.get('datr')
#sb = requu12.cookies.get('sb')
#fr = requu12.cookies.get('fr')
log_data = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(requu1.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(requu1.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': uid, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': '0', 'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw), 'bi_wvdp': '', 'fb_dtsg': '', 'jazoest': re.search('name="jazoest" value="(.*?)"',str(requu1.text)).group(1), 'lsd': re.search('name="lsd" value="(.*?)"',str(requu1.text)).group(1), '__dyn': '', '__csr': '', '__req': random.choice(["1","2","3","4","5","6","7","8","9","0"]), '__fmt': '0', '__a': '',  '__user': '0'}
#cookies ={"datr": datr, "sb": sb, "m_pixel_ratio": "2.75", "wd": "393x851", "fr": fr}
url = "https://web.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110"
#url = 'https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100'
headers = {
    'authority': 'limited.facebook.com',
    'accept': '/',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'datr=AvxaauBxe8J2e6uqNRe7Ks5u; sb=AvxaanntJgRoS-6c3x6h_Z-w; m_pixel_ratio=2.75; wd=393x851; ps_l=1; ps_n=1; fr=0mN3NySo4ygtsuEdo..BqWvwC..AAA.0.0.BqWvwc.AWf9_qxR9LNotvAZnbuzCekImP0',
    'origin': 'https://limited.facebook.com',
    'referer': 'https://limited.facebook.com/login/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-asbd-id': '359341',
    'x-fb-lsd': re.search('name="lsd" value="(.*?)"',str(requu1.text)).group(1),
    'x-requested-with': 'XMLHttpRequest',
    'x-response-format': 'JSONStream',
}


response = Session.post(url,data=log_data,headers=headers,allow_redirects=False)
print(response.text)
#print(response.status_code)
#print(response.text)
# Check login success
log_cookies = Session.cookies.get_dict().keys()
if "c_user" in log_cookies:
    print('\033[1;92m OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK ')
elif 'checkpoint' in log_cookies:
    print('\033[1;92m CP CP  CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP')
