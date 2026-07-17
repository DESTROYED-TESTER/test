import json
import requests
import time
import re

pw = "9382852655"
uid = "9382852655"

# 1. Ensure these cookies correspond to the exact browser session you pulled fb_dtsg from!
cookies = {
    'datr': 'wAhaaoWSVzIXuO-SRKTMYDT_',
    'sb': 'wAhaatzRPpx34vixN9pPmnax',
    'm_pixel_ratio': '2.4740447998046875',
    'wd': '393x895',
    'fr': '0Gi8Oovt8kzQprsuq..BqWgjA..AAA.0.0.BqWgji.AWeWs4-38367KIwuz_Mcl3xyT8Y',
}

# 2. Re-aligned user agents and Client Hints to ensure structural consistency
headers = {
    'authority': 'm.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'origin': 'https://m.facebook.com',
    'referer': 'https://m.facebook.com/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"23076PC4BI"',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36',
}

params = {
    'appid': 'com.bloks.www.bloks.caa.login.async.send_login_request',
    'type': 'action',
    '__bkv': '78a73311662c30ce39030ac75c7e304d4dd7b7baadc860957cb2e07cc0a31c2b',
}

# 3. Fixed the broken format string syntax bug
timestamp = str(int(time.time()))
formatted_password = f"#PWD_BROWSER:0:{timestamp}:{pw}"

# Inner Bloks Layer
client_input_params = {
    "machine_id": "",
    "cloud_trust_token": None,
    "block_store_machine_id": "",
    "zero_balance_state": "",
    "contact_point": uid,
    "password": formatted_password,
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
    "aymh_accounts": [],
    "sso_accounts_auth_data": [],
    "blocked_uids": [],
    "network_bssid": None,
    "lois_settings": {"lois_token": ""},
    "aac": ""
}

server_params = {
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
}

# Complete Outer Layer Construction
payload = {
    "__aaid": "0",
    "__user": "0", 
    "__a": "1",
    "__req": "7",
    "__hs": "20651.BP:wbloks_caa_pkg.2.0...0",
    "dpr": "3",
    "__ccg": "GOOD",
    "__rev": "1043355061",
    "__s": "681how:9to5tg:3j0b2o",
    "__hsi": "7663447342458262173",
    "__dyn": "0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x67o1g8hw23E52q1ew2io0D24o1MUaE1Do1u81x82ewnE3fwww5NyE25w8W0Lo6-1CwOw5jw4JwzK0zo3jwea",
    "fb_dtsg": "NAfwOUcx-SmYxhP_PXB3YiyL9qCba2rNYeAxkHR6rz5KyDnDQCycdzQ:0:0", # MUST match active datr session
    "jazoest": "25126",
    "lsd": "AdT278_mLXkqhH1J_qKBLtRPYlU",
    "__jssesw": "10",
    "params": json.dumps({
        "params": json.dumps({
            "server_params": server_params,
            "client_input_params": client_input_params
        })
    })
}

# Send the request
response = requests.post(
    'https://facebook.com',
    params=params,
    cookies=cookies,
    headers=headers,
    data=payload
)

response_text = response.text
response_cookies = response.cookies.get_dict()

print(f"HTTP Code: {response.status_code}")

# Improved response verification structural checks
if response.status_code == 200:
    if "c_user" in response_cookies:
        print(f"STATUS: LOGIN OK | UID: {response_cookies.get('c_user')}")
    elif "checkpoint" in response_cookies or "checkpoint" in response_text:
        print("STATUS: ERROR | REASON: Account Checkpoint / 2FA Verification Required")
    else:
        # Check inside raw Bloks structured payload wrappers
        error_match = re.search(r'"error_message":"([^"]+)"', response_text)
        title_match = re.search(r'"error_title":"([^"]+)"', response_text)
        
        if error_match:
            title = title_match.group(1) if title_match else "Authentication Rejected"
            print(f"STATUS: ERROR | REASON: {title} - {error_match.group(1)}")
        elif "login_error" in response_text or "display_message" in response_text:
            print("STATUS: ERROR | REASON: Invalid credentials or session token mismatched")
        else:
            # Output raw payload fragment if structure remains unique
            print("STATUS: ERROR | REASON: Unexpected response structure from server.")
            print(f"Snippet: {response_text[:300]}")
else:
    print(f"STATUS: HTTP FAILURE | {response.status_code}")
