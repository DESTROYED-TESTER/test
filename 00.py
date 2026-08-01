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
uid = "9907854044"
pw = "990785"
Session = requests.Session()
#head = {"authority":"m.prod.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","accept-language":"en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7","cache-control":"max-age=0","dpr":"3","sec-ch-prefers-color-scheme":"light","sec-fetch-dest":"document","sec-fetch-mode":"navigate","sec-fetch-site":"none","sec-fetch-user":"?1","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0","viewport-width":"980"}
#requu12 = Session.get('https://www.facebook.com/',headers=head)
#free_fb = Session.get('https://touch.facebook.com/')
free_fb = Session.get('https://touch.facebook.com/').text
#datr = requu12.cookies.get('datr')
#sb = requu12.cookies.get('sb')
#fr = requu12.cookies.get('fr')
cookies = {
    'datr': 'WXltatd2ENUjZUyfA3yVvrhw',
    'sb': 'gXltaqNiraYlzznawgFOc3Qf',
    'locale': 'bn_IN',
    'wd': '1143x773',
}
#log_data = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(requu1.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(requu1.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': uid, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': '0', 'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw), 'bi_wvdp': '', 'fb_dtsg': '', 'jazoest': re.search('name="jazoest" value="(.*?)"',str(requu1.text)).group(1), 'lsd': re.search('name="lsd" value="(.*?)"',str(requu1.text)).group(1), '__dyn': '', '__csr': '', '__req': random.choice(["1","2","3","4","5","6","7","8","9","0"]), '__fmt': '0', '__a': '',  '__user': '0'}
log_data = {
    'jazoest': '22474',
    'lsd': 'AdRRDLpqanHVfvAWy_sUXtH_OJc',
    'initial_request_id': 'A10tPfatOkwvT0WG7gWVNnY',
    'timezone': '-330',
    'lgndim': 'eyJ3IjoxNDQwLCJoIjo5MDAsImF3IjoxNDQwLCJhaCI6ODYwLCJjIjozMn0=',
    'lgnrnd': '214622_uurZ',
    'lgnjs': 'n',
    'email': '9749797453',
    'pass': '#PWD_BROWSER:5:1785559664:AZ5QAOWfT8EO2FqaVqWoHd8xdImXBZXJ4mbWDqdkbNxndqh1Zhdc2gNQ35LlRHRtpLRQ66HmREl8z9XkhNXm5vumHq7GgpetBsvVZhPwzD4N1sFDJtsq62iZ9xbKwl/MYQMt/EMOOSaRq/bA',
    'default_persistent': '',
}

#cookies ={"datr": datr, "sb": sb, "m_pixel_ratio": "2.75", "wd": "393x851", "fr": fr}
#url = "https://edge-mqtt.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
url = 'https://www.messenger.com/login/password/'
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'dpr': '1',
    'origin': 'https://www.messenger.com',
    'priority': 'u=0, i',
    'referer': 'https://www.messenger.com/login/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Google Chrome";v="145.0.7632.5", "Chromium";v="145.0.7632.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    'viewport-width': '1143',
    # 'cookie': 'datr=WXltatd2ENUjZUyfA3yVvrhw; sb=gXltaqNiraYlzznawgFOc3Qf; locale=bn_IN; wd=1143x773',
}

response = Session.post(url,cookies=cookies,headers=headers,data=data,allow_redirects=False)
print(response.text)
print(response)
#print(response.status_code)
#print(response.text)
# Check login success
log_cookies = Session.cookies.get_dict().keys()
if "c_user" in log_cookies:
    print('\033[1;92m OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK ')
elif 'checkpoint' in log_cookies:
    print('\033[1;92m CP CP  CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP')
