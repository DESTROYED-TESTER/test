import requests,json,time


session = requests.Session()

cookies = {
    'datr': 'nkzTafyVQH5LzCTO5vvJ9H0O',
    'fr': '05JM1NKdAURcsnsVf.AWeLEYd-Wy_MpBRM-wpyz9HBtCXCe_HHs15Ns7uJz7y1ce3-cLU.BpAiwa..AAA.0.0.Bp00ye.AWetEDKaoeOCN8LSfX37esQ7af0',
    'sb': 'nkzTaYf6K76ZGssAj6WcFzrA',
    'wd': '1189x773',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'dpr': '1',
    'origin': 'https://www.facebook.com',
    'priority': 'u=0, i',
    'referer': 'https://www.facebook.com/dafword/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Google Chrome";v="145.0.7632.5", "Chromium";v="145.0.7632.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    'viewport-width': '1189',
    # 'cookie': 'datr=nkzTafyVQH5LzCTO5vvJ9H0O; fr=05JM1NKdAURcsnsVf.AWeLEYd-Wy_MpBRM-wpyz9HBtCXCe_HHs15Ns7uJz7y1ce3-cLU.BpAiwa..AAA.0.0.Bp00ye.AWetEDKaoeOCN8LSfX37esQ7af0; sb=nkzTaYf6K76ZGssAj6WcFzrA; wd=1189x773',
}

params = {
    'login_attempt': '1',
}

data = {
    'email': '61575467930154',
    'cuid': '',
    'guid': 'fde4bed090b04130f',
    'lgnjs': '1775455438',
    'lgnrnd': '230355_XxUa',
    'locale': 'en_GB',
    'login_source': 'comet_login_header',
    'next': 'https://www.facebook.com/dafword/',
    'skstamp': '',
    'timezone': '-330',
    'prefill_contact_point': '',
    'prefill_source': '',
    'lsd': 'AdQhqilliDPKo3UfE-WYRJybA14',
    'jazoest': '22292',
    'lgndim': 'eyJ3IjoxNDQwLCJoIjo5MDAsImF3IjoxNDQwLCJhaCI6ODYwLCJjIjozMn0=',
    'ab_test_data': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
    'seo_visit_from_session': '1',
    'encpass': '#PWD_BROWSER:5:1775455477:ASpQANmacctjqZ7MNMFFgrl/EAXlKab4v/3SmzNF44VuVeMZU57QYk5o8Am0Gr7BQ5MruugN15qHOlW8vFEWGEX/4FBXuv9oqTBz0BdeXJI/3DHc+j2qTdCa5rqZPKCQ5dO6kxgmw1r7Vf3FWw==',
}

response = session.post(
    'https://free.facebook.com/login/device-based/regular/login/',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
# Get cookies after request
cookie_dict = session.cookies.get_dict()

if "c_user" in cookie_dict:
    print("✅ Login success")
else:
    print("❌ Login failed")
