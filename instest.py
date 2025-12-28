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
    'csrftoken': 'BmNt-I_2zrCJZhCDSC3Mqi',
    'datr': 'Lo1RaQ0s2F5q7mq6H-pASwAf',
    'ig_did': '4F436F83-C15F-456A-9365-77F0D22727E6',
    'mid': 'aVGNLgALAAH2E0OEaISl_MAnse8K',
    'wd': '885x779',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.instagram.com',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/',
    'sec-ch-ua': '"Brave";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Brave";v="143.0.0.0", "Chromium";v="143.0.0.0", "Not A(Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'x-asbd-id': '359341',
    'x-csrftoken': 'BmNt-I_2zrCJZhCDSC3Mqi',
    'x-fb-friendly-name': 'useCDSWebLoginMutation',
    'x-fb-lsd': 'AdElFI6SrbI',
    'x-ig-app-id': '936619743392459',
    # 'cookie': 'csrftoken=BmNt-I_2zrCJZhCDSC3Mqi; datr=Lo1RaQ0s2F5q7mq6H-pASwAf; ig_did=4F436F83-C15F-456A-9365-77F0D22727E6; mid=aVGNLgALAAH2E0OEaISl_MAnse8K; wd=885x779',
}

data = {
    'av': '0',
    '__d': 'www',
    '__user': '0',
    '__a': '1',
    '__req': 'i',
    '__hs': '20450.HYP:instagram_web_pkg.2.1...0',
    'dpr': '1',
    '__ccg': 'GOOD',
    '__rev': '1031500594',
    '__s': '8hc0dn:fr9pfp:w7ozv3',
    '__hsi': '7589002077230607721',
    '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0qa0FE2awpUO0n24o5-1ywOwv89k2C1Fwc60D85m1mzXwae4UaEW2G0AEco5G0zK1swa-0raazo7u1xwIwbS1LwTwKG0hq1Iwqo5p0qZ6goK10xKi2K7E5y1rwGwa6byohw5yw',
    '__csr': 'gLrcBdfPnOjPgD94Nkjia8alOkiuLih9eCAFrAh9EC9rCCxvCArzF9-4oOGXz9DHkCE_harl9G-AWHKGB-Ig8hed8Eqx8gMxDib3aFlMyrgG8yk2WXwEhqCF2oGbFrrKqGKl1dkqAF9aAle6Z4Bgeod889u2K8xWh5BGiag9Xx678K6kGDxqaAAw05F2yEoxG0sgM0rqw8O20EcuUtw6ZgowlE09ve1Fo6C8w3mU1sUK8w5kwN4wNw24VA6412Oxp03w816Hw0u5o0orw2Ko0Zm05a6',
    '__hsdp': 'go46NSJ5UP7wlRG9UWcKm8A26gy6dDV88ogxAwkG081wYxu0iWcyAb8cGA22cGbxR1gmh28O2ia5wwa9ghx100Otwdzw6ew1ui',
    '__hblp': '06AxuE0w63O1Nwe63q1Vwgbz8vxW3mq1qxC2G0km0Re1jwXDyo4K0eUwfG0gO2a0agwkEy2ubw2b80Si0AU1d823wOK260YE2mzEeE',
    '__sjsp': 'go46NSJ5UP7wlRG9UWcKm8Ad4V6Nzp-i2648p85aw20of8nw4Kz8F2O3aF0wzayUtgk5AgycwAyxo82yk4ogg',
    '__comet_req': '7',
    'lsd': 'AdElFI6SrbI',
    'jazoest': '2907',
    '__spin_r': '1031500594',
    '__spin_b': 'trunk',
    '__spin_t': '1766952238',
    '__crn': 'comet.igweb.PolarisCAAIGLoginHomepageRoute',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'useCDSWebLoginMutation',
    'server_timestamps': 'true',
    'variables': json.dumps({
        "input": {
            "client_mutation_id": "1",
            "actor_id": "0",
            "app": "instagram",
            "auth_domain_data_key": None,
            "caa_login_request_extra_info": {
                "ab_test_data": "",
                "shared_prefs_data": "",
                "cuid": "",
                "guid": "f403aeb52f840108c",
                "jazoest": "",
                "lgndim": "",
                "lgnjs": "1766686097",
                "lgnrnd": "",
                "locale": "",
                "login_source": "caa_login",
                "lsd": "",
                "next": "",
                "prefill_contact_point": "",
                "prefill_source": "",
                "prefill_type": "",
                "skstamp": "",
                "timezone": ""
            },
            "credential_type": "password",
            "dyi_job_id": "",
            "enc_password": {
                "sensitive_string_value": "#PWD_BROWSER:10:1766686138:AbdQAOZzsjQulmliglJJH5aJ0j55DLUiJCwCc+yrpwHQoFVbckErBhgdltmRKbLI5JZOKjeaaGSg+8wcLTJKAPiSQIperZ+7GqehmlLu8sjFwJr9XEpCf0OIeMSg0U5h4YE905LCRV2L7Q=="
            },
            "event_request_id": "e6610824-4d9f-4a26-bc47-5614f2547640",
            "identifier": "8918224528",
            "ig_web_device_id": "4F436F83-C15F-456A-9365-77F0D22727E6",
            "initial_request_id": "1",
            "lids": None,
            "login_source": "COMET_HEADERLESS_LOGIN",
            "next": None,
            "passkey_payload": None,
            "password": {
                "sensitive_string_value": "#PWD_BROWSER:10:1766686138:AbdQAOZzsjQulmliglJJH5aJ0j55DLUiJCwCc+yrpwHQoFVbckErBhgdltmRKbLI5JZOKjeaaGSg+8wcLTJKAPiSQIperZ+7GqehmlLu8sjFwJr9XEpCf0OIeMSg0U5h4YE905LCRV2L7Q=="
            },
            "persistent": True,
            "query_params": "{}",
            "trusted_device_records": "{}",
            "use_uid_to_login": False,
            "waterfall_id": "b6fad2ac-edb8-4edb-a187-8421bcdea7cb"
        }
    }),
    'doc_id': '25351082227851825',
}

response = session.post('https://www.instagram.com/api/graphql', cookies=cookies, headers=headers, data=data)

    ## Check if login was successful
wanted = ["ds_user_id", "sessionid"]
all_cookies = session.cookies.get_dict()
extracted = {k: all_cookies[k] for k in wanted if k in all_cookies}
cookie_str = "; ".join(f"{k}={v}" for k, v in extracted.items())
print("Cookies:", cookie_str)
print(response.text)
