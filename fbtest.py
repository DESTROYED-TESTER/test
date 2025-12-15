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
uid = input("Enter UID / Email: ").strip()
pw = input("Enter Password: ").strip()
enpass =  "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),

cookies = {
    'ps_l': '1',
    'ps_n': '1',
    'sb': 'err0aNeUDQ1wJz7g339S3YR3',
    'datr': 'err0aLFyeHZl73bBArjRa1WN',
    'locale': 'en_US',
    'fr': '1NdqEGAzzGsGA9kzI.AWevGZMpZ5MghzRNlVyMhf97HHimD4M-CB-q9dwFofwKvMwlj3g.BpA6Jl..AAA.0.0.BpQEG1.AWd7mMQ1okNLHe5JIr-8eo7ZaR8',
    'wd': '1136x773',
    'dpr': '1',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7,hi;q=0.6,gu;q=0.5,bn;q=0.4',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'dpr': '1',
    'origin': 'https://www.facebook.com',
    'priority': 'u=0, i',
    'referer': 'https://www.facebook.com/login/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="143.0.7499.41", "Chromium";v="143.0.7499.41", "Not A(Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'viewport-width': '1136',
    # 'cookie': 'ps_l=1; ps_n=1; sb=err0aNeUDQ1wJz7g339S3YR3; datr=err0aLFyeHZl73bBArjRa1WN; locale=en_US; fr=1NdqEGAzzGsGA9kzI.AWevGZMpZ5MghzRNlVyMhf97HHimD4M-CB-q9dwFofwKvMwlj3g.BpA6Jl..AAA.0.0.BpQEG1.AWd7mMQ1okNLHe5JIr-8eo7ZaR8; wd=1136x773; dpr=1',
}

params = {
    'login_attempt': '1',
    'lwv': '100',
}

data = {
    'jazoest': '2979',
    'lsd': 'AdG9wjSQeMw',
    'display': '',
    'isprivate': '',
    'return_session': '',
    'skip_api_login': '',
    'signed_next': '',
    'trynum': '1',
    'timezone': '-330',
    'lgndim': 'eyJ3IjoxNDQwLCJoIjo5MDAsImF3IjoxNDQwLCJhaCI6ODYwLCJjIjoyNH0=',
    'lgnrnd': '091325_euvt',
    'lgnjs': '1765818806',
    'shared_prefs_data': 'eyIzMDAwMCI6W3sidCI6MTc2NTgxODgwNi41MiwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luLyJ9LCJ2IjpmYWxzZX1dLCIzMDAwMSI6W3sidCI6MTc2NTgxODgwNi41MjEsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi8ifSwidiI6NX1dLCIzMDAwMiI6W3sidCI6MTc2NTgxODgwNi41MjEsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi8ifSwidiI6Mn1dLCIzMDAwMyI6W3sidCI6MTc2NTgxODgwNi41MjEsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi8ifSwidiI6WyJlbi1JTiIsImVuLVVTIiwiZW4tR0IiLCJlbiIsImhpIiwiZ3UiLCJibiJdfV0sIjMwMDA0IjpbeyJ0IjoxNzY1ODE4ODA2LjUyMiwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luLyJ9LCJ2IjoxNTB9XSwiMzAwMDUiOlt7InQiOjE3NjU4MTg4MDYuNTIyLCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4vIn0sInYiOnsidyI6MTQ0MCwiaCI6NzczfX1dLCIzMDAwNyI6W3sidCI6MTc2NTgxODgwNi41MjIsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi8ifSwidiI6ImRlZmF1bHQifV0sIjMwMDA4IjpbeyJ0IjoxNzY1ODE4ODA2LjU0NSwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luLyJ9LCJ2IjoicHJvbXB0In1dLCIzMDAxMiI6W3sidCI6MTc2NTgxODgwNi41MjMsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi8ifSwidiI6Ikdvb2dsZSBJbmMuIn1dLCIzMDAxMyI6W3sidCI6MTc2NTgxODgwNi41MjMsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi8ifSwidiI6IjUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTQzLjAuMC4wIFNhZmFyaS81MzcuMzYifV0sIjMwMDE1IjpbeyJ0IjoxNzY1ODE4ODA2LjUyMywiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luLyJ9LCJ2IjoiV2luMzIifV0sIjMwMDE4IjpbeyJ0IjoxNzY1ODE4ODA2LjUyNCwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luLyJ9LCJ2IjoyfV0sIjMwMDIyIjpbeyJ0IjoxNzY1ODE4ODA2LjUzNSwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luLyJ9LCJ2Ijp0cnVlfV0sIjMwMDQwIjpbeyJ0IjoxNzY1ODE4ODA2LjUzNSwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luLyJ9LCJ2IjotMzMwfV0sIjMwMDkzIjpbeyJ0IjoxNzY1ODE4ODA2LjUzNSwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luLyJ9LCJ2IjowfV0sIjMwMDk0IjpbeyJ0IjoxNzY1ODE4ODA2LjUzNSwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luLyJ9LCJ2IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzE0My4wLjAuMCBTYWZhcmkvNTM3LjM2In1dLCIzMDA5NSI6W3sidCI6MTc2NTgxODgwNi41MzUsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi8ifSwidiI6M31dLCIzMDEwNiI6W3sidCI6MTc2NTgxODgwNi41MTYsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi8ifSwidiI6ZmFsc2V9LHsidCI6MTc2NTgxODgwNi43NTEsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi8ifSwidiI6dHJ1ZX1dLCIzMDEwNyI6W3sidCI6MTc2NTgxODgwNi41MTYsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi8ifSwidiI6ZmFsc2V9XX0=',
    'email': uid,
    'prefill_contact_point': '',
    'prefill_source': '',
    'prefill_type': '',
    'first_prefill_source': '',
    'first_prefill_type': '',
    'had_cp_prefilled': 'false',
    'had_password_prefilled': 'false',
    'ab_test_data': '/AAAAAAA/AA/AAAAA/AAAA/AAAAAAAAAAAAAAAA/AAA/AfffffDFAA',
    'encpass': enpass,
}

response = requests.post(
    'https://www.facebook.com/login/device-based/regular/login/',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
print("Status code:", response.status_code)
print("Response URL:", response.url)
print("Response headers:", response.headers)
print("Response text (first 500 chars):", response.text[:500])



