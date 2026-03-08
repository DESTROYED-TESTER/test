import requests

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.facebook.com',
    'Referer': 'https://www.facebook.com/facebook/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'dpr': '1',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-full-version-list': '"Not;A=Brand";v="99.0.0.0", "Google Chrome";v="139.0.7258.139", "Chromium";v="139.0.7258.139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'viewport-width': '1136',
}

params = {
    'login_attempt': '1',
}

data = {
    'email': '100069889795658',
    'cuid': '',
    'guid': 'fe7c9ad27486757c4',
    'lgnjs': '1772949169',
    'lgnrnd': '215248_5sPy',
    'locale': 'en_GB',
    'login_source': 'comet_login_header',
    'next': 'https://www.facebook.com/facebook/',
    'skstamp': '',
    'timezone': '-330',
    'prefill_contact_point': '',
    'prefill_source': '',
    'lsd': 'AdR3xKrdycBYAeO3Mdb7UwKg9AY',
    'jazoest': '22301',
    'lgndim': 'eyJ3IjoxNDQwLCJoIjo5MDAsImF3IjoxNDQwLCJhaCI6ODYwLCJjIjoyNH0=',
    'ab_test_data': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
    'encpass': '#PWD_BROWSER:5:1772949202:AQ1QAC3SoMlbwtWK6vcSjXsRD6T8bZZ4wNYVbgxP+KQVKapai2iiDNhBwQyt/vhx9zh6T2ENqY31N0unRP4SRSfReTpeGW0X7EgQzwRRfAHT+g6wB2a3JgPKakdR28YSUkcOvUzUlPJgXaMg',
}

response = requests.post('https://www.facebook.com/login/device-based/regular/login/', params=params, headers=headers, data=data)
print(response.text)
