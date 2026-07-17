import requests
import json
import time
import base64
import urllib.parse
from bs4 import BeautifulSoup

def generate_encrypted_password(password, timestamp=None):
    """Generate Facebook's password encryption format"""
    if timestamp is None:
        timestamp = int(time.time())
    encoded = base64.b64encode(password.encode()).decode()
    return f"#PWD_BROWSER:5:{timestamp}:{encoded}"

def get_login_tokens():
    """Extract fresh tokens from Facebook login page"""
    try:
        # Get the login page
        login_url = 'https://m.facebook.com/login/'
        headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36'
        }
        
        response = requests.get(login_url, headers=headers)
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
        
        # Extract datr cookie
        datr = None
        for cookie in response.cookies:
            if cookie.name == 'datr':
                datr = cookie.value
                break
        
        return {
            'lsd': lsd,
            'fb_dtsg': fb_dtsg,
            'jazoest': jazoest,
            'datr': datr,
            'sb': response.cookies.get('sb', ''),
            'wd': response.cookies.get('wd', '')
        }
    except Exception as e:
        print(f"⚠️ Error extracting tokens: {e}")
        return None

# ============== SET YOUR CREDENTIALS HERE ==============
PHONE_NUMBER = "9382026415"  # Your phone number or email
ACTUAL_PASSWORD = "93820264"  # <-- CHANGE THIS!
# ======================================================

# Get fresh tokens
tokens = get_login_tokens()
if not tokens or not tokens['lsd'] or not tokens['fb_dtsg']:
    print("❌ Failed to get login tokens. Please check your internet connection.")
    print("💡 Using fallback tokens...")
    # Fallback tokens (may not work)
    tokens = {
        'lsd': 'AdT278_mLXkqhH1J_qKBLtRPYlU',
        'fb_dtsg': 'NAfwOUcx-SmYxhP_PXB3YiyL9qCba2rNYeAxkHR6rz5KyDnDQCycdzQ:0:0',
        'jazoest': '25126',
        'datr': 'wAhaaoWSVzIXuO-SRKTMYDT_'
    }

# Generate encrypted password
encrypted_password = generate_encrypted_password(ACTUAL_PASSWORD)

# Headers
headers = {
    'authority': 'm.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'cookie': f'datr={tokens["datr"]}; sb=; m_pixel_ratio=2.4740447998046875; wd=393x895; fr=',
    'origin': 'https://m.facebook.com',
    'referer': 'https://m.facebook.com/',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
}

# Build the params structure
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
            "INTERNAL__latency_qpl_instance_id": str(int(time.time() * 1000)),
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

# Convert params to JSON string
params_json = json.dumps(params_data)
encoded_params = urllib.parse.quote(params_json)

# Generate a unique hsi value
hsi_value = str(int(time.time() * 1000)) + str(int(time.time() * 100))

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
    'hsi': hsi_value,
    'dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x67o1g8hw23E52q1ew2io0D24o1MUaE1Do1u81x82ewnE3fwww5NyE25w8W0Lo6-1CwOw5jw4JwzK0zo3jwea',
    'fb_dtsg': tokens['fb_dtsg'],
    'jazoest': tokens['jazoest'],
    'lsd': tokens['lsd'],
    'jssesw': '10',
    'params': encoded_params
}

# URL with the bkv parameter
url = 'https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&__bkv=78a73311662c30ce39030ac75c7e304d4dd7b7baadc860957cb2e07cc0a31c2b'

print("🔐 Attempting to login...")
print(f"📱 Phone: {PHONE_NUMBER}")
print(f"🔑 Password: {ACTUAL_PASSWORD[:3]}***")
print("-" * 50)

# Debug: Print the request data (without password for security)
debug_data = data.copy()
debug_data['params'] = debug_data['params'][:100] + '...' if len(debug_data['params']) > 100 else debug_data['params']
print("📤 Request Data (truncated):")
print(json.dumps(debug_data, indent=2))
print("-" * 50)

try:
    # Make the request with proper error handling
    response = requests.post(
        url, 
        headers=headers, 
        data=data,
        timeout=30,
        allow_redirects=False
    )
    
    print(f"📡 Status Code: {response.status_code}")
    print(f"📝 Response Headers:")
    for key, value in response.headers.items():
        if key.lower() in ['content-type', 'content-length', 'location']:
            print(f"  {key}: {value}")
    
    print(f"📄 Response Length: {len(response.text)} characters")
    
    # Try different response parsers
    if response.status_code == 500:
        print("\n❌ Server Error (500) - This usually means:")
        print("  1. The __bkv token is expired or invalid")
        print("  2. The request format has changed")
        print("  3. Facebook's API is temporarily down")
        print("\n💡 Solutions:")
        print("  - Get fresh __bkv token from a browser session")
        print("  - Use a different login endpoint")
        print("  - Wait and try again later")
        print("\n📄 Raw Response:")
        print(response.text[:500])
        
    elif response.status_code == 302 or response.status_code == 303:
        print("\n✅ Redirect detected - This might be a successful login!")
        redirect_url = response.headers.get('Location', '')
        print(f"📍 Redirect to: {redirect_url}")
        
    else:
        # Try to parse as JSON
        try:
            result = response.json()
            print("\n📊 Response:")
            print(json.dumps(result, indent=2))
            
            if 'error' in result:
                error_msg = result.get('error', {})
                if isinstance(error_msg, dict):
                    error_text = error_msg.get('message', str(error_msg))
                else:
                    error_text = str(error_msg)
                print(f"\n❌ Error: {error_text}")
                
                if "incorrect" in error_text.lower() or "invalid" in error_text.lower():
                    print("\n💡 Check your password - it appears to be incorrect")
                    
            elif 'data' in result:
                print("\n✅ Request processed successfully!")
                if 'caa_login_web' in result.get('data', {}):
                    login_data = result['data']['caa_login_web']
                    if 'error_code' in login_data:
                        print(f"\n⚠️ Login error: {login_data.get('error_message', {}).get('text', 'Unknown error')}")
                    else:
                        print("\n🎉 Login successful!")
                        
        except json.JSONDecodeError:
            print("\n📄 Raw Response (non-JSON):")
            print(response.text[:500])
            
            if "incorrect" in response.text.lower():
                print("\n❌ Login failed: Incorrect username or password")
            elif "checkpoint" in response.text.lower():
                print("\n⚠️ Login requires additional verification")
            elif "2fa" in response.text.lower():
                print("\n⚠️ Two-factor authentication required")
                
except requests.exceptions.RequestException as e:
    print(f"❌ Request failed: {e}")
