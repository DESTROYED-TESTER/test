import json
import uuid
import time
import requests
import random
import urllib.parse
username = 'sumonh44'
passwd = 'sumon@12M'
useragent = 'Mozilla/5.0 (Linux; Android 12; SKY PAD10 Build/S00812; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/141.0.7390.122 Safari/537.36 Instagram 406.0.0.58.159 Android (31/12; 200dpi; 1280x740; Sky Devices/SKY; SKY PAD10; SKY_PAD10; ums312_2h10; en_US; 822917963; IABMV/1)'
## Create an MD5 hash for the username and password
session = requests.Session()

cookies = {
    'csrftoken': 'DN428oaO0xlMkgH4QWty3v',
    'datr': 'hUBJaYrVv_B2DWSgbhlOCWOQ',
    'ig_did': '684CC997-77C5-4694-ACFE-85B110A8F2CA',
    'mid': 'aUlAhQABAAHCsfc0nwJXSm7C26hw',
    'ig_nrcb': '1',
    'ps_l': '1',
    'ps_n': '1',
    'dpr': '2.4740447998046875',
    'wd': '437x838',
}

headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    # 'cookie': 'csrftoken=DN428oaO0xlMkgH4QWty3v; datr=hUBJaYrVv_B2DWSgbhlOCWOQ; ig_did=684CC997-77C5-4694-ACFE-85B110A8F2CA; mid=aUlAhQABAAHCsfc0nwJXSm7C26hw; ig_nrcb=1; ps_l=1; ps_n=1; dpr=2.4740447998046875; wd=437x838',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/login/?next=%2F&source=mobile_nav',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"23076PC4BI"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
}

params = {
    'appid': 'com.bloks.www.bloks.caa.login.async.send_login_request',
    'type': 'action',
    '__bkv': '18e653ed0a636b36596363c9706a9bd03428e6a0bfce3029e9d6739f59a31409',
}

