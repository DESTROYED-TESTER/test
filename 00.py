import requests
import time
Session = requests.Session()

cookies = {
    'datr': 'jmjoaVfeB7W3jZ4BQHD6-_N1',
    'sb': 'j2joaQZbhunBrfQCUtmi-X-G',
    'ps_l': '1',
    'ps_n': '1',
    'dpr': '2.75',
    'm_pixel_ratio': '2.75',
    'wd': '393x851',
    'fr': '0GnupA319Ud1tcna7..Bp6GiO..AAA.0.0.Bp6ITQ.AWd63pbibkJ0PYkNC2svQYNc7bQ',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2010J19SI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-model': '"M2010J19SI"',
    'sec-ch-ua-mobile': '?1',
    'viewport-width': '393',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'dpr': '2.75',
    'sec-ch-ua-full-version-list': '".Not/A)Brand";v="99.0.0.0", "Google Chrome";v="103.0.5060.129", "Chromium";v="103.0.5060.129"',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua-platform': '"Android"',
    'origin': 'https://m.facebook.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://m.facebook.com/login/device-based/regular/login/?login_attempt=1',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': 'datr=jmjoaVfeB7W3jZ4BQHD6-_N1; sb=j2joaQZbhunBrfQCUtmi-X-G; ps_l=1; ps_n=1; dpr=2.75; m_pixel_ratio=2.75; wd=393x851; fr=0GnupA319Ud1tcna7..Bp6GiO..AAA.0.0.Bp6ITQ.AWd63pbibkJ0PYkNC2svQYNc7bQ',
}

params = {
    'appid': 'com.bloks.www.bloks.caa.login.async.send_login_request',
    'type': 'action',
    'bkv': 'b7fb9726bc1fc393a9d9ca95c0a85c5fd9e24af496e45a3b86182631fcc46540',
}

data = {
    'aaid': '0',
    'user': '0',
    'a': '1',
    'req': '6',
    'hs': '20565.BP:wbloks_caa_pkg.2.0...0',
    'dpr': '3',
    'ccg': 'EXCELLENT',
    'rev': '1037878879',
    's': 'cn04xq:u4yav7:h0iyc9',
    'hsi': '7631495404926016587',
    'dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x67o1g8hw23E52q1ew2io0D24o1MUaE1Do1u81x82ewnE3fwww5NyE25w8W0Lo6-1CwOw5jw4JwzK0zo3jwea',
    'fb_dtsg': 'NAfufp9JPXIYDAG49CjMqD65d5UA_jgL0Mbl_PptU0uXX66qHpoV6RA:0:0',
    'jazoest': '24746',
    'lsd': 'AdQW9Fjy2nwOicSpDMW_EjRLc9c',
    'jssesw': '10',
    'params': '{"params":"{\\"server_params\\":{\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"s829fj:66\\",\\"password_text_input_id\\":\\"s829fj:67\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":0,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_aymh\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"two_step_login_type\\":\\"one_step_login\\",\\"left_nav_button_action\\":\\"NONE\\",\\"INTERNALlatency_qpl_marker_id\\":36707139,\\"INTERNALlatency_qpl_instance_id\\":\\"170659539100204\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"44b02b6f-1e8c-42b9-a77b-83f85958cee6\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\",\\"login_surface\\":\\"login_home\\",\\"login_entry_point\\":\\"logged_out\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"cloud_trust_token\\":null,\\"block_store_machine_id\\":\\"\\",\\"zero_balance_state\\":\\"\\",\\"contact_point\\":\\"bithikasumon81@gmail.com\\",\\"password\\":\\"#PWD_BROWSER:5:1776846033:ATpQABDd95c2JXOZFvOoBoyVx4U9xR2Ntr7HHA+TOKd11AJL1ksFnw7cCn1ahXIukhsvt7FTXq+fhd0fx1g3AcFQPYUfkIU6AZl6BYu74+gJE3YHtxU6w6s181NB+EdaLtt67CDprrDWE1j4IQ==\\",\\"accounts_list\\":[],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":1,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"gms_incoming_call_retriever_eligibility\\":\\"client_not_upported\\",\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"aymh_accounts\\":[{\\"id\\":\\"\\",\\"profiles\\":{\\"id\\":{\\"user_id\\":\\"\\",\\"name\\":\\"\\",\\"profile_picture_url\\":\\"\\",\\"small_profile_picture_url\\":null,\\"notification_count\\":0,\\"credential_type\\":\\"none\\",\\"token\\":\\"\\",\\"last_access_time\\":0,\\"is_derived\\":0,\\"username\\":\\"\\",\\"password\\":\\"\\",\\"has_smartlock\\":0,\\"account_center_id\\":\\"\\",\\"account_source\\":\\"\\",\\"credentials\\":[],\\"nta_eligibility_reason\\":null,\\"from_accurate_privacy_result\\":0,\\"dbln_validated\\":0}}}],\\"sso_accounts_auth_data\\":[],\\"network_bssid\\":null,\\"lois_settings\\":{\\"lois_token\\":\\"\\"},\\"aac\\":\\"\\"}}"}',
}

response = Session.post('https://m.facebook.com/async/wbloks/fetch/', params=params, cookies=cookies, headers=headers, data=data)

# Check login success
log_cookies = Session.cookies.get_dict().keys()
if "c_user" in log_cookies:
    print('\033[1;92m OK')
