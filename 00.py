import requests,json,time


session = requests.Session()

cookies = {
    'pas': '100007740248754%3A0w4YH5n86J',
    'vpd': 'v1%3B720x393x2.75',
    'ps_l': '1',
    'ps_n': '1',
    'wl_cbv': 'v2%3Bclient_version%3A3125%3Btimestamp%3A1774581775',
    'datr': 'xD3HaSy8GJ1IsEQmSYosz1Jp',
    'sb': 'xT3HaalWuRMTZeJkkbwLXwq2',
    'm_pixel_ratio': '2.75',
    'locale': 'en_US',
    'dpr': '3.0234789848327637',
    'wd': '393x851',
    'fr': '0VXlxkS22xPhRZ7QH.AWchxwJktkC-uOQ3xENEazpRlY8hCdavv-mEsFSHvBuYVE_7eto.Bpw6jH..AAA.0.0.Bp00qU.AWdAy9y2YIZQX-ZZDS9_KzVOMMc',
}

headers = {
    'authority': 'm.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    # 'cookie': 'pas=100007740248754%3A0w4YH5n86J; vpd=v1%3B720x393x2.75; ps_l=1; ps_n=1; wl_cbv=v2%3Bclient_version%3A3125%3Btimestamp%3A1774581775; datr=xD3HaSy8GJ1IsEQmSYosz1Jp; sb=xT3HaalWuRMTZeJkkbwLXwq2; m_pixel_ratio=2.75; locale=en_US; dpr=3.0234789848327637; wd=393x851; fr=0VXlxkS22xPhRZ7QH.AWchxwJktkC-uOQ3xENEazpRlY8hCdavv-mEsFSHvBuYVE_7eto.Bpw6jH..AAA.0.0.Bp00qU.AWdAy9y2YIZQX-ZZDS9_KzVOMMc',
    'origin': 'https://m.facebook.com',
    'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=505270809499689&kid_directed_site=0&app_id=505270809499689&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D505270809499689%26redirect_uri%3Dhttps%253A%252F%252Faccount.asus.com%252Foauth%252Ffacebook%252Fcallback.aspx%26state%3DeyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJTdGF0ZSI6IjRGSjNTV1M2NVoiLCJSZXR1cm5VcmwiOiJodHRwczovL3d3dy5hc3VzLmNvbS9pbi8iLCJBcHBJZCI6IjAwMDAwMDAwMDIiLCJOb25jZSI6IkZVUFpJN05YIiwiTm9uY2VFeHBpcmVUaW1lIjoiNC82LzIwMjYgMjowNDoxMiBQTSIsIklzRmFjZUJvb2tCaW5kYmFjayI6Ik5vdEZhY2Vib29rQmluZGJhY2siLCJXZWJzaXRlQ29kZSI6ImluIn0.gNgdx7qoVJu0eASevvC_z8PWfS_H3v4WSMJBdVsQULo%26nonce%3DFUPZI7NX%26scope%3Dopenid%2Buser_birthday%2Bpublic_profile%2Bemail%26auth_type%3Drerequest%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D1b700989-f4c9-4aac-bf87-208231eb8790%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccount.asus.com%2Foauth%2Ffacebook%2Fcallback.aspx%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJTdGF0ZSI6IjRGSjNTV1M2NVoiLCJSZXR1cm5VcmwiOiJodHRwczovL3d3dy5hc3VzLmNvbS9pbi8iLCJBcHBJZCI6IjAwMDAwMDAwMDIiLCJOb25jZSI6IkZVUFpJN05YIiwiTm9uY2VFeHBpcmVUaW1lIjoiNC82LzIwMjYgMjowNDoxMiBQTSIsIklzRmFjZUJvb2tCaW5kYmFjayI6Ik5vdEZhY2Vib29rQmluZGJhY2siLCJXZWJzaXRlQ29kZSI6ImluIn0.gNgdx7qoVJu0eASevvC_z8PWfS_H3v4WSMJBdVsQULo%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&is_business_login=0&refsrc=deprecated',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-full-version-list': '"Chromium";v="139.0.7339.0", "Not;A=Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"M2010J19SI"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
}

params = {
    'appid': 'com.bloks.www.bloks.caa.login.async.send_login_request',
    'type': 'action',
    '__bkv': 'c41a736f68c4f99148bbc5f20c1a79cb81e79585374dd83b20119a79174bd379',
}

