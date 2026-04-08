import requests,json,time


session = requests.Session()

import requests

headers = {
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Google Chrome";v="145.0.7632.5", "Chromium";v="145.0.7632.5"',
    'sec-ch-ua-platform': '"Android"',
    'Referer': 'https://m.facebook.com/login/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-model': '"Nexus 5"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-prefers-color-scheme': 'dark',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'sec-ch-ua-platform-version': '"6.0"',
}

params = {
    'appid': 'com.bloks.www.bloks.caa.login.async.send_login_request',
    'type': 'action',
    '__bkv': 'ffa98ae2b9b0ee7550fe316efcb87fcc5ae987d69dbe0f8fadf9cbc84c0722c7',
}

data = {
    '__aaid': '0',
    '__user': '0',
    '__a': '1',
    '__req': 'k',
    '__hs': '20551.BP:wbloks_caa_pkg.2.0...0',
    'dpr': '3',
    '__ccg': 'EXCELLENT',
    '__rev': '1036861941',
    '__s': '2t38w1:re8mql:3oazzm',
    '__hsi': '7626211268843966763',
    '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x67o1g8hw23E52q1ew2io0D24o1MUaE1Do1u81x82ewnE3fwww5NyE25w8W0Lo6-1CwOw5jw4JwzK0zo3jwea',
    'fb_dtsg': 'NAfuzuFvI9H2reu1C3UCIk5hvnHchnoxYUKyr0EU-HjkpXYTlb0Dj2w:0:0',
    'jazoest': '25071',
    'lsd': 'AdRE36uI4vKYKjSNxHfJURONZCw',
    '__jssesw': '10',
    'params': '{"params":"{\\"server_params\\":{\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"fqjdim:66\\",\\"password_text_input_id\\":\\"fqjdim:67\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":1,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_aymh\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"two_step_login_type\\":\\"one_step_login\\",\\"left_nav_button_action\\":\\"NONE\\",\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"95156663800300\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"b630fab1-dc63-49bb-89e0-7b497e5567ad\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":1,\\"access_flow_version\\":\\"pre_mt_behavior\\",\\"login_surface\\":\\"login_home\\",\\"login_entry_point\\":\\"logged_out\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"cloud_trust_token\\":null,\\"block_store_machine_id\\":\\"\\",\\"zero_balance_state\\":\\"\\",\\"contact_point\\":\\"61575467930154\\",\\"password\\":\\"#PWD_BROWSER:5:1775459553:ASxQANWIvs2bUNAAhgflG+i7zRTsdBANiKPlg9dRmFv1YXMJ4kfNY7xaVlWnbrbWrS2gSlxwNZG1TnoJAIsMvx8uKPej/5sV/1YTF0lGWr4D2647Pf4ZRodMDKaMHP9hIt4Hws2BpGn1KEIEzw==\\",\\"accounts_list\\":[{\\"uid\\":\\"61575467930154\\",\\"credential_type\\":\\"nonce\\",\\"token\\":\\"\\",\\"cloud_identifier\\":\\"\\",\\"obfuscated_token\\":null,\\"username\\":\\"\\",\\"encrypted_password\\":\\"\\",\\"name\\":\\"\\",\\"profile_pic_url\\":\\"\\",\\"small_profile_pic_url\\":null,\\"metadata\\":{\\"last_access_time\\":0,\\"FXAccessLibraryAccountSavedSource\\":\\"\\",\\"previously_authenticated_nonce\\":\\"\\",\\"source_device_id\\":\\"\\"},\\"email\\":\\"\\",\\"account_source\\":\\"\\",\\"sim_phone_number\\":null,\\"encrypted_user_id\\":\\"\\",\\"lva_flow_type\\":null,\\"blob\\":\\"\\"}],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":1,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"gms_incoming_call_retriever_eligibility\\":\\"client_not_supported\\",\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"aymh_accounts\\":[],\\"sso_accounts_auth_data\\":[],\\"network_bssid\\":null,\\"lois_settings\\":{\\"lois_token\\":\\"\\"},\\"aac\\":\\"\\"}}"}',
}

response = requests.post('https://m.facebook.com/async/wbloks/fetch/', params=params, headers=headers, data=data)
# Get cookies after request
cookie_dict = session.cookies.get_dict()

if "c_user" in cookie_dict:
    print("✅ Login success")
else:
    print("❌ Login failed")