data = {
    'd': 'www',
    'user': '0',
    'a': '1',
    'req': 'c',
    'hs': '20456.HYP:instagram_web_pkg.2.1...0',
    'dpr': '3',
    'ccg': 'GOOD',
    'rev': '1031603888',
    's': 'pejpwu:68imtk:n8s9ho',
    'hsi': '7591207422758764832',
    'dyn': '7xeUjG1mwt8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0qa0FE2awt81s8hwGwQwoEcE7O2l0Fwqo31w9O0H8jwae4UaEW2G0AEco5G0zK5o4q0HU1IEGdwtU662O0Lo6-3u2WE15E6O1FwlA1HQp1yU5Oi2K7E5y1rwGwa6byohw5yweu',
    'csr': 'gJPPjMF24Z_d96aD9C_HlKZp5B8WZ2VVaGp4VQmGz8O9V9XAxzK8yuFpu4o-5ErDBx2az85yFVEizoC4Q9yHiCwyyobRwq8S4FpoO4UswHgiCG5UaUTChki2a4oHiwwxW00myuUoU0Nm58mS06wU8Edrz8kw4Ew6r80UE0vhai8gKlKq350aipzkAh1u0bowjUzw5fo1sUUPy41gweO0kFwl9L8U0_u78047y017mw3y81Ro0Zi04k6',
    'hsdp': 'gR3N75OumQcMy1ljAEk8jzEjKDRlh4YggWzokz63K0h-0J4aBwdS03Du0oaaw53w1ni',
    'hblp': '0dG0WU17U36wuU22xi78aEe8vwko3qxS0OE1BE4e1Vxi1DwHw16i0c_wTwpocEmw9B1u1cw7hwcW0aiw4OwqFU6O3-2C2i0D81t8',
    'sjsp': 'gR3N75OumQcMy1ljAEk8jzEjKDRlh2dekWzokz63K0h-0J4aBw',
    'comet_req': '7',
    'lsd': 'AdGN0nwJDTI',
    'jazoest': '2890',
    'spin_r': '1031603888',
    'spin_b': 'trunk',
    'spin_t': '1767465710',
    'crn': 'comet.igweb.PolarisWebBloksLoginRoute',
    'params': '{"params":"{\\"server_params\\":{\\"next_uri\\":\\"/\\",\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"ng7gaa:64\\",\\"password_text_input_id\\":\\"ng7gaa:65\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":0,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"ar_context\\":\\"Ac-8IBkfzydn5C8phoMq4wOBcXHasceCdRwaM7Ixbq4LB2fvNuUHrN0r6pYtq7lOoRdAq7Q9ZBriVS2q6bsZl9Lu56Ey4i_om2gMOvuVkhTbpPj3CpmSl6gJ5a2SHSGOje4o3ThMtX9ussux5AOOjyl0pR48ATh8NK3Tvc9kG6UKba-WjKRJZS0ekVWiIMlrsANyix1BsQhLompS17D4RICyK-E1peA5X10BCmRtOsp54OsZWQ21hiS0WLLot5F3jpFjd7iah1jqi_hWMBdsqYHhb9q4DUFTiUz_jCioEVALdm2qy-A3YrYOqNfmItrqw-OtrAzN0fylkl9k1F-6y881ij5789g5Sb8OLYbRMGT2pijMcy6L1ytNaIkmZPb8-5b17nK4VrxR-imakc5qmGbuB2qDuhqhhi4|arm\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_aymh\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"two_step_login_type\\":\\"one_step_login\\",\\"is_vanilla_password_page_empty_password\\":0,\\"left_nav_button_action\\":\\"NONE\\",\\"INTERNALlatency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\"3A\\"141794360200430\\",\\"device_id\\":\\"aUlAhQABAAHCsfc0nwJXSm7C26hw\\",\\"family_device_id\\":null,\\"waterfall_id\\":\\"bdb921db-42a4-4c0c-b3dc-b1c1cbe77e19\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"cloud_trust_token\\":null,\\"block_store_machine_id\\":\\"\\",\\"zero_balance_state\\":\\"\\",\\"contact_point\\":\\"8918168736\\",\\"password\\":\\"#PWD_BROWSER:5:1767465765:Ac1QALkczDragfAvSjmCxZzIW594ll5LN1G2JE3th2AvEnIOFCrvxq5yIiNiMSwm394MLdndHi+0ODXO+UE+BvmfkUfi0bmBooGsUKKLKwXsrP1k/jRpAWugrKPCWrNneVlhvcZJpyznXA==\\",\\"accounts_list\\":[],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":1,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"aymh_accounts\\":[{\\"id\\":\\"\\",\\"profiles\\":{\\"id\\":{\\"user_id\\":\\"\\",\\"name\\":\\"\\",\\"profile_picture_url\\":\\"\\",\\"small_profile_picture_url\\":null,\\"notification_count\\":0,\\"credential_type\\":\\"none\\",\\"token\\":\\"\\",\\"last_access_time\\":0,\\"is_derived\\":0,\\"username\\":\\"\\",\\"password\\":\\"\\",\\"has_smartlock\\":0,\\"account_center_id\\":\\"\\",\\"account_source\\":\\"\\",\\"credentials\\":[],\\"nta_eligibility_reason\\":null,\\"from_accurate_privacy_result\\":0,\\"dbln_validated\\":0}}}],\\"network_bssid\\":null,\\"lois_settings\\":{\\"lois_token\\":\\"\\"},\\"aac\\":\\"\\"}}"}',
}

response = session.post('https://www.instagram.com/async/wbloks/fetch/', params=params, cookies=cookies, headers=headers, data=data)

    ## Check if login was successful
wanted = ["ds_user_id", "sessionid"]
all_cookies = session.cookies.get_dict()
extracted = {k: all_cookies[k] for k in wanted if k in all_cookies}
cookie_str = "; ".join(f"{k}={v}" for k, v in extracted.items())
print("Cookies:", cookie_str)
print(response.text)
