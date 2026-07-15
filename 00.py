import requests

import requests

cookies = {
    'datr': 'T2pMatYpRyu33ilGGvWEcgBf',
    'sb': 'U2pMao6sufYLNdm4lzUwZb9P',
    'checkpoint': '%7B%22u%22%3A100047459924718%2C%22t%22%3A1784135224%2C%22step%22%3A0%2C%22n%22%3A%22bfeHqxOqpJw%3D%22%2C%22inst%22%3A1538401414418508%2C%22f%22%3A465803052217681%2C%22st%22%3A%22c%22%2C%22aid%22%3Anull%2C%22ca%22%3Anull%2C%22la%22%3A%22%22%2C%22ta%22%3A%221784135234.ch.s%3An619%3Apw.9zBEAiBDtkZkMGeeixGMYr-J6h8yDBgV_i9E0Pr2yvOj0Ch12QIgKPRruuaz18lzOSCPubku4lf_QThprPkSQATVKnd7Z7s%22%2C%22tfvaid%22%3Anull%2C%22tfvasec%22%3Anull%2C%22sat%22%3Anull%2C%22idg%22%3Afalse%2C%22cidue%22%3A%22%22%2C%22tfuln%22%3Anull%2C%22tfvri%22%3Anull%2C%22ct%22%3A%22AWTuuQbv9HUC3Cky_cbOPJ98Kf_FOp_yebYShYSLg4tqwAr2mzC2Q1RDbkJ-DBlM-a8hDHNlPqbBRylHNIvCldtXuPBryZi7gMAxf4ZkIQeUlnUHgoLRFtI0vuuDtrAxC3AWZz4CEW0jbi90N4dzusuxBhPbZ_rFVS4IiU1i4v1ZvX_UymjLqt61YwhKtC_r7_vZRUmj8VkzQ3RR9QTJaKEiEaAYXRHUjPybrJ913jNvLFehj53eF9Ud6G9n7wHHgxuR5oKhJ3tGPT1KqFNf7a55MvHAKTilnN9Ce3d1ejkxiUupl7DG2U-Sr8X9MEI6VH_s-jZa-XlfW6TdhMkmwUpywpSEE57IoSuRInwTeQdH6fZgvN4y4EPnxWUoDgvKC4Gb_WV0yy2VjEnhkVjMTNC-1q1bEK3v1A%22%2C%22aads%22%3Anull%2C%22s%22%3A%22AWbPN4k3OAML8RkCXnA%22%2C%22cs%22%3A%5B%5D%2C%22ssp%22%3A1%7D',
    'locale': 'en_GB',
    'ps_l': '1',
    'ps_n': '1',
    'm_pixel_ratio': '2',
    'wd': '400x686',
    'sfau': 'AYgGJlpvaeydwl_7O1GE50k0B1IdSxB7V0DbknHNjp33Rhm9y_xe8Ok0XCgJGSPXPyylgpO3cSy1mWTS5Qlh7NbxreZeRTFYiwurTjD4uxsLdCNJL1M4MRSjMyPKMrWzVET4riOCE5gG7Efe49lX5fRL4hMcibTlvszrEuIfG9xKPngzBVWWNQhU2DxTVds2m-AwJeiaGgCRR_1H8yGL5M1VELQZ-3QiRo2NrB6SbJKcX94oGwsl-SQK6uUGl9FzcrfGOawmwulzdTFB3jzMiEMz',
    'fr': '0jqlpbnLhz2sgCMRv..BqV73S..AAA.0.0.BqV8gs.AWeFfEaUJgxKs6SvthdbtycjeN8',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'origin': 'https://m.facebook.com',
    'priority': 'u=1, i',
    'referer': 'https://m.facebook.com/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-full-version-list': '"Not;A=Brand";v="99.0.0.0", "Google Chrome";v="139.0.7258.139", "Chromium";v="139.0.7258.139"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Nexus 5"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"6.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'datr=T2pMatYpRyu33ilGGvWEcgBf; sb=U2pMao6sufYLNdm4lzUwZb9P; checkpoint=%7B%22u%22%3A100047459924718%2C%22t%22%3A1784135224%2C%22step%22%3A0%2C%22n%22%3A%22bfeHqxOqpJw%3D%22%2C%22inst%22%3A1538401414418508%2C%22f%22%3A465803052217681%2C%22st%22%3A%22c%22%2C%22aid%22%3Anull%2C%22ca%22%3Anull%2C%22la%22%3A%22%22%2C%22ta%22%3A%221784135234.ch.s%3An619%3Apw.9zBEAiBDtkZkMGeeixGMYr-J6h8yDBgV_i9E0Pr2yvOj0Ch12QIgKPRruuaz18lzOSCPubku4lf_QThprPkSQATVKnd7Z7s%22%2C%22tfvaid%22%3Anull%2C%22tfvasec%22%3Anull%2C%22sat%22%3Anull%2C%22idg%22%3Afalse%2C%22cidue%22%3A%22%22%2C%22tfuln%22%3Anull%2C%22tfvri%22%3Anull%2C%22ct%22%3A%22AWTuuQbv9HUC3Cky_cbOPJ98Kf_FOp_yebYShYSLg4tqwAr2mzC2Q1RDbkJ-DBlM-a8hDHNlPqbBRylHNIvCldtXuPBryZi7gMAxf4ZkIQeUlnUHgoLRFtI0vuuDtrAxC3AWZz4CEW0jbi90N4dzusuxBhPbZ_rFVS4IiU1i4v1ZvX_UymjLqt61YwhKtC_r7_vZRUmj8VkzQ3RR9QTJaKEiEaAYXRHUjPybrJ913jNvLFehj53eF9Ud6G9n7wHHgxuR5oKhJ3tGPT1KqFNf7a55MvHAKTilnN9Ce3d1ejkxiUupl7DG2U-Sr8X9MEI6VH_s-jZa-XlfW6TdhMkmwUpywpSEE57IoSuRInwTeQdH6fZgvN4y4EPnxWUoDgvKC4Gb_WV0yy2VjEnhkVjMTNC-1q1bEK3v1A%22%2C%22aads%22%3Anull%2C%22s%22%3A%22AWbPN4k3OAML8RkCXnA%22%2C%22cs%22%3A%5B%5D%2C%22ssp%22%3A1%7D; locale=en_GB; ps_l=1; ps_n=1; m_pixel_ratio=2; wd=400x686; sfau=AYgGJlpvaeydwl_7O1GE50k0B1IdSxB7V0DbknHNjp33Rhm9y_xe8Ok0XCgJGSPXPyylgpO3cSy1mWTS5Qlh7NbxreZeRTFYiwurTjD4uxsLdCNJL1M4MRSjMyPKMrWzVET4riOCE5gG7Efe49lX5fRL4hMcibTlvszrEuIfG9xKPngzBVWWNQhU2DxTVds2m-AwJeiaGgCRR_1H8yGL5M1VELQZ-3QiRo2NrB6SbJKcX94oGwsl-SQK6uUGl9FzcrfGOawmwulzdTFB3jzMiEMz; fr=0jqlpbnLhz2sgCMRv..BqV73S..AAA.0.0.BqV8gs.AWeFfEaUJgxKs6SvthdbtycjeN8',
}

