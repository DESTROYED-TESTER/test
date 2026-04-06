import requests,json,time


session = requests.Session()
cookies = {
    'locale': 'en_GB',
    'pas': '61573832370121%3ApgGqTXpG7y',
    'wl_cbv': 'v2%3Bclient_version%3A3128%3Btimestamp%3A1774906764',
    'vpd': 'v1%3B754x393x2.4740447998046875',
    'datr': '4DjTaQtWTWKrsbs8YOmad9Pj',
    'm_pixel_ratio': '2.4740447998046875',
    'wd': '393x895',
    'sb': '5DjTaWwgMKgUjL41K8q6jNjF',
    'fr': '10296q4XBTILTnpPu.AWfvSGyRaXPpU2MPGYaXH4MM9hm2uq3WDM2beQF5qeN-ny5d_tA.Bpyu2N..AAA.0.0.Bp0zkD.AWf9_N0drAMlpBpI4WYjnsLqTmA',
}

headers = {
    'authority': 'm.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    # 'cookie': 'locale=en_GB; pas=61573832370121%3ApgGqTXpG7y; wl_cbv=v2%3Bclient_version%3A3128%3Btimestamp%3A1774906764; vpd=v1%3B754x393x2.4740447998046875; datr=4DjTaQtWTWKrsbs8YOmad9Pj; m_pixel_ratio=2.4740447998046875; wd=393x895; sb=5DjTaWwgMKgUjL41K8q6jNjF; fr=10296q4XBTILTnpPu.AWfvSGyRaXPpU2MPGYaXH4MM9hm2uq3WDM2beQF5qeN-ny5d_tA.Bpyu2N..AAA.0.0.Bp0zkD.AWf9_N0drAMlpBpI4WYjnsLqTmA',
    'origin': 'https://m.facebook.com',
    'referer': 'https://m.facebook.com/',
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
    '__bkv': 'c41a736f68c4f99148bbc5f20c1a79cb81e79585374dd83b20119a79174bd379',
}

data = {
    'aaid': '0',
    'user': '0',
    'a': '1',
    'req': '6',
    'hs': '20549.BP:wbloks_caa_pkg.2.0...0',
    'dpr': '3',
    'ccg': 'GOOD',
    'rev': '1036705643',
    's': 'zxk38z:7clel3:8duo42',
    'hsi': '7625501147636239718',
    'dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x67o1g8hw23E52q1ew2io0D24o1MUaE1Do1u81x82ewnE3fwww5NyE25w8W0Lo6-1CwOw5jw4JwzK0zo3jwea',
    'fb_dtsg': 'NAfvL8bXQAVg9O4xLFj_qUPDV4QyE3EsQUye8c-erowIqr-ZrQFHedA:0:0',
    'jazoest': '24944',
    'lsd': 'AdSz6o5_LoZleh0d8MG530zG-zU',
    'params': json.dumps({
        "params": json.dumps({
            "server_params": {
                "credential_type": "password",
                "username_text_input_id": "paj9ud:74",
                "password_text_input_id": "paj9ud:75",
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
                "INTERNALlatency_qpl_instance_id": "152934978100204",
                "device_id": None,
                "family_device_id": None,
                "waterfall_id": "8ad70d97-b8ef-4cff-a6e4-ce4e161f6363",
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
                "contact_point": "100013349915494",
                "password": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], "977593"),
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
                "network_bssid": None,
                "lois_settings": {
                    "lois_token": ""
                },
                "aac": ""
            }
        })
    })
}


response = requests.post('https://m.facebook.com/async/wbloks/fetch/', params=params, cookies=cookies, headers=headers, data=data)
# Get cookies after request
cookie_dict = session.cookies.get_dict()

if "c_user" in cookie_dict:
    print("✅ Login success")
    print("User ID:", cookie_dict["c_user"])
else:
    print("❌ Login failed")
