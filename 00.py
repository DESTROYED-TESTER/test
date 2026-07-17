import requests
import json

# Cookies
cookies = {
    'datr': 'wAhaaoWSVzIXuO-SRKTMYDT_',
    'sb': 'wAhaatzRPpx34vixN9pPmnax',
    'm_pixel_ratio': '2.4740447998046875',
    'wd': '393x895',
    'fr': '0Gi8Oovt8kzQprsuq..BqWgjA..AAA.0.0.BqWgji.AWeWs4-38367KIwuz_Mcl3xyT8Y',
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

# Query parameters
params = {
    'appid': 'com.bloks.www.bloks.caa.login.async.send_login_request',
    'type': 'action',
    '__bkv': '78a73311662c30ce39030ac75c7e304d4dd7b7baadc860957cb2e07cc0a31c2b',
}

# Build the nested JSON structure for the params field
params_data = {
    "params": json.dumps({
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
            "INTERNALlatency_qpl_instance_id": "178043855200348",
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
            "contact_point": "9907664835",
            "password": "#PWD_BROWSER:5:1784285413:AY9QALgu+IdwcRrOxEs7w7BLAPkUvvEQlEVm/hnSz9OuVBcD6IvEOiHQH1gX87tJ6T3k5gpPKfsmZP4JY8WKwTKPT+GciufJcmeEKEckL2jKJObObYGK6Qv9xXn4n+PvLOl/3Ara1Ok5oA==",
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
            "auth_secure_device_i": "",
            "client_known_key_hash": "",
            "has_whatsapp_installed": 0,
            "sso_token_map_json_string": "",
            "should_show_nested_nta_from_aymh": 0,
            "gms_incoming_call_retriever_eligibility": "client_not_supported",
            "password_contains_non_ascii": "false",
            "has_granted_read_contacts_permissions": 0,
            "has_granted_read_phone_permissions": 0,
            "app_manager_id": "",
            "aymh_accounts": [{
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
            }],
            "sso_accounts_auth_data": [],
            "blocked_uids": [],
            "network_bssid": None,
            "lois_settings": {
                "lois_token": ""
            },
            "aac": ""
        }
    })
}

# Form data
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
    '__hsi': '7663447342458262173',
    '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x67o1g8hw23E52q1ew2io0D24o1MUaE1Do1u81x82ewnE3fwww5NyE25w8W0Lo6-1CwOw5jw4JwzK0zo3jwea',
    'fb_dtsg': 'NAfwOUcx-SmYxhP_PXB3YiyL9qCba2rNYeAxkHR6rz5KyDnDQCycdzQ:0:0',
    'jazoest': '25126',
    'lsd': 'AdT278_mLXkqhH1J_qKBLtRPYlU',
    '__jssesw': '10',
    'params': params_data['params']
}

