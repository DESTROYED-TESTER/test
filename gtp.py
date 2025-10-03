import requests,time, io, struct, base64, re
import urllib.parse

# --- (use your existing headers/cookies/params/data) ---
cookies = {
    'datr': 'E2HfaC1esUHFUPm1LLzXx4Gg',
    'sb': 'E2HfaAojnK6mDputqTLHjbdf',
    'm_pixel_ratio': '2.4749999046325684',
    'wd': '437x973',
    'fr': '0t3Dqio7YRHpb2kNK..Bo32ET..AAA.0.0.Bo32G3.AWcxwMvmgZxYDvgeMA13kMqTeMU',
}  # keep your dict as in your snippet
headers = 
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; V2060 Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.7390.43 Mobile Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": "application/x-www-form-urlencoded",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-ch-ua": "\"Android WebView\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
    "x-response-format": "JSONStream",
    "sec-ch-ua-mobile": "?1",
    "x-asbd-id": "359341",
    "x-fb-lsd": "AdG4MaF1lMY",
    "x-requested-with": "XMLHttpRequest",
    "origin": "https://limited.facebook.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://limited.facebook.com/",
    "accept-language": "en-US,en;q=0.9",
    "priority": "u=1, i",
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
    # same as your snippet
url_params =  {
    "m_ts": "1759469883",
    "li": "O2HfaLAo7bVGvZPQG82c0rCz",
    "try_number": "0",
    "unrecognized_tries": "1",
    "email": "100043514448161",
    "prefill_contact_point": "",
    "prefill_source": "",
    "prefill_type": "",
    "first_prefill_source": "",
    "first_prefill_type": "",
    "had_cp_prefilled": "false",
    "had_password_prefilled": "false",
    "is_smart_lock": "false",
    "bi_xrwh": "92004344361786634",
    "encpass": "#PWD_BROWSER:5:1759470013:AXFQAFR+m6xV60t/daao75mDiksRllns3FmiwDtPgkmfqwdBora2bvBxEcEjOmVJhqkf3GeHgd65YGmKQWY5lnzoS0nkSTNb9lS9z+CR0QGGQ6r8GLu3N5HHdqpa8USptdrWVvYUq2uVUQ==",
    "fb_dtsg": "NAfuectLGHfYX-RmiH8_hDi90WfiyxXI3zCibgs1XEUtJNv9Q-e4bCw:0:0",
    "jazoest": "24988",
    "lsd": "AdG4MaF1lMY",
    "dyn": "1KQdAG1mws8-t0BBBzEnwSwgE98nwgU2owpUuwcC4o1nEhw23E52q1ewb60Y82Cwro0wa4o1MUaE36wdq0ny0oi0zE1jU1soG0hi0Lo6-0Co178dE1UU3jwea",
    "csr": "",
    "hsdp": "",
    "hblp": "",
    "sjsp": "",
    "req": "c",
    "fmt": "1",
    "a": "AYzwUgcaIDOJMECyMhAx45JxDD2EWE3v_AcJsGHy-3waZ4-0cmEVcHVnckE-fvYu5v55-oI-6Kll-MLJy-MG4ldQs0GV4CLokbk",
    "__user": "0"
}

urlencoded_string = urllib.parse.urlencode(url_params)
url = "https://m.facebook.com/login/device-based/login/async/"

# --- Do the POST using a Session so cookies persist ---
session = requests.Session()
# set headers on the session (helps keep them for redirects)
session.headers.update(headers)
# preload client-side cookies (optional; requests will send them)
for k, v in cookies.items():
    session.cookies.set(k, v, domain=".facebook.com")

# perform the request
resp = session.post(url, data=url_params, allow_redirects=True, timeout=30)

# extract cookies from the session
cookies_after = session.cookies.get_dict()

# check for typical FB login cookies (most reliable: 'c_user' and 'xs')
if "c_user" in cookies_after:
    print("Login appears SUCCESSFUL.")
    # Build a cookie header string you can re-use in subsequent requests:
    cookie_header = "; ".join([f"{k}={v}" for k, v in cookies_after.items()])
    print("Cookie header to reuse:")
    print(cookie_header)
    # If you want individual pieces:
    print("c_user:", cookies_after.get("c_user"))
    print("xs:", cookies_after.get("xs"))
else:
    print("Login does NOT appear successful.")
    print("HTTP status:", resp.status_code)
    # show a short resp preview to help debugging
    preview = resp.text[:500].replace("\n", " ")
    print("Response preview:", preview)

