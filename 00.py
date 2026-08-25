import requests
import json
import time
import re
import uuid

def x1():
    """Generate a realistic Facebook mobile user-agent"""
    return "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36"

# Your credentials
uid = "100065314603669"  # Replace with your Facebook email/phone
pw = "7029507010"  # Replace with your password

Session = requests.Session()

# IMPORTANT: Get a fresh OAuth token from Facebook's official API
# You cannot reuse the hardcoded one
# Use Facebook's official login flow or Graph API

Session.headers.update({
    'host': 'b-graph.facebook.com',
    'x-fb-connection-type': 'MOBILE.LTE',
    'x-zero-state': 'unknown',
    'user-agent': x1(),
    'x-tigon-is-retry': 'False',
    'x-fb-device-group': '4783',
    'x-graphql-request-purpose': 'fetch',
    'x-fb-privacy-context': '3643298472347298',
    'x-fb-friendly-name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request',
    'x-graphql-client-library': 'graphservice',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-net-hni': '51011',
    'x-fb-sim-hni': '51011',
    # ⚠️ REPLACE THIS WITH A FRESH TOKEN:
    'authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
    'x-fb-request-analytics-tags': '{"network_tags":{"product":"350685531728","purpose":"fetch","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}',
    'x-fb-http-engine': 'Tigon/Liger',
    'x-fb-client-ip': 'True',
    'x-fb-server-cluster': 'True'
})

apcb = '#PWD_FB4A:0:{}:{}'.format(str(int(time.time())), pw)

