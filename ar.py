import uuid
import random
import requests
import re

# Generate unique identifiers
data = {
    'email': '100062756363125',
    'password': '620660',
    'adid': str(uuid.uuid4()),
    'device_id': str(uuid.uuid4()),
    'family_device_id': str(uuid.uuid4()),
    'session_id': str(uuid.uuid4()),
    'advertiser_id': str(uuid.uuid4()),
    'reg_instance': str(uuid.uuid4()),
    'logged_out_id': str(uuid.uuid4()),
    'locale': 'en_US',
    'client_country_code': 'US',
    'cpl': 'true',
    'source': 'login',
    'format': 'json',
    'omit_response_on_success': 'false',
    'credentials_type': 'password',
    'error_detail_type': 'button_with_disabled',
    'generate_session_cookies': '1',
    'generate_analytics_claim': '1',
    'generate_machine_id': '1',
    'tier': 'regular',
    'currently_logged_in_userid': '0',
    'fb_api_req_friendly_name': 'authenticate',
    'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
    'fb4a_shared_phone_cpl_experiment': 'fb4a_shared_phone_nonce_cpl_at_risk_v3',
    'fb4a_shared_phone_cpl_group': 'enable_v3_at_risk',
    'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
    'api_key': '882a8490361da98702bf97a021ddc14d',
    'sig': '62f8ce9f74b12f84c123cc23437a4a32'
}

# Set headers for authentication request
headers = {
    'Host': 'graph.facebook.com',
    'User-Agent': 'Your User Agent Here',  # Replace with your UA method
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
    'X-FB-Connection-Bandwidth': '27181576',
    'X-FB-Connection-Quality': 'EXCELLENT',
    'X-FB-Connection-Type': 'MOBILE.LTE',
    'X-FB-HTTP-Engine': 'Liger',
    'X-FB-Client-IP': 'True',
    'X-FB-Friendly-Name': 'authenticate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '1026'
}

# Send authentication request
url = "https://graph.facebook.com/auth/login"
response = requests.post(url, data=data, headers=headers)

# Process the response
if response.status_code == 200:
    for i in re.findall('href="/changeemail(.*?)"', response.text):
        url = "/changeemail" + i
        change_email_response = requests.get("https://m.facebook.com" + url, headers=headers)
        print(change_email_response.text)
else:
    print("Failed to authenticate or no change email URL found.")
