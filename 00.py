import requests
import json
import time
import base64
import urllib.parse

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

# ============== SET YOUR CREDENTIALS HERE ==============
PHONE_NUMBER = "9382502976"  # Your phone number
ACTUAL_PASSWORD = "93825029"  # <-- CHANGE THIS!
# ======================================================

# Generate encrypted password
encrypted_password = generate_encrypted_password(ACTUAL_PASSWORD)

# Headers from the cURL request
headers = {
    'authority': 'm.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'cookie': 'datr=wAhaaoWSVzIXuO-SRKTMYDT_; sb=wAhaatzRPpx34vixN9pPmnax; m_pixel_ratio=2.4740447998046875; wd=393x895; fr=0Gi8Oovt8kzQprsuq..BqWgjA..AAA.0.0.BqWgji.AWeWs4-38367KIwuz_Mcl3xyT8Y',
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

# Build the data payload
# The params structure from the cURL request
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
            "INTERNAL__latency_qpl_instance_id": "178043855200348",
            "device_id": None,
            "family_device_id": None,
            "waterfall_id": "1fff9e97-0cdb-4e73-8bbc-ee8abc8fa986",
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
            "contact_point": PHONE_NUMBER,
            "password": encrypted_password,
            "accounts_list": [],
            "fb_ig_device_id": [],
            "secure_family_device_id": "",
            "encryptd_msisdn": "",
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
            "aymh_accounts": [
                {
                    "id": "",
                    "profiles": {
                        "id": {
                            "user_id": "",
                            "name": "",
                            "profile_picture_url": "",
                            "small_profile_picture_url": None,
                            "notification_count": 0,
                            "credential_type": "none",
                            "token": "",
                            "last_access_time": 0,
                            "is_derived": 0,
                            "username": "",
                            "password": "",
                            "has_smartlock": 0,
                            "account_center_id": "",
                            "account_source": "",
                            "credentials": [],
                            "nta_eligibility_reason": None,
                            "from_accurate_privacy_result": 0,
                            "dbln_validated": 0
                        }
                    }
                }
            ],
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

# Convert params to JSON string and then URL encode it
params_json = json.dumps(params_data)
encoded_params = urllib.parse.quote(params_json)

# Build the form data
data = {
    'aaid': '0',
    'user': '0',
    'a': '1',
    'req': '7',
    'hs': '20651.BP:wbloks_caa_pkg.2.0...0',
    'dpr': '3',
    'ccg': 'GOOD',
    'rev': '1043355061',
    's': '681how:9to5tg:3j0b2o',
    'hsi': '7663447342458262173',
    'dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x67o1g8hw23E52q1ew2io0D24o1MUaE1Do1u81x82ewnE3fwww5NyE25w8W0Lo6-1CwOw5jw4JwzK0zo3jwea',
    'fb_dtsg': 'NAfwOUcx-SmYxhP_PXB3YiyL9qCba2rNYeAxkHR6rz5KyDnDQCycdzQ:0:0',
    'jazoest': '25126',
    'lsd': 'AdT278_mLXkqhH1J_qKBLtRPYlU',
    'jssesw': '10',
    'params': encoded_params
}

# Make the request
url = 'https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&__bkv=78a73311662c30ce39030ac75c7e304d4dd7b7baadc860957cb2e07cc0a31c2b'

print("🔐 Attempting to login...")
print(f"📱 Phone: {PHONE_NUMBER}")
print(f"🔑 Password: {ACTUAL_PASSWORD[:3]}***")
print("-" * 50)

try:
    response = requests.post(url, headers=headers, data=data)
    
    print(f"📡 Status Code: {response.status_code}")
    print(f"📝 Response Length: {len(response.text)} characters")
    
    # Try to parse the response
    try:
        result = response.json()
        print("\n📊 Response:")
        print(json.dumps(result, indent=2))
        
        # Check for errors
        if isinstance(result, dict):
            if 'error' in result:
                print(f"\n❌ Error: {result.get('error')}")
            elif 'data' in result:
                print("\n✅ Request successful!")
            else:
                print("\n⚠️ Unexpected response format")
                
    except json.JSONDecodeError:
        # If not JSON, print raw response
        print(f"\n📄 Raw Response (first 500 chars):")
        print(response.text[:500])
        
        # Check for common error indicators
        if "incorrect" in response.text.lower():
            print("\n❌ Login failed: Incorrect username or password")
        elif "checkpoint" in response.text.lower():
            print("\n⚠️ Login requires additional verification (checkpoint)")
        elif "2fa" in response.text.lower() or "two factor" in response.text.lower():
            print("\n⚠️ Two-factor authentication required")
        else:
            print("\n❌ Login failed. Please check your credentials.")
            
except requests.exceptions.RequestException as e:
    print(f"❌ Request failed: {e}")
