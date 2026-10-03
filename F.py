import random
import re
import sys
import time
import hashlib
import uuid
import json
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

uid = '7797970810'
pw = '7797970810'

url = 'https://x.facebook.com/login/device-based/regular/login/?login_attempt=1'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.facebook.com',
    'Referer': 'https://www.facebook.com/cass.mcdonnell/posts/pfbid0PnH92D3JTvZJgoyzjEdYdKPbZdcnG24emHL6vvmqb9hZZTwq5zBZNKsfDF8nZTC7l?rdid=PgskDFDqekeyZPSH',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'dpr': '1',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-full-version-list': '"Not;A=Brand";v="99.0.0.0", "Google Chrome";v="139.0.7258.139", "Chromium";v="139.0.7258.139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'viewport-width': '1189'
}
data = {
    'email': uid,
    'cuid': '',
    'guid': 'fd703f5e8d9f6f077',
    'lgnjs': '1791049474',
    'lgnrnd': '104433_p-XH',
    'locale': 'en_GB',
    'login_source': 'comet_login_header',
    'next': 'https://www.facebook.com/cass.mcdonnell/posts/pfbid0PnH92D3JTvZJgoyzjEdYdKPbZdcnG24emHL6vvmqb9hZZTwq5zBZNKsfDF8nZTC7l?rdid=PgskDFDqekeyZPSH#',
    'skstamp': '',
    'timezone': '-330',
    'prefill_contact_point': '',
    'prefill_source': '',
    'lsd': 'AdTMgVzG8s6XSJTvSsY3Kvx54V0',
    'jazoest': '22270',
    'lgndim': 'eyJ3IjoxNDQwLCJoIjo5MDAsImF3IjoxNDQwLCJhaCI6ODYwLCJjIjoyNH0%3D',
    'ab_test_data': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
    'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw)
}

response = requests.post(url, headers=headers, data=data)
print("Status:", response.status_code)
print(response.text)
