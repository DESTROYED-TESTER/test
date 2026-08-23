import requests
import datetime
session = requests.Session()
username = 'sanju_dawar_007'
password = '626370'

time_now = int(datetime.datetime.now().timestamp())
enc_password = f"#PWD_INSTAGRAM_BROWSER:0:{time_now}:{password}"
# First, visit the login page to get fresh tokens
login_page_url = 'https://www.instagram.com/accounts/login/'
response = session.get(login_page_url)
csrf_token = session.cookies.get('csrftoken')
url = 'https://www.instagram.com/api/graphql'

headers = {
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,bn;q=0.6',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.instagram.com',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/mimi_roy_44/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Google Chrome";v="145.0.7632.5", "Chromium";v="145.0.7632.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    'x-asbd-id': '359341',
    'x-csrftoken': csrf_token,
    'x-ig-app-id': '936619743392459',
    'x-ig-max-touch-points': '0',
    'x-ig-www-claim': 'hmac.AR0lFPVrPWfUaasIaEe7P5wZzNvi4rTJt5zBnbJl9QfE-UHY',
    'x-instagram-ajax': '1045824267',
    'x-requested-with': 'XMLHttpRequest',
    'x-web-session-id': '4ziyhh:phqive:z3fwdd',
    # 'cookie': 'datr=SBrwaf3Y15r2UkQ9xEwXcQDh; ig_did=930F84D3-D442-4F9C-846F-F960E608B359; mid=afAaSAALAAH1E9oBPA3kaW94g3fT; ps_l=1; ps_n=1; csrftoken=oDNTFgzDdVPf88WsSSxeJ0FwHhxfPuEr; ds_user_id=71197200037; sessionid=71197200037%3AP8LtN0N5BN3Tst%3A28%3AAYgwEhio0gZ-Oo05l8S1hFNrSlRyDuUFaoQWA1QQBg; wd=1189x773; rur=SCU%2C17841471041129650%2C1788670351%3A01ff52172a32f247871d088231e3e4ceeb85573b1428cc241b97bb47cbbc71323b07912a',
}