params = {
    'appid': 'com.bloks.www.bloks.caa.login.async.send_login_request',
    'type': 'action',
    '__bkv': '5690ad2fda139a918bf005ada8d714228ff398260630dc694697ac35ea3ac9de',
}

data = {
    '__aaid': '0',
    '__user': '0',
    '__a': '1',
    '__req': 'r',
    '__hs': '20649.BP:wbloks_caa_pkg.2.0...0',
    'dpr': '3',
    '__ccg': 'GOOD',
    '__rev': '1043203988',
    '__s': 'mktv5z:7a7rcd:wpo6qv',
    '__hsi': '7662813034871606553',
    '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x67o1g8hw23E52q1ew2io0D24o1MUaE1Do1u81x82ewnE3fwww5NyE25w8W0Lo6-1CwOw5jw4JwzK0zo3jwea',
    'fb_dtsg': 'bfeHqxOqpJw=',
    'jazoest': '21164',
    'lsd': '3LPgrtTv3JuEa_SuZ9_d8z',
    'params': '{"params":"{\\"server_params\\":{\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"dilpob:58\\",\\"password_text_input_id\\":\\"dilpob:59\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":0,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_aymh\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"two_step_login_type\\":\\"one_step_login\\",\\"left_nav_button_action\\":\\"NONE\\",\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"81730642700315\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"7f8272dd-4b22-4761-af2b-63a20a1d9141\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\",\\"login_surface\\":\\"login_home\\",\\"login_entry_point\\":\\"logged_out\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"cloud_trust_token\\":null,\\"block_store_machine_id\\":\\"\\",\\"zero_balance_state\\":\\"\\",\\"contact_point\\":\\"9382296421\\",\\"password\\":\\"#PWD_BROWSER:5:1784137772:AY1QAJcXxdlUPii+izlxGhL+3BNZ+XqWyrvTEXu7MSTGcAAPdRdP8M8hzvO0g/mWIt8p453b1SRH12c6n+rS9l1O+dNAmhEnIJxvS2fwLP4ZoYBEcDgfZC+Ghb1cROYL0OZbmSXaeuCdIGzyN6g=\\",\\"accounts_list\\":[],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":2,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"gms_incoming_call_retriever_eligibility\\":\\"client_not_supported\\",\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"aymh_accounts\\":[{\\"id\\":\\"\\",\\"profiles\\":{\\"id\\":{\\"user_id\\":\\"\\",\\"name\\":\\"\\",\\"profile_picture_url\\":\\"\\",\\"small_profile_picture_url\\":null,\\"notification_count\\":0,\\"credential_type\\":\\"none\\",\\"token\\":\\"\\",\\"last_access_time\\":0,\\"is_derived\\":0,\\"username\\":\\"\\",\\"password\\":\\"\\",\\"has_smartlock\\":0,\\"account_center_id\\":\\"\\",\\"account_source\\":\\"\\",\\"credentials\\":[],\\"nta_eligibility_reason\\":null,\\"from_accurate_privacy_result\\":0,\\"dbln_validated\\":0}}}],\\"sso_accounts_auth_data\\":[],\\"blocked_uids\\":[],\\"network_bssid\\":null,\\"lois_settings\\":{\\"lois_token\\":\\"\\"},\\"aac\\":\\"\\"}}"}',
}

response = requests.post('https://m.facebook.com/async/wbloks/fetch/', params=params, cookies=cookies, headers=headers, data=data)

# Print response metadata
print(f"Status Code: {response.status_code}")
print(response.text[:500]) # Prints the first 500 characters of the payload
