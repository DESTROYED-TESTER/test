import requests
import json

url = "https://b-graph.facebook.com/graphql"

headers = {
    "X-Tigon-Is-Retry": "False",
    "Authorization": "OAuth YOUR_APP_OR_ACCESS_TOKEN",
    "X-Fb-Sim-Hni": "51000",
    "X-Fb-Net-Hni": "51000",
    "Content-Type": "application/x-www-form-urlencoded",
    "X-Iorg-Bsid": "YOUR_DEVICE_ID",
    "X-Graphql-Client-Library": "graphservice",
    "X-Fb-Friendly-Name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
    "User-Agent": (
        "Dalvik/2.1.0 (Linux; U; Android 9; SM-G960N Build/PQ3A.190605.03171033) "
        "[FBAN/Orca-Android;FBAV/500.1.0.71.108;FBPN/com.facebook.orca;"
        "FBLC/in_ID;FBBV/713721466;FBCR/PSN;FBMF/samsung;FBBD/samsung;"
        "FBDV/SM-G960N;FBSV/9;FBCA/x86_64:arm64-v8a;"
        "FBDM/{density=2.0,width=900,height=1600};FB_FW/1;]"
    ),
    "X-Zero-State": "unknown",
    "X-Fb-Connection-Type": "WIFI",
    "X-Fb-Http-Engine": "Tigon/Liger",
    "X-Fb-Client-Ip": "True",
    "X-Fb-Server-Cluster": "True",
}

client_input_params = {
    "blocked_uids": [],
    "aac": json.dumps({
        "aac_init_timestamp": 1781434103,
        "aacjid": "YOUR_AACJID",
        "aaccs": "YOUR_AACCS"
    }, separators=(",", ":")),
    "sim_phones": [""],
    "aymh_accounts": [],
    "network_bssid": None,
    "secure_family_device_id": "YOUR_SECURE_FAMILY_DEVICE_ID",

    "attestation_result": {
        "data": "YOUR_ATTESTATION_DATA",
        "signature": "YOUR_ATTESTATION_SIGNATURE",
        "keyHash": "YOUR_KEY_HASH"
    },

    "has_granted_read_contacts_permissions": 0,
    "auth_secure_device_id": "",
    "has_whatsapp_installed": 1,

    # Use only the credential generated for your own account/session.
    "password": "YOUR_PWD_MSGR_VALUE",

    "sso_token_map_json_string": "",
    "block_store_machine_id": "",
    "cloud_trust_token": None,
    "event_flow": "login_manual",
    "password_contains_non_ascii": "false",
    "client_known_key_hash": "",
    "sso_accounts_auth_data": [],
    "encrypted_msisdn": "",
    "has_granted_read_phone_permissions": 0,
    "app_manager_id": "",
    "should_show_nested_nta_from_aymh": 0,

    "device_id": "YOUR_DEVICE_ID",
    "zero_balance_state": "",
    "login_attempt_count": 1,
    "machine_id": "YOUR_MACHINE_ID",
    "accounts_list": [],
    "gms_incoming_call_retriever_eligibility": "client_not_supported",
    "family_device_id": "YOUR_FAMILY_DEVICE_ID",
    "fb_ig_device_id": [],
    "device_emails": [],
    "try_num": 1,
    "lois_settings": {
        "lois_token": ""
    },
    "event_step": "home_page",
    "headers_infra_flow_id": "",
    "openid_tokens": {},

    # Your own Facebook username/email/phone
    "contact_point": "YOUR_USERNAME"
}

server_params = {
    "should_trigger_override_login_2fa_action": 0,
    "is_from_logged_out": 0,
    "should_trigger_override_login_success_action": 0,
    "login_credential_type": "none",
    "server_login_source": "login",
    "waterfall_id": "YOUR_WATERFALL_ID",
    "two_step_login_type": "one_step_login",
    "login_source": "Login",
    "is_platform_login": 0,
    "pw_encryption_try_count": 1,
    "login_entry_point": "logged_out",
    "INTERNAL__latency_qpl_marker_id": 36707139,
    "is_from_aymh": 0,
    "offline_experiment_group": "caa_iteration_v3_perf_msg_6",
    "is_from_landing_page": 0,
    "left_nav_button_action": "NONE",
    "password_text_input_id": "nvb5wc:95",
    "is_from_empty_password": 0,
    "is_from_msplit_fallback": 0,
    "ar_event_source": "login_home_page",
    "username_text_input_id": "nvb5wc:94",
    "layered_homepage_experiment_group": None,
    "device_id": "YOUR_DEVICE_ID",
    "login_surface": "login_home",
    "INTERNAL__latency_qpl_instance_id": 1.44331100400549E14,
    "reg_flow_source": "login_home_native_integration_point",
    "is_caa_perf_enabled": 1,
    "credential_type": "password",
    "is_from_password_entry_page": 0,
    "caller": "gslr",
    "family_device_id": "YOUR_FAMILY_DEVICE_ID",
    "is_from_assistive_id": 0,
    "access_flow_version": "pre_mt_behavior",
    "is_from_logged_in_switcher": 0
}

inner_params = {
    "params": {
        "client_input_params": client_input_params,
        "server_params": server_params
    }
}

variables = {
    "params": {
        "params": json.dumps(inner_params, separators=(",", ":")),
        "bloks_versioning_id": "9331af72e2c20ac63fea39c6d6b2d22641149512b1b9f2a6e3ba2b6def08dbea",
        "app_id": "com.bloks.www.bloks.caa.login.async.send_login_request"
    },
    "scale": "2",
    "nt_context": {
        "using_white_navbar": True,
        "styles_id": "a034d732ad4a263c448a487d61a61f40",
        "pixel_ratio": 2,
        "is_push_on": True,
        "debug_tooling_metadata_token": None,
        "is_flipper_enabled": False,
        "theme_params": [],
        "bloks_version": "9331af72e2c20ac63fea39c6d6b2d22641149512b1b9f2a6e3ba2b6def08dbea"
    }
}

data = {
    "method": "post",
    "pretty": "false",
    "format": "json",
    "server_timestamps": "true",
    "locale": "id_ID",
    "fb_api_req_friendly_name":
        "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
    "fb_api_caller_class": "graphservice",
    "client_doc_id": "119940804216663295833025359905",
    "fb_api_client_context": json.dumps(
        {"is_background": False},
        separators=(",", ":")
    ),
    "variables": json.dumps(variables, separators=(",", ":")),
    "fb_api_analytics_tags": '["GraphServices"]',
    "client_trace_id": "YOUR_CLIENT_TRACE_ID"
}

r = requests.post(
    url,
    headers=headers,
    data=data,
    timeout=30
)

print("Status:", r.status_code)
print(r.text)
