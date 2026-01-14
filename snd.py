import requests

import requests

cookies = {
    'datr': 'Eitnac9Jr55lMaaETcsXwk3D',
    'sb': 'EitnaZzbPfbccAsuj6eJIYfE',
    'ps_l': '1',
    'ps_n': '1',
    'wd': '885x773',
    'fr': '0DBxBjQV9WtPFwBoS..BpZysS..AAA.0.0.BpZztO.AWfGeKdmKj0jFW8rYpsnEF6YsKo',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.facebook.com',
    'priority': 'u=1, i',
    'referer': 'https://www.facebook.com/login/identify/?ctx=recover&from_login_screen=0',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="143.0.7499.170", "Chromium";v="143.0.7499.170", "Not A(Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'x-asbd-id': '359341',
    'x-fb-lsd': 'AdEWFxxwPB8',
    # 'cookie': 'datr=Eitnac9Jr55lMaaETcsXwk3D; sb=EitnaZzbPfbccAsuj6eJIYfE; ps_l=1; ps_n=1; wd=885x773; fr=0DBxBjQV9WtPFwBoS..BpZysS..AAA.0.0.BpZztO.AWfGeKdmKj0jFW8rYpsnEF6YsKo',
}

params = {
    'ctx': 'recover',
}

data = {
    'jazoest': '2952',
    'lsd': 'AdEWFxxwPB8',
    'email': '8101729293',
    'did_submit': '1',
    '__user': '0',
    '__a': '1',
    '__req': '5',
    '__hs': '20467.BP:DEFAULT.2.0...0',
    'dpr': '1',
    '__ccg': 'GOOD',
    '__rev': '1031974328',
    '__s': 'kfnkhv:t1mczh:hk6em3',
    '__hsi': '7595108429310200628',
    '__dyn': '7xeUmwkHg7ebwKBAg5S1Dxu13wqovzEdEc8uxa0CEbo1nEhw2nVE4W0qa0FE2awt81s8hwGwQw4iwBgao6C0Mo2swaO4U2zxe3C0D85a1qw8Xxm16wa-0raazo7u0zE2ZwrU6C0hq1Iw5lwnqwIwtU5K0UE62',
    '__hsdp': 'gIMggq8yqAy8F8O948QDQoKUyUYx4cyEcm7Uqg29wIym0TE2pwrQl0bfwfu',
    '__hblp': '0Uwau1kw6Pw4Uw6_wde0anwsE0uPw6Fw1N-04OAHCw0oxo2Mw1jO8VUeU0KF01s-046o1xE',
    '__spin_r': '1031974328',
    '__spin_b': 'trunk',
    '__spin_t': '1768373984',
}


try:
    response = requests.get(
    'https://www.facebook.com/ajax/login/help/identify.php',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
    
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        print("✓ SMS code page loaded")
        print(response.text)
    else:
        print(f"✗ Failed: {response.status_code}")
        
except Exception as e:
    print(f"✗ Error: {e}")
