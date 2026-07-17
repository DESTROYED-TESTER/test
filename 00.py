import json
import requests
import os,sys,re,time,uuid,json,string,random,base64,platform
pw = "9382852655"
uid = "9382852655"
cookies = {
    'datr': 'wAhaaoWSVzIXuO-SRKTMYDT_',
    'sb': 'wAhaatzRPpx34vixN9pPmnax',
    'm_pixel_ratio': '2.4740447998046875',
    'wd': '393x895',
    'fr': '0Gi8Oovt8kzQprsuq..BqWgjA..AAA.0.0.BqWgji.AWeWs4-38367KIwuz_Mcl3xyT8Y',
}

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

params = {
    'appid': 'com.bloks.www.bloks.caa.login.async.send_login_request',
    'type': 'action',
    '__bkv': '78a73311662c30ce39030ac75c7e304d4dd7b7baadc860957cb2e07cc0a31c2b',
}

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
    "fb_dtsg": "NAfwOUcx-SmYxhP_PXB3YiyL9qCba2rNYeAxkHR6rz5KyDnDQCycdzQ:0:0",
    "jazoest": "25126",
    "lsd": "AdT278_mLXkqhH1J_qKBLtRPYlU",
    "__jssesw": "10",
    "params": json.dumps({
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
                "contact_point": uid,
                "password": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),
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
    })
}

# Make the request
response = requests.post(
    'https://m.facebook.com/async/wbloks/fetch/',
    params=params,
    cookies=cookies,
    headers=headers,
    data=payload
)

# Parse response status
response_text = response.text

if response.status_code == 200:
    # Check for successful session markers
    if "c_user" in response.cookies or "checkpoint" in response.cookies:
        if "checkpoint" in response.cookies:
            print("STATUS: 2FA / CHECKPOINT REQUIRED")
        else:
            print(f"STATUS: LOGIN OK | UID: {response.cookies.get('c_user')}")
            print(f"COOKIES: {response.cookies.get_dict()}")
            
    # If cookies aren't set, parse the text payload for Facebook Bloks error data
    elif "error_title" in response_text or "error_message" in response_text:
        title = re.search(r'"error_title":"([^"]+)"', response_text)
        message = re.search(r'"error_message":"([^"]+)"', response_text)
        
        err_title = title.group(1) if title else "Login Error"
        err_msg = message.group(1) if message else "Unknown Reason"
        
        print(f"STATUS: ERROR | REASON: {err_title} - {err_msg}")
        
    elif "checkpoint" in response_text:
        print("STATUS: ERROR | REASON: Account Checkpoint / Verification Required")
        
    elif "login_error" in response_text:
        print("STATUS: ERROR | REASON: Invalid credentials or disabled account")
        
    else:
        # Fallback regex lookups for localized raw strings in Bloks payload
        msg_clean = re.search(r'\\"message\\":\\"([^\\"]+)\\"', response_text)
        if msg_clean:
            print(f"STATUS: ERROR | REASON: {msg_clean.group(1)}")
        else:
            print("STATUS: ERROR | REASON: Unknown structural response (Check parameters/cookies)")
else:
    print(f"STATUS: HTTP ERROR | CODE: {response.status_code}")
