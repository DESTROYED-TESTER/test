import requests
import base64
import struct
import io
import time
import json
import uuid
import random
import re
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_v1_5
from Crypto.Random import get_random_bytes

password = "630110"
uid = "100053582633432"

def PWD_FB4A(password, public_key=None, key_id="25"):
    if public_key is None:
        pwd_key_fetch = 'https://b-graph.facebook.com/pwd_key_fetch'
        pwd_key_fetch_data = {
            'version': '2',
            'flow': 'CONTROLLER_INITIALIZATION',
            'method': 'GET',
            'fb_api_req_friendly_name': 'pwdKeyFetch',
            'fb_api_caller_class': 'com.facebook.auth.login.AuthOperations',
            'access_token': '438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28'
        }
        response = requests.post(pwd_key_fetch, params=pwd_key_fetch_data).json()
        public_key = response.get('public_key')
        key_id = str(response.get('key_id', key_id))
    
    rand_key = get_random_bytes(32)
    iv = get_random_bytes(12)
    pubkey = RSA.import_key(public_key)
    cipher_rsa = PKCS1_v1_5.new(pubkey)
    encrypted_rand_key = cipher_rsa.encrypt(rand_key)
    cipher_aes = AES.new(rand_key, AES.MODE_GCM, nonce=iv)
    current_time = int(time.time())
    cipher_aes.update(str(current_time).encode("utf-8"))
    encrypted_passwd, auth_tag = cipher_aes.encrypt_and_digest(password.encode("utf-8"))
    
    buf = io.BytesIO()
    buf.write(bytes([1, int(key_id)]))
    buf.write(iv)
    buf.write(struct.pack("<h", len(encrypted_rand_key)))
    buf.write(encrypted_rand_key)
    buf.write(auth_tag)
    buf.write(encrypted_passwd)
    encoded = base64.b64encode(buf.getvalue()).decode("utf-8")
    
    return f"#PWD_FB4A:2:{current_time}:{encoded}"



# str(uuid.uuid4()),
def facebook_login(uid, password):
    session = requests.Session()
    data = {
    'adid': str(uuid.uuid4()),
    'format': 'json',
    'device_id': str(uuid.uuid4()),
    'email': uid,
    'password': PWD_FB4A(password),
    'generate_analytics_claim': '1',
    'community_id': '',
    'cpl': 'true',
    'try_num': '1',
    'cds_experiment_group': '-1',
    'family_device_id': str(uuid.uuid4()),
    'secure_family_device_id': str(uuid.uuid4()),
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
    'advertiser_id': str(uuid.uuid4()),
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
    # 'Accept-Encoding': 'gzip, deflate',
    'X-FB-HTTP-Engine': 'Liger',
    'X-FB-Client-IP': 'True',
    'X-FB-Server-Cluster': 'True',
    'Connection': 'keep-alive',
    # 'Content-Length': '1314',
}

    url = "https://b-graph.facebook.com/auth/login"
    
    try:
        resul  = session.post(url, data=data, headers=headers)
        # Check for successful login
        result = resul.json()
        if "session_key" in str(result):
            print("✓ Login successful!")
            #kuki=";".join([f"{key}={session.cookies.get(key)}" for key in ['datr', 'fr', 'sb', 'c_user', 'xs']])
            print(resul.text)
            #print("Response.:", json.dumps(result, indent=2))
            return result
        else:
            print("✗ Login failed!")
            print("Response:", json.dumps(result, indent=2))
            return None
            
    except Exception as e:
        print(f"Error: {e}")
        return None

# Execute login
if __name__ == "__main__":
    result = facebook_login(uid, password)
