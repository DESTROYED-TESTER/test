import requests

session = requests.Session()

cookies = {
    'datr': 'wDF1aOt9UdNuCskTeplHs7Yx',
    'ig_did': '534026BE-B655-4318-AB86-5CFD617D4D50',
    'mid': 'aHUxwQALAAEhOjO5lKEpzt85Xu9g',
    'ig_nrcb': '1',
    'ps_l': '1',
    'ps_n': '1',
    'wd': '1155x773',
    'rur': '"CCO\\05479957305321\\0541797856743:01fe07c54e37147ebbc67f3a7ff89858d9e72fa0e96320c926f32037994497420ca612e6"',
    'csrftoken': 'jzo24auvRRTr2iTuPDhMNcWMvbRVPQNr',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7,hi;q=0.6,gu;q=0.5,bn;q=0.4',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.instagram.com',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/?flo=true',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="143.0.7499.147", "Chromium";v="143.0.7499.147", "Not A(Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'x-asbd-id': '359341',
    'x-csrftoken': 'jzo24auvRRTr2iTuPDhMNcWMvbRVPQNr',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR0ZBluzE5eab1oDGWSBU1s4d6pzUESqf9_kO8JTPMBUVa5I',
    'x-instagram-ajax': '1031378256',
    'x-requested-with': 'XMLHttpRequest',
    'x-web-session-id': 'xwu66r:r3cl82:m1ree6',
    # 'cookie': 'datr=wDF1aOt9UdNuCskTeplHs7Yx; ig_did=534026BE-B655-4318-AB86-5CFD617D4D50; mid=aHUxwQALAAEhOjO5lKEpzt85Xu9g; ig_nrcb=1; ps_l=1; ps_n=1; wd=1155x773; rur="CCO\\05479957305321\\0541797856743:01fe07c54e37147ebbc67f3a7ff89858d9e72fa0e96320c926f32037994497420ca612e6"; csrftoken=jzo24auvRRTr2iTuPDhMNcWMvbRVPQNr',
}

data = {
    'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1766320757:Aa9QAPfLbN88u/LgEpAzt8Fshi7IJFEM545thZfwQe9F4M8OfogTaHUf5MZw4dbOw769J8AmnL1nUWMw/++guiPkK3+jnEXCJkt0PmoRCtCqb1CKShghVXRD+4fHM9t2wv5BYVVNMdZkz4n6Uw==',
    'caaF2DebugGroup': '0',
    'isPrivacyPortalReq': 'false',
    'loginAttemptSubmissionCount': '0',
    'optIntoOneTap': 'false',
    'queryParams': '{"flo":"true"}',
    'trustedDeviceRecords': '{}',
    'username': 'sumonh44',
    'jazoest': '22898',
}

response = session.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', cookies=cookies, headers=headers, data=data)

wanted = ["sessionid", "csrftoken", "ds_user_id"]
all_cookies = session.cookies.get_dict()

extracted = {k: all_cookies[k] for k in wanted if k in all_cookies}
print(extracted)

# Instagram-style cookie string
cookie_str = "; ".join(f"{k}={v}" for k, v in extracted.items())
print(cookie_str)
