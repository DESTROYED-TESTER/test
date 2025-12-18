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
requu1 = requests.get(url1,headers=head)

headers = {
    'sec-ch-ua-full-version-list': '"Not;A=Brand";v="99.0.0.0", "Google Chrome";v="139.0.7258.139", "Chromium";v="139.0.7258.139"',
    'sec-ch-ua-platform': '"Windows"',
    'Referer': 'https://www.facebook.com/login/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'X-FB-Friendly-Name': 'useCDSWebLoginMutation',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'X-ASBD-ID': '359341',
    'X-FB-LSD': 'AdFAZc32Q1g',
    'sec-ch-prefers-color-scheme': 'light',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'sec-ch-ua-platform-version': '"8.0.0"',
}

data = {
    'av': '0',
    '__aaid': '0',
    '__user': '0',
    '__a': '1',
    '__req': 'c',
    '__hs': '20419.HYP:comet_loggedout_pkg.2.1...0',
    'dpr': '1',
    '__ccg': 'EXCELLENT',
    '__rev': '1030403648',
    '__s': 'nygxma:a7xfrm:k7b2t7',
    '__hsi': '7577365859538649122',
    '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0qa0FE2awpUO0n24oaEd86a3a1YwBgao6C0Mo2swaOfK0EUjwGzE2ZwNwmE2eUlwhE2Lw6OyES1Tw8W0Lo6-1CG0hq1Iwqo5p0qWCgoK1sigaU7u1rwea4o4W0he1Sw',
    '__csr': 'gKgWaR25_lmHXyAcWBHAjguy8pxe8QVtp4QgCqZ9FqlLtqnoOijHaUqS7Unx2mU9eq9xm11U2pzppKfx62emm15w_wkbS4ozxq7Eaox0xwFKm0jW0p608mwww1rS0YDo1oU5u03lS032i0fpw052C8031128Ssw6W9w8uU0SUE1_o0aAE0xa0e9w5og081C0Vo0K63m047C08bg2fw1Uq480Jsm02DaU2CKfxC0my0UUUw2gw4xyK0hx3Ci',
    '__hsdp': 'gSg2cyWQ-kfda4Hg30hE0EWxE8k4U1IU0jlwXw7gw2WE1a83hw10G0te1sw17-06LE',
    '__hblp': '014u0iS0Co0jlwXw7gw49xi0j20CE1a8e82oxm0QE7OeG0a1x20Po2pwqU5O0vG0jK0k2u10xW0ii3Oew865o0NK0zE2Gw',
    '__sjsp': 'gSg2cyWQ-kpsqQEiJ0c16w2zG6wxgjw',
    '__comet_req': '15',
    'lsd': 'AdFAZc32Q1g',
    'jazoest': '2823',
    '__spin_r': '1030403648',
    '__spin_b': 'trunk',
    '__spin_t': '1764242970',
    'qpl_active_flow_ids': '175125627',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'useCDSWebLoginMutation',
    'server_timestamps': 'true',
    'variables': json.dumps({
        "input": {
            "client_mutation_id": "1",
            "actor_id": "0",
            "app": "facebook",
            "auth_domain_data_key": None,
            "caa_login_request_extra_info": {
                "ab_test_data": "/AKAKVqAfKKAAKAAAAAAAAAAAAAAAAAKAAAAAAAAPvP/v/PfPAKAAA",
                "shared_prefs_data": "eyIzMDAwMCI6W3sidCI6MTc2NDI0Mjk3MS40MzEsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi8ifSwidiI6ZmFsc2V9XSwiMzAwMDEiOlt7InQiOjE3NjQyNDI5NzEuNDMyLCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4vIn0sInYiOjJ9XSwiMzAwMDIiOlt7InQiOjE3NjQyNDI5NzEuNDMyLCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4vIn0sInYiOjJ9XSwiMzAwMDMiOlt7InQiOjE3NjQyNDI5NzEuNDMyLCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4vIn0sInYiOlsiZW4tVVMiLCJlbiJdfV0sIjMwMDA0IjpbeyJ0IjoxNzY0MjQyOTcxLjQzMiwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luLyJ9LCJ2IjoyMDB9XSwiMzAwMDUiOlt7InQiOjE3NjQyNDI5NzEuNDMyLCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4vIn0sInYiOnsidyI6MTM2NiwiaCI6NjQxfX1dLCIzMDAwNyI6W3sidCI6MTc2NDI0Mjk3MS40MzIsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi8ifSwidiI6ImRlbmllZCJ9XSwiMzAwMDgiOlt7InQiOjE3NjQyNDI5NzEuNDQxLCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4vIn0sInYiOiJkZW5pZWQifV0sIjMwMDEyIjpbeyJ0IjoxNzY0MjQyOTcxLjQzMywiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luLyJ9LCJ2IjoiR29vZ2xlIEluYy4ifV0sIjMwMDEzIjpbeyJ0IjoxNzY0MjQyOTcxLjQzMywiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luLyJ9LCJ2IjoiNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMzkuMC4wLjAgU2FmYXJpLzUzNy4zNiJ9XSwiMzAwMTUiOlt7InQiOjE3NjQyNDI5NzEuNDMzLCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4vIn0sInYiOiJXaW4zMiJ9XSwiMzAwMTgiOlt7InQiOjE3NjQyNDI5NzEuNDMzLCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4vIn0sInYiOjh9XSwiMzAwMjIiOlt7InQiOjE3NjQyNDI5NzEuNDQsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi8ifSwidiI6dHJ1ZX1dLCIzMDA0MCI6W3sidCI6MTc2NDI0Mjk3MS40NCwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luLyJ9LCJ2IjotMzMwfV0sIjMwMDkzIjpbeyJ0IjoxNzY0MjQyOTcxLjQ0LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4vIn0sInYiOjB9XSwiMzAwOTQiOlt7InQiOjE3NjQyNDI5NzEuNDQsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi8ifSwidiI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMzkuMC4wLjAgU2FmYXJpLzUzNy4zNiJ9XSwiMzAwOTUiOlt7InQiOjE3NjQyNDI5NzEuNDQsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi8ifSwidiI6Mn1dLCIzMDEwNiI6W3sidCI6MTc2NDI0Mjk3MS40MzEsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi8ifSwidiI6ZmFsc2V9LHsidCI6MTc2NDI0Mjk5NC4yOTksImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi8ifSwidiI6dHJ1ZX1dLCIzMDEwNyI6W3sidCI6MTc2NDI0Mjk3MS40MzEsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi8ifSwidiI6ZmFsc2V9XX0=",
            "cuid": "",
            "guid": "f2546b690d3f51ff3",
            "jazoest": "2814",
            "lgndim": "eyJ3IjoxMzY2LCJoIjo3NjgsImF3IjoxMzY2LCJhaCI6NzI4LCJjIjoyNH0=",
            "lgnjs": "1764242971",
            "lgnrnd": "032930_RTea",
            "locale": "en_GB",
            "login_source": "comet_headerless_login",
            "lsd": "AdFAZc323lA",
            "next": "",
            "prefill_contact_point": "",
            "prefill_source": "",
            "prefill_type": "",
            "skstamp": "",
            "timezone": "-330"
        },
        "credential_type": "password",
        "dyi_job_id": "",
        "enc_password": {
            "sensitive_string_value": "#PWD_BROWSER:5:1764243049:AahQAJSagtjx7zqD95KwNpEfweyKPmA/rA9OBmO1aYzWTXsO/LOmLCWXVUAD/+oM8tGhg+PlhcDAF8bfHn3M06yCQ8knfLnTlVk0ezZD0sdkAZ6OBjIU8TJI017jVfBazn8UpT/L557lz7xEQps18G4CkQI9M9UOnw=="
        },
        "event_request_id": "74d4a096-a851-4a2b-ab2f-097d0c550b37",
        "identifier": "61562871116780",
        "ig_web_device_id": None,
        "initial_request_id": "1",
        "lids": None,
        "login_source": "LOGIN",
        "next": None,
        "passkey_payload": None,
        "password": {
            "sensitive_string_value": "#PWD_BROWSER:5:1764243049:AahQAJSagtjx7zqD95KwNpEfweyKPmA/rA9OBmO1aYzWTXsO/LOmLCWXVUAD/+oM8tGhg+PlhcDAF8bfHn3M06yCQ8knfLnTlVk0ezZD0sdkAZ6OBjIU8TJI017jVfBazn8UpT/L557lz7xEQps18G4CkQI9M9UOnw=="
        },
        "persistent": True,
        "query_params": None,
        "trusted_device_records": "{}",
        "use_uid_to_login": False,
        "waterfall_id": "4f83c4b0-b799-4e08-b385-8e67729f2ba9"
    }),
    'doc_id': '25351082227851825',
    'fb_api_analytics_tags': '["qpl_active_flow_ids=175125627"]',
}

response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)

print("Status code:", response.status_code)
print("Response URL:", response.url)
print("Status Code:", response.status_code)
print("Reason:", response.reason)
print("Response Text:", response.text)
print("\n--- RESPONSE COOKIES ---")
if response.cookies:
    for k, v in response.cookies.get_dict().items():
        print(f"{k} = {v}")
else:
    print("No cookies set by server")



