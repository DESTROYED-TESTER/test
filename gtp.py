import requests,time
Session = requests.Session()
cookies = {
    'datr': 'QeKNaUGL6JReD3XKEE0QEpw3',
    'sb': 'etcGaeXQAhgH5N9EXJxlkrgM',
    'ps_l': '1',
    'ps_n': '1',
    'fr': '1HjGayH6x3Ok5PKBf.AWc5oQE5b2xqgvT0wO6m_RK5Q4dqB4s2sd6hBtvzD9m2AkMyZQc.BphwUz..AAA.0.0.Bpq7BU.AWc_wgUyR-DiNfCb61JcUziTT8A',
    'wd': '1136x773',
    'locale': 'en_GB',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'dpr': '1',
    'origin': 'https://www.facebook.com',
    'priority': 'u=0, i',
    'referer': 'https://www.facebook.com/facebook/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-full-version-list': '"Not;A=Brand";v="99.0.0.0", "Google Chrome";v="139.0.7258.139", "Chromium";v="139.0.7258.139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'viewport-width': '1136',
    # 'cookie': 'datr=QeKNaUGL6JReD3XKEE0QEpw3; sb=etcGaeXQAhgH5N9EXJxlkrgM; ps_l=1; ps_n=1; fr=1HjGayH6x3Ok5PKBf.AWc5oQE5b2xqgvT0wO6m_RK5Q4dqB4s2sd6hBtvzD9m2AkMyZQc.BphwUz..AAA.0.0.Bpq7BU.AWc_wgUyR-DiNfCb61JcUziTT8A; wd=1136x773; locale=en_GB',
}

params = {
    'login_attempt': '1',
}

data = {
    'email': '100068373534275',
    'cuid': '',
    'guid': 'f26a6b52fe26838f9',
    'lgnjs': '1772952835',
    'lgnrnd': '225350_Kmyx',
    'locale': 'en_GB',
    'login_source': 'comet_login_header',
    'next': 'https://www.facebook.com/facebook/',
    'skstamp': '',
    'timezone': '-330',
    'prefill_contact_point': '',
    'prefill_source': '',
    'lsd': 'AdR3xKrdycBYAeO3Mdb7UwKgheQ',
    'jazoest': '22376',
    'lgndim': 'eyJ3IjoxNDQwLCJoIjo5MDAsImF3IjoxNDQwLCJhaCI6ODYwLCJjIjoyNH0=',
    'ab_test_data': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
    'seo_visit_from_session': '1',
    'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0],'soumyadip123'),
}

response = Session.post(
    'https://www.facebook.com/login/device-based/regular/login/',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
log_cookies = Session.cookies.get_dict().keys()
if "checkpoint" in log_cookies:
  print(log_cookies)
else:
   print("gud")