data = {
    '__aaid': '0',
    '__user': '0',
    '__a': '1',
    '__req': '6',
    '__hs': '20549.BP:wbloks_caa_pkg.2.0...0',
    'dpr': '3',
    '__ccg': 'EXCELLENT',
    '__rev': '1036705643',
    '__s': 'xc0ko5:gjioai:6j7u2m',
    '__hsi': '7625520525867633771',
    '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x67o1g8hw23E52q1ew2io0D24o1MUaE1Do1u81x82ewnE3fwww5NyE25w8W0Lo6-1CwOw5jw4JwzK0zo3jwea',
    'locale': 'en_GB',
    'fb_dtsg': 'NAfv8NcTJHRxUJMRxkkVBgCfGuUT499QZ15zho-hVJJhBZavTfaB_jg:0:0',
    'jazoest': '24960',
    'lsd': 'AdRSMAkC7SufJE96m2FF26hNHww',
    'params': '{"params":"{\\"server_params\\":{\\"next_uri\\":\\"https://m.facebook.com/dialog/oauth?response_type=code&client_id=505270809499689&redirect_uri=https%3A%2F%2Faccount.asus.com%2Foauth%2Ffacebook%2Fcallback.aspx&state=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJTdGF0ZSI6IjRGSjNTV1M2NVoiLCJSZXR1cm5VcmwiOiJodHRwczovL3d3dy5hc3VzLmNvbS9pbi8iLCJBcHBJZCI6IjAwMDAwMDAwMDIiLCJOb25jZSI6IkZVUFpJN05YIiwiTm9uY2VFeHBpcmVUaW1lIjoiNC82LzIwMjYgMjowNDoxMiBQTSIsIklzRmFjZUJvb2tCaW5kYmFjayI6Ik5vdEZhY2Vib29rQmluZGJhY2siLCJXZWJzaXRlQ29kZSI6ImluIn0.gNgdx7qoVJu0eASevvC_z8PWfS_H3v4WSMJBdVsQULo&nonce=FUPZI7NX&scope=openid+user_birthday+public_profile+email&auth_type=rerequest&ret=login&fbapp_pres=0&logger_id=1b700989-f4c9-4aac-bf87-208231eb8790&tp=unspecified\\",\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"rz8b7s:74\\",\\"password_text_input_id\\":\\"rz8b7s:75\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":0,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_aymh\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"two_step_login_type\\":\\"one_step_login\\",\\"left_nav_button_action\\":\\"NONE\\",\\"INTERNALlatency_qpl_marker_id\\":36707139,\\"INTERNALlatency_qpl_instance_id\\":\\"169176109600461\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"cd6889d0-91f3-41d7-b2b9-64c1fffc2956\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\",\\"login_surface\\":\\"login_home\\",\\"login_entry_point\\":\\"logged_out\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"cloud_trust_token\\":null,\\"block_store_machine_id\\":\\"\\",\\"zero_balance_state\\":\\"\\",\\"contact_point\\":\\"61575467930154\\",\\"password\\":\\"#PWD_BROWSER:5:1775454874:ASpQAEjoNQTjObtiEHW2BQxCTM1vMnUbjrJ6lwU2pybjrj4HHYxY9jnnFzpE/B/uxv7On6vZqjDWGVoOub0zCy1GDgThJ1hkakz22KfLmqINuniFHkTZ8SlfU5xgEws974BSmVfCjR++y/DJbg==\\",\\"accounts_list\\":[],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":1,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"gms_incoming_call_retriever_eligibility\\":\\"client_not_supported\\",\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"aymh_accounts\\":[{\\"id\\":\\"\\",\\"profiles\\":{\\"id\\":{\\"user_id\\":\\"\\",\\"name\\":\\"\\",\\"profile_picture_url\\":\\"\\",\\"small_profile_picture_url\\":null,\\"notification_count\\":0,\\"credential_type\\":\\"none\\",\\"token\\":\\"\\",\\"last_access_time\\":0,\\"is_derived\\":0,\\"username\\":\\"\\",\\"password\\":\\"\\",\\"has_smartlock\\":0,\\"account_center_id\\":\\"\\",\\"account_source\\":\\"\\",\\"credentials\\":[],\\"nta_eligibility_reason\\":null,\\"from_accurate_privacy_result\\":0,\\"dbln_validated\\":0}}}],\\"sso_accounts_auth_data\\":[],\\"network_bssid\\":null,\\"lois_settings\\":{\\"lois_token\\":\\"\\"},\\"aac\\":\\"\\"}}"}',
}

response = requests.post('https://m.facebook.com/async/wbloks/fetch/', params=params, cookies=cookies, headers=headers, data=data)

# Get cookies after request
cookie_dict = session.cookies.get_dict()

if "c_user" in cookie_dict:
    print("✅ Login success")
    print("User ID:", cookie_dict["c_user"])
else:
    print("❌ Login failed")
