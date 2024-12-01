import json

data = {
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
            "contact_point": "9342536255",
            "password": "#PWD_BROWSER:5:1733079858:AT9QALJVOB+fxQEnvSGCp/aDBsHhVxvnLTxpCS3UXlcf30c1tzwuoCekWNlxFJQSxX3h/eS2Lt9iOGmVijVS825CyT3ffmTgqyXX8c479UfszdYo+XW9S1eQDZcDF6ylZ0Vi62nBYSDBr6IO",
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
            "lois_settings": {
                "lois_token": "",
                "lara_override": ""
            }
        }
    })
}

print(json.dumps(data))
