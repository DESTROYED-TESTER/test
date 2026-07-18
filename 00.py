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
import time,subprocess,platform,uuid
import random
import base64
import string
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
uid = "9907854044"
pw = "990785"
Session = requests.Session()
#head = {"authority":"m.prod.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","accept-language":"en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7","cache-control":"max-age=0","dpr":"3","sec-ch-prefers-color-scheme":"light","sec-fetch-dest":"document","sec-fetch-mode":"navigate","sec-fetch-site":"none","sec-fetch-user":"?1","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0","viewport-width":"980"}
#requu12 = Session.get('https://www.facebook.com/',headers=head)
#free_fb = Session.get('https://touch.facebook.com/')
free_fb = Session.get('https://touch.facebook.com/').text
#datr = requu12.cookies.get('datr')
#sb = requu12.cookies.get('sb')
#fr = requu12.cookies.get('fr')
#log_data = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(requu1.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(requu1.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': uid, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': '0', 'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw), 'bi_wvdp': '', 'fb_dtsg': '', 'jazoest': re.search('name="jazoest" value="(.*?)"',str(requu1.text)).group(1), 'lsd': re.search('name="lsd" value="(.*?)"',str(requu1.text)).group(1), '__dyn': '', '__csr': '', '__req': random.choice(["1","2","3","4","5","6","7","8","9","0"]), '__fmt': '0', '__a': '',  '__user': '0'}
log_data = {
    "aaid": 0,
    "user": 0,
    "a": 1,
    "req": 7,
    "hs": "20652.BP:wbloks_caa_pkg.2.0...0",
    "dpr": 3,
    "ccg": "GOOD",
    "rev": 1043419488,
    "s": "yiar42:dl594l:id4lh8",
    "hsi": 7663779509929542939,
    "dyn": "0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x67o1g8hw23E52q1ew2io0D24o1MUaE1Do1u81x82ewnE3fwww5NyE25w8W0Lo6-1CwOw5jw4JwzK0zo3jwea",
    "fb_dtsg": "NAfy0gmdDEgMdILhHKzbzGdZhtu1YFuk8v7i_Ze-eyyWQFkJN612uVQ:0:0",
    "jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
    "lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
    "params": json.dumps({
        "params": json.dumps({
            "server_params": {
                "credential_type": "password",
                "username_text_input_id": "3hogww:58",
                "password_text_input_id": "3hogww:59",
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
                "INTERNALlatency_qpl_instance_id": "21109366400348",
                "device_id": None,
                "family_device_id": None,
                "waterfall_id": "9e2fecbe-5cb2-420e-ab38-f0a16f9342d8",
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
#cookies ={"datr": datr, "sb": sb, "m_pixel_ratio": "2.75", "wd": "393x851", "fr": fr}
#url = "https://edge-mqtt.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
url = 'https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&__bkv=78a73311662c30ce39030ac75c7e304d4dd7b7baadc860957cb2e07cc0a31c2b'
headers = {
    'authority': 'limited.facebook.com',
    'accept': '/',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'datr=AvxaauBxe8J2e6uqNRe7Ks5u; sb=AvxaanntJgRoS-6c3x6h_Z-w; m_pixel_ratio=2.75; wd=393x851; ps_l=1; ps_n=1; fr=0mN3NySo4ygtsuEdo..BqWvwC..AAA.0.0.BqWvwc.AWf9_qxR9LNotvAZnbuzCekImP0',
    'origin': 'https://limited.facebook.com',
    'referer': 'https://limited.facebook.com/login/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-asbd-id': '359341',
    'x-fb-lsd': 'AdSNT0fGVLz2A_OHQKjrDgDTwkI',
    'x-requested-with': 'XMLHttpRequest',
    'x-response-format': 'JSONStream',
}

response = Session.post(url,data=log_data,headers=headers,allow_redirects=False)
print(response.text)
print(response)
#print(response.status_code)
#print(response.text)
# Check login success
log_cookies = Session.cookies.get_dict().keys()
if "c_user" in log_cookies:
    print('\033[1;92m OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK ')
elif 'checkpoint' in log_cookies:
    print('\033[1;92m CP CP  CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP CP')
