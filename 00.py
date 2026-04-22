import requests
import time
Session = requests.Session()

import requests

url = "https://limited.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"

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
    "datr": "gInoaXuWGJqxvHs2O0xvwWA-",
    "sb": "iInoaUeweC7RC3qUJVB1odJ0",
    "m_pixel_ratio": "2.75",
    "wd": "393x851",
    "fr": "0QYJOzT2T4bYtWUTw..Bp6ImA..AAA.0.0.Bp6Imo.AWfPEW7kbLdLKeVFD9e9xUKO104",
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
    "encpass": "#PWD_BROWSER:5:1776847274:ATpQAIFHbpCo3DiUMJV6o3fMoQ8jBlQdQAk0/DfW5e4PAZgdcgCeeNBx63crxoltfl9bet9bCP2wkbZFt5zr975yNI2VdpDCT90lKjWVJ5wC5MdH19XCLHrnd9s5iZMU4QxYcr42BbM2Nev1Sg==",
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
