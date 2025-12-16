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
    'datr': 'OpqVaPyImvfQapu_w36Tb6w9',
    'sb': 'OpqVaFnrZ4qPlR6kiDeA96JW',
    'ps_l': '1',
    'ps_n': '1',
    'm_pixel_ratio': '2',
    'pas': '100061465976024%3A2Br3qvc3Zi',
    'dpr': '1',
    'wd': '400x686',
    'fr': '14GtYkQTpeiC1REGX.AWd_vhrUYobjO8DuKiC98oM3pinpfd5k47Y8B0U3tm9fzubqdxc.BpQbzh..AAA.0.0.BpQcBv.AWe68x2KLB5_lcvMawf-W-Z4I_A',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,bn;q=0.6',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'origin': 'https://m.facebook.com',
    'priority': 'u=1, i',
    'referer': 'https://m.facebook.com/login/?next=https%3A%2F%2Fm.facebook.com%2Fasync%2Fwbloks%2Ffetch%2F%3Fappid%3Dcom.bloks.www.bloks.caa.login.async.send_login_request%26type%3Daction%26__bkv%3D5870af81e45750eb22160e3fe74a22f1ec7a22fa20d66f6fa34875f44676e658%26wtsid%3Drdr_0EQ7sA15easbCjdcs',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="143.0.7499.41", "Chromium";v="143.0.7499.41", "Not A(Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Nexus 5"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"6.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'datr=OpqVaPyImvfQapu_w36Tb6w9; sb=OpqVaFnrZ4qPlR6kiDeA96JW; ps_l=1; ps_n=1; m_pixel_ratio=2; pas=100061465976024%3A2Br3qvc3Zi; dpr=1; wd=400x686; fr=14GtYkQTpeiC1REGX.AWd_vhrUYobjO8DuKiC98oM3pinpfd5k47Y8B0U3tm9fzubqdxc.BpQbzh..AAA.0.0.BpQcBv.AWe68x2KLB5_lcvMawf-W-Z4I_A',
}

params = {
    'appid': 'com.bloks.www.bloks.caa.login.async.send_login_request',
    'type': 'action',
    '__bkv': '5870af81e45750eb22160e3fe74a22f1ec7a22fa20d66f6fa34875f44676e658',
}

data = {
    '__aaid': '0',
    '__user': '0',
    '__a': '1',
    '__req': '8',
    '__hs': '20438.BP:wbloks_caa_pkg.2.0...0',
    'dpr': '3',
    '__ccg': 'GOOD',
    '__rev': '1031154218',
    '__s': 'bf72tk:w7pc92:xr04hw',
    '__hsi': '7584554703271452991',
    '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x60lW4o0wW1gCwjE0AC09Mx60se2G0pS0ny0oi0zE5W0Y81soG0xo2ewbS1LwpEcE1kU1bo8Xw8S0QU3yw',
    'fb_dtsg': 'NAfswT-5iGUy0OIXErmeAkhJWRQzHOGo86gkifn919S8eu18jRyx1jg:0:0',
    'jazoest': '24940',
    'lsd': 'AdEt_BZHc1I',
    'params': '{"params":"{\\"server_params\\":{\\"next_uri\\":\\"https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&__bkv=5870af81e45750eb22160e3fe74a22f1ec7a22fa20d66f6fa34875f44676e658&wtsid=rdr_0EQ7sA15easbCjdcs\\",\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"18ran1:68\\",\\"password_text_input_id\\":\\"18ran1:69\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":1,\\"reg_flow_source\\":\\"aymh_single_profile_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_aymh\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"two_step_login_type\\":\\"one_step_login\\",\\"is_vanilla_password_page_empty_password\\":0,\\"left_nav_button_action\\":\\"BACK\\",\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"7517660500366\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"95dbfe51-b1fd-402e-9a58-1be48dc6eb61\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"cloud_trust_token\\":null,\\"block_store_machine_id\\":\\"\\",\\"zero_balance_state\\":\\"\\",\\"contact_point\\":\\"100094455925591\\",\\"password\\":\\"#PWD_BROWSER:5:1765916791:AbtQALCVa1diVxPwnHJK76jD6N5WTUPakhEdlN1nLHxQ+DdK1RCRNkJ5HOxHz+NrFbMTA7jZcbs77giomRFV8MDrvlClCIuMu/kmzWXdo/52u4KMaWS8meh1A+2cuf6Pj4EIr4NIl/dC/w==\\",\\"accounts_list\\":[{\\"uid\\":\\"100061465976024\\",\\"credential_type\\":\\"nonce\\",\\"token\\":\\"\\",\\"cloud_identifier\\":\\"\\",\\"obfuscated_token\\":null,\\"username\\":\\"\\",\\"encrypted_password\\":\\"\\",\\"name\\":\\"\\",\\"profile_pic_url\\":\\"\\",\\"small_profile_pic_url\\":null,\\"metadata\\":{\\"last_access_time\\":0,\\"FXAccessLibraryAccountSavedSource\\":\\"\\",\\"previously_authenticated_nonce\\":\\"\\",\\"source_device_id\\":\\"\\"},\\"email\\":\\"\\",\\"account_source\\":\\"\\",\\"sim_phone_number\\":null,\\"encrypted_user_id\\":\\"\\",\\"lva_flow_type\\":null,\\"blob\\":\\"\\"}],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":1,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":1,\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"aymh_accounts\\":[{\\"id\\":\\"100061465976024\\",\\"profiles\\":{\\"100061465976024\\":{\\"credential_type\\":\\"nonce\\",\\"name\\":\\"Jaan Amar\\",\\"is_derived\\":0,\\"last_access_time\\":0,\\"notification_count\\":0,\\"password\\":\\"\\",\\"profile_picture_url\\":\\"https://scontent-ccu2-1.xx.fbcdn.net/v/t1.30497-1/453178253_471506465671661_2781666950760530985_n.png?stp=dst-png_s720x720&_nc_cat=1&ccb=1-7&_nc_sid=dfcde4&_nc_ohc=3VTDhbZZG98Q7kNvwH8iUz3&_nc_oc=AdnBmoel6-vyMY7ywJik1ESqt4VfHFvpe9uZnBCdOaDX_Hx4lR5XwoF2oRzJAgyTJ-k&_nc_zt=24&_nc_ht=scontent-ccu2-1.xx&oh=00_AflqA0FRGJe8hukDvXiQ2v-Q8gU1yqf9P-xGFNJ_kQe7LQ&oe=69691BBA\\",\\"small_profile_picture_url\\":null,\\"token\\":\\"\\",\\"user_id\\":\\"100061465976024\\",\\"username\\":\\"\\",\\"has_smartlock\\":0,\\"account_center_id\\":\\"100061465976024\\",\\"account_source\\":\\"\\",\\"credentials\\":[{\\"credential_type\\":\\"nonce\\",\\"token\\":\\"\\"}],\\"nta_eligibility_reason\\":null,\\"from_accurate_privacy_result\\":0,\\"encrypted_user_id\\":null,\\"dbln_validated\\":0}}}],\\"network_bssid\\":null,\\"lois_settings\\":{\\"lois_token\\":\\"\\"},\\"aac\\":\\"\\"}}"}',
}

response = requests.post('https://m.facebook.com/async/wbloks/fetch/', params=params, cookies=cookies, headers=headers, data=data)

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



