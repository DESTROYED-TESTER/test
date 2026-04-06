import requests,json,time


session = requests.Session()
cookies = {
    'datr': 'h3mDaRuTI_GQPEWt-Bi2FwNH',
    'sb': 'h3mDaZGUIq8Dh_QCRYakcHRG',
    'ps_l': '1',
    'ps_n': '1',
    'fr': '0V99TyOmvdy5qQtEp..Bpg3mH..AAA.0.0.Bp00Qa.AWcq_YKEsoVTxwHCvl4ECR74YLQ',
    'wd': '700x786',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7,hi;q=0.6,gu;q=0.5,bn;q=0.4',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.facebook.com',
    'priority': 'u=1, i',
    'referer': 'https://www.facebook.com/login/?next=https%3A%2F%2Fbusiness.facebook.com%2Fbusiness%2Funifiedfblogin%2Fcallback%2F%3Fnext%3Dhttps%253A%252F%252Fbusiness.facebook.com%252F%253Fnav_ref%253Dbiz_unified_f3_login_page_to_mbs%2526biz_login_source%253Dbiz_unified_f3_fb_login_button%2526join_id%253D48c767e5-02a7-4c47-911a-fb3b374baf42%26f3_request_id%3Dajaodfolgnciifkhdjbnmokidfdfiiaennnkoohk%26full_page_redirect%3D0&request_id=ajaodfolgnciifkhdjbnmokidfdfiiaennnkoohk',
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
    'x-fb-friendly-name': 'useCDSWebLoginMutation',
    'x-fb-lsd': 'AdS-cN2PzP4mDM4ep3oiYVAwsNI',
    # 'cookie': 'datr=h3mDaRuTI_GQPEWt-Bi2FwNH; sb=h3mDaZGUIq8Dh_QCRYakcHRG; ps_l=1; ps_n=1; fr=0V99TyOmvdy5qQtEp..Bpg3mH..AAA.0.0.Bp00Qa.AWcq_YKEsoVTxwHCvl4ECR74YLQ; wd=700x786',
}


