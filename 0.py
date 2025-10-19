import requests,time

cookies = {
    'fr': '0yNyOdBia7SurAz5e..Bo9J-7..AAA.0.0.Bo9J-7.AWcpcPtzmuPsw5P6FNpwX8Zx-Tw',
    'sb': 'u5_0aFF51EbifVBDoEnsi9Ut',
    'datr': 'u5_0aCroimhveeODthgePFtZ',
    'dpr': '2.4749999046325684',
    'wd': '980x1146',
}

headers = {
    'authority': 'www.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'fr=0yNyOdBia7SurAz5e..Bo9J-7..AAA.0.0.Bo9J-7.AWcpcPtzmuPsw5P6FNpwX8Zx-Tw; sb=u5_0aFF51EbifVBDoEnsi9Ut; datr=u5_0aCroimhveeODthgePFtZ; dpr=2.4749999046325684; wd=980x1146',
    'dpr': '2.4749999046325684',
    'origin': 'https://www.facebook.com',
    'referer': 'https://www.facebook.com/Facebookids',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Chromium";v="107.0.5304.74", "Not=A?Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'viewport-width': '980',
}

params = {
    'login_attempt': '1',
}

data = {
    'email': '06301466463',
    'cuid': '',
    'guid': 'f0a5a0c737fcfe167',
    'lgnjs': '1760862174',
    'lgnrnd': '012253_q6Bs',
    'locale': 'en_GB',
    'login_source': 'comet_login_header',
    'next': 'https://www.facebook.com/Facebookids',
    'skstamp': '',
    'timezone': '-330',
    'prefill_contact_point': '',
    'prefill_source': '',
    'lsd': 'AdFiLirodjc',
    'jazoest': '21051',
    'lgndim': 'eyJ3Ijo0MzcsImgiOjk3MywiYXciOjQzNywiYWgiOjk3MywiYyI6MjR9',
    'ab_test_data': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAI',
    'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], '630153'),
}

response = requests.post(
    'https://www.facebook.com/login/device-based/regular/login/',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
    allow_redirects=False
)

# Simple check
if 'c_user' in response.cookies and 'xs' in response.cookies:
    print("✅ Login Successful!")
    print(f"User ID: {response.cookies['c_user']}")
else:
    print("❌ Login Failed")
    print(response)
