import requests
import re
import json
import time

# Start a session
Session = requests.Session()

# Step 1: Fetch the initial page to get dynamic values like jazoest and lsd
free_fb = Session.get('https://touch.facebook.com/').text

# Step 2: Extract dynamic tokens from the page
jazoest = re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1)
lsd = re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1)

# Step 3: Prepare the data payload with login details (username, password, etc.)
data2 = {
    '__aaid': '0',
    '__user': '0',
    '__a': '1',
    '__req': 'f',
    '__hs': '20058.BP:wbloks_caa_pkg.2.0..0.0',
    'dpr': '3',
    '__ccg': 'EXCELLENT',
    '__rev': '1018538768',
    '__s': '3o19vx:6unffp:0ifzbp',
    '__hsi': '7443521229922239744',
    '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13w9y1DxW0Oohw5ux60Vo1a852q1ew2io0D24o1MUaE1Do1u81x82ewnE3Mw4WwSyE25w8W0Lo6-1CwOw5jw4JwzK0zo3jw',
    '__csr': '',
    'fb_dtsg': 'NAcOlfpCOM2BFnghClV_Fbk2SejAMCvE1gYRFgP4Eh4s03fmjrbDwEA:0:0',
    'jazoest': jazoest,
    'lsd': lsd,
    'params': json.dumps({
        "params": json.dumps({
            "server_params": {
                "credential_type": "password",
                "username_text_input_id": "yzmero:69",
                "password_text_input_id": "yzmero:70",
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
                "is_from_password_entry_page": 0,
                "is_from_assistive_id": 0,
                "is_from_msplit_fallback": 0,
                "INTERNALlatency_qpl_marker_id": 36707139,
                "INTERNALlatency_qpl_instance_id": "211568211600414",
                "device_id": None,
                "family_device_id": None,
                "waterfall_id": "9b12f14d-e937-4714-94bf-015a5d6b4db3",
                "offline_experiment_group": None,
                "layered_homepage_experiment_group": None,
                "is_platform_login": 0,
                "is_from_logged_in_switcher": 0,
                "is_from_logged_out": 0,
                "access_flow_version": "F2_FLOW"
            },
            "client_input_params": {
                "machine_id": "",
                "contact_point": '61556968163616',
                "password": "#PWD_BROWSER:0:{}:{}".format(str(int(time.time())), '939948'),
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
                "lois_settings": {"lois_token": "", "lara_override": ""}
            }
        })
    })
}

# Step 4: Define headers
headers = {
    'authority': 'm.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'origin': 'https://m.facebook.com',
    'referer': 'https://m.facebook.com/login/?privacy_mutation_token=...',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-fetch-dest': 'empty',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

# Step 5: Define the login URL
url = "https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&__bkv=e83b925010f428c02e9a28277ebe1ac259315059ef636d91d59afb3de1f921fa"

# Step 6: Send the POST request
response = Session.post(url, data=data2, headers=headers)

# Step 7: Check for successful login
if response.status_code == 200 and "Login approval" not in response.text:
    print("Login successful!")
    # Extract cookies from the session
    cookies = Session.cookies.get_dict()
    print("Extracted cookies:")
    print(cookies)
else:
    print("Login failed. Please check your credentials or the response for errors.")

# Optionally, print the response to debug further if needed
print(response.text)
