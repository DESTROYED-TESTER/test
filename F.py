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

url = 'https://free.facebook.com/login/device-based/regular/login/?login_attempt=1'
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
session = requests.Session()
respon = session.post(url, headers=headers, data=data, allow_redirects=False)
cookies = session.cookies.get_dict()
location = respon.headers.get("Location", "") or ""
body = respon.text or ""

print("HTTP Status:", respon.status_code)
print("Location:", location)

if "c_user" in cookies:
    print("\033[1;92m[SUCCESS] Login successful")
    print("UID:", cookies.get("c_user"))

elif "checkpoint" in location.lower() or "checkpoint" in body.lower():
    print("\033[1;93m[CHECKPOINT] Verification required")

elif (
    "two_factor" in location.lower()
    or "two-factor" in body.lower()
    or "two factor" in body.lower()
):
    print("\033[1;93m[2FA] Two-factor authentication required")

else:
    print(f"\033[1;91m[FAILED] Status code: {respon.status_code}")

    # Try to find common Facebook error messages
    patterns = [
        r'<div[^>]*class="[^"]*_9ay7[^"]*"[^>]*>(.*?)</div>',
        r'<div[^>]*role="alert"[^>]*>(.*?)</div>',
        r'<span[^>]*>([^<>]*(?:password|email|phone|account|login)[^<>]*)</span>',
    ]

    reason = None

    for pattern in patterns:
        match = re.search(pattern, body, flags=re.I | re.S)
        if match:
            reason = re.sub(r"<[^>]+>", "", match.group(1))
            reason = re.sub(r"\s+", " ", reason).strip()

            if reason:
                break

    if reason:
        print("[REASON]", reason)
    else:
        # Useful fallback diagnostics
        if "incorrect password" in body.lower():
            print("[REASON] Incorrect password")

        elif "password you entered is incorrect" in body.lower():
            print("[REASON] Incorrect password")

        elif "email or phone" in body.lower():
            print("[REASON] Email/phone may be invalid")

        elif "login" in location.lower():
            print("[REASON] Redirected back to login page")

        else:
            print("[REASON] Facebook did not return a clear error message")
            print("\nResponse preview:")
            print(body[:1500])
