import requests

# ------------------------------
# 1. COOKIES
# ------------------------------
cookies = {
    'csrftoken': 'SUW-lWl5CeniuolLF14E-O',
    'datr': 'hvMmaRTfFUseHoQfN3VkRNSH',
    'ig_did': 'FA4BC7A3-44CC-4A3D-95E4-76BBBF760ED9',
    'mid': 'aSbziAALAAE62ug2B-ACpkrK-MfG',
    'ig_nrcb': '1',
    'ps_l': '1',
    'ps_n': '1',
    'wd': '1440x587',
}

# ------------------------------
# 2. HEADERS
# ------------------------------
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'X-CSRFToken': 'SUW-lWl5CeniuolLF14E-O',
    'X-Instagram-AJAX': '1030879028',
    'X-IG-App-ID': '936619743392459',
    'X-ASBD-ID': '359341',
    'X-IG-WWW-Claim': '0',
    'X-Web-Session-ID': '00e0wl:jus0ke:fv6ahj',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://www.instagram.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://www.instagram.com/fxcal/auth/login/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

# ------------------------------
# 3. FORM DATA
# ------------------------------
data = {
    'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1765357106:AaRQAIKyTK72w1Ty6ce72W/tZtnTPdxdraGMTXgo7Xn9/60NKMMkp/pIIpW8BLc9Kebsg0tBtbeKgMsTQqUUL7wS1KTp7fuhaoNa71O+pHmzlSwNCXK+5J4qxcJ/P1xySOsKJ9mURlRjkdbczA==',
    'etoken': 'AbkpnoYTtMvuRC6gfTQL3T-_TJL4ve8wNyo6ur5mcSYBfjW_AT6hRU6COL7eZ7ttaxiv8uLZu0jtMS0dJXbYPrFErqiztaXpe6J2NJK5bIYo6bZ1GtM',
    'username': '7029868180',
    'jazoest': '21815',
}

# ------------------------------
# 4. SEND LOGIN REQUEST
# ------------------------------
response = requests.post(
    'https://www.instagram.com/api/v1/web/fxcal/auth/login/ajax/',
    cookies=cookies,
    headers=headers,
    data=data,
)

# ------------------------------
# 5. EXTRACT COOKIES
# ------------------------------
new_cookies = response.cookies.get_dict()

print("\n===== RAW COOKIE DICT =====")
print(new_cookies)

print("\n===== MERGED COOKIES =====")
merged = {**cookies, **new_cookies}
print(merged)

print("\n===== BROWSER COOKIE STRING =====")
cookie_string = "; ".join([f"{k}={v}" for k, v in merged.items()])
print(cookie_string)
