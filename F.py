import random
import re
import sys
import time
import hashlib
import uuid
import json
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
uid = '7797970810'
pw = '7797970810'
url = "https://b-graph.facebook.com/graphql"

headers = {
    "X-Tigon-Is-Retry": "False",
    "Authorization": "OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895",
    "X-Fb-Sim-Hni": "51000",
    "X-Fb-Net-Hni": "51000",
    "Content-Type": "application/x-www-form-urlencoded",
    "X-Iorg-Bsid": "cef4b24e-3af1-4333-bb9a-cde46e637ee7",
    "X-Graphql-Client-Library": "graphservice",
    "X-Fb-Friendly-Name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; SM-G960N Build/PQ3A.190605.03171033) [FBAN/Orca-Android;FBAV/500.1.0.71.108;FBPN/com.facebook.orca;FBLC/in_ID;FBBV/713721466;FBCR/PSN;FBMF/samsung;FBBD/samsung;FBDV/SM-G960N;FBSV/9;FBCA/x86_64:arm64-v8a;FBDM/{density=2.0,width=900,height=1600};FB_FW/1;]",
    "Content-Encoding": "gzip",
    "X-Zero-Eh": "664c0faaac849cb891d0a261fbb72a12",
    "X-Zero-State": "unknown",
    "X-Fb-Connection-Type": "WIFI",
    "Priority": "u=3, i",
    "X-Fb-Rmd": "fail=Server:NoUrlMap,Default:INVALID_MAP;v=;ip=;tkn=;reqTime=0;recvTime=1756921072",
    "X-Fb-Request-Analytics-Tags": '{"network_tags":{"product":"256002347743983","purpose":"none","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}',
    "Accept-Encoding": "gzip, deflate, br",
    "X-Fb-Http-Engine": "Tigon/Liger",
    "X-Fb-Client-Ip": "True",
    "X-Fb-Server-Cluster": "True",
}

client_input_params = {
    "blocked_uids": [],
    "aac": json.dumps({
        "aac_init_timestamp": 1781434103,
        "aacjid": "1223a659-19fb-4c8d-9735-f89e12a1a4a2",
        "aaccs": "3XcWErexKcNOdRZVOdkSrMvcnVSROsTSyct7babVClk"
    }, separators=(",", ":")),
    "sim_phones": [""],
    "aymh_accounts": [],
    "network_bssid": None,
    "secure_family_device_id": "86aa9df8-8391-4c69-9b37-c9bcf487a626",

    "attestation_result": {
        "data": "eyJjaGFsbGVuZ2Vfbm9uY2UiOiJQc0VhTFJVZXFKZDNaVUZNYndyNjgzKy93UVAvRVFCSjI5K3BpYThXMWdnPSIsInVzZXJuYW1lIjoibG9wYWRhZGFzZGFkYSJ9",
        "signature": "MEQCIH2H5bPs8ewYi421HimJxtqeW7vmc+SeI71SNsBPhIOGAiBiKjPu00LUjegos6pG9Ol5F37MeuhHkB7OAFw5+HsZYQ==",
        "keyHash": "6f40e2b9b3f1b0a2fb223ff91daab06b93c5587cc0d9db988c737b0c47220a0c"
    },

    "has_granted_read_contacts_permissions": 0,
    "auth_secure_device_id": "",
    "has_whatsapp_installed": 1,
    "password": '#PWD_MSGR:0:{}:{}'.format(str(int(time.time())), pw),
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

    "device_id": "86aa9df8-8391-4c69-9b37-c9bcf487a626",
    "zero_balance_state": "",
    "login_attempt_count": 1,
    "machine_id": "MlMmahAZ9nZeHnaFggyXvkg0",
    "accounts_list": [],
    "gms_incoming_call_retriever_eligibility": "client_not_supported",
    "family_device_id": "3c02a314-ffb1-464f-9d8d-6c5d48019f1e",
    "fb_ig_device_id": [],
    "device_emails": [],
    "try_num": 1,
    "lois_settings": {
        "lois_token": ""
    },
    "event_step": "home_page",
    "headers_infra_flow_id": "",
    "openid_tokens": {},
    "contact_point": uid
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
    "family_device_id": "3c02a314-ffb1-464f-9d8d-6c5d48019f1e",
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