def check_login_status(response):
    """Check if login was successful by analyzing response"""
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code != 200:
        print("❌ Request failed - HTTP error")
        return False
    
    try:
        response_text = response.text
        
        # Check for common success indicators
        success_indicators = [
            '"success":true',
            '"status":"ok"',
            '"error":false',
            '"is_logged_in":true',
            '"login_success":true',
            'session_key',
            '"user_id"',
            '"access_token"',
            'c_user'  # Facebook cookie name for user ID
        ]
        
        # Check for failure indicators
        failure_indicators = [
            '"error":true',
            '"error_code"',
            '"error_msg"',
            '"error_message"',
            'incorrect password',
            'invalid credentials',
            'wrong password',
            'account locked',
            'challenge_required',
            'two_factor_required',
            'checkpoint_required'
        ]
        
        # Check if there's a cookie indicating login
        login_cookies = ['c_user', 'xs', 'datr', 'sb']
        has_login_cookies = any(cookie in response.cookies for cookie in login_cookies)
        
        print("\n🔍 Analyzing Response:")
        print("=" * 50)
        print(f"Response preview: {response_text[:500]}...\n")
        
        # Check for login success
        is_success = False
        
        # Check for success indicators in response
        for indicator in success_indicators:
            if indicator in response_text.lower():
                is_success = True
                print(f"✅ Found success indicator: {indicator}")
        
        # Check for failure indicators
        is_failure = False
        for indicator in failure_indicators:
            if indicator in response_text.lower():
                is_failure = True
                print(f"❌ Found failure indicator: {indicator}")
        
        # Try to parse JSON if possible
        try:
            json_response = response.json()
            print(f"\n📊 Parsed JSON Response:")
            print(json.dumps(json_response, indent=2))
            
            # Check specific JSON fields
            if 'error' in json_response:
                if json_response['error'] == True or json_response['error'] == 'true':
                    is_failure = True
                    print(f"❌ Error in response: {json_response.get('error_msg', json_response.get('error_message', 'Unknown error'))}")
            
            if 'success' in json_response:
                if json_response['success'] == True or json_response['success'] == 'true':
                    is_success = True
            
            if 'status' in json_response:
                if json_response['status'] in ['ok', 'success']:
                    is_success = True
                    
        except json.JSONDecodeError:
            print("⚠️ Response is not valid JSON")
        
        # Final verdict
        print("\n" + "=" * 50)
        print("📋 Login Verdict:")
        
        if is_success and not is_failure:
            print("✅ LOGIN SUCCESSFUL!")
            print(f"   Cookies: {dict(response.cookies)}")
            
            # Extract user ID if available
            if 'c_user' in response.cookies:
                print(f"   User ID: {response.cookies['c_user']}")
            
            # Try to extract session info from response
            if 'access_token' in response_text:
                import re
                token_match = re.search(r'"access_token":"([^"]+)"', response_text)
                if token_match:
                    print(f"   Access Token: {token_match.group(1)[:20]}...")
            
            return True
            
        elif is_failure:
            print("❌ LOGIN FAILED")
            
            # Try to extract error message
            error_messages = []
            for key in ['error_msg', 'error_message', 'error', 'message']:
                if key in response_text:
                    try:
                        import re
                        msg_match = re.search(rf'"{key}":"([^"]+)"', response_text)
                        if msg_match:
                            error_messages.append(msg_match.group(1))
                    except:
                        pass
            
            if error_messages:
                print(f"   Error: {error_messages[0]}")
            else:
                print("   Reason: Invalid credentials or account issue")
            
            return False
            
        elif has_login_cookies:
            print("✅ LOGIN SUCCESSFUL (detected by cookies)!")
            print(f"   Cookies set: {dict(response.cookies)}")
            return True
            
        else:
            print("⚠️ UNKNOWN STATUS - Need manual review")
            print("   Response may contain checkpoint or 2FA requirement")
            return False
            
    except Exception as e:
        print(f"❌ Error analyzing response: {e}")
        return False

# Make the request
try:
    response = requests.post(
        'https://m.facebook.com/async/wbloks/fetch/',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
        allow_redirects=False  # Don't follow redirects to see actual response
    )
    
    # Check login status
    login_success = check_login_status(response)
    
    # Additional check - try to verify with a subsequent request
    if login_success:
        print("\n🔐 Attempting to verify login with a test request...")
        
        # Try to access home page
        verify_headers = headers.copy()
        verify_headers['cookie'] = '; '.join([f"{k}={v}" for k, v in response.cookies.items()])
        
        verify_response = requests.get(
            'https://m.facebook.com/',
            headers=verify_headers,
            cookies=response.cookies,
            allow_redirects=False
        )
        
        print(f"Verification Status: {verify_response.status_code}")
        
        if verify_response.status_code == 200:
            print("✅ Login verified - Can access home page")
        elif verify_response.status_code == 302:
            location = verify_response.headers.get('Location', '')
            if 'login' not in location and 'checkpoint' not in location:
                print("✅ Login verified - Redirected to home/dashboard")
            else:
                print("⚠️ Login may require additional verification (2FA/checkpoint)")
        else:
            print("⚠️ Login verification inconclusive")
    
except requests.exceptions.RequestException as e:
    print(f"❌ Error making request: {e}")
