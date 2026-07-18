import requests
import time
import re
Session = requests.Session()

head = {"authority":"m.prod.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","accept-language":"en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7","cache-control":"max-age=0","dpr":"3","sec-ch-prefers-color-scheme":"light","sec-fetch-dest":"document","sec-fetch-mode":"navigate","sec-fetch-site":"none","sec-fetch-user":"?1","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0","viewport-width":"980"}
requu1 = Session.get('https://m.prod.facebook.com/',headers=head)
datr = requu1.cookies.get('datr')
sb = requu1.cookies.get('sb')
fr = requu1.cookies.get('fr')
data = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(requu1.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(requu1.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': uid, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': '0', 'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw), 'bi_wvdp': '', 'fb_dtsg': '', 'jazoest': re.search('name="jazoest" value="(.*?)"',str(requu1.text)).group(1), 'lsd': re.search('name="lsd" value="(.*?)"',str(requu1.text)).group(1), '__dyn': '', '__csr': '', '__req': random.choice(["1","2","3","4","5","6","7","8","9","0"]), '__fmt': '0', '__a': '',  '__user': '0'}
cookies = {
    "datr": datr,
    "sb": sb,
    "m_pixel_ratio": "2.75",
    "wd": "393x851",
    "fr": fr,
}
url = "https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; M2010J19SI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    "sec-ch-ua-mobile": "?1",
    "x-response-format": "JSONStream",
    "x-fb-lsd": "AdSJgVEeaG-HDOhvnYZ0anTTqW4",
    "x-requested-with": "XMLHttpRequest",
    "x-asbd-id": "359341",
    "sec-ch-ua-platform": '"Android"',
    "origin": "https://limited.facebook.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://limited.facebook.com/login/",
    "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
}


response = Session.post(url, headers=headers, cookies=cookies, data=data)
print(cookies)
#print(response.status_code)
#print(response.text)
# Check login success
log_cookies = Session.cookies.get_dict().keys()
if "c_user" in log_cookies:
    print('\033[1;92m OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK ')
