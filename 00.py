import requests
import json
from datetime import datetime
import uuid
import time

username = 'djsistom123'  # or 'djsistom123' as in original
password = '62675345'

def generate_encrypted_password(password):
    timestamp = int(datetime.now().timestamp())
    return f"#PWD_INSTAGRAM_BROWSER:0:{timestamp}:{password}"

def generate_guid():
    return str(uuid.uuid4()).replace('-', '')[:16]

def generate_device_id():
    return str(uuid.uuid4()).upper()

# Get current timestamp
current_time = int(time.time() * 1000)

# Generate encrypted password
enc_password = generate_encrypted_password(password)

# Create the variables JSON payload
variables = {
    "input": {
        "actor_id": "0",
        "client_mutation_id": "2",
        "access_flow_version": "pre_mt_behavior",
        "account_recovery_entry_point": None,
        "app": "instagram",
        "auth_domain_data_key": None,
        "caa_login_request_extra_info": {
            "ab_test_data": "",
            "shared_prefs_data": "",
            "cuid": "",
            "guid": generate_guid(),
            "jazoest": "",
            "lgndim": "",
            "lgnjs": str(current_time),
            "lgnrnd": "",
            "locale": "",
            "login_source": "caa_login",
            "lsd": "",
            "next": "/fxcal/auth/login/?app_id=2220391788200892&etoken=AbmtqARV8MNr_s3bXdlv4Odks17CCdUG2knaxqmioU2ck4xMJzddk8pdPhsHarUMukqvsRc2qZlRc8lLXxHhzJFPWYhLujW3i6v_tXsbDDDi06Wmb2k&next=https%253A%252F%252Faccountscenter.facebook.com%252Fadd%252F%253Fauth_flow%253Dig_linking%2526background_page%253D%25252F&flow=igcalcomettest&entry_point=fb_web_settings&is_from_ig=0&is_initiator_feta=0&web_auth_logged=1",
            "prefill_contact_point": "",
            "prefill_source": "",
            "prefill_type": "",
            "skstamp": "",
            "timezone": ""
        },
        "credential_type": "password",
        "dyi_job_id": "",
        "enc_password": {
            "sensitive_string_value": enc_password
        },
        "event_request_id": str(uuid.uuid4()),
        "identifier": username,
        "ig_web_device_id": generate_device_id(),
        "initial_request_id": "1",
        "lids": None,
        "login_source": "LOGIN",
        "next": "/fxcal/auth/login/?app_id=2220391788200892&etoken=AbmtqARV8MNr_s3bXdlv4Odks17CCdUG2knaxqmioU2ck4xMJzddk8pdPhsHarUMukqvsRc2qZlRc8lLXxHhzJFPWYhLujW3i6v_tXsbDDDi06Wmb2k&next=https%253A%252F%252Faccountscenter.facebook.com%252Fadd%252F%253Fauth_flow%253Dig_linking%2526background_page%253D%25252F&flow=igcalcomettest&entry_point=fb_web_settings&is_from_ig=0&is_initiator_feta=0&web_auth_logged=1",
        "passkey_payload": None,
        "password": {
            "sensitive_string_value": enc_password
        },
        "persistent": True,
        "query_params": '{"force_authentication":null,"next":"/fxcal/auth/login/?app_id=2220391788200892&etoken=AbmtqARV8MNr_s3bXdlv4Odks17CCdUG2knaxqmioU2ck4xMJzddk8pdPhsHarUMukqvsRc2qZlRc8lLXxHhzJFPWYhLujW3i6v_tXsbDDDi06Wmb2k&next=https%253A%252F%252Faccountscenter.facebook.com%252Fadd%252F%253Fauth_flow%253Dig_linking%2526background_page%253D%25252F&flow=igcalcomettest&entry_point=fb_web_settings&is_from_ig=0&is_initiator_feta=0&web_auth_logged=1","oneTapUsers":"[\"71197200037\"]"}',
        "trusted_device_records": '{"71197200037":{"machine_id":"afAaSAALAAH1E9oBPA3kaW94g3fT","nonce":"3wQWQEa1bhApmLnMUuObWk0uwmWXdePxIg9cUI7IyfEAwTLJxEJWdB4IPKme32DX"}}',
        "use_uid_to_login": False,
        "waterfall_id": str(uuid.uuid4())
    },
    "scale": 1
}

# Convert variables to JSON string
variables_json = json.dumps(variables, separators=(',', ':'))