# The data payload with encrypted password inserted
data = f'av=0&__d=www&__user=0&__a=1&__req=l&__hs=20688.HYP%3Ainstagram_web_pkg.2.1...0&dpr=1&__ccg=GOOD&__rev=1045824267&__s=rxr3j7%3Apjqrf3%3Ad0ggqi&__hsi=7677087663459085213&__dyn=7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0qa0FE2awpUO0n24o5-1ywOwv89k2C1FwnE6a0D85m1mzXwae4UaEW2G0AEco5G0zK1swa-0oa2-azo7u1xwIwbS1LwTwKG1pg2Xwr86C1mgO1uQp1yU426V8aUuwm826wa6byohw5nyE7K1Hw4XwRwoE&__csr=g9BgUIRlsdsWJN2liAh3d99ZaRQW5tgHduBf_iHrbAmHyp-4FYBAAthlR8ZF9rGhb5-hTNVd9iiO8GGAAN4RbuoAA-tAECB8rz4u7oWFfFBCy968WKaKi8FzlhpaF4K5kG8ADecghgcF84OaKuey-UgWVVEy4US2W17K6oCdx9aAdxt5DzEiDy8JDGewIJG2aqqEO00mou07Toy8gK03oq081ocEW08yCg0ZK8g5-4o5G850qi0e2p034F8eEzw0UTw0le453w0Hlw&__hsdp=ghI4kNhhn17eYe4zy1ly84uuwK3D-E3hwZwnOeeg2SxWooyw0omU1nA0aXw0Czw&__hblp=04Xxy3D-E2jwZxe2C1kwVx-16Bwk8owd66ogzodEvwkE1zU3rwzw8y0Bo2wCxK2G0Io0V2ewcvwCwnE3Ow1Uu0cHwb-dwVwZw3Bo3jwbB1W1Qw3mE1Fo2swh819p87a0ia&__sjsp=ghI4kNhhn17cj35Azy1ly84uuwK3C-E3hwZwnOeeg2SxWooyw&__comet_req=7&lsd=AdR-m-1Xxm62Ymimyqjo-hJGdbY&jazoest=22360&__spin_r=1045824267&__spin_b=trunk&__spin_t={time_now}&__crn=comet.igweb.PolarisCAAIGLoginHomepageRoute&qpl_active_flow_ids=175125627%2C516759801&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=useCDSWebLoginMutation&server_timestamps=true&variables=%7B%22input%22%3A%7B%22actor_id%22%3A%220%22%2C%22client_mutation_id%22%3A%222%22%2C%22access_flow_version%22%3A%22pre_mt_behavior%22%2C%22account_recovery_entry_point%22%3Anull%2C%22app%22%3A%22instagram%22%2C%22auth_domain_data_key%22%3Anull%2C%22caa_login_request_extra_info%22%3A%7B%22ab_test_data%22%3A%22%22%2C%22shared_prefs_data%22%3A%22%22%2C%22cuid%22%3A%22%22%2C%22guid%22%3A%22f29c66bd23eb38508%22%2C%22jazoest%22%3A%22%22%2C%22lgndim%22%3A%22%22%2C%22lgnjs%22%3A%22{time_now}%22%2C%22lgnrnd%22%3A%22%22%2C%22locale%22%3A%22%22%2C%22login_source%22%3A%22caa_login%22%2C%22lsd%22%3A%22%22%2C%22next%22%3A%22%2Ffxcal%2Fauth%2Flogin%2F%3Fapp_id%3D2220391788200892%26etoken%3DAbmtqARV8MNr_s3bXdlv4Odks17CCdUG2knaxqmioU2ck4xMJzddk8pdPhsHarUMukqvsRc2qZlRc8lLXxHhzJFPWYhLujW3i6v_tXsbDDDi06Wmb2k%26next%3Dhttps%25253A%25252F%25252Faccountscenter.facebook.com%25252Fadd%25252F%25253Fauth_flow%25253Dig_linking%252526background_page%25253D%2525252F%26flow%3Digcalcomettest%26entry_point%3Dfb_web_settings%26is_from_ig%3D0%26is_initiator_feta%3D0%26web_auth_logged%3D1%22%2C%22prefill_contact_point%22%3A%22%22%2C%22prefill_source%22%3A%22%22%2C%22prefill_type%22%3A%22%22%2C%22skstamp%22%3A%22%22%2C%22timezone%22%3A%22%22%7D%2C%22credential_type%22%3A%22password%22%2C%22dyi_job_id%22%3A%22%22%2C%22enc_password%22%3A%7B%22sensitive_string_value%22%3A%22{enc_password}%22%7D%2C%22event_request_id%22%3A%22e5c6a142-09f0-42cc-89f9-0539937cab04%22%2C%22identifier%22%3A%22{username}%22%2C%22ig_web_device_id%22%3A%22930F84D3-D442-4F9C-846F-F960E608B359%22%2C%22initial_request_id%22%3A%221%22%2C%22lids%22%3Anull%2C%22login_source%22%3A%22LOGIN%22%2C%22next%22%3A%22%2Ffxcal%2Fauth%2Flogin%2F%3Fapp_id%3D2220391788200892%26etoken%3DAbmtqARV8MNr_s3bXdlv4Odks17CCdUG2knaxqmioU2ck4xMJzddk8pdPhsHarUMukqvsRc2qZlRc8lLXxHhzJFPWYhLujW3i6v_tXsbDDDi06Wmb2k%26next%3Dhttps%253A%252F%252Faccountscenter.facebook.com%252Fadd%252F%253Fauth_flow%253Dig_linking%2526background_page%253D%25252F%26flow%3Digcalcomettest%26entry_point%3Dfb_web_settings%26is_from_ig%3D0%26is_initiator_feta%3D0%26web_auth_logged%3D1%22%2C%22passkey_payload%22%3Anull%2C%22password%22%3A%7B%22sensitive_string_value%22%3A%22{enc_password}%22%7D%2C%22persistent%22%3Atrue%2C%22query_params%22%3A%22%7B%5C%22force_authentication%5C%22%3Anull%2C%5C%22next%5C%22%3A%5C%22%2Ffxcal%2Fauth%2Flogin%2F%3Fapp_id%3D2220391788200892%26etoken%3DAbmtqARV8MNr_s3bXdlv4Odks17CCdUG2knaxqmioU2ck4xMJzddk8pdPhsHarUMukqvsRc2qZlRc8lLXxHhzJFPWYhLujW3i6v_tXsbDDDi06Wmb2k%26next%3Dhttps%253A%252F%252Faccountscenter.facebook.com%252Fadd%252F%253Fauth_flow%253Dig_linking%2526background_page%253D%25252F%26flow%3Digcalcomettest%26entry_point%3Dfb_web_settings%26is_from_ig%3D0%26is_initiator_feta%3D0%26web_auth_logged%3D1%5C%22%2C%5C%22oneTapUsers%5C%22%3A%5C%22%5B%5C%5C%5C%2271197200037%5C%5C%5C%22%5D%5C%22%7D%22%2C%22trusted_device_records%22%3A%22%7B%5C%2271197200037%5C%22%3A%7B%5C%22machine_id%5C%22%3A%5C%22afAaSAALAAH1E9oBPA3kaW94g3fT%5C%22%2C%5C%22nonce%5C%22%3A%5C%223wQWQEa1bhApmLnMUuObWk0uwmWXdePxIg9cUI7IyfEAwTLJxEJWdB4IPKme32DX%5C%22%7D%7D%22%2C%22use_uid_to_login%22%3Afalse%2C%22waterfall_id%22%3A%22bd435455-062e-4365-abb6-ed8fd4934f22%22%7D%2C%22scale%22%3A1%7D&doc_id=9807605492696448&fb_api_analytics_tags=%5B%22qpl_active_flow_ids%3D175125627%2C516759801%22%5D'

response = requests.post(url, headers=headers, data=data)

print(response.status_code)
print(response.text)
