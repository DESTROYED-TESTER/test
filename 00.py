import requests
import time
import re
Session = requests.Session()

head = {"authority": "m.prod.facebook.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "dpr": "3",
            "sec-ch-prefers-color-scheme": "light",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0',
            "viewport-width": "980"}
response2 = Session.get('https://limited.facebook.com')

url = 'https://limited.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100'

headers = {
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://limited.facebook.com/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'X-Response-Format': 'JSONStream',
    'sec-ch-ua-mobile': '?1',
    'X-ASBD-ID': '359341',
    'X-FB-LSD': 'iK-keICulHM0IodUqvXHV_',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
}


data = {
    'm_ts': '1784135433',
    'li': 'Cb9XavaIo6kZl89eYYR7aE4g',
    'try_number': '1',
    'unrecognized_tries': '0',
    'email': '9907228129',
    'prefill_contact_point': '9907228129',
    'prefill_source': 'browser_dropdown',
    'prefill_type': 'password',
    'first_prefill_source': 'browser_dropdown',
    'first_prefill_type': 'contact_point',
    'had_cp_prefilled': 'true',
    'had_password_prefilled': 'true',
    'is_smart_lock': 'false',
    'bi_xrwh': '0',
    'encpass': '%23PWD_BROWSER%3A5%3A1784135522%3AAY1QACngqdeszC5n4ZUSC5hqOMVAhq0yr3Ysh9udx6Ju9c9lrHI5Y99eRox5TeOPLlWLLbI3xqJZOVV9FeO5TGicYGdm9Lhczvm70%2FciCV9OEr3MesmC4nAT9RmA5vV0aJCux5eEJeps3iQNLnI%3D',
    'bi_wvdp': '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
    'fb_dtsg': 'bfeHqxOqpJw=',
    'jazoest': '21164',
    'lsd': 'iK-keICulHM0IodUqvXHV_',
    '__dyn': '1KQdAG1mws8-t0BBBzEnwSwgE98nwgU2owpUuwcC4o1nEhw23E52q1ewb60Y82Cwro0wa4o1MUaE36wdq0ny0oi0zE1jU1soG0hi0Lo6-0Co178dE1UU3jwea',
    '__csr': '',
    '__hsdp': '',
    '__hblp': '',
    '__sjsp': '',
    '__req': 'c',
    '__fmt': '1',
    '__a': 'AYw8lvLYydGQ_F-H3DyGh3DR3e3LhFzrnMUOgpQxwg2LdChSgtI_TfgIzIlcmKpokOXoFsqvFVW7AYg3KT5JY7JMXnt2woebTWA',
    '__user': '0'
}

response = Session.post(url, headers=headers, data=data)

print(response.status_code)
print(response.text)
# Check login success
log_cookies = Session.cookies.get_dict().keys()
if "c_user" in log_cookies:
    print('\033[1;92m OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK ')