data = {
    'av': '0',
    '__aaid': '0',
    '__user': '0',
    '__a': '1',
    '__req': 'b',
    '__hs': '20549.HYP:comet_loggedout_pkg.2.1...0',
    'dpr': '1',
    '__ccg': 'EXCELLENT',
    '__rev': '1036705643',
    '__s': '6q8q1j:1mcuv0:y55xrm',
    '__hsi': '7625513474556908922',
    '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0qa0FE2awpUO0n24oaEd86a3a1YwBgao6C0Mo2swaOfK0EUjwGzE2ZwNwmE2eUlwhE2Lw6OyES1Tw8W0Lo6-1CG0hq1Iwqo5p0qWCgoK1sigaU7u0jW4o4W0he0oq0D8',
    '__csr': 'siwH2_32ax4T4hqaBA_z8zAmdBxDwKypoO4EF1aazS5EO598sggx2dxe4FAi2a5U2gUaEB5gKcxm4ovwGwwCx-18wxxS19U0M236S1CCxW4qG3-1Yw6Tw33U8ocU2owh7wam04nU0d5E2mw0MTgy5Vk2vw16-i1Pw4cw2EU0u5w0fMa8o0f6F82pxS0Ck0hj809Xw18C0fjw3Vo2ow2-EYyxx010S058k1Uwe501wqcyo0bkm04uo4eaN00h_hQ8zFp80kRwjEG1ao08Gp95wbmii8w6pykq7E0mfBw1Ibw',
    '__hsdp': 'gcGaiH3RgJ7Jo0Ci09xw4kw4Dw2aE0c182gw7Dwei0CE23ws80-e',
    '__hblp': '0aK0dew6iw4kw4Dw2aE3EwlE7C0s20ahw6fw3UE24wLwo81VU3AzE2bxqbzEkwYws81yohwf20M8c8d8bUjwRG0iy0i-',
    '__sjsp': 'gcGaiH2JOl2QuRw2p8',
    '__comet_req': '15',
    'lsd': 'AdS-cN2PzP4mDM4ep3oiYVAwsNI',
    'jazoest': '22265',
    '__spin_r': '1036705643',
    '__spin_b': 'trunk',
    '__spin_t': '1775453210',
    'qpl_active_flow_ids': '175125627,516759801',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'useCDSWebLoginMutation',
    'server_timestamps': 'true',
    'variables': json.dumps({
        "input": {
            "actor_id": "0",
            "client_mutation_id": "1",
            "access_flow_version": "pre_mt_behavior",
            "app": "facebook",
            "auth_domain_data_key": None,
            "caa_login_request_extra_info": {
                "ab_test_data": "/AAAAAAAAAAAAAAAf/AAAfAAAAAAAAAAAAfAAAAAA/yMAAAAMADBAG",
                "shared_prefs_data": "eyIzMDAwMCI6W3sidCI6MTc3NTQ1MzIxMi42NDUsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi8ifSwidiI6ZmFsc2V9XSwiMzAwMDEiOlt7InQiOjE3NzU0NTMyMTIuNjQ1LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4vIn0sInYiOjV9XSwiMzAwMDIiOlt7InQiOjE3NzU0NTMyMTIuNjQ1LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4vIn0sInYiOjJ9XSwiMzAwMDMiOlt7InQiOjE3NzU0NTMyMTIuNjQ4LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4vIn0sInYiOlsiZW4tSU4iLCJlbi1VUyIsImVuLUdCIiwiZW4iLCJoaSIsImd1IiwiYm4iXX1dLCIzMDAwNCI6W3sidCI6MTc3NTQ1MzIxMi42NDksImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi8ifSwidiI6MTUwfV0sIjMwMDA1IjpbeyJ0IjoxNzc1NDUzMjEyLjY0OSwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luLyJ9LCJ2Ijp7InciOjcwMCwiaCI6Nzg2fX1dLCIzMDAwNyI6W3sidCI6MTc3NTQ1MzIxMi42NDksImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi8ifSwidiI6ImRlZmF1bHQifV0sIjMwMDA4IjpbeyJ0IjoxNzc1NDUzMjEyLjY4OCwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luLyJ9LCJ2IjoicHJvbXB0In1dLCIzMDAxMiI6W3sidCI6MTc3NTQ1MzIxMi42NSwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luLyJ9LCJ2IjoiR29vZ2xlIEluYy4ifV0sIjMwMDEzIjpbeyJ0IjoxNzc1NDUzMjEyLjY1MSwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luLyJ9LCJ2IjoiNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xNDUuMC4wLjAgU2FmYXJpLzUzNy4zNiJ9XSwiMzAwMTUiOlt7InQiOjE3NzU0NTMyMTIuNjUxLCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4vIn0sInYiOiJXaW4zMiJ9XSwiMzAwMTgiOlt7InQiOjE3NzU0NTMyMTIuNjUxLCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4vIn0sInYiOjJ9XSwiMzAwMjIiOlt7InQiOjE3NzU0NTMyMTIuNjY2LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4vIn0sInYiOnRydWV9XSwiMzAwNDAiOlt7InQiOjE3NzU0NTMyMTIuNjY3LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4vIn0sInYiOi0zMzB9XSwiMzAwOTMiOlt7InQiOjE3NzU0NTMyMTIuNjY3LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4vIn0sInYiOjB9XSwiMzAwOTQiOlt7InQiOjE3NzU0NTMyMTIuNjY3LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4vIn0sInYiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTQ1LjAuMC4wIFNhZmFyaS81MzcuMzYifV0sIjMwMDk1IjpbeyJ0IjoxNzc1NDUzMjEyLjY2NywiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luLyJ9LCJ2IjoxfV0sIjMwMTA2IjpbeyJ0IjoxNzc1NDUzMjEyLjY0MywiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luLyJ9LCJ2IjpmYWxzZX0seyJ0IjoxNzc1NDUzMjE0LjU1NCwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luLyJ9LCJ2Ijp0cnVlfV0sIjMwMTA3IjpbeyJ0IjoxNzc1NDUzMjEyLjY0NCwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luLyJ9LCJ2IjpmYWxzZX1dfQ==",
                "cuid": "",
                "guid": "f98454881ff44b2c1",
                "jazoest": "22190",
                "lgndim": "eyJ3IjoxNDQwLCJoIjo5MDAsImF3IjoxNDQwLCJhaCI6ODYwLCJjIjozMn0=",
                "lgnjs": "1775453212",
                "lgnrnd": "222650_45m0",
                "locale": "bn_IN",
                "login_source": "comet_headerless_login",
                "lsd": "AdS-cN2PzP4mDM4ep3oiYVAw6DE",
                "next": "https://business.facebook.com/business/unifiedfblogin/callback/?next=https%253A%252F%252Fbusiness.facebook.com%252F%253Fnav_ref%253Dbiz_unified_f3_login_page_to_mbs%2526biz_login_source%253Dbiz_unified_f3_fb_login_button%2526join_id%253D48c767e5-02a7-4c47-911a-fb3b374baf42&f3_request_id=ajaodfolgnciifkhdjbnmokidfdfiiaennnkoohk&full_page_redirect=0",
                "prefill_contact_point": "",
                "prefill_source": "",
                "prefill_type": "",
                "skstamp": "",
                "timezone": "-330"
            },
            "credential_type": "password",
            "dyi_job_id": "",
            "enc_password": {
                "sensitive_string_value": "#PWD_BROWSER:5:1775453257:ASpQAKYBqBKkLJn753ICiWAiu70S8wnQoYzn5f9Y1hDT6mgwwXxspG63jHJHRwf8KvwqxHitbw+PyckN3WWDAH9NqNIUB7ion+R10vi3qicELKfMOTjo9muhhfk7vO/QF7kUQmWGnFKyd2OcLw=="
            },
            "event_request_id": "357092f8-15e6-42e7-a4ed-7fffe83b0841",
            "identifier": "61575467930154",
            "ig_web_device_id": None,
            "initial_request_id": "1",
            "lids": None,
            "login_source": "LOGIN",
            "next": "https://business.facebook.com/business/unifiedfblogin/callback/?next=https%3A%2F%2Fbusiness.facebook.com%2F%3Fnav_ref%3Dbiz_unified_f3_login_page_to_mbs%26biz_login_source%3Dbiz_unified_f3_fb_login_button%26join_id%3D48c767e5-02a7-4c47-911a-fb3b374baf42&f3_request_id=ajaodfolgnciifkhdjbnmokidfdfiiaennnkoohk&full_page_redirect=0",
            "passkey_payload": None,
            "password": {
                "sensitive_string_value": "#PWD_BROWSER:5:1775453257:ASpQAKYBqBKkLJn753ICiWAiu70S8wnQoYzn5f9Y1hDT6mgwwXxspG63jHJHRwf8KvwqxHitbw+PyckN3WWDAH9NqNIUB7ion+R10vi3qicELKfMOTjo9muhhfk7vO/QF7kUQmWGnFKyd2OcLw=="
            },
            "persistent": True,
            "query_params": "{\"next\":\"https://business.facebook.com/business/unifiedfblogin/callback/?next=https%3A%2F%2Fbusiness.facebook.com%2F%3Fnav_ref%3Dbiz_unified_f3_login_page_to_mbs%26biz_login_source%3Dbiz_unified_f3_fb_login_button%26join_id%3D48c767e5-02a7-4c47-911a-fb3b374baf42&f3_request_id=ajaodfolgnciifkhdjbnmokidfdfiiaennnkoohk&full_page_redirect=0\\\",\\\"request_id\\\":\\\"ajaodfolgnciifkhdjbnmokidfdfiiaennnkoohk\\\"}",
            "trusted_device_records": "{}",
            "use_uid_to_login": False,
            "waterfall_id": "ajaodfolgnciifkhdjbnmokidfdfiiaennnkoohk"
        }
    }),
    'doc_id': '9807605492696448',
    'fb_api_analytics_tags': '["qpl_active_flow_ids=175125627,516759801"]',
}


response = requests.post('https://www.facebook.com/api/graphql/', cookies=cookies, headers=headers, data=data)
# Get cookies after request
cookie_dict = session.cookies.get_dict()

if "c_user" in cookie_dict:
    print("✅ Login success")
    print("User ID:", cookie_dict["c_user"])
else:
    print("❌ Login failed")
