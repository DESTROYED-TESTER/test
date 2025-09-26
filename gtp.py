import requests

cookies = {
    'datr': '7DnMaEaBSi1euh0ZrTxnFPXZ',
    'sb': '7DnMaMKotlR75LUbGLYU-TYB',
    'm_pixel_ratio': '2.4749999046325684',
    'ps_l': '1',
    'ps_n': '1',
    'pas': '100056503155212%3AfxOzQdbFmo',
    'dpr': '2.4749999046325684',
    'wd': '437x973',
    'fr': '02n8peqk75hF9D13g.AWcYnHXf1GZF8b7MXvQBW4q05cEXwaTcJhJCnUnlt93z2xfY_YY.BozDns..AAA.0.0.Bo1hLI.AWcm2HkPoopHsJCgNGiCAIgqHgw',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 13; V2060 Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.155 Mobile Safari/537.36',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/x-www-form-urlencoded',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Android WebView";v="140"',
    'x-response-format': 'JSONStream',
    'sec-ch-ua-mobile': '?1',
    'x-asbd-id': '359341',
    'x-fb-lsd': 'AdEVi-OFg_s',
    'x-requested-with': 'XMLHttpRequest',
    'origin': 'https://limited.facebook.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://limited.facebook.com/login.php?skip_api_login=1&api_key=1393952984244777&kid_directed_site=0&app_id=1393952984244777&signed_next=1&next=https://m.facebook.com/v16.0/dialog/oauth?app_id=1393952984244777&cbt=1758859215730&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfedd56e5da955addb%26domain%3Dwww.boomplay.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.boomplay.com%252Ff8911011906172fa2%26relation%3Dopener&client_id=1393952984244777&display=touch&domain=www.boomplay.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fwww.boomplay.com%2Fsongs%2F216051730&locale=en_US&logger_id=fb5ecf6aa44bb1de3&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df9bf310860cbd212d%26domain%3Dwww.boomplay.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.boomplay.com%252Ff8911011906172fa2%26relation%3Dopener%26frame%3Dfb8a321b81d3ff397&response_type=token%2Csigned_request%2Cgraph_domain&sdk=joey&version=v16.0&ret=login&fbapp_pres=0&tp=unspecified&cancel_url=https://staticxx.facebook.com/x/connect/xd_arbiter/?version=46',
    'accept-language': 'en-US,en;q=0.9',
    'priority': 'u=1, i',
    # 'Cookie': 'datr=7DnMaEaBSi1euh0ZrTxnFPXZ; sb=7DnMaMKotlR75LUbGLYU-TYB; m_pixel_ratio=2.4749999046325684; ps_l=1; ps_n=1; pas=100056503155212%3AfxOzQdbFmo; dpr=2.4749999046325684; wd=437x973; fr=02n8peqk75hF9D13g.AWcYnHXf1GZF8b7MXvQBW4q05cEXwaTcJhJCnUnlt93z2xfY_YY.BozDns..AAA.0.0.Bo1hLI.AWcm2HkPoopHsJCgNGiCAIgqHgw',
}

params = {
    'api_key': '1393952984244777',
    'auth_token': '3ea524ab821dcb9e2140fbe35e5e09fd',
    'skip_api_login': '1',
    'signed_next': '1',
    'next': 'https://m.facebook.com/v16.0/dialog/oauth?app_id=1393952984244777&cbt=1758859978311&logger_id=2fb35fb5-cdb2-46af-8dc4-996548b0ec0b',
    'refsrc': 'deprecated',
    'app_id': '1393952984244777',
    'cancel': 'https://staticxx.facebook.com/x/connect/xd_arbiter/?version=46',
    'lwv': '100',
}

data = 'm_ts=1758859976&li=yBLWaNo3yCbGoJgrOxFDDjjk&try_number=0&unrecognized_tries=0&email=100056503155212&prefill_contact_point=100056503155212&prefill_source=browser_dropdown&prefill_type=password&first_prefill_source=browser_dropdown&first_prefill_type=contact_point&had_cp_prefilled=true&had_password_prefilled=true&is_smart_lock=false&bi_xrwh=92004344361786634&encpass=%23PWD_BROWSER%3A5%3A1758859991%3AAWpQAJ78nsELQ6oAmTKN60TUqyU3S%2B4pPGhmFdKL40ndAsgorMtdauIzLDtczxHxR4kOLhmbNJkWpCygokCpNw8PfXHkkW2FIuFOnkmliVxJMjoA4sCgle6XrNEM5RuiTcxtyzWenyCyqw%3D%3D&fb_dtsg=NAfup2Me3JHXJFN2yxBY35qKn-1LtNpMqJhQzaJ3AqYbs8PMFOvFhGw%3A0%3A0&jazoest=24862&lsd=AdEVi-OFg_s&_dyn=1KQdAG1mws8-t0BBBzEnwuo98nwgU2owpUuwcC4o1nEhw23E52q1ew6ywaq1Jw20Ehw73wGwcq0RE1u81x82ew5fw5NyE1582ZwrU2pw4swSw7zwde0UE&csr&hsdp&hblp&sjsp&req=1&fmt=1&a=AYrzCMozrxxEkLpLMe4Y2HjtqtsmVGwYzrN5JRYYClldhdPtYgFp1Jf_aTSnrZs9GEMJRGEqpBnp7Yr7bbjZFjK5_l3XCV2rjhwTOtu5o4lWwg&_user=0'

response = requests.post(
    'https://limited.facebook.com/login/device-based/login/async/',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
).text

print(response)
