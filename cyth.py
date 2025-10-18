import requests
import base64
import struct
import io
import time
import json
import uuid
import random
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_v1_5
from Crypto.Random import get_random_bytes

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

def generate_device_id():
    """Generate consistent device ID"""
    return str(uuid.uuid4())

def facebook_login_v2(email, password):
    """Alternative login method using auth/login endpoint"""
    
    device_id = generate_device_id()
    
    # Use traditional auth endpoint instead of Bloks
    url = "https://b-graph.facebook.com/auth/login"
    
    data = {
        'adid': str(uuid.uuid4()),
        'format': 'json',
        'device_id': device_id,
        'cpl': 'true',
        'family_device_id': device_id,
        'credentials_type': 'device_based_login_password',
        'error_detail_type': 'button_with_disabled',
        'source': 'device_based_login',
        'email': email,
        'password': PWD_FB4A(password),
        'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
        'generate_session_cookies': '1',
        'meta_inf_fbmeta': '',
        'advertiser_id': str(uuid.uuid4()),
        'currently_logged_in_userid': '0',
        'locale': 'en_US',
        'client_country_code': 'US',
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '882a8e91361575a2203f99d4a7f5e5f5'
    }
    
    headers = {
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 11; SM-G973F Build/RP1A.200720.012)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'b-graph.facebook.com',
        'X-FB-Net-HNI': str(random.randint(20000, 40000)),
        'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
        'X-FB-Connection-Type': 'WIFI',
        'X-Tigon-Is-Retry': 'False',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
        'x-fb-device-group': '5120',
        'X-FB-Friendly-Name': 'ViewerReauthenticationConfig',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True',
        'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
    }
    
    try:
        response = requests.post(url, data=data, headers=headers)
        result = response.json()
        
        if 'access_token' in result or 'session_key' in result:
            print("✓ Login successful!")
            print(f"Access Token: {result.get('access_token', 'N/A')}")
            print(f"User ID: {result.get('uid', 'N/A')}")
            return result
        else:
            print("✗ Login failed!")
            print("Response:", json.dumps(result, indent=2))
            return None
            
    except Exception as e:
        print(f"Error: {e}")
        return None

def facebook_login_v3(email, password):
    """Method 3: Using method/auth.login"""
    
    url = "https://b-graph.facebook.com/method/auth.login"
    
    data = {
        'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'JSON',
        'sdk_version': '2',
        'email': email,
        'locale': 'en_US',
        'password': PWD_FB4A(password),
        'sdk': 'android',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
    }
    
    headers = {
        'User-Agent': '[FBAN/FB4A;FBAV/424.0.0.27.91;FBBV/480086274;FBDM/{density=2.75,width=1080,height=2137};FBLC/en_US;FBRV/481416311;FBCR/Verizon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'b-graph.facebook.com',
        'X-FB-Net-HNI': str(random.randint(20000, 40000)),
        'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
        'X-FB-Connection-Type': 'WIFI',
    }
    
    try:
        response = requests.post(url, data=data, headers=headers)
        result = response.json()
        
        if 'access_token' in result or 'session_key' in result:
            print("✓ Login successful!")
            print(json.dumps(result, indent=2))
            return result
        else:
            print("✗ Login failed!")
            print("Response:", json.dumps(result, indent=2))
            return None
            
    except Exception as e:
        print(f"Error: {e}")
        return None

# Test with your credentials
if __name__ == "__main__":
    uid = "100053582633432"
    password = "630110"
    
    print("=" * 50)
    print("Attempting Method 2: auth/login")
    print("=" * 50)
    result = facebook_login_v2(uid, password)
    
    if not result:
        print("\n" + "=" * 50)
        print("Attempting Method 3: method/auth.login")
        print("=" * 50)
        time.sleep(5)  # Wait before retry
        result = facebook_login_v3(uid, password)
