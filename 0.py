import requests

url = "https://limited.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; V2060 Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.7444.21 Mobile Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": "application/x-www-form-urlencoded",
    "sec-ch-ua-platform": '"Android"',
    "sec-ch-ua": '"Chromium";v="142", "Android WebView";v="142", "Not_A Brand";v="99"',
    "x-response-format": "JSONStream",
    "sec-ch-ua-mobile": "?1",
    "x-asbd-id": "359341",
    "x-fb-lsd": "AdGm0XNgPZI",
    "x-requested-with": "XMLHttpRequest",
    "origin": "https://limited.facebook.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://limited.facebook.com/",
    "accept-language": "en-US,en;q=0.9",
    "priority": "u=1, i",
    "Cookie": "datr=j2D0aGNfrkhe6gsD30X9rocd; sb=j2D0aAXaXOHjOD9-oe2tBQq3; m_pixel_ratio=2.4749999046325684; wd=437x973; fr=0Cgs75RqCn7Ic4eLB..Bo9GCP..AAA.0.0.Bo9NIG.AWevxQpVa2RjMHVgm1WI0GmCmdY"
}

data = {
    "m_ts": "1760874943",
    "li": "v9H0aI7R_BQkzL03WnfHN8aI",
    "try_number": "0",
    "unrecognized_tries": "0",
    "email": "100058660152667",
    "prefill_contact_point": "100058660152667|964119|",
    "prefill_source": "browser_dropdown",
    "prefill_type": "password",
    "first_prefill_source": "browser_dropdown",
    "first_prefill_type": "contact_point",
    "had_cp_prefilled": "true",
    "had_password_prefilled": "true",
    "is_smart_lock": "false",
    "bi_xrwh": "92004344361786634",
    "encpass": "#PWD_BROWSER:5:1760875018:AYFQAEU6J/oHurmTPKUMYpcEutIj32eX4NsMcUtALmTB6t5NdBjqShcJx38tk531kbV8ZapQMO+RKvV5BcFJ7iTbaDo0+oUJfLMR87wvmXDZ539KQg1b7bchMxanDdfIL5U21rXEt2Awqg==",
    "fb_dtsg": "NAfsTy_nVmMY-aPq2jodNfEfMAoYxODjAWsWDzfAH8A75HyboS_sRKg:0:0",
    "jazoest": "25078",
    "lsd": "AdGm0XNgPZI",
    "_dyn": "1KQdAG1mws8-t0BBBzEnwSwgE98nwgU2owpUuwcC4o1nEhw23E52q1ewb60Y82Cwro0wa4o1MUaE36wdq0ny0oi0zE1jU1soG0hi0Lo6-0Co178dE1UU3jwea",
    "csr": "",
    "hsdp": "",
    "hblp": "",
    "sjsp": "",
    "req": "7",
    "fmt": "1",
    "a": "AYyQqdylf2eoq8yXWSG7K_Msk0NY97pal6sBjs63bUJC904PTS5BYy4tJzgHZU9E7RpVfhWJ4bHrnLAwXzSmITIqS3nGPb_LZ0Y",
    "_user": "0"
}

response = requests.post(url, headers=headers, data=data)

print(response.status_code)
print(response.text)
