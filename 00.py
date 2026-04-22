import requests
Session = requests.Session()

cookies = {
    'datr': 'S0TnaWmFEDgALo6du8Tdjr1c',
    'sb': 'S0Tnac5OlkzFt40liPjo4nnE',
    'm_pixel_ratio': '2.75',
    'wd': '393x851',
    'fr': '0e0TKXKqNm1Oe5PDf.AWeJXCextk1yw2fMDDriPwzd1EvsCy_XjfjMaEhSA-JOP4Jn59A.Bp50RL..AAA.0.0.Bp50pA.AWdehuygLj5s5yC6U468Z9y81jU',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2010J19SI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded',
    'cache-control': 'max-age=0',
    'dpr': '2.75',
    'viewport-width': '980',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-ch-ua-model': '"M2010J19SI"',
    'sec-ch-ua-full-version-list': '".Not/A)Brand";v="99.0.0.0", "Google Chrome";v="103.0.5060.129", "Chromium";v="103.0.5060.129"',
    'sec-ch-prefers-color-scheme': 'light',
    'upgrade-insecure-requests': '1',
    'origin': 'https://m.facebook.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://m.facebook.com/login/device-based/password/?uid=61551769793551&next=https%3A%2F%2Fm.facebook.com%2Ffxreauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbljjNFddxZHsR3x2CX3AdJWgDFOSv6byXjyGHvtqcRxYyy9OaXwgJ4vSrw2U6kPDT59QnBqV-hd2Q%26account_id%3D61551769793551%26force_logout%3D0%26extra_data%3D%252Fprofiles%252F61551769793551%252Fname%252F%26native_app_login_flow%3Dfbreauthcomet&flow=fx_reauth&wtsid=rdr_083GyyJq4X5XOGmJo&http_ref=eyJ0cyI6IjE3NzY3NjU0NTY4ODgiLCJyIjoiaHR0cHM6XC9cL2FjY291bnRzY2VudGVyLmluc3RhZ3JhbS5jb21cLyJ9&refsrc=deprecated&_rdr',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': 'datr=S0TnaWmFEDgALo6du8Tdjr1c; sb=S0Tnac5OlkzFt40liPjo4nnE; m_pixel_ratio=2.75; wd=393x851; fr=0e0TKXKqNm1Oe5PDf.AWeJXCextk1yw2fMDDriPwzd1EvsCy_XjfjMaEhSA-JOP4Jn59A.Bp50RL..AAA.0.0.Bp50pA.AWdehuygLj5s5yC6U468Z9y81jU',
}

params = {
    'shbl': '0',
}

data = {
    'lsd': 'AdTCIsyB3AIWOfa4e1Hlxa5GpOM',
    'jazoest': '22236',
    'uid': '61551769793551',
    'next': 'https://m.facebook.com/fxreauth/?app_id=1217981644879628&etoken=AbljjNFddxZHsR3x2CX3AdJWgDFOSv6byXjyGHvtqcRxYyy9OaXwgJ4vSrw2U6kPDT59QnBqV-hd2Q&account_id=61551769793551&force_logout=0&extra_data=%2Fprofiles%2F61551769793551%2Fname%2F&native_app_login_flow=fbreauthcomet',
    'flow': 'fx_reauth',
    'encpass': '#PWD_BROWSER:5:1776765511:ATlQAAaDLiOr5r69bk4CUlg+4QMdLvkEKykUdvYepofIouxKcMVutRDGt/DvwpEiJdCyvB8j2DyLSA+4McL/1QffdRhVCXLMXoOjtaoIpPn/vyy4O8PsGaxjF1RDlxusgd3CosAsM1c9zg==',
}

response = Session.post(
    'https://m.facebook.com/login/device-based/validate-password/',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)

# Check login success
log_cookies = Session.cookies.get_dict().keys()
if "c_user" in log_cookies:
    print('\033[1;92m OK')
