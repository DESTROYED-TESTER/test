import requests
import json,time

headers = {
    'Priority': 'u=3, i',
    'Authorization': 'OAuth null',
    'X-FB-Connection-Quality': 'GOOD',
    'X-FB-SIM-HNI': '47007',
    'X-FB-Net-HNI': '47002',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 14; TECNO CK7n Build/UP1A.231005.007) [FBAN/FB4A;FBAV/370.0.0.23.112;FBPN/com.facebook.katana;FBLC/en_US;FBBV/374931177;FBCR/Airtel;FBMF/TECNO;FBBD/TECNO;FBDV/TECNO CK7n;FBSV/14;FBCA/arm64-v8a:null;FBDM/{density=2.7375,width=1080,height=2292};FB_FW/1;FBRV/0;]',
    'Content-Encoding': 'gzip',
    'Host': 'b-graph.facebook.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-FB-Connection-Type': 'MOBILE.LTE',
    'x-fb-device-group': '701',
    'X-Tigon-Is-Retry': 'False',
    'X-FB-Friendly-Name': 'authenticate',
    'X-FB-Request-Analytics-Tags': 'unknown',
    'X-FB-HTTP-Engine': 'Liger',
    'X-FB-Client-IP': 'True',
    'X-FB-Server-Cluster': 'True',
    'Connection': 'keep-alive',
}

data = {
    'adid': '01a378a8-2b90-498a-bdf1-ae0359bcd2c4',
    'format': 'json',
    'device_id': 'a143397c-0621-4803-a8e5-fcce42e40197',
    'email': '61572000904841',
    'password': "#PWD_FB4A:0:{}:{}".format(str(time.time()).split('.')[0], '790891'),
    'generate_analytics_claim': '1',
    'community_id': '',
    'cpl': 'true',
    'try_num': '1',
    'cds_experiment_group': '-1',
    'family_device_id': 'd3e35bd2-fe96-4678-b809-af07741237cb',
    'secure_family_device_id': '441d9943-87fc-4ab8-aa47-65c4b7ce2c9f',
    'sim_serials': '["3a:fa:04:81:8a:f9"]',
    'credentials_type': 'password',
    'fb4a_shared_phone_cpl_experiment': 'fb4a_shared_phone_nonce_cpl_at_risk_v3',
    'fb4a_shared_phone_cpl_group': 'enable_v3_at_risk',
    'enroll_misauth': 'false',
    'generate_session_cookies': '1',
    'error_detail_type': 'button_with_disabled',
    'source': 'login',
    'generate_machine_id': '1',
    'jazoest': '22271',
    'meta_inf_fbmeta': 'NO_FILE',
    'advertiser_id': '01a378a8-2b90-498a-bdf1-ae0359bcd2c4',
    'encrypted_msisdn': 'Ae8zzUIz7jzFEdYZ_MfSxNpfJWWf7sEjY1NcPkmF77iy5htR_9up5PTD5F_uiQSsTCZcpD6rkVKsXX2cruVjuomJSgv_6CL0D4W8NgP4t0l2RP7KEaCvZMfTSfs480JL0VxLr2pOTnPU0pWtqQG1BE3UX5lYgtmL60shj5eL4tK1OzKSUzVjy_FPAw6SR7bw1Lw9-j9ZJDnDyTYN30pSSbLnMMZbU9wDeEWpqRmFWt2FieCt1NCk22eRtTagf0_SZr77UhSVsCyCZpOWv3ZokAaubmoZzdePyaj36KeapwcqWnt9hpkv9CuFc_PoCnKyx7cIPAnx-sGkYvCP8XYMjUIp',
    'currently_logged_in_userid': '0',
    'locale': 'en_US',
    'client_country_code': 'BD',
    'fb_api_req_friendly_name': 'authenticate',
    'fb_api_caller_class': 'Fb4aAuthHandler',
    'api_key': '882a8490361da98702bf97a021ddc14d',
    'sig': '80272038ac17dd62a2e00dc4a78b45c7',
    'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
}

response = requests.post('https://b-graph.facebook.com/auth/login', headers=headers, data=data)

# Parse the response JSON
try:
    q = response.json()
    
    # Check if access_token exists in response
    if 'access_token' in q:
        print("Access token found:", q['access_token'])
        # Do something with the access token
        
    # Check for www.facebook.com in error message
    elif 'error' in q and 'message' in q['error'] and 'www.facebook.com' in q['error']['message']:
        print("Redirect to www.facebook.com detected in error message")
        print("Error message:", q['error']['message'])
        # Handle the redirect case
        
    else:
        print("Response doesn't match expected patterns")
        print("Response:", json.dumps(q, indent=2))
        
except json.JSONDecodeError:
    print("Failed to parse JSON response")
    print("Raw response:", response.text)
