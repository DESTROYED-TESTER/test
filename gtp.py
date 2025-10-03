import requests

url = "https://limited.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"

headers = {
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
    "Cookie": "datr=E2HfaC1esUHFUPm1LLzXx4Gg; sb=E2HfaAojnK6mDputqTLHjbdf; m_pixel_ratio=2.4749999046325684; wd=437x973; fr=0t3Dqio7YRHpb2kNK..Bo32ET..AAA.0.0.Bo32G3.AWcxwMvmgZxYDvgeMA13kMqTeMU"
}

data = {
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

response = requests.post(url, headers=headers, data=data)
print(response.text)
