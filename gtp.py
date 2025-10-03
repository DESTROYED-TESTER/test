import requests

cookies = {
    'datr': 'xJxPaKQpoJElo6Qa5Stty0z3',
    'fr': '0RBYWl1RkhYfcDKNN..BoT5zE..AAA.0.0.Bo32Wq.AWc0KrnRiyGg2jvu-bDILFD-9N8',
    'sb': 'xJxPaBlxTvSWwpAbuoUHWKCU',
    'ps_l': '1',
    'ps_n': '1',
    'wd': '1440x525',
    'locale': 'en_GB',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:143.0) Gecko/20100101 Firefox/143.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.facebook.com/?_rdr',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.facebook.com',
    'Connection': 'keep-alive',
}

data = {
    'jazoest': '2924',
    'lsd': 'AdHsL0R9suM',
    'email': '61556720024158',
    'login_source': 'comet_headerless_login',
    'next': '',
    'encpass': '#PWD_BROWSER:5:1759471040:AXFQAEuVrDY3WFW4qX0hwrgskkWI/SNPIwuqjXy06j8DStFZi6T5t5mceDUYqcvBzJNdReUdJdDX/Zp9pdyytsw99EiVwnO3X0TkRWt6pg0hOsvdvm8NKwad6FfO3M3B01JdbYa/jmOc3g==',
}

# Use a session so cookies persist
session = requests.Session()

response = session.post(
    'https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzU5NDcxMDE4LCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D&next',
    cookies=cookies,
    headers=headers,
    data=data,
    allow_redirects=True
)

# Check cookies for login success
cookie_dict = session.cookies.get_dict()

if "c_user" in cookie_dict:
    print("✅ Login successful as user:", cookie_dict["c_user"])
elif "checkpoint" in response.url or "confirmemail.php" in response.url:
    print("⚠️ Login requires verification:", response.url)
else:
    print("❌ Login failed")
    print("Final URL:", response.url)
