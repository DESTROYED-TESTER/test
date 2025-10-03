import requests

url = 'https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=120&lwc=1348028'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '"Android WebView";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'Origin': 'https://www.facebook.com',
    'Upgrade-Insecure-Requests': '1',
    'X-Requested-With': 'mark.via.gp',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100',
    'Accept-Language': 'en-US,en;q=0.9',
    'Priority': 'u=0, i',
    'Cookie': 'datr=E2HfaC1esUHFUPm1LLzXx4Gg; sb=E2HfaAojnK6mDputqTLHjbdf; m_pixel_ratio=2.4749999046325684; dpr=2.4749999046325684; fr=0t3Dqio7YRHpb2kNK..Bo32ET..AAA.0.0.Bo33sH.AWcqUI_-iTw-xf3gQLRcFcTEr0s; wd=1280x2367'
}

data = {
    'jazoest': '2869',
    'lsd': 'AdG4MaF1R_o',
    'display': '',
    'isprivate': '',
    'return_session': '',
    'skip_api_login': '',
    'signed_next': '',
    'trynum': '2',
    'timezone': '-330',
    'lgndim': 'eyJ3Ijo0MzcsImgiOjk3MywiYXciOjQzNywiYWgiOjk3MywiYyI6MjR9',
    'lgnrnd': '002807_TGOq',
    'lgnjs': '1759476486',
    'shared_prefs_data': 'eyIzMDAwMCI6W3sidCI6MTc1OTQ3NjQ4Ni42MTIsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi9kZXZpY2UtYmFzZWQvcmVndWxhci9sb2dpbi8ifSwidiI6ZmFsc2V9XS...',
    'email': '100043514448161',
    'prefill_contact_point': '1000262740228556',
    'prefill_source': 'browser_dropdown',
    'prefill_type': 'password',
    'first_prefill_source': 'browser_dropdown',
    'first_prefill_type': 'contact_point',
    'had_cp_prefilled': 'true',
    'had_password_prefilled': 'true',
    'ab_test_data': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
    'encpass': '#PWD_BROWSER:5:1759476526:AXFQANw5oazwXINXvoJ6vdCiq16lV983bef7cnjxr8mi+zMgxfOPdS3sMyAe1TY+UBce/QWQUy+27GJYJCvHReh8hu9s2yUIF1fLL2V9C4o1FimlmifOHuvt+2cYSfrxLtcAotKZerKuvg=='
}
session = requests.Session()
response = session.post(url, headers=headers, data=data)
if 'c_user' in session.cookies.get_dict():
    print("✅ Login successful!")
    print("User ID:", session.cookies.get_dict()['c_user'])
else:
    print("❌ Login failed.")
    if 'checkpoint' in session.cookies.get_dict():
        print("⚠️ Account is checkpointed or requires verification.")
    else:
        print("Cookies returned:", session.cookies.get_dict())
