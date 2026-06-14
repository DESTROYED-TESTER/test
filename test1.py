import requests
import json
import time

headers = {
    'Priority': 'u=3, i',
    'Authorization': 'OAuth null',
    'X-FB-Connection-Quality': 'GOOD',
    'X-FB-SIM-HNI': '47007',
    'X-FB-Net-HNI': '47002',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 14; TECNO CK7n Build/UP1A.231005.007) [FBAN/FB4A;FBAV/370.0.0.23.112;FBPN/com.facebook.katana;FBLC/en_US;FBBV/374931177;FBCR/Airtel;FBMF/TECNO;FBBD/TECNO;FBDV/TECNO CK7n;FBSV/14;FBCA/arm64-v8a:null;FBDM/{density=2.7375,width=1080,height=2292};FB_FW/1;FBRV/0;]',
    # 'Content-Encoding': 'gzip',  # REMOVED - requests handles this automatically
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
    'Accept-Encoding': 'gzip, deflate',  # Let requests handle compression
}

# Generate password with current timestamp
current_time = str(int(time.time()))
password = f"#PWD_FB4A:0:{current_time}:57273200"

data = {
    'adid': '01a378a8-2b90-498a-bdf1-ae0359bcd2c4',
    'format': 'json',
    'device_id': 'a143397c-0621-4803-a8e5-fcce42e40197',
    'email': '9883157121',
    'password': password,
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

# Make the request with debugging
print(f"Attempting login for: {data['email']}")
print(f"Using password hash: {password}")
print("-" * 50)

response = requests.post(
    'https://b-graph.facebook.com/auth/login', 
    headers=headers, 
    data=data,
    allow_redirects=False  # Don't automatically follow redirects
)

# Debug information
print(f"Status Code: {response.status_code}")
print(f"Response Headers: {dict(response.headers)}")
print(f"Content-Type: {response.headers.get('Content-Type', 'Unknown')}")
print("-" * 50)

# Check if we got a redirect
if response.status_code in [301, 302, 303, 307, 308]:
    print(f"Redirect detected to: {response.headers.get('Location', 'Unknown')}")
    print("The server is redirecting instead of returning JSON")

# Try to parse the response
try:
    # First, check if response is HTML
    if 'text/html' in response.headers.get('Content-Type', ''):
        print("Server returned HTML instead of JSON")
        if 'checkpoint' in response.text or 'blocked' in response.text:
            print("This might be a checkpoint or blocked account page")
        # Extract first 500 chars for debugging
        print(f"HTML Preview: {response.text[:500]}")
    else:
        q = response.json()
        print("Successfully parsed JSON response:")
        print(json.dumps(q, indent=2))
        
        # Check if access_token exists in response
        if 'access_token' in q:
            print("\n✅ Access token found:", q['access_token'])
        elif 'error' in q:
            error_msg = q['error'].get('message', 'No message')
            print(f"\n❌ Error: {error_msg}")
            if 'www.facebook.com' in error_msg:
                print("Redirect to www.facebook.com detected in error message")
        else:
            print("\n⚠️ Unexpected response format")
            
except json.JSONDecodeError as e:
    print(f"❌ Failed to parse JSON: {e}")
    print(f"Raw response (first 1000 chars):\n{response.text[:1000]}")
    
    # Check for common issues
    if 'www.facebook.com' in response.text:
        print("\nDetected 'www.facebook.com' in response - likely a redirect page")
    elif 'checkpoint' in response.text.lower():
        print("\nDetected checkpoint - account may need verification")
    elif 'login' in response.text.lower():
        print("\nDetected login page - authentication may have failed")
