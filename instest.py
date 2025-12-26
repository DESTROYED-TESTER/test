import requests

session = requests.Session()

cookies = {
    'ig_did': 'D069581B-C422-4096-9D2B-D592084D58FF',
    'csrftoken': 'M6pJlXaPItT_AvHbjJUtSA',
    'datr': '5nVJaQHM2QMcbAVBnTN1nd4f',
    'wd': '1440x566',
    'mid': 'aUl15gALAAFW6QEW0QpMl3CLgsAR',
    'ig_nrcb': '1',
    'ps_l': '1',
    'ps_n': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:146.0) Gecko/20100101 Firefox/146.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-FB-Friendly-Name': 'useCDSWebLoginMutation',
    'X-CSRFToken': 'M6pJlXaPItT_AvHbjJUtSA',
    'X-IG-App-ID': '936619743392459',
    'X-FB-LSD': 'AdGyjbpBIgk',
    'X-ASBD-ID': '359341',
    'Origin': 'https://www.instagram.com',
    'Alt-Used': 'www.instagram.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.instagram.com/accounts/login/?hl=en',
    # 'Cookie': 'ig_did=D069581B-C422-4096-9D2B-D592084D58FF; csrftoken=M6pJlXaPItT_AvHbjJUtSA; datr=5nVJaQHM2QMcbAVBnTN1nd4f; wd=1440x566; mid=aUl15gALAAFW6QEW0QpMl3CLgsAR; ig_nrcb=1; ps_l=1; ps_n=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

data = {
    'av': '0',
    'hl': 'en',
    '__d': 'www',
    '__user': '0',
    '__a': '1',
    '__req': '9',
    '__hs': '20448.HYP:instagram_web_pkg.2.1...0',
    'dpr': '1',
    '__ccg': 'MODERATE',
    '__rev': '1031477873',
    '__s': 'vx1l8w:k75u7m:pgyknv',
    '__hsi': '7588142348331216302',
    '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0qa0FE2awt81s8hwnU6a3a1YwBgao6C0Mo2swlo5q4U2zxe2GewGw9a361qw8Xwn82Lw6OyES1Twoob82ZwrUdUbGw4mwr86C1mg6LhA6bwg8rAwHxW1owmUaE2xyUC4o1oE',
    '__csr': 'gGJlj6YYQh9kYl5l7RNfaAiKijrGRHLFrAt4im-mq4oyuEmJ3F98rpUyfiVqjSFpO4nK_myWGBykHkSv9N4JCQ4oLBz_mGhQl24Sz4hkDmFbhr98DmAdCH98ByEqy8Waz9p99GzVUDxrzoG8Q49UZ1O14h8Twwz8dUgyojKu2mU-5EKazojyoyryoS8y8cU01pn83DKU1BHa07bVeU2ya1lyo1Jdw0Fsoqg1be0a1w4Nxd05xwhC4oaA2a9x507Mo56ac0dXwf-i01UGw1yS0b2w3Qo0jco',
    '__hsdp': 'go42s-QngP7wkoxaEBa4FedAXv6h5Ouh6yUlyErAJw2hV84-1tyFUGpxu0wi0Z-2m4N1osa8gmgjg8U0dUE1GUK0nC06xU',
    '__hblp': '04pw8ai09dwl84S2abw4SxqUkwwwhU2kwgo7u0xo0w65UoxW04SU0TK0JUjwio9U2Iw-wOw24E0ghw8W3S0Z828wABwro2Jweq3G',
    '__sjsp': 'go42s-QngP7wkoxaEBa4FedAXv6sTOuh6yUlyErAJw2hV84-1txaaConw84wfvwBxcgm72y45A4Q2e',
    '__comet_req': '7',
    'lsd': 'AdGyjbpBIgk',
    'jazoest': '21022',
    '__spin_r': '1031477873',
    '__spin_b': 'trunk',
    '__spin_t': '1766752067',
    '__crn': 'comet.igweb.PolarisCAAIGLoginHomepageRoute',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'useCDSWebLoginMutation',
    'server_timestamps': 'true',
    'variables': '{"input":{"client_mutation_id":"1","actor_id":"0","app":"instagram","auth_domain_data_key":null,"caa_login_request_extra_info":{"ab_test_data":"","shared_prefs_data":"","cuid":"","guid":"f72f6210cd2291f95","jazoest":"","lgndim":"","lgnjs":"1766686140","lgnrnd":"","locale":"","login_source":"caa_login","lsd":"","next":"","prefill_contact_point":"","prefill_source":"","prefill_type":"","skstamp":"","timezone":""},"credential_type":"password","dyi_job_id":"","enc_password":{"sensitive_string_value":"#PWD_BROWSER:10:1766686199:AbRQAA2u7IofUWbpokla/oJmVQugTcHwGB+s0x61+Ul18ToavnrHQGF+sxuTw0u3QZYrgKQFqd5HWbh3p3AQSWilcby/4YaeTMK+Ibc8ZgrYG75/g7VEi139xcPTxQAcqxSnaJwdC8/jNQ=="},"event_request_id":"292f17cc-9c78-47b3-bec0-c657a9249031","identifier":"8918224528","ig_web_device_id":"D069581B-C422-4096-9D2B-D592084D58FF","initial_request_id":"1","lids":null,"login_source":"LOGIN","next":null,"passkey_payload":null,"password":{"sensitive_string_value":"#PWD_BROWSER:10:1766686199:AbRQAA2u7IofUWbpokla/oJmVQugTcHwGB+s0x61+Ul18ToavnrHQGF+sxuTw0u3QZYrgKQFqd5HWbh3p3AQSWilcby/4YaeTMK+Ibc8ZgrYG75/g7VEi139xcPTxQAcqxSnaJwdC8/jNQ=="},"persistent":true,"query_params":"{\\"hl\\":\\"en\\"}","trusted_device_records":"{}","use_uid_to_login":false,"waterfall_id":"0616b2cd-4d7b-408a-ae47-1ca405edf6ce"},"scale":1}',
    'doc_id': '25351082227851825',
}

response = requests.post('https://www.instagram.com/api/graphql', cookies=cookies, headers=headers, data=data)


try:
    res_json = response.json()
except ValueError:
    print("Invalid JSON response")
    exit()

# Basic success checks
login_data = res_json.get("data", {}).get("login", {}) \
    or res_json.get("data", {}).get("useCDSWebLoginMutation", {})

if login_data.get("authenticated") is True:
    print("[+] Login successful")
elif "errors" in res_json:
    print("[-] Login failed:", res_json["errors"])
else:
    print("[-] Login failed or checkpoint required")