# The data payload
data = {
    'av': '0',
    '__d': 'www',
    '__user': '0',
    '__a': '1',
    '__req': 'l',
    '__hs': '20688.HYP:instagram_web_pkg.2.1...0',
    'dpr': '1',
    '__ccg': 'GOOD',
    '__rev': '1045824267',
    '__s': 'rxr3j7:pjqrf3:d0ggqi',
    '__hsi': '7677087663459085213',
    '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0qa0FE2awpUO0n24o5-1ywOwv89k2C1FwnE6a0D85m1mzXwae4UaEW2G0AEco5G0zK1swa-0oa2-azo7u1xwIwbS1LwTwKG1pg2Xwr86C1mgO1uQp1yU426V8aUuwm826wa6byohw5nyE7K1Hw4XwRwoE',
    '__csr': 'g9BgUIRlsdsWJN2liAh3d99ZaRQW5tgHduBf_iHrbAmHyp-4FYBAAthlR8ZF9rGhb5-hTNVd9iiO8GGAAN4RbuoAA-tAECB8rz4u7oWFfFBCy968WKaKi8FzlhpaF4K5kG8ADecghgcF84OaKuey-UgWVVEy4US2W17K6oCdx9aAdxt5DzEiDy8JDGewIJG2aqqEO00mou07Toy8gK03oq081ocEW08yCg0ZK8g5-4o5G850qi0e2p034F8eEzw0UTw0le453w0Hlw',
    '__hsdp': 'ghI4kNhhn17eYe4zy1ly84uuwK3D-E3hwZwnOeeg2SxWooyw0omU1nA0aXw0Czw',
    '__hblp': '04Xxy3D-E2jwZxe2C1kwVx-16Bwk8owd66ogzodEvwkE1zU3rwzw8y0Bo2wCxK2G0Io0V2ewcvwCwnE3Ow1Uu0cHwb-dwVwZw3Bo3jwbB1W1Qw3mE1Fo2swh819p87a0ia',
    '__sjsp': 'ghI4kNhhn17cj35Azy1ly84uuwK3C-E3hwZwnOeeg2SxWooyw',
    '__comet_req': '7',
    'lsd': 'AdR-m-1Xxm62Ymimyqjo-hJGdbY',
    'jazoest': '22360',
    '__spin_r': '1045824267',
    '__spin_b': 'trunk',
    '__spin_t': str(current_time),
    '__crn': 'comet.igweb.PolarisCAAIGLoginHomepageRoute',
    'qpl_active_flow_ids': '175125627,516759801',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'useCDSWebLoginMutation',
    'server_timestamps': 'true',
    'variables': variables_json,
    'doc_id': '9807605492696448',
    'fb_api_analytics_tags': '["qpl_active_flow_ids=175125627,516759801"]'
}

headers = {
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Google Chrome";v="145.0.7632.5", "Chromium";v="145.0.7632.5"',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-mobile': '?0',
    'X-IG-App-ID': '936619743392459',
    'X-FB-LSD': 'AdR-m-1Xxm62Ymimyqjo-hJGdbY',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-CSRFToken': 'PHHto5kyJCtXZhPpgy8OlGnoWaLlAmT6',
    'Referer': 'https://www.instagram.com/accounts/login/?force_authentication&next=%2Ffxcal%2Fauth%2Flogin%2F%3Fapp_id%3D2220391788200892%26etoken%3DAbmtqARV8MNr_s3bXdlv4Odks17CCdUG2knaxqmioU2ck4xMJzddk8pdPhsHarUMukqvsRc2qZlRc8lLXxHhzJFPWYhLujW3i6v_tXsbDDDi06Wmb2k%26next%3Dhttps%253A%252F%252Faccountscenter.facebook.com%252Fadd%252F%253Fauth_flow%253Dig_linking%2526background_page%253D%25252F%26flow%3Digcalcomettest%26entry_point%3Dfb_web_settings%26is_from_ig%3D0%26is_initiator_feta%3D0%26web_auth_logged%3D1',
    'X-IG-Max-Touch-Points': '0',
    'X-FB-Friendly-Name': 'useCDSWebLoginMutation',
    'X-ASBD-ID': '359341',
    'sec-ch-prefers-color-scheme': 'dark',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    'sec-ch-ua-platform-version': '"10.0.0"',
}

# Make the request
url = 'https://www.instagram.com/api/graphql'
response = requests.post(url, headers=headers, data=data)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
