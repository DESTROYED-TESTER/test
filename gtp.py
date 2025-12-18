import requests
import json

print("🔄 FACEBOOK RE-LOGIN ATTEMPT")
print("=" * 40)

# Load previous cookies
with open('facebook_cookies.json', 'r') as f:
    old_cookies = json.load(f)

print("🍪 Previous cookies loaded")
print(f"   User ID: {old_cookies.get('c_user', 'Not found')}")

# Login request with same credentials
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
    'referer': 'https://www.messenger.com/?locale=en_US',
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
    session = requests.Session()
    session.cookies.update(cookies)
    
    response = session.post('https://www.messenger.com/login/password/', headers=headers, data=data)
    
    print(f"📊 Status: {response.status_code}")
    print(f"🔗 Final URL: {response.url}")
    
    # Extract new cookies
    new_cookies = requests.utils.dict_from_cookiejar(session.cookies)
    
    print("\n🍪 NEW FACEBOOK LOGIN COOKIES:")
    print("=" * 40)
    
    for name, value in new_cookies.items():
        if name in ['c_user', 'xs', 'sb', 'datr']:
            print(f"✅ {name}: {value}")
        else:
            print(f"   {name}: {value}")
    
    # Save new cookies
    with open('facebook_cookies_new.json', 'w') as f:
        json.dump(new_cookies, f, indent=2)
    
    # Create curl format
    curl_format = "; ".join([f"{k}={v}" for k, v in new_cookies.items()])
    with open('facebook_cookies_new_curl.txt', 'w') as f:
        f.write(curl_format)
    
    print(f"\n💾 Saved to: facebook_cookies_new.json")
    print(f"📋 Curl format: facebook_cookies_new_curl.txt")
    
    # Check if login successful
    if 'c_user' in new_cookies:
        print(f"\n🎉 LOGIN SUCCESSFUL!")
        print(f"👤 User ID: {new_cookies['c_user']}")
    else:
        print(f"\n❌ LOGIN FAILED!")
    
except Exception as e:
    print(f"❌ ERROR: {e}")
