#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instagram User ID Fetcher & Follower/Following Dumper
Unlimited dump with high-speed optimization - Single file output
"""

import requests
import json
import re
import time
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# Color codes
RED = "\033[1;91m"
GREEN = "\033[1;92m"
YELLOW = "\033[1;93m"
BLUE = "\033[1;94m"
WHITE = "\033[1;97m"
CYAN = "\033[1;96m"
RESET = "\033[0m"

# Global variables
Uuid = []
xx = 0
total_collected = 0
lock = threading.Lock()
stop_dump = False
current_username = ""
dump_filename = ""

# User agent for API requests
ua = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 instagram 360.0.0.33.104 (iPhone16,2; iOS 18.2; en_US; en; scale=3.00; 1170x2532; 510000000)'
}

def clear():
    """Clear screen"""
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        print('\n' * 100)

def linex():
    """Print decorative line separator"""
    print(f"{WHITE}{'='*56}{RESET}")

def test_cookies(coki):
    """Test if cookies are still valid using multiple methods"""
    
    if isinstance(coki, str):
        coki = {'cookie': coki}
    
    print(f"{YELLOW}Testing cookies...{RESET}")
    
    # Method 1: Try to get user info using the API
    try:
        cookie_str = coki.get('cookie', '') if isinstance(coki, dict) else str(coki)
        uid_match = re.search(r'ds_user_id=(\d+)', cookie_str)
        
        if uid_match:
            uid = uid_match.group(1)
            response = requests.get(
                f'https://i.instagram.com/api/v1/users/{uid}/info/',
                headers=ua,
                cookies=coki,
                timeout=10
            )
            
            if response.status_code == 200:
                try:
                    data = response.json()
                    if 'user' in data and data['user'].get('username'):
                        print(f"{GREEN}✓ Cookies are valid!{RESET}")
                        print(f"{WHITE}  Username: {CYAN}{data['user'].get('username')}{RESET}")
                        print(f"{WHITE}  Full Name: {CYAN}{data['user'].get('full_name', 'N/A')}{RESET}")
                        print(f"{WHITE}  Followers: {CYAN}{data['user'].get('follower_count', 0)}{RESET}")
                        return True
                except:
                    pass
    except:
        pass
    
    # Method 2: Try to access the login ajax endpoint
    try:
        test_session = requests.Session()
        test_session.max_redirects = 3
        response = test_session.get(
            'https://www.instagram.com/api/v1/web/accounts/login/ajax/',
            cookies=coki,
            timeout=10,
            allow_redirects=False
        )
        
        if response.status_code == 200:
            print(f"{GREEN}✓ Cookies are valid!{RESET}")
            return True
        elif response.status_code in [302, 401]:
            print(f"{RED}✗ Cookies may be expired!{RESET}")
            return False
    except:
        pass
    
    print(f"{RED}✗ Cookies appear to be invalid!{RESET}")
    return False

def validate_cookie_format(cookie_str):
    """Validate if the cookie string has required fields"""
    required_fields = ['sessionid', 'ds_user_id']
    missing = []
    
    for field in required_fields:
        if field not in cookie_str:
            missing.append(field)
    
    if missing:
        print(f"{RED}✗ Cookie is missing: {', '.join(missing)}{RESET}")
        return False
    
    session_match = re.search(r'sessionid=([^;]+)', cookie_str)
    if session_match:
        session_value = session_match.group(1)
        if not session_value or len(session_value) < 5:
            print(f"{RED}✗ Session ID appears invalid (too short){RESET}")
            return False
    
    user_match = re.search(r'ds_user_id=([^;]+)', cookie_str)
    if user_match:
        user_id = user_match.group(1)
        if not user_id.isdigit():
            print(f"{RED}✗ User ID appears invalid (not a number){RESET}")
            return False
    
    print(f"{GREEN}✓ Cookie format looks valid{RESET}")
    return True

def get_user_id(username, cookies):
    """Get user ID with high-speed optimization"""
    
    # Try using the official API first (fastest)
    try:
        url = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={username}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15',
            'x-ig-app-id': '1217981644879628',
            'Accept': 'application/json'
        }
        response = requests.get(url, headers=headers, cookies=cookies, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'user' in data['data']:
                user_id = data['data']['user'].get('id')
                if user_id:
                    return user_id
    except:
        pass
    
    # Try scraping the profile page (fallback)
    try:
        session = requests.Session()
        session.max_redirects = 2
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15'
        }
        response = session.get(f'https://www.instagram.com/{username}/', headers=headers, cookies=cookies, timeout=5)
        
        if response.status_code == 200:
            patterns = [
                r'"user_id":"(\d+)"',
                r'"profilePage_(\d+)"',
                r'"id":"(\d+)","username":"' + username + '"',
                r'"userId":"(\d+)"',
            ]
            
            for pattern in patterns:
                match = re.search(pattern, response.text)
                if match:
                    return match.group(1)
    except:
        pass
    
    return None

def save_to_file(user_data):
    """Save user data to the dump file"""
    global dump_filename
    
    try:
        with lock:
            with open(dump_filename, "a", encoding='utf-8') as f:
                f.write(f"{user_data}\n")
    except Exception as e:
        print(f"\n{RED}Error saving to file: {e}{RESET}")

def fast_dump_followers(userid, cookies, after=''):
    """Fast dump followers with optimized requests"""
    global total_collected, stop_dump, current_username
    
    api = "https://www.instagram.com/graphql/query/"
    query_hash = "37479f2b8209594dde7facb0d904896a"
    
    variables = {
        "id": userid,
        "first": 100,
        "after": after
    }
    
    params = {
        'query_hash': query_hash,
        'variables': json.dumps(variables)
    }
    
    try:
        ptk = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15",
            "Accept": "application/json",
            "x-ig-app-id": "1217981644879628"
        }
        
        if isinstance(cookies, dict) and 'cookie' in cookies:
            cookies_dict = {'cookie': cookies['cookie']}
        elif isinstance(cookies, dict):
            cookies_dict = cookies
        else:
            cookies_dict = {'cookie': cookies}
        
        session = requests.Session()
        session.max_redirects = 3
        
        req = session.get(api, params=params, headers=ptk, cookies=cookies_dict, timeout=15)
        req.raise_for_status()
        req_json = req.json()
        
        if 'require_login' in req_json:
            print(f'\n{RED}[!] Invalid Cookie - Need to login{RESET}')
            stop_dump = True
            return
        
        if 'status' in req_json and req_json['status'] == 'fail':
            print(f'\n{RED}Request failed: {req_json.get("message", "Unknown error")}{RESET}')
            return
        
        if 'data' not in req_json or 'user' not in req_json['data']:
            print(f"\n{RED}User not found or private{RESET}")
            return
        
        user_data = req_json['data']['user']
        
        if 'edge_followed_by' not in user_data:
            print(f"\n{RED}This user has no visible followers or is private{RESET}")
            return
        
        edges = user_data['edge_followed_by'].get('edges', [])
        if not edges:
            print(f"\n{YELLOW}No followers found for this user{RESET}")
            return
        
        # Process edges quickly and save to file
        new_count = 0
        for xyz in edges:
            username = xyz['node'].get('username', '')
            full_name = xyz['node'].get('full_name', '')
            user_id = xyz['node'].get('id', '')
            
            if username:
                xy = f"{username}|{full_name}|{user_id}"
                with lock:
                    if xy not in Uuid:
                        Uuid.append(xy)
                        new_count += 1
                        total_collected += 1
                        # Save immediately to file
                        save_to_file(xy)
        
        if new_count > 0:
            print(f'\r{WHITE}Collected {GREEN}{new_count}{WHITE} new users | {CYAN}Total: {GREEN}{len(Uuid)}{WHITE}                      ', end='', flush=True)
        
        # Check for pagination
        page_info = user_data['edge_followed_by'].get('page_info', {})
        if page_info.get('has_next_page', False) and not stop_dump:
            after = page_info.get('end_cursor', '')
            if after:
                time.sleep(0.1)
                fast_dump_followers(userid, cookies, after)
                
    except requests.exceptions.Timeout:
        print(f"\n{RED}Timeout error - retrying...{RESET}")
        time.sleep(1)
        if not stop_dump:
            fast_dump_followers(userid, cookies, after)
    except Exception as e:
        print(f"\n{RED}Error: {e}{RESET}")

def fast_dump_following(userid, cookies, after=''):
    """Fast dump following with optimized requests"""
    global total_collected, stop_dump, current_username
    
    api = "https://www.instagram.com/graphql/query/"
    query_hash = "58712303d941c6855d4e888c5f0cd22f"
    
    variables = {
        "id": userid,
        "first": 100,
        "after": after
    }
    
    params = {
        'query_hash': query_hash,
        'variables': json.dumps(variables)
    }
    
    try:
        ptk = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15",
            "Accept": "application/json",
            "x-ig-app-id": "1217981644879628"
        }
        
        if isinstance(cookies, dict) and 'cookie' in cookies:
            cookies_dict = {'cookie': cookies['cookie']}
        elif isinstance(cookies, dict):
            cookies_dict = cookies
        else:
            cookies_dict = {'cookie': cookies}
        
        session = requests.Session()
        session.max_redirects = 3
        
        req = session.get(api, params=params, headers=ptk, cookies=cookies_dict, timeout=15)
        req.raise_for_status()
        req_json = req.json()
        
        if 'require_login' in req_json:
            print(f'\n{RED}[!] Invalid Cookie - Need to login{RESET}')
            stop_dump = True
            return
        
        if 'status' in req_json and req_json['status'] == 'fail':
            print(f'\n{RED}Request failed: {req_json.get("message", "Unknown error")}{RESET}')
            return
        
        if 'data' not in req_json or 'user' not in req_json['data']:
            print(f"\n{RED}User not found or private{RESET}")
            return
        
        user_data = req_json['data']['user']
        
        if 'edge_follow' not in user_data:
            print(f"\n{RED}This user has no visible following or is private{RESET}")
            return
        
        edges = user_data['edge_follow'].get('edges', [])
        if not edges:
            print(f"\n{YELLOW}No following found for this user{RESET}")
            return
        
        # Process edges quickly and save to file
        new_count = 0
        for xyz in edges:
            username = xyz['node'].get('username', '')
            full_name = xyz['node'].get('full_name', '')
            user_id = xyz['node'].get('id', '')
            
            if username:
                xy = f"{username}|{full_name}|{user_id}"
                with lock:
                    if xy not in Uuid:
                        Uuid.append(xy)
                        new_count += 1
                        total_collected += 1
                        # Save immediately to file
                        save_to_file(xy)
        
        if new_count > 0:
            print(f'\r{WHITE}Collected {GREEN}{new_count}{WHITE} new users | {CYAN}Total: {GREEN}{len(Uuid)}{WHITE}                      ', end='', flush=True)
        
        # Check for pagination
        page_info = user_data['edge_follow'].get('page_info', {})
        if page_info.get('has_next_page', False) and not stop_dump:
            after = page_info.get('end_cursor', '')
            if after:
                time.sleep(0.1)
                fast_dump_following(userid, cookies, after)
                
    except requests.exceptions.Timeout:
        print(f"\n{RED}Timeout error - retrying...{RESET}")
        time.sleep(1)
        if not stop_dump:
            fast_dump_following(userid, cookies, after)
    except Exception as e:
        print(f"\n{RED}Error: {e}{RESET}")

def unlimited_dump():
    """Unlimited dump for 1 username with high speed - Single file"""
    global total_collected, Uuid, xx, stop_dump, current_username, dump_filename
    
    clear()
    
    print(f"{CYAN}{'='*56}{RESET}")
    print(f"{CYAN}     🚀 INSTAGRAM UNLIMITED DUMPER 🚀{RESET}")
    print(f"{CYAN}{'='*56}{RESET}")
    print(f" {WHITE}[{GREEN}•{WHITE}] Unlimited dumping for 1 username{RESET}")
    print(f" {WHITE}[{GREEN}•{WHITE}] High-speed optimization enabled{RESET}")
    print(f" {WHITE}[{GREEN}•{WHITE}] All data saved to ONE file{RESET}")
    linex()
    
    # Get cookie
    print(f"{YELLOW}Enter your Instagram cookie (should contain sessionid){RESET}")
    cookie_input = input(f"{WHITE}[{GREEN}?{WHITE}] Cookie: {GREEN}").strip()
    
    if not cookie_input:
        print(f"{RED}No cookie entered!{RESET}")
        return
    
    if not validate_cookie_format(cookie_input):
        print(f"{RED}Invalid cookie format!{RESET}")
        return
    
    cookies = {'cookie': cookie_input}
    
    if not test_cookies(cookies):
        print(f"{RED}Cookie validation failed!{RESET}")
        return
    
    # Get username
    print(f"\n{YELLOW}Enter the Instagram username to dump{RESET}")
    username = input(f"{WHITE}[{GREEN}?{WHITE}] Username: {GREEN}").strip()
    
    if not username:
        print(f"{RED}No username entered!{RESET}")
        return
    
    current_username = username
    
    # Get user ID
    print(f"\n{YELLOW}Fetching user ID for {CYAN}{username}{RESET}")
    user_id = get_user_id(username, cookies)
    
    if not user_id:
        print(f"{RED}Could not find user ID for: {username}{RESET}")
        return
    
    print(f"{GREEN}✓ User ID found: {CYAN}{user_id}{RESET}")
    
    # Choose dump mode
    print(f"\n{WHITE}[{GREEN}1{WHITE}] Dump Followers Only{RESET}")
    print(f"{WHITE}[{GREEN}2{WHITE}] Dump Following Only{RESET}")
    print(f"{WHITE}[{GREEN}3{WHITE}] Dump Both (Unlimited){RESET}")
    choice = input(f"{WHITE}[{GREEN}?{WHITE}] Select: {GREEN}").strip()
    
    # Reset global variables
    Uuid = []
    total_collected = 0
    xx = 0
    stop_dump = False
    
    # Create single dump file
    timestamp = int(time.time())
    dump_filename = f"{username}_dump_{timestamp}.txt"
    
    # Clear file if it exists
    with open(dump_filename, "w", encoding='utf-8') as f:
        f.write(f"# Instagram Dump for: {username}\n")
        f.write(f"# Dump Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"# Format: username|full_name|user_id\n")
        f.write(f"{'='*56}\n\n")
    
    print(f"\n{GREEN}✓ Results will be saved to: {CYAN}{dump_filename}{RESET}")
    
    # Start dumping
    clear()
    print(f"{CYAN}{'='*56}{RESET}")
    print(f"{CYAN}     🔥 UNLIMITED DUMP IN PROGRESS 🔥{RESET}")
    print(f"{CYAN}{'='*56}{RESET}")
    print(f"{WHITE}Target: {CYAN}{username}{WHITE} (ID: {CYAN}{user_id}{WHITE}){RESET}")
    print(f"{WHITE}Mode: {CYAN}{'Followers' if choice == '1' else 'Following' if choice == '2' else 'Both'}{RESET}")
    print(f"{WHITE}File: {CYAN}{dump_filename}{RESET}")
    print(f"{WHITE}Press {RED}Ctrl+C{RESET} to stop at any time")
    print(f"{CYAN}{'='*56}{RESET}")
    
    start_time = time.time()
    
    try:
        if choice == '1':
            print(f"\n{GREEN}Dumping Followers...{RESET}\n")
            fast_dump_followers(user_id, cookies)
        elif choice == '2':
            print(f"\n{GREEN}Dumping Following...{RESET}\n")
            fast_dump_following(user_id, cookies)
        elif choice == '3':
            print(f"\n{GREEN}Dumping Followers...{RESET}\n")
            fast_dump_followers(user_id, cookies)
            print(f"\n\n{GREEN}Dumping Following...{RESET}\n")
            fast_dump_following(user_id, cookies)
        else:
            print(f"{RED}Invalid choice!{RESET}")
            return
    
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}[!] Dump stopped by user{RESET}")
    
    # Calculate results
    end_time = time.time()
    execution_time = end_time - start_time
    
    # Display results
    linex()
    print(f"{GREEN}{'='*56}{RESET}")
    print(f" {GREEN}[✓] DUMP COMPLETED!{RESET}")
    print(f"{GREEN}{'='*56}{RESET}")
    print(f" {WHITE}[📊] Total Users Collected: {GREEN}{len(Uuid)}{RESET}")
    print(f" {WHITE}[📁] File: {CYAN}{dump_filename}{RESET}")
    print(f" {WHITE}[⏱️] Execution Time: {YELLOW}{execution_time:.2f} seconds{RESET}")
    print(f" {WHITE}[🚀] Speed: {CYAN}{len(Uuid)/execution_time:.2f} users/second{RESET}")
    
    if len(Uuid) > 0:
        print(f"\n{WHITE}Sample of collected users:{RESET}")
        for i, user in enumerate(Uuid[:5]):
            parts = user.split('|')
            print(f"  {GREEN}{i+1}. {CYAN}{parts[0]}{RESET}")
        if len(Uuid) > 5:
            print(f"  {YELLOW}... and {len(Uuid)-5} more{RESET}")
        
        # Show file size
        try:
            file_size = os.path.getsize(dump_filename)
            if file_size < 1024:
                size_str = f"{file_size} bytes"
            elif file_size < 1024 * 1024:
                size_str = f"{file_size/1024:.2f} KB"
            else:
                size_str = f"{file_size/(1024*1024):.2f} MB"
            print(f" {WHITE}[📦] File Size: {CYAN}{size_str}{RESET}")
        except:
            pass
    
    linex()
    input(f"\n{WHITE}[{RED}!{WHITE}] Press Enter to return to menu...{RESET}")

def menu():
    """Interactive main menu"""
    global dump_filename
    
    while True:
        clear()
        print(f"{CYAN}{'='*56}{RESET}")
        print(f"{CYAN}     🚀 INSTAGRAM UNLIMITED DUMPER 🚀{RESET}")
        print(f"{CYAN}{'='*56}{RESET}")
        print(f" {WHITE}[{GREEN}1{WHITE}] 🚀 Start Unlimited Dump{RESET}")
        print(f" {WHITE}[{GREEN}2{WHITE}] 📊 View Statistics{RESET}")
        print(f" {WHITE}[{GREEN}3{WHITE}] 📁 Open Dump File{RESET}")
        print(f" {WHITE}[{GREEN}4{WHITE}] ❌ Exit Program{RESET}")
        print(f"{CYAN}{'='*60}{RESET}")
        
        choice = input(f" {WHITE}[{GREEN}?{WHITE}] Select Option: {GREEN}{RESET}").strip()
        
        if choice == '1':
            unlimited_dump()
        elif choice == '2':
            clear()
            print(f"{CYAN}{'='*56}{RESET}")
            print(f"{CYAN}     📊 DUMP STATISTICS 📊{RESET}")
            print(f"{CYAN}{'='*56}{RESET}")
            print(f" {WHITE}[📝] Total Users Collected: {GREEN}{len(Uuid)}{RESET}")
            print(f" {WHITE}[📁] Last Dump File: {CYAN}{dump_filename if dump_filename else 'N/A'}{RESET}")
            print(f" {WHITE}[🔄] Last Dump Time: {YELLOW}{time.strftime('%Y-%m-%d %H:%M:%S')}{RESET}")
            linex()
            input(f" {WHITE}[{RED}!{WHITE}] Press Enter to continue...{RESET}")
        elif choice == '3':
            if dump_filename and os.path.exists(dump_filename):
                try:
                    if os.name == 'nt':  # Windows
                        os.startfile(dump_filename)
                    else:  # Linux/Mac
                        os.system(f'xdg-open "{dump_filename}"' if os.name == 'posix' else f'open "{dump_filename}"')
                    print(f"{GREEN}✓ Opening file: {dump_filename}{RESET}")
                except:
                    print(f"{RED}Could not open file. Please open manually: {dump_filename}{RESET}")
                time.sleep(2)
            else:
                print(f"{RED}No dump file found! Please run a dump first.{RESET}")
                time.sleep(2)
        elif choice == '4':
            clear()
            print(f"{GREEN}{'='*56}{RESET}")
            print(f" {GREEN}     👋 GOODBYE! THANKS FOR USING OUR TOOL! 👋{RESET}")
            print(f"{GREEN}{'='*56}{RESET}")
            if len(Uuid) > 0:
                print(f" {YELLOW}[!] Total users dumped: {len(Uuid)}{RESET}")
                print(f" {YELLOW}[!] Saved in: {dump_filename}{RESET}")
            time.sleep(3)
            break
        else:
            print(f" {RED}[!] Invalid option! Please choose 1, 2, 3, or 4.{RESET}")
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
