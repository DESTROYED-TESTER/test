import requests
import datetime
import urllib.parse

username = 'keshrsi1'
password = '626776'
# Create session to maintain cookies
session = requests.Session()

# STEP 1: Visit login page to get fresh CSRF token
print("Getting fresh CSRF token...")
login_response = session.get('https://www.instagram.com/accounts/login/')
csrf_token = session.cookies.get('csrftoken')
print(f"CSRF Token: {csrf_token}")
time_now = int(datetime.datetime.now().timestamp())
enc_password = f"#PWD_INSTAGRAM_BROWSER:0:{time_now}:{password}"
enc_password_encoded = urllib.parse.quote(enc_password)

url = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/'

headers = {
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Google Chrome";v="145.0.7632.5", "Chromium";v="145.0.7632.5"',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-mobile': '?0',
    'X-IG-App-ID': '936619743392459',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept': '*/*',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Instagram-AJAX': '1045824267',
    'X-CSRFToken': csrf_token,
    'X-Web-Session-ID': 'vnolst:phqive:f5i8pp',
    'Referer': 'https://www.instagram.com/mimi_roy_44/',
    'X-IG-Max-Touch-Points': '0',
    'X-ASBD-ID': '359341',
    'sec-ch-prefers-color-scheme': 'dark',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    'X-IG-WWW-Claim': 'hmac.AR0lFPVrPWfUaasIaEe7P5wZzNvi4rTJt5zBnbJl9QfE-UHY',
    'sec-ch-ua-platform-version': '"10.0.0"',
}

data = f'enc_password={enc_password_encoded}&caaF2DebugGroup=-1&isPrivacyPortalReq=false&loginAttemptSubmissionCount=0&optIntoOneTap=false&queryParams=%7B%22oneTapUsers%22%3A%22%5B%5C%2271197200037%5C%22%5D%22%7D&trustedDeviceRecords=%7B%2271197200037%22%3A%7B%22machine_id%22%3A%22afAaSAALAAH1E9oBPA3kaW94g3fT%22%2C%22nonce%22%3A%223wQWQEa1bhApmLnMUuObWk0uwmWXdePxIg9cUI7IyfEAwTLJxEJWdB4IPKme32DX%22%7D%7D&username={username}&jazoest=22902&fb_dtsg=NAfyFFlfztZGS1a5mQLPSTxampkgFsMeFeO9BbRWiV5VgtEFJ71WCCg%3A17843709688147332%3A1787460646'

response = session.post(url, headers=headers, data=data)
wanted = ["ds_user_id", "sessionid"]
all_cookies = session.cookies.get_dict()
extracted = {k: all_cookies[k] for k in wanted if k in all_cookies}
cookie_str = "; ".join(f"{k}={v}" for k, v in extracted.items())
print("Cookies:", cookie_str)
print(response.status_code)
print(response.text)
