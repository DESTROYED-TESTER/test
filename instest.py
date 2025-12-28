import hashlib
import uuid
import time
import requests
import random
import urllib.parse
username = 'sumonh44'
passwd = 'sumon@12M'
useragent = 'Mozilla/5.0 (Linux; Android 12; SKY PAD10 Build/S00812; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/141.0.7390.122 Safari/537.36 Instagram 406.0.0.58.159 Android (31/12; 200dpi; 1280x740; Sky Devices/SKY; SKY PAD10; SKY_PAD10; ums312_2h10; en_US; 822917963; IABMV/1)'
## Create an MD5 hash for the username and password
session = requests.Session()

headers = {
    'x-instagram-ajax': '0',
    'sec-ch-ua-platform': '"Windows"',
    'x-csrftoken': 'RhEmFDtIqpnOqzcRw3ZS6A',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="143.0.7499.170", "Chromium";v="143.0.7499.170", "Not A(Brand";v="24.0.0.0"',
    'Referer': 'https://www.threads.com/login',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-mobile': '?0',
    'x-ig-app-id': '238260118697367',
    'x-asbd-id': '359341',
    'x-bloks-version-id': '11e8fa4e266f93b1e8d4bea36f35069667b775acf94d6996c23f6a5175d24494',
    'sec-ch-prefers-color-scheme': 'dark',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'sec-ch-ua-platform-version': '"10.0.0"',
}

data = {
    'can_threads_signup_with_ig': 'false',
    'enc_password': '#PWD_BROWSER:10:1766686387:AbdQAKqDlw1Ro99mGKpiWMuDfkoLOQcO5JDRmj/jMWs0wqUyxET4okNc6fOSt+YdOm9dxmphSCTwW5+WmkROurG/Dwnmi4dZ4lXNwKEKwBWq9NWX9k0A7ncM+QMTlWb1HIhp13y9t9/+KslZdQ==',
    'optIntoOneTap': 'false',
    'queryParams': '{}',
    'stopDeletionNonce': '',
    'textAppStopDeletionToken': '',
    'username': 'sumonh44',
    'jazoest': '21983',
}

response = session.post('https://www.threads.com/api/v1/web/accounts/login/ajax/', headers=headers, data=data)

    ## Check if login was successful
wanted = ["ds_user_id", "sessionid"]
all_cookies = session.cookies.get_dict()
extracted = {k: all_cookies[k] for k in wanted if k in all_cookies}
cookie_str = "; ".join(f"{k}={v}" for k, v in extracted.items())
print("Cookies:", cookie_str)
print(response.text)