data = {
    'method': "post",
    'pretty': "false",
    'format': "json",
    'server_timestamps': "true",
    'locale': "id_ID",
    'purpose': "fetch",
    'fb_api_req_friendly_name': "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
    'fb_api_caller_class': "graphservice",
    'client_doc_id': "119940804214876861379510865434",  # This may be outdated
    'variables': json.dumps({
        "params": {
            "params": "{\"params\":\"{\\\"client_input_params\\\":{\\\"sim_phones\\\":[],\\\"secure_family_device_id\\\":\\\"67db191d-c496-4ce6-b16a-40d465504065\\\",\\\"attestation_result\\\":{\\\"data\\\":\\\"eyJjaGFsbGVuZ2Vfbm9uY2UiOiIrZHJubFJJdndKSkxmUnR4TkdLRWlscWRHOUc2KzJPZWdsY1gyN1d0UEEwPSIsInVzZXJuYW1lIjoieHlhZmFqYXJAZ21haWwuY29tIn0=\\\",\\\"signature\\\":\\\"MEQCIDireQS4hTnMyBiyJckHln2WFJ65OU6a31Bx6JGyCjttAiBpZw4ixxyyyNNC0xMgiqmiAd1rVi8ZGsfyTrqvBIibqw==\\\",\\\"keyHash\\\":\\\"f344d852976b8878bd5ccda3f95074528c7564fcebcde45abc51c9b43bc234e4\\\"},\\\"has_granted_read_contacts_permissions\\\":0,\\\"auth_secure_device_id\\\":\\\"\\\",\\\"has_whatsapp_installed\\\":1,\\\"password\\\":\\\"" + apcb + "\\\",\\\"sso_token_map_json_string\\\":\\\"\\\",\\\"event_flow\\\":\\\"login_manual\\\",\\\"password_contains_non_ascii\\\":\\\"false\\\",\\\"sim_serials\\\":[],\\\"client_known_key_hash\\\":\\\"\\\",\\\"encrypted_msisdn\\\":\\\"\\\",\\\"has_granted_read_phone_permissions\\\":0,\\\"app_manager_id\\\":\\\"\\\",\\\"should_show_nested_nta_from_aymh\\\":0,\\\"device_id\\\":\\\"41889e22-bee8-4c81-8ec6-add9a221bd3f\\\",\\\"login_attempt_count\\\":1,\\\"machine_id\\\":\\\"\\\",\\\"flash_call_permission_status\\\":{\\\"READ_PHONE_STATE\\\":\\\"DENIED\\\",\\\"READ_CALL_LOG\\\":\\\"DENIED\\\",\\\"ANSWER_PHONE_CALLS\\\":\\\"DENIED\\\"},\\\"accounts_list\\\":[{},{}],\\\"family_device_id\\\":\\\"f7eab582-f690-4123-b350-132bb5ec5500\\\",\\\"fb_ig_device_id\\\":[],\\\"device_emails\\\":[],\\\"try_num\\\":1,\\\"lois_settings\\\":{\\\"lois_token\\\":\\\"\\\",\\\"lara_override\\\":\\\"\\\"},\\\"event_step\\\":\\\"home_page\\\",\\\"headers_infra_flow_id\\\":\\\"\\\",\\\"openid_tokens\\\":{},\\\"contact_point\\\":\\\"" + uid + "\\\"},\\\"server_params\\\":{\\\"should_trigger_override_login_2fa_action\\\":0,\\\"is_from_logged_out\\\":0,\\\"should_trigger_override_login_success_action\\\":0,\\\"login_credential_type\\\":\\\"none\\\",\\\"server_login_source\\\":\\\"login\\\",\\\"waterfall_id\\\":\\\"12020f76-d875-4059-82fc-93f8debb8784\\\",\\\"login_source\\\":\\\"Login\\\",\\\"is_platform_login\\\":0,\\\"pw_encryption_try_count\\\":1,\\\"INTERNAL__latency_qpl_marker_id\\\":36707139,\\\"offline_experiment_group\\\":\\\"caa_iteration_v6_perf_fb_2\\\",\\\"is_from_landing_page\\\":0,\\\"password_text_input_id\\\":\\\"6vcvjp:102\\\",\\\"is_from_empty_password\\\":0,\\\"is_from_msplit_fallback\\\":0,\\\"ar_event_source\\\":\\\"login_home_page\\\",\\\"username_text_input_id\\\":\\\"6vcvjp:101\\\",\\\"layered_homepage_experiment_group\\\":null,\\\"device_id\\\":\\\"41889e22-bee8-4c81-8ec6-add9a221bd3f\\\",\\\"INTERNAL__latency_qpl_instance_id\\\":4.154659090078E13,\\\"reg_flow_source\\\":\\\"login_home_native_integration_point\\\",\\\"is_caa_perf_enabled\\\":1,\\\"credential_type\\\":\\\"password\\\",\\\"is_from_password_entry_page\\\":0,\\\"caller\\\":\\\"gslr\\\",\\\"family_device_id\\\":\\\"f7eab582-f690-4123-b350-132bb5ec5500\\\",\\\"is_from_assistive_id\\\":0,\\\"access_flow_version\\\":\\\"F2_FLOW\\\",\\\"is_from_logged_in_switcher\\\":0}}\"}",
            "bloks_versioning_id": "3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5",
            "app_id": "com.bloks.www.bloks.caa.login.async.send_login_request"
        },
        "scale": "3",
        "nt_context": {
            "using_white_navbar": True,
            "styles_id": "cfe75e13b386d5c54b1de2dcca1bee5a",
            "pixel_ratio": 3,
            "is_push_on": True,
            "debug_tooling_metadata_token": None,
            "is_flipper_enabled": False,
            "theme_params": [],
            "bloks_version": "3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5"
        }
    }),
    'fb_api_analytics_tags': '["GraphServices"]',
    'client_trace_id': str(uuid.uuid4())
}

try:
    response = Session.post('https://b-graph.facebook.com/graphql', data=data, allow_redirects=True, timeout=30)
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text[:500]}...")  # Print first 500 chars
    
    if response.status_code == 200:
        if "c_user" in response.text and "access_token" in response.text:
            cookie_raw = re.sub(r'\\(?!/)', '', response.text)
            match = re.search(r'"session_cookies"\s*:\s*(\[[^\]]+\])', cookie_raw)
            if match:
                cookies_raw = match.group(1)
                cookies_json = json.loads(cookies_raw)
                cok = ";".join(f'{c["name"]}={c["value"]}' for c in cookies_json)
                c_user = next((c["value"] for c in cookies_json if c["name"] == "c_user"), None)
                print(f"\n✅ SUCCESS: Logged in as {c_user}")
                print(f"Cookies: {cok}")
                
                # Optional: Save to file (modify path for your system)
                # with open("facebook_session.txt", "w") as f:
                #     f.write(f"{c_user}|{pw}|{cok}\n")
        else:
            print("❌ Login failed - check your credentials or 2FA requirements")
            # Parse error message
            try:
                error_data = json.loads(response.text)
                print(f"Error: {error_data.get('errors', [{}])[0].get('message', 'Unknown error')}")
            except:
                print("Could not parse error response")
    else:
        print(f"❌ HTTP Error: {response.status_code}")
        
except requests.exceptions.RequestException as e:
    print(f"❌ Request failed: {e}")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
