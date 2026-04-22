import requests
import time
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
response = Session.get('https://www.facebook.com/login',headers=head)
datr = response.cookies.get('datr')
sb = response.cookies.get('sb')
fr = response.cookies.get('fr')
url = "https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"

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

cookies = {
    "datr": datr,
    "sb": sb,
    "m_pixel_ratio": "2.75",
    "wd": "393x851",
    "fr": fr,
}

data = {
    "m_ts": "1776847240",
    "li": "iInoaUeC-fKxXMoj2g1DhteN",
    "try_number": "0",
    "unrecognized_tries": "0",
    "email": "bithikasumon81@gmail.com",
    "prefill_contact_point": "bithikasumon81@gmail.com",
    "prefill_source": "browser_dropdown",
    "prefill_type": "contact_point",
    "first_prefill_source": "browser_dropdown",
    "first_prefill_type": "contact_point",
    "had_cp_prefilled": "true",
    "had_password_prefilled": "false",
    "is_smart_lock": "false",
    "bi_xrwh": "0",
    "bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
    "encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], 'sumon@12M'),
    "fb_dtsg": "NAfsfb_rRUK1j8xFoiAUrWhu_BKjct4Ic-TBEHU19VbowNsaWe4Hcag:0:0",
    "jazoest": "25035",
    "lsd": "AdSJgVEeaG-HDOhvnYZ0anTTqW4",
    "dyn": "1KQdAG1mws8-t0BBBzEnwuo98nwgU2owpUuwcC4o1nEhw23E52q1ewb60Y82Cwro0wa4o1MUaE36wdq0ny0oi0zE1jU1soG0hi0Lo6-0Co178dE1UU3jwGwbu",
    "csr": "",
    "hsdp": "",
    "hblp": "",
    "sjsp": "",
    "req": "5",
    "fmt": "1",
    "a": "AYyfLpBu5achetlX00INO5Qb-dC_HCzf5HpaqdSNxtCol1NACQ9pj5LesUA4hsAU2-iBu36gNbh8uE_qvzKIC2khJKVeM7RacPE",
    "__user": "0",
}

response = Session.post(url, headers=headers, cookies=cookies, data=data)

print(response.status_code)
print(response.text)
# Check login success
log_cookies = Session.cookies.get_dict().keys()
if "c_user" in log_cookies:
    print('\033[1;92m OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK ')
