import requests
import json
import time
import base64
import urllib.parse
import re
from bs4 import BeautifulSoup

def generate_encrypted_password(password, timestamp=None):
    """
    Generate Facebook's password encryption format
    #PWD_BROWSER:version:timestamp:encrypted_password
    """
    if timestamp is None:
        timestamp = int(time.time())
    
    # Base64 encoding
    encoded = base64.b64encode(password.encode()).decode()
    return f"#PWD_BROWSER:5:{timestamp}:{encoded}"

def get_login_tokens():
    """
    Extract fresh tokens from Facebook login page
    Returns: dict with lsd, fb_dtsg, jazoest, and cookies
    """
    try:
        session = requests.Session()
        login_url = 'https://m.facebook.com/login/'
        headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36'
        }
        
        response = session.get(login_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract lsd
        lsd_input = soup.find('input', {'name': 'lsd'})
        lsd = lsd_input.get('value') if lsd_input else None
        
        # Extract fb_dtsg
        fb_dtsg_input = soup.find('input', {'name': 'fb_dtsg'})
        fb_dtsg = fb_dtsg_input.get('value') if fb_dtsg_input else None
        
        # Extract jazoest
        jazoest_input = soup.find('input', {'name': 'jazoest'})
        jazoest = jazoest_input.get('value') if jazoest_input else None
        
        return {
            'lsd': lsd,
            'fb_dtsg': fb_dtsg,
            'jazoest': jazoest,
            'session': session,
            'cookies': session.cookies.get_dict()
        }
    except Exception as e:
        print(f"⚠️ Error extracting tokens: {e}")
        return None

def build_params_payload(phone_number, encrypted_password):
    """
    Build the nested params structure for the login request
    """
    params_data = {
        "params": {
            "server_params": {
                "credential_type": "password",
                "username_text_input_id": "tg0z6g:58",
                "password_text_input_id": "tg0z6g:59",
                "login_source": "Login",
                "login_credential_type": "none",
                "server_login_source": "login",
                "ar_event_source": "login_home_page",
                "should_trigger_override_login_success_action": 0,
                "should_trigger_override_login_2fa_action": 0,
                "is_caa_perf_enabled": 0,
                "reg_flow_source": "login_home_native_integration_point",
                "caller": "gslr",
                "is_from_landing_page": 0,
                "is_from_empty_password": 0,
                "is_from_aymh": 0,
                "is_from_password_entry_page": 0,
                "is_from_assistive_id": 0,
                "is_from_msplit_fallback": 0,
                "two_step_login_type": "one_step_login",
                "left_nav_button_action": "NONE",
                "INTERNALlatency_qpl_marker_id": 36707139,
                "INTERNALlatency_qpl_instance_id": str(int(time.time() * 1000)),
                "device_id": None,
                "family_device_id": None,
                "waterfall_id": f"{int(time.time()):x}-{int(time.time()*100):x}-4e73-8bbc-{int(time.time()*1000):x}",
                "offline_experiment_group": None,
                "layered_homepage_experiment_group": None,
                "is_platform_login": 0,
                "is_from_logged_in_switcher": 0,
                "is_from_logged_out": 0,
                "access_flow_version": "pre_mt_behavior",
                "login_surface": "login_home",
                "login_entry_point": "logged_out"
            },
            "client_input_params": {
                "machine_id": "",
                "cloud_trust_token": None,
                "block_store_machine_id": "",
                "zero_balance_state": "",
                "contact_point": phone_number,
                "password": encrypted_password,
                "accounts_list": [],
                "fb_ig_device_id": [],
                "secure_family_device_id": "",
                "encrypted_msisdn": "",
                "headers_infra_flow_id": "",
                "try_num": 1,
                "login_attempt_count": 1,
                "event_flow": "login_manual",
                "event_step": "home_page",
                "openid_tokens": {},
                "auth_secure_device_id": "",
                "client_known_key_hash": "",
                "has_whatsapp_installed": 0,
                "sso_token_map_json_string": "",
                "should_show_nested_nta_from_aymh": 0,
                "gms_incoming_call_retriever_eligibility": "client_not_supported",
                "password_contains_non_ascii": "false",
                "has_granted_read_contacts_permissions": 0,
                "has_granted_read_phone_permissions": 0,
                "app_manager_id": "",
                "aymh_accounts": [],
                "sso_accounts_auth_data": [],
                "blocked_uids": [],
                "network_bssid": None,
                "lois_settings": {
                    "lois_token": ""
                },
                "aac": ""
            }
        }
    }
    return params_data

# ============== CONFIGURATION ==============
# UPDATE THESE WITH YOUR ACTUAL CREDENTIALS
PHONE_NUMBER = "9382324860"  # Your phone number or email
ACTUAL_PASSWORD = "9382324860"  # CHANGE THIS!
# ===========================================

print("🔐 Facebook Login Script")
print("=" * 60)

# Get fresh tokens
print("📡 Fetching login tokens...")
tokens = get_login_tokens()

if tokens and tokens['lsd'] and tokens['fb_dtsg']:
    print("✅ Tokens fetched successfully")
    cookies_dict = tokens['cookies']
    lsd = tokens['lsd']
    fb_dtsg = tokens['fb_dtsg']
    jazoest = tokens['jazoest']
else:
    print("⚠️ Using fallback tokens (may not work)")
    # Fallback tokens from the original request
    cookies_dict = {
        'datr': 'wAhaaoWSVzIXuO-SRKTMYDT_',
        'sb': 'wAhaatzRPpx34vixN9pPmnax',
        'm_pixel_ratio': '2.4740447998046875',
        'wd': '393x895',
        'fr': '0Gi8Oovt8kzQprsuq..BqWgjA..AAA.0.0.BqWgji.AWeWs4-38367KIwuz_Mcl3xyT8Y',
    }
    lsd = 'AdT278_mLXkqhH1J_qKBLtRPYlU'
    fb_dtsg = 'NAfwOUcx-SmYxhP_PXB3YiyL9qCba2rNYeAxkHR6rz5KyDnDQCycdzQ:0:0'
    jazoest = '25126'

# Generate encrypted password
print("🔑 Generating encrypted password...")
encrypted_password = generate_encrypted_password(ACTUAL_PASSWORD)
print(f"✅ Password encrypted: {encrypted_password[:50]}...")

# Build cookies
cookies = {
    'datr': cookies_dict.get('datr', ''),
    'sb': cookies_dict.get('sb', ''),
    'm_pixel_ratio': '2.4740447998046875',
    'wd': '393x895',
    'fr': cookies_dict.get('fr', ''),
}

# Headers
headers = {
    'authority': 'm.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'origin': 'https://m.facebook.com',
    'referer': 'https://m.facebook.com/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-full-version-list': '"Chromium";v="139.0.7339.0", "Not;A=Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"23076PC4BI"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
}

# Build the params payload
params_payload = build_params_payload(PHONE_NUMBER, encrypted_password)

# Convert params to JSON and URL encode it
params_json = json.dumps(params_payload)
encoded_params = urllib.parse.quote(params_json)

# Data payload
data = {
    '__aaid': '0',
    '__user': '0',
    '__a': '1',
    '__req': '7',
    '__hs': '20651.BP:wbloks_caa_pkg.2.0...0',
    'dpr': '3',
    '__ccg': 'GOOD',
    '__rev': '1043355061',
    '__s': '681how:9to5tg:3j0b2o',
    '__hsi': str(int(time.time() * 1000)) + str(int(time.time() * 100)),
    '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x67o1g8hw23E52q1ew2io0D24o1MUaE1Do1u81x82ewnE3fwww5NyE25w8W0Lo6-1CwOw5jw4JwzK0zo3jwea',
    'fb_dtsg': fb_dtsg,
    'jazoest': jazoest,
    'lsd': lsd,
    '__jssesw': '10',
    'params': encoded_params,
}

# Parameters for the URL
params = {
    'appid': 'com.bloks.www.bloks.caa.login.async.send_login_request',
    'type': 'action',
    '__bkv': '78a73311662c30ce39030ac75c7e304d4dd7b7baadc860957cb2e07cc0a31c2b',
}

print("\n" + "=" * 60)
print(f"📱 Phone/Email: {PHONE_NUMBER}")
print(f"🔑 Password: {'*' * len(ACTUAL_PASSWORD)}")
print(f"🌐 URL: https://m.facebook.com/async/wbloks/fetch/")
print("=" * 60 + "\n")

# Make the request
try:
    print("📤 Sending login request...")
    response = requests.post(
        'https://m.facebook.com/async/wbloks/fetch/',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
        timeout=30,
        allow_redirects=False
    )
    
    print(f"📡 Status Code: {response.status_code}")
    print(f"📝 Response Headers:")
    for key, value in response.headers.items():
        if key.lower() in ['content-type', 'content-length', 'location', 'x-fb-debug']:
            print(f"  {key}: {value}")
    
    print(f"\n📄 Response Body (first 1000 chars):")
    print("-" * 60)
    
    # Try to parse as JSON
    try:
        result = response.json()
        print(json.dumps(result, indent=2))
        
        # Analyze the response
        if 'data' in result:
            if 'caa_login_web' in result['data']:
                login_data = result['data']['caa_login_web']
                if 'error_code' in login_data and login_data['error_code']:
                    error_msg = login_data.get('error_message', {}).get('text', 'Unknown error')
                    print(f"\n❌ Login Failed: {error_msg}")
                else:
                    print("\n✅ Login Successful!")
                    if 'redirect_uri' in login_data:
                        print(f"📍 Redirect to: {login_data['redirect_uri']}")
        elif 'error' in result:
            print(f"\n❌ Error: {result.get('error', 'Unknown error')}")
        else:
            print("\n⚠️ Unexpected response format")
            
    except json.JSONDecodeError:
        print(response.text[:1000])
        
        # Check for common error indicators
        if "incorrect" in response.text.lower():
            print("\n❌ Login failed: Incorrect username or password")
            print("💡 Please check your credentials and try again")
        elif "checkpoint" in response.text.lower():
            print("\n⚠️ Login requires additional verification")
            print("💡 Please check your Facebook app for verification requests")
        elif "2fa" in response.text.lower() or "two factor" in response.text.lower():
            print("\n⚠️ Two-factor authentication required")
            print("💡 You need to complete 2FA verification")
        elif "rate" in response.text.lower() or "limit" in response.text.lower():
            print("\n⚠️ Rate limited. Please try again later")
        else:
            print("\n❌ Unknown error occurred")
    
    print("-" * 60)
    
except requests.exceptions.Timeout:
    print("❌ Request timed out. Please check your internet connection.")
except requests.exceptions.ConnectionError:
    print("❌ Connection error. Unable to reach Facebook.")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
