import requests

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

try:
    response = requests.post('https://www.messenger.com/login/password/', cookies=cookies, headers=headers, data=data)
    
    print(f"Status Code: {response.status_code}")
    print(f"Response Headers: {dict(response.headers)}")
    
    # Extract cookies from response
    response_cookies = response.cookies
    print("\nResponse Cookies:")
    for cookie in response_cookies:
        print(f"{cookie.name}: {cookie.value}")
    
    # Convert cookies to dictionary
    cookies_dict = requests.utils.dict_from_cookiejar(response_cookies)
    print(f"\nCookies Dictionary: {cookies_dict}")
    
except requests.exceptions.RequestException as e:
    print(f"Error making request: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
