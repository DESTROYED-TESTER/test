import httpx

url = "https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=120&lwc=1348028"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Content-Type": "application/x-www-form-urlencoded",
    "cache-control": "max-age=0",
    "sec-ch-ua": '"Android WebView";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "origin": "https://www.facebook.com",
    "upgrade-insecure-requests": "1",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": "https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100",
    "accept-language": "en-US,en;q=0.9",
    "priority": "u=0, i",
}

cookies = {
    "datr": "E2HfaC1esUHFUPm1LLzXx4Gg",
    "sb": "E2HfaAojnK6mDputqTLHjbdf",
    "m_pixel_ratio": "2.4749999046325684",
    "dpr": "2.4749999046325684",
    "fr": "0t3Dqio7YRHpb2kNK..Bo32ET..AAA.0.0.Bo33sH.AWcqUI_-iTw-xf3gQLRcFcTEr0s",
    "wd": "1280x2367",
}

data = {
    # same data dict as above
    "jazoest": "2869",
    "lsd": "AdG4MaF1R_o",
    "display": "",
    "isprivate": "",
    "return_session": "",
    "skip_api_login": "",
    "signed_next": "",
    "trynum": "2",
    "timezone": "-330",
    # ... (include the rest exactly as above) ...
    "email": "100043514448161",
    "prefill_contact_point": "1000262740228556",
    "prefill_source": "browser_dropdown",
    "prefill_type": "password",
    "first_prefill_source": "browser_dropdown",
    "first_prefill_type": "contact_point",
    "had_cp_prefilled": "true",
    "had_password_prefilled": "true",
    "ab_test_data": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
    "encpass": "#PWD_BROWSER:5:1759476526:AXFQANw5oazwXINXvoJ6vdCiq16lV983bef7cnjxr8mi+zMgxfOPdS3sMyAe1TY+UBce/QWQUy+27GJYJCvHReh8hu9s2yUIF1fLL2V9C4o1FimlmifOHuvt+2cYSfrxLtcAotKZerKuvg==",
}

with httpx.Client(http2=True, headers=headers, cookies=cookies, timeout=30) as client:
    resp = client.post(url, data=data, follow_redirects=True)
    print("Status:", resp.status_code)
    print("Final URL:", resp.url)
    print("Response snippet:", resp.text[:800])
