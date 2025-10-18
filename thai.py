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

def extract_cookies(response):
    """Extract cookies from response headers and JSON"""
    cookies = {}
    
    # Extract from response headers
    if 'Set-Cookie' in response.headers:
        cookie_header = response.headers['Set-Cookie']
        for cookie in cookie_header.split(','):
            if '=' in cookie:
                key_value = cookie.split(';')[0].strip()
                if '=' in key_value:
                    key, value = key_value.split('=', 1)
                    cookies[key.strip()] = value.strip()
    
    # Extract from response.cookies
    for cookie in response.cookies:
        cookies[cookie.name] = cookie.value
    
    return cookies

def extract_session_data(result):
    """Extract session data from JSON response"""
    session_data = {}
    
    try:
        # Navigate through the nested JSON structure
        if isinstance(result, dict):
            # Look for session_key, access_token, uid, etc.
            def search_dict(d, parent_key=''):
                for key, value in d.items():
                    if key in ['session_key', 'access_token', 'uid', 'session_cookies', 'secret']:
                        session_data[key] = value
                    elif isinstance(value, dict):
                        search_dict(value, key)
                    elif isinstance(value, list):
                        for item in value:
                            if isinstance(item, dict):
                                search_dict(item, key)
            
            search_dict(result)
    except Exception as e:
        print(f"Error extracting session data: {e}")
    
    return session_data

def format_cookie_string(cookies):
    """Format cookies as a cookie string"""
    return '; '.join([f"{key}={value}" for key, value in cookies.items()])

# Main login function
def facebook_login(uid, password):
    data = {
        'method': 'post',
        'pretty': False,
        'format': 'json',
        'server_timestamps': True,
        'locale': 'id_ID, en-US',
        'purpose': 'fetch',
        'fb_api_req_friendly_name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request',
        'fb_api_caller_class': 'graphservice',
        'client_doc_id': '119940804214876861379510865434',
        'variables': json.dumps({
            "params": {
                "params": json.dumps({
                    "params": json.dumps({
                        "client_input_params": {
                            "device_id": str(uuid.uuid4()),
                            "lois_settings": {
                                "lois_token": "",
                                "lara_override": ""
                            },
                            "name": None,
                            "machine_id": "FXQ7Z_eNU42Pnt5I_CpRlzIh",
                            "profile_pic_url": None,
                            "contact_point": uid,
                            "encrypted_password": PWD_FB4A(password)
                        },
                        "server_params": {
                            "is_from_logged_out": 1,
                            "layered_homepage_experiment_group": None,
                            "device_id": str(uuid.uuid4()),
                            "waterfall_id": str(uuid.uuid4()),
                            "INTERNAL__latency_qpl_instance_id": 2.9809277900605E13,
                            "login_source": "Login",
                            "is_platform_login": 0,
                            "INTERNAL__latency_qpl_marker_id": 36707139,
                            "family_device_id": str(uuid.uuid4()),
                            "offline_experiment_group": "caa_iteration_v6_perf_fb_2",
                            "INTERNAL_INFRA_THEME": "default,default",
                            "access_flow_version": "F2_FLOW",
                            "is_from_logged_in_switcher": 0
                        }
                    })
                }),
                "bloks_versioning_id": "3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5",
                "app_id": "com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request"
            },
            "scale": "2",
            "nt_context": {
                "using_white_navbar": True,
                "styles_id": "cfe75e13b386d5c54b1de2dcca1bee5a",
                "pixel_ratio": 2,
                "is_push_on": False,
                "debug_tooling_metadata_token": None,
                "is_flipper_enabled": False,
                "theme_params": [],
                "bloks_version": "3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5"
            }
        }),
        'fb_api_analytics_tags': '["GraphServices"]',
        'client_trace_id': str(uuid.uuid4())
    }

    headers = {
        'host': 'graph.facebook.com',
        'x-fb-connection-type': 'MOBILE.LTE',
        'user-agent':f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/336.0.0.20.117;FBBV/287214784;FBDM/{density=4.0,width=1200,height=812};FBLC/en_US;FBCR/Grameenphone;FBMF/AllView;FBBD/allview;FBPN/com.facebook.katana;FBDV/ Viva H1003 LTE;FBSV/10;FBCA/armeabi-v7a:armeabi;]",
        'x-tigon-is-retry': 'False',
        'x-fb-device-group': str(random.randint(1000, 5999)),
        'x-graphql-request-purpose': 'fetch',
        'x-fb-privacy-context': '3643298472347298',
        'x-fb-friendly-name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request',
        'x-graphql-client-library': 'graphservice',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'x-fb-net-hni': str(random.randint(5000, 5999)),
        'x-fb-sim-hni': str(random.randint(5000, 5999)),
        'authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
        'x-fb-request-analytics-tags': '{"network_tags":{"product":"350685531728","purpose":"fetch","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}',
        'x-requested-with': 'XMLHttpCanary',
        'x-fb-http-engine': 'Tigon/Liger',
        'x-fb-client-ip': 'True',
        'x-fb-server-cluster': 'True',
    }

    url = "https://b-graph.facebook.com/graphql"
    
    try:
        response = requests.post(url, data=data, headers=headers)
        
        # Extract cookies from response
        cookies = extract_cookies(response)
        
        # Parse JSON response
        result = response.json()
        
        # Extract session data from JSON
        session_data = extract_session_data(result)
        
        # Check for successful login
        if "session_key" in str(result) or session_data:
            print("=" * 60)
            print("✓ LOGIN SUCCESSFUL!")
            print("=" * 60)
            
            # Print cookies from headers
            if cookies:
                print("\n📌 COOKIES FROM HEADERS:")
                print("-" * 60)
                for key, value in cookies.items():
                    print(f"{key}: {value}")
                
                print("\n📋 COOKIE STRING:")
                print("-" * 60)
                print(format_cookie_string(cookies))
            
            # Print session data from JSON
            if session_data:
                print("\n🔑 SESSION DATA:")
                print("-" * 60)
                for key, value in session_data.items():
                    print(f"{key}: {value}")
            
            # Print full response for debugging
            print("\n📄 FULL RESPONSE:")
            print("-" * 60)
            print(json.dumps(result, indent=2))
            print("=" * 60)
            
            return {
                'cookies': cookies,
                'session_data': session_data,
                'response': result
            }
        else:
            print("=" * 60)
            
