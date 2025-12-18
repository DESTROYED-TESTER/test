import requests
import json

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
    # Create a session to maintain cookies
    session = requests.Session()
    session.cookies.update(cookies)
    
    response = session.post('https://www.messenger.com/login/password/', headers=headers, data=data)
    
    print("=" * 60)
    print("FACEBOOK LOGIN RESPONSE ANALYSIS")
    print("=" * 60)
    
    print(f"Status Code: {response.status_code}")
    print(f"URL: {response.url}")
    
    # Check if login was successful by looking for redirects or content
    if response.history:
        print(f"\nRedirects occurred:")
        for resp in response.history:
            print(f"  {resp.status_code} -> {resp.url}")
        print(f"Final destination: {response.url}")
    
    # Extract all cookies from the session
    print(f"\nSession Cookies:")
    session_cookies = session.cookies
    if session_cookies:
        for cookie in session_cookies:
            print(f"  {cookie.name}: {cookie.value[:50]}{'...' if len(cookie.value) > 50 else ''}")
    else:
        print("  No cookies found in session")
    
    # Convert to different formats
    cookies_dict = requests.utils.dict_from_cookiejar(session_cookies)
    cookies_string = requests.utils.dict_from_cookiejar(session_cookies)
    
    print(f"\nCookies as Dictionary:")
    print(json.dumps(cookies_dict, indent=2))
    
    # Save cookies to file for future use
    with open('facebook_cookies.json', 'w') as f:
        json.dump(cookies_dict, f, indent=2)
    print(f"\nCookies saved to 'facebook_cookies.json'")
    
    # Save cookies as curl format for easy copying
    curl_cookies = "; ".join([f"{k}={v}" for k, v in cookies_dict.items()])
    with open('facebook_cookies_curl.txt', 'w') as f:
        f.write(curl_cookies)
    print(f"Cookies saved in curl format to 'facebook_cookies_curl.txt'")
    print(f"Curl format: {curl_cookies[:100]}{'...' if len(curl_cookies) > 100 else ''}")
    
    # Check response content for login indicators
    if 'home' in response.url.lower() or 'messages' in response.url.lower():
        print(f"\n✅ Login appears SUCCESSFUL!")
    else:
        print(f"\n❌ Login may have failed or requires additional verification")
        print(f"Final URL: {response.url}")
    
    # Show part of the response content for debugging
    print(f"\nResponse Content Preview (first 500 chars):")
    print(response.text[:500])
    
except requests.exceptions.RequestException as e:
    print(f"❌ Network Error: {e}")
except Exception as e:
    print(f"❌ Unexpected Error: {e}")
    import traceback
    traceback.print_exc()
