#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instagram User ID Fetcher & Follower/Following Dumper
Unlimited dump with high-speed optimization - Fixed dumping
"""

import requests
import json
import re
import time
import os
import sys
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
total_collected = 0
lock = threading.Lock()
stop_dump = False
current_username = ""
dump_filename = ""

# User agent for API requests
ua = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
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
    """Test if cookies are still valid"""
    try:
        if isinstance(coki, str):
            coki = {'cookie': coki}
        
        # Try to get user info
        cookie_str = coki.get('cookie', '') if isinstance(coki, dict) else str(coki)
        uid_match = re.search(r'ds_user_id=(\d+)', cookie_str)
        
        if uid_match:
            uid = uid_match.group(1)
            response = requests.get(
                f'https://i.instagram.com/api/v1/users/{uid}/info/',
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'},
                cookies=coki,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                if 'user' in data and data['user'].get('username'):
                    print(f"{GREEN}✓ Cookies are valid!{RESET}")
                    print(f"{WHITE}  Username: {CYAN}{data['user'].get('username')}{RESET}")
                    print(f"{WHITE}  Full Name: {CYAN}{data['user'].get('full_name', 'N/A')}{RESET}")
                    return True
        return False
    except:
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
    
    print(f"{GREEN}✓ Cookie format looks valid{RESET}")
    return True

def get_user_id(username, cookies):
    """Get user ID from username"""
    try:
        # Method 1: Official API
        url = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={username}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'x-ig-app-id': '936619743392459',
            'Accept': 'application/json'
        }
        
        if isinstance(cookies, dict) and 'cookie' in cookies:
            cookie_str = cookies['cookie']
            cookies_dict = {}
            for item in cookie_str.split(';'):
                if '=' in item:
                    key, value = item.strip().split('=', 1)
                    cookies_dict[key] = value
        else:
            cookies_dict = cookies
            
        response = requests.get(url, headers=headers, cookies=cookies_dict, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'user' in data['data']:
                user_id = data['data']['user'].get('id')
                if user_id:
                    return user_id
    except Exception as e:
        print(f"{YELLOW}Method 1 failed: {e}{RESET}")
    
    # Method 2: GraphQL
    try:
        url = 'https://www.instagram.com/graphql/query/'
        params = {
            'query_hash': 'c9100bf9110dd6361671f113dd02e7d6',
            'variables': json.dumps({'username': username})
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'x-ig-app-id': '936619743392459',
        }
        
        if isinstance(cookies, dict) and 'cookie' in cookies:
            cookie_str = cookies['cookie']
            cookies_dict = {}
            for item in cookie_str.split(';'):
                if '=' in item:
                    key, value = item.strip().split('=', 1)
                    cookies_dict[key] = value
        else:
            cookies_dict = cookies
            
        response = requests.get(url, params=params, headers=headers, cookies=cookies_dict, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'user' in data['data']:
                user_id = data['data']['user'].get('id')
                if user_id:
                    return user_id
    except Exception as e:
        print(f"{YELLOW}Method 2 failed: {e}{RESET}")
    
    return None

def parse_cookies(cookies):
    """Parse cookies from string or dict to dict"""
    if isinstance(cookies, dict) and 'cookie' in cookies:
        cookie_str = cookies['cookie']
        cookies_dict = {}
        for item in cookie_str.split(';'):
            if '=' in item:
                key, value = item.strip().split('=', 1)
                cookies_dict[key] = value
        return cookies_dict
    elif isinstance(cookies, dict):
        return cookies
    else:
        return {'cookie': cookies}

def save_to_file(user_data):
    """Save user data to the dump file"""
    global dump_filename
    
    try:
        with lock:
            with open(dump_filename, "a", encoding='utf-8') as f:
                f.write(f"{user_data}\n")
    except Exception as e:
        pass

def dump_followers(userid, cookies, after=''):
    """Dump followers with proper authentication"""
    global total_collected, stop_dump
    
    api = "https://www.instagram.com/graphql/query/"
    query_hash = "37479f2b8209594dde7facb0d904896a"
    
    variables = {
        "id": userid,
        "first": 50,
        "after": after
    }
    
    params = {
        'query_hash': query_hash,
        'variables': json.dumps(variables)
    }
    
    try:
        # Parse cookies properly
        cookies_dict = parse_cookies(cookies)
        
        # Add required headers
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/json",
            "x-ig-app-id": "936619743392459",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Host": "www.instagram.com",
            "Origin": "https://www.instagram.com",
            "Referer": "https://www.instagram.com/"
        }
        
        session = requests.Session()
        session.max_redirects = 3
        
        print(f"{YELLOW}Requesting followers...{RESET}")
        req = session.get(api, params=params, headers=headers, cookies=cookies_dict, timeout=30)
        
        print(f"{WHITE}Response Status: {req.status_code}{RESET}")
        
        if req.status_code != 200:
            print(f"{RED}Error: Status code {req.status_code}{RESET}")
            return
        
        req_json = req.json()
        
        # Check for errors
        if 'require_login' in str(req_json) or 'login' in str(req_json).lower():
            print(f'{RED}[!] Authentication required - Cookie may be invalid{RESET}')
            stop_dump = True
            return
        
        if 'data' not in req_json:
            print(f'{RED}[!] No data in response{RESET}')
            print(f'{YELLOW}Response: {json.dumps(req_json, indent=2)[:500]}{RESET}')
            return
        
        if 'user' not in req_json['data'] or not req_json['data']['user']:
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
        
        # Process edges
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
                        save_to_file(xy)
        
        if new_count > 0:
            print(f'\r{WHITE}Collected {GREEN}{new_count}{WHITE} new users | {CYAN}Total: {GREEN}{len(Uuid)}{WHITE}                      ', end='', flush=True)
        
        # Check for pagination
        page_info = user_data['edge_followed_by'].get('page_info', {})
        if page_info.get('has_next_page', False) and not stop_dump:
            after = page_info.get('end_cursor', '')
            if after:
                print(f"\n{YELLOW}Loading next page...{RESET}")
                time.sleep(1)
                dump_followers(userid, cookies, after)
                
    except requests.exceptions.Timeout:
        print(f"\n{RED}Timeout error - retrying...{RESET}")
        time.sleep(2)
        if not stop_dump:
            dump_followers(userid, cookies, after)
    except json.JSONDecodeError as e:
        print(f"\n{RED}JSON Decode Error: {e}{RESET}")
        print(f"{YELLOW}Response text: {req.text[:200]}{RESET}")
    except Exception as e:
        print(f"\n{RED}Error: {e}{RESET}")

def dump_following(userid, cookies, after=''):
    """Dump following with proper authentication"""
    global total_collected, stop_dump
    
    api = "https://www.instagram.com/graphql/query/"
    query_hash = "58712303d941c6855d4e888c5f0cd22f"
    
    variables = {
        "id": userid,
        "first": 50,
        "after": after
    }
    
    params = {
        'query_hash': query_hash,
        'variables': json.dumps(variables)
    }
    
    try:
        # Parse cookies properly
        cookies_dict = parse_cookies(cookies)
        
        # Add required headers
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/json",
            "x-ig-app-id": "936619743392459",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Host": "www.instagram.com",
            "Origin": "https://www.instagram.com",
            "Referer": "https://www.instagram.com/"
        }
        
        session = requests.Session()
        session.max_redirects = 3
        
        print(f"{YELLOW}Requesting following...{RESET}")
        req = session.get(api, params=params, headers=headers, cookies=cookies_dict, timeout=30)
        
        print(f"{WHITE}Response Status: {req.status_code}{RESET}")
        
        if req.status_code != 200:
            print(f"{RED}Error: Status code {req.status_code}{RESET}")
            return
        
        req_json = req.json()
        
        # Check for errors
        if 'require_login' in str(req_json) or 'login' in str(req_json).lower():
            print(f'{RED}[!] Authentication required - Cookie may be invalid{RESET}')
            stop_dump = True
            return
        
        if 'data' not in req_json:
            print(f'{RED}[!] No data in response{RESET}')
            print(f'{YELLOW}Response: {json.dumps(req_json, indent=2)[:500]}{RESET}')
            return
        
        if 'user' not in req_json['data'] or not req_json['data']['user']:
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
        
        # Process edges
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
                        save_to_file(xy)
        
        if new_count > 0:
            print(f'\r{WHITE}Collected {GREEN}{new_count}{WHITE} new users | {CYAN}Total: {GREEN}{len(Uuid)}{WHITE}                      ', end='', flush=True)
        
        # Check for pagination
        page_info = user_data['edge_follow'].get('page_info', {})
        if page_info.get('has_next_page', False) and not stop_dump:
            after = page_info.get('end_cursor', '')
            if after:
                print(f"\n{YELLOW}Loading next page...{RESET}")
                time.sleep(1)
                dump_following(userid, cookies, after)
                
    except requests.exceptions.Timeout:
        print(f"\n{RED}Timeout error - retrying...{RESET}")
        time.sleep(2)
        if not stop_dump:
            dump_following(userid, cookies, after)
    except json.JSONDecodeError as e:
        print(f"\n{RED}JSON Decode Error: {e}{RESET}")
        print(f"{YELLOW}Response text: {req.text[:200]}{RESET}")
    except Exception as e:
        print(f"\n{RED}Error: {e}{RESET}")

def unlimited_dump():
    """Unlimited dump for 1 username with high speed"""
    global total_collected, Uuid, stop_dump, current_username, dump_filename
    
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
    print(f"{WHITE}Example: sessionid=abc123; ds_user_id=123456; csrftoken=xyz789{RESET}")
    cookie_input = input(f"{WHITE}[{GREEN}?{WHITE}] Cookie: {GREEN}").strip()
    
    if not cookie_input:
        print(f"{RED}No cookie entered!{RESET}")
        return
    
    if not validate_cookie_format(cookie_input):
        print(f"{RED}Invalid cookie format!{RESET}")
        return
    
    cookies = {'cookie': cookie_input}
    
    if not test_cookies(cookies):
        print(f"{RED}Cookie validation failed! Do you want to continue anyway?{RESET}")
        cont = input(f"{WHITE}[{GREEN}?{WHITE}] Continue? (y/n): {GREEN}").strip().lower()
        if cont != 'y':
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
        print(f"{YELLOW}Make sure the username exists and is correct{RESET}")
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
    stop_dump = False
    
    # Create single dump file
    timestamp = int(time.time())
    dump_filename = f"{username}_dump_{timestamp}.txt"
    
    # Clear file and write header
    with open(dump_filename, "w", encoding='utf-8') as f:
        f.write(f"# Instagram Dump for: {username}\n")
        f.write(f"# User ID: {user_id}\n")
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
            print(f"\n{GREEN}Starting Followers Dump...{RESET}\n")
            dump_followers(user_id, cookies)
        elif choice == '2':
            print(f"\n{GREEN}Starting Following Dump...{RESET}\n")
            dump_following(user_id, cookies)
        elif choice == '3':
            print(f"\n{GREEN}Starting Followers Dump...{RESET}\n")
            dump_followers(user_id, cookies)
            print(f"\n\n{GREEN}Starting Following Dump...{RESET}\n")
            dump_following(user_id, cookies)
        else:
            print(f"{RED}Invalid choice!{RESET}")
            return
    
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}[!] Dump stopped by user{RESET}")
    except Exception as e:
        print(f"\n{RED}[!] Error during dump: {e}{RESET}")
    
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
    if execution_time > 0 and len(Uuid) > 0:
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
            if dump_filename and os.path.exists(dump_filename):
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
