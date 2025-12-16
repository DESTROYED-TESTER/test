import random
import re
import sys
import time
import hashlib
import uuid
import urllib.request
import requests
import string
import os
import time,subprocess,platform,uuid,json
import random
import base64
import string
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
uid = input("Enter UID / Email: ").strip()
pw = input("Enter Password: ").strip()
enpass = "#PWD_BROWSER:0:{}:{}".format(int(time.time()), pw)

cookies = {
    'datr': '461BaaB95sc8Opemj4Ei4iHy',
    'sb': '461BaY5SglNKASxxZmHqT5cR',
    'm_pixel_ratio': '2.75',
    'wd': '393x895',
    'ps_l': '1',
    'ps_n': '1',
    'sfiu': 'AYh_h-D4-8-eP7eONjXJJav7Y0d0GZKwwweqUZG5ZpEUDd0vmUc0aQgwe-i6MgA220V9p7MU64MFjWHvclUc460MnoH9xngmDmZPEVQGqrl9-4SQMqMPjqZm4VKe6bT-r2x8ji_BXFVpHqRHx0D8e2ZyPPM8kz8uRQXI1oecFnw5Hvrgv7MlOJ55K6ORqoWghsNOb4jozPHH4AtxHb_Ohu-7MaPdtfplFKhlirLr0zoSgK2fbAXEenlUC_M6v1zSEr_Ol0-k1cAu-OQ8D3Q2m-HDPNZoOvagTSbQJ7-hLuTAvA',
    'fr': '0JK23wZvWx4ufdWJh..BpQa3j..AAA.0.0.BpQbEi.AWfVuqrdNfq7HLjRVQHNMJFyfKQ',
}

headers = {
    'authority': 'm.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    # 'cookie': 'datr=461BaaB95sc8Opemj4Ei4iHy; sb=461BaY5SglNKASxxZmHqT5cR; m_pixel_ratio=2.75; wd=393x895; ps_l=1; ps_n=1; sfiu=AYh_h-D4-8-eP7eONjXJJav7Y0d0GZKwwweqUZG5ZpEUDd0vmUc0aQgwe-i6MgA220V9p7MU64MFjWHvclUc460MnoH9xngmDmZPEVQGqrl9-4SQMqMPjqZm4VKe6bT-r2x8ji_BXFVpHqRHx0D8e2ZyPPM8kz8uRQXI1oecFnw5Hvrgv7MlOJ55K6ORqoWghsNOb4jozPHH4AtxHb_Ohu-7MaPdtfplFKhlirLr0zoSgK2fbAXEenlUC_M6v1zSEr_Ol0-k1cAu-OQ8D3Q2m-HDPNZoOvagTSbQJ7-hLuTAvA; fr=0JK23wZvWx4ufdWJh..BpQa3j..AAA.0.0.BpQbEi.AWfVuqrdNfq7HLjRVQHNMJFyfKQ',
    'origin': 'https://m.facebook.com',
    'referer': 'https://m.facebook.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Chromium";v="107.0.5304.74", "Not=A?Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"23076PC4BI"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 15; 23076PC4BI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
}

params = {
    'appid': 'com.bloks.www.bloks.caa.login.async.send_login_request',
    'type': 'action',
    '__bkv': '5870af81e45750eb22160e3fe74a22f1ec7a22fa20d66f6fa34875f44676e658',
}

data = {
    'aaid': '0',
    'user': '0',
    'a': '1',
    'req': '4',
    'hs': '20438.BP:wbloks_caa_pkg.2.0...0',
    'dpr': '3',
    'ccg': 'EXCELLENT',
    'rev': '1031148438',
    's': ':89f4eh:fxi6ar',
    'hsi': '7584537852578368255',
    'dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x60lW4o0wW1gCwjE0AC09Mx60se2G0pS0ny0oi0zE5W0Y81soG0xo2ewbS1LwpEcE1kU1bo8Xw8S0QU3yw',
    'fb_dtsg': 'NAfsobNUnLNU3HQhHZfkJqASamjmiSJnpXDmlb2342eF7dlyTS8BSvw:0:0',
    'jazoest': '25050',
    'lsd': 'AdF3FM2CtGc',
    'params': json.dumps({
        "params": {
            "server_params": {
                "credential_type": "password",
                "username_text_input_id": "ywkgyx:66",
                "password_text_input_id": "ywkgyx:67",
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
                "is_vanilla_password_page_empty_password": 0,
                "left_nav_button_action": "NONE",
                "INTERNALlatency_qpl_marker_id": 36707139,
                "INTERNALlatency_qpl_instance_id": "211055280900203",
                "device_id": None,
                "family_device_id": None,
                "waterfall_id": "ea8c742b-b345-4455-ae4e-a57021bc0681",
                "offline_experiment_group": None,
                "layered_homepage_experiment_group": None,
                "is_platform_login": 0,
                "is_from_logged_in_switcher": 0,
                "is_from_logged_out": 0,
                "access_flow_version": "pre_mt_behavior"
            },
            "client_input_params": {
                "machine_id": "",
                "cloud_trust_token": None,
                "block_store_machine_id": "",
                "zero_balance_state": "",
                "contact_point": "9641364255",
                "password": "#PWD_BROWSER:5:1765912899:AbtQAJcQxu+pSgFATsNW04B8mOK4XCRYJoU6j4SsKrl47yQqSDH/IKszEKtdr6umgVeNi1Q6tfFVqHTQXxt7vbK+joBG7bhIe4EFPPH0Hnzihhs8Bg/SxpqW7IZpjpQwcUmkcO0RooBPB8DkQ==",
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
                "network_bssid": None,
                "lois_settings": {
                    "lois_token": ""
                },
                "aac": ""
            }
        }
    })
}

response = requests.post('https://www.facebook.com/async/wbloks/fetch/', params=params, cookies=cookies, headers=headers, data=data)

print("Status code:", response.status_code)
print("Response URL:", response.url)
print("Status Code:", response.status_code)
print("Reason:", response.reason)
print("Response Text:", response.text)
print("\n--- RESPONSE COOKIES ---")
if response.cookies:
    for k, v in response.cookies.get_dict().items():
        print(f"{k} = {v}")
else:
    print("No cookies set by server")



