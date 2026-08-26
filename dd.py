#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Instagram Data Dumper - Collects followers/following data
Version: 2.1
Author: Sumon
"""

import os
import sys
import json
import time
import re
import uuid
import base64
import hashlib
import random
import threading
import datetime
from datetime import datetime
from urllib.parse import quote
from concurrent.futures import ThreadPoolExecutor

import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import print as rich_print
from rich.table import Table
from rich.text import Text

# Initialize console
console = Console()

# Global variables
Uuid = []  # Store collected users as "username|full_name"
Uid_cache = {}  # Cache for user IDs
Ok = Cp = Loop = 0
xx = 0
SistemLog = "api.instagram.com"

# Color codes
WHITE = '\x1b[1;97m'
RED = '\x1b[1;91m'
GREEN = '\x1b[1;92m'
YELLOW = '\x1b[1;93m'
BLUE = '\x1b[1;94m'
PURPLE = '\x1b[1;95m'
CYAN = '\x1b[1;96m'
ORANGE = '\033[38;2;255;127;0;1m'
RESET = '\x1b[0m'
campur = random.choice([WHITE, GREEN, YELLOW, BLUE, PURPLE, CYAN, ORANGE, RESET])

# Headers
HEADERS = {
    'Host': 'www.instagram.com',
    'x-ig-app-id': '1217981644879628',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 instagram 360.0.0.33.104 (iPhone16,2; iOS 18_2; en_US; en; scale=3.00; 1170x2532; 510000000)',
    'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest',
    'accept-language': 'en-US,en;q=0.9'
}

# Create necessary directories
def ensure_directories():
    """Create required directories if they don't exist"""
    dirs = ['data', 'output']
    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d)

def clear_screen():
    """Clear terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')

# ============ COOKIE MANAGEMENT ============
def validate_cookie(cookie_str):
    """Validate cookie format and extract components"""
    if not cookie_str or len(cookie_str) < 10:
        return False, "Cookie too short"
    
    # Check for required fields
    required = ['sessionid', 'ds_user_id']
    missing = [f for f in required if f not in cookie_str]
    
    if missing:
        return False, f"Missing: {', '.join(missing)}"
    
    # Extract sessionid
    session_match = re.search(r'sessionid=([^;]+)', cookie_str)
    if not session_match or len(session_match.group(1)) < 5:
        return False, "Invalid sessionid"
    
    # Extract user ID
    user_match = re.search(r'ds_user_id=([^;]+)', cookie_str)
    if not user_match or not user_match.group(1).isdigit():
        return False, "Invalid ds_user_id"
    
    return True, "Cookie format valid"

def load_cookie():
    """Load cookie from file or prompt user"""
    cookie_file = 'data/cookie.txt'
    
    if os.path.exists(cookie_file):
        try:
            with open(cookie_file, 'r') as f:
                cookie_str = f.read().strip()
            
            if cookie_str:
                valid, msg = validate_cookie(cookie_str)
                if valid:
                    return {'cookie': cookie_str}
                else:
                    print(f"{YELLOW}⚠ Invalid cookie in file: {msg}{RESET}")
                    print(f"{YELLOW}  Please re-enter your cookie{RESET}")
                    os.remove(cookie_file)
        except Exception as e:
            print(f"{RED}Error reading cookie file: {e}{RESET}")
    
    # Prompt for new cookie
    print(f"\n{BLUE}╔════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{BLUE}║{RESET}  {CYAN}Please enter your Instagram session cookie{RESET}")
    print(f"{BLUE}║{RESET}  {YELLOW}⚠ Use a throwaway account to avoid ban{RESET}")
    print(f"{BLUE}║{RESET}  {WHITE}Cookie format: sessionid=xxx; ds_user_id=xxx; ...{RESET}")
    print(f"{BLUE}╚════════════════════════════════════════════════════════════════╝{RESET}")
    
    cookie_input = input(f"\n{RED}[{WHITE}▶{RED}] {BLUE}Cookie :{YELLOW} ").strip()
    
    if not cookie_input:
        print(f"{RED}✗ No cookie entered!{RESET}")
        return load_cookie()
    
    valid, msg = validate_cookie(cookie_input)
    if not valid:
        print(f"{RED}✗ Invalid cookie: {msg}{RESET}")
        time.sleep(1)
        return load_cookie()
    
    # Save cookie
    try:
        with open(cookie_file, 'w') as f:
            f.write(cookie_input)
        print(f"{GREEN}✓ Cookie saved successfully{RESET}")
    except Exception as e:
        print(f"{RED}✗ Failed to save cookie: {e}{RESET}")
    
    return {'cookie': cookie_input}

def test_cookie(cookie_dict):
    """Test if cookie is still valid"""
    try:
        cookie_str = cookie_dict.get('cookie', '')
        
        # Try to get user info
        user_match = re.search(r'ds_user_id=([^;]+)', cookie_str)
        if not user_match:
            return False, "No user ID in cookie"
        
        user_id = user_match.group(1)
        url = f'https://i.instagram.com/api/v1/users/{user_id}/info/'
        
        response = requests.get(
            url,
            headers=HEADERS,
            cookies=cookie_dict,
            timeout=15
        )
        
        if response.status_code == 200:
            data = response.json()
            if 'user' in data:
                user = data['user']
                username = user.get('username', 'Unknown')
                full_name = user.get('full_name', 'Unknown')
                followers = user.get('follower_count', 0)
                return True, f"Logged in as: @{username} ({full_name}) - {followers} followers"
        
        # Try alternative check
        response = requests.get(
            'https://www.instagram.com/api/v1/web/accounts/login/ajax/',
            headers=HEADERS,
            cookies=cookie_dict,
            timeout=10,
            allow_redirects=False
        )
        
        if response.status_code == 200:
            return True, "Cookie appears valid"
        elif response.status_code in [302, 401]:
            return False, "Cookie expired or invalid"
        
        return False, "Cookie validation failed"
        
    except requests.exceptions.RequestException as e:
        return False, f"Network error: {e}"
    except Exception as e:
        return False, f"Error: {e}"

# ============ USER ID RETRIEVAL ============
def get_user_id(username, cookie_dict, retries=3):
    """Get user ID from username with multiple methods"""
    if username in Uid_cache:
        return Uid_cache[username]
    
    for attempt in range(retries):
        try:
            # Method 1: Official API
            url = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={username}'
            response = requests.get(
                url,
                headers=HEADERS,
                cookies=cookie_dict,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                if 'data' in data and 'user' in data['data']:
                    user_id = data['data']['user'].get('id')
                    if user_id:
                        Uid_cache[username] = user_id
                        return user_id
            
            # Method 2: GraphQL
            url = 'https://www.instagram.com/graphql/query/'
            params = {
                'query_hash': 'c9100bf9110dd6361671f113dd02e7d6',
                'variables': json.dumps({'username': username})
            }
            response = requests.get(
                url,
                params=params,
                headers=HEADERS,
                cookies=cookie_dict,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                if 'data' in data and 'user' in data['data']:
                    user_id = data['data']['user'].get('id')
                    if user_id:
                        Uid_cache[username] = user_id
                        return user_id
            
            # Method 3: Profile page
            session = requests.Session()
            session.max_redirects = 3
            response = session.get(
                f'https://www.instagram.com/{username}/',
                cookies=cookie_dict,
                timeout=10
            )
            
            if response.status_code == 200:
                # Search for user ID in various patterns
                patterns = [
                    r'"user_id":"(\d+)"',
                    r'"profilePage_(\d+)"',
                    r'"id":"(\d+)","username":"' + username + '"'
                ]
                for pattern in patterns:
                    match = re.search(pattern, response.text)
                    if match:
                        user_id = match.group(1)
                        Uid_cache[username] = user_id
                        return user_id
            
            # Wait before retry
            time.sleep(0.5 * (attempt + 1))
            
        except Exception as e:
            if attempt == retries - 1:
                print(f"{RED}✗ Failed to get user ID for {username}: {e}{RESET}")
            time.sleep(0.5)
    
    return None

# ============ DATA COLLECTION ============
def collect_followers(user_id, cookie_str, after=''):
    """Collect followers using GraphQL"""
    global Uuid, xx
    
    url = "https://www.instagram.com/graphql/query/"
    query_hash = "37479f2b8209594dde7facb0d904896a"
    
    variables = {
        "id": user_id,
        "first": 50,
        "after": after
    }
    
    headers = {
        'User-Agent': HEADERS['user-agent'],
        'x-ig-app-id': HEADERS['x-ig-app-id'],
        'Cookie': cookie_str,
        'Accept': 'application/json'
    }
    
    try:
        response = requests.get(
            url,
            params={'query_hash': query_hash, 'variables': json.dumps(variables)},
            headers=headers,
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        
        # Check for errors
        if 'status' in data and data['status'] == 'fail':
            print(f"\n{RED}✗ Request failed: {data.get('message', 'Unknown error')}{RESET}")
            return False
        
        if 'data' not in data or 'user' not in data['data']:
            print(f"\n{RED}✗ User not found or private{RESET}")
            return False
        
        user_data = data['data']['user']
        if 'edge_followed_by' not in user_data:
            print(f"\n{YELLOW}⚠ No followers found or user is private{RESET}")
            return False
        
        # Process edges
        edges = user_data['edge_followed_by'].get('edges', [])
        if not edges:
            print(f"\n{YELLOW}⚠ No followers in this batch{RESET}")
        
        for edge in edges:
            node = edge.get('node', {})
            username = node.get('username', '')
            full_name = node.get('full_name', '')
            
            if username:
                entry = f"{username}|{full_name}"
                if entry not in Uuid:
                    Uuid.append(entry)
                    xx += 1
                    if xx % 10 == 0:
                        print(f'\r{WHITE}📊 Collected: {GREEN}{len(Uuid)}{WHITE} users so far...{RESET}', end='', flush=True)
        
        # Pagination
        page_info = user_data['edge_followed_by'].get('page_info', {})
        if page_info.get('has_next_page', False):
            next_cursor = page_info.get('end_cursor', '')
            if next_cursor:
                print(f"\n{YELLOW}↻ Loading next page...{RESET}")
                time.sleep(0.5)
                return collect_followers(user_id, cookie_str, next_cursor)
        
        return True
        
    except requests.exceptions.Timeout:
        print(f"\n{RED}✗ Timeout error{RESET}")
        return False
    except requests.exceptions.RequestException as e:
        print(f"\n{RED}✗ Network error: {e}{RESET}")
        return False
    except json.JSONDecodeError:
        print(f"\n{RED}✗ Invalid response{RESET}")
        return False
    except Exception as e:
        print(f"\n{RED}✗ Error: {e}{RESET}")
        return False

def collect_following(user_id, cookie_str, after=''):
    """Collect following using GraphQL"""
    global Uuid, xx
    
    url = "https://www.instagram.com/graphql/query/"
    query_hash = "58712303d941c6855d4e888c5f0cd22f"
    
    variables = {
        "id": user_id,
        "first": 50,
        "after": after
    }
    
    headers = {
        'User-Agent': HEADERS['user-agent'],
        'x-ig-app-id': HEADERS['x-ig-app-id'],
        'Cookie': cookie_str,
        'Accept': 'application/json'
    }
    
    try:
        response = requests.get(
            url,
            params={'query_hash': query_hash, 'variables': json.dumps(variables)},
            headers=headers,
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        
        # Check for errors
        if 'status' in data and data['status'] == 'fail':
            print(f"\n{RED}✗ Request failed: {data.get('message', 'Unknown error')}{RESET}")
            return False
        
        if 'data' not in data or 'user' not in data['data']:
            print(f"\n{RED}✗ User not found or private{RESET}")
            return False
        
        user_data = data['data']['user']
        if 'edge_follow' not in user_data:
            print(f"\n{YELLOW}⚠ No following found or user is private{RESET}")
            return False
        
        # Process edges
        edges = user_data['edge_follow'].get('edges', [])
        if not edges:
            print(f"\n{YELLOW}⚠ No following in this batch{RESET}")
        
        for edge in edges:
            node = edge.get('node', {})
            username = node.get('username', '')
            full_name = node.get('full_name', '')
            
            if username:
                entry = f"{username}|{full_name}"
                if entry not in Uuid:
                    Uuid.append(entry)
                    xx += 1
                    if xx % 10 == 0:
                        print(f'\r{WHITE}📊 Collected: {GREEN}{len(Uuid)}{WHITE} users so far...{RESET}', end='', flush=True)
        
        # Pagination
        page_info = user_data['edge_follow'].get('page_info', {})
        if page_info.get('has_next_page', False):
            next_cursor = page_info.get('end_cursor', '')
            if next_cursor:
                print(f"\n{YELLOW}↻ Loading next page...{RESET}")
                time.sleep(0.5)
                return collect_following(user_id, cookie_str, next_cursor)
        
        return True
        
    except requests.exceptions.Timeout:
        print(f"\n{RED}✗ Timeout error{RESET}")
        return False
    except requests.exceptions.RequestException as e:
        print(f"\n{RED}✗ Network error: {e}{RESET}")
        return False
    except json.JSONDecodeError:
        print(f"\n{RED}✗ Invalid response{RESET}")
        return False
    except Exception as e:
        print(f"\n{RED}✗ Error: {e}{RESET}")
        return False

# ============ SAVE FUNCTIONS ============
def save_data_sdcard():
    """Save data to /sdcard/dump.txt (Android/Termux)"""
    if not Uuid:
        print(f"{RED}✗ No data to save!{RESET}")
        return False
    
    try:
        # Check storage permission
        if not os.access('/sdcard', os.W_OK):
            print(f"{YELLOW}⚠ Storage not writable. Use custom save instead.{RESET}")
            return False
        
        output_file = '/sdcard/dump.txt'
        with open(output_file, 'w', encoding='utf-8') as f:
            for item in Uuid:
                f.write(item + '\n')
        
        print(f"\n{GREEN}✓ Saved {len(Uuid)} users to: {output_file}{RESET}")
        print(f"{WHITE}  Format: username|full_name{RESET}")
        
        # Show sample
        print(f"\n{YELLOW}Sample data:{RESET}")
        for i, item in enumerate(Uuid[:5], 1):
            parts = item.split('|')
            print(f"  {i}. {GREEN}{parts[0]}{RESET} | {CYAN}{parts[1] if len(parts) > 1 else 'N/A'}{RESET}")
        if len(Uuid) > 5:
            print(f"  ... and {len(Uuid)-5} more")
        
        return True
        
    except PermissionError:
        print(f"{RED}✗ Permission denied! In Termux, run: termux-setup-storage{RESET}")
        return False
    except Exception as e:
        print(f"{RED}✗ Failed to save: {e}{RESET}")
        return False

def save_data_custom(filename):
    """Save data to custom file"""
    if not Uuid:
        print(f"{RED}✗ No data to save!{RESET}")
        return False
    
    # Ensure .txt extension
    if not filename.endswith('.txt'):
        filename += '.txt'
    
    # Add timestamp if just filename
    if filename == '.txt':
        filename = f"dump_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    filepath = os.path.join(output_dir, filename)
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# Instagram Data Dump - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"# Total: {len(Uuid)} users\n")
            f.write(f"# Format: username|full_name\n\n")
            for item in Uuid:
                f.write(item + '\n')
        
        print(f"\n{GREEN}✓ Saved {len(Uuid)} users to: {filepath}{RESET}")
        return True
        
    except Exception as e:
        print(f"{RED}✗ Failed to save: {e}{RESET}")
        return False

def view_data():
    """Display collected data in table format"""
    if not Uuid:
        print(f"\n{RED}No data to display!{RESET}")
        return
    
    table = Table(title=f"Collected Users ({len(Uuid)})", style="cyan")
    table.add_column("#", style="yellow", width=4)
    table.add_column("Username", style="green", width=20)
    table.add_column("Full Name", style="white", width=30)
    
    for i, item in enumerate(Uuid[:20], 1):
        parts = item.split('|')
        username = parts[0] if parts else 'Unknown'
        fullname = parts[1] if len(parts) > 1 else ''
        table.add_row(str(i), username, fullname)
    
    if len(Uuid) > 20:
        table.add_row("...", f"... and {len(Uuid)-20} more", "")
    
    console.print(table)

def clear_data():
    """Clear collected data"""
    global Uuid
    if not Uuid:
        print(f"{YELLOW}⚠ No data to clear{RESET}")
        return
    
    confirm = input(f"{RED}Are you sure you want to clear {len(Uuid)} users? (y/n): {RESET}").strip().lower()
    if confirm == 'y':
        Uuid = []
        print(f"{GREEN}✓ Data cleared{RESET}")
    else:
        print(f"{YELLOW}Operation cancelled{RESET}")

# ============ MAIN MENU ============
def show_menu():
    """Display main menu with stats"""
    clear_screen()
    
    # Load cookie
    cookie_dict = load_cookie()
    valid, msg = test_cookie(cookie_dict)
    
    # Extract username from cookie
    username = "Unknown"
    followers = 0
    if valid:
        cookie_str = cookie_dict.get('cookie', '')
        user_match = re.search(r'ds_user_id=([^;]+)', cookie_str)
        if user_match:
            try:
                user_id = user_match.group(1)
                url = f'https://i.instagram.com/api/v1/users/{user_id}/info/'
                response = requests.get(url, headers=HEADERS, cookies=cookie_dict, timeout=5)
                if response.status_code == 200:
                    data = response.json()
                    if 'user' in data:
                        username = data['user'].get('username', 'Unknown')
                        followers = data['user'].get('follower_count', 0)
            except:
                pass
    
    # Display banner
    print(f"""{CYAN}
    ╔══════════════════════════════════════════════════════════════╗
    ║                    INSTAGRAM DATA DUMPER                     ║
    ║                   Auto Username Detection                    ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    # Status panel
    status_color = GREEN if valid else RED
    status_text = f"{status_color}● Active{WHITE}" if valid else f"{RED}● Invalid{WHITE}"
    print(f"{WHITE}┌{'─'*78}┐{RESET}")
    print(f"{WHITE}│{RESET}  {CYAN}Session:{WHITE} @{username:<30} {status_text}")
    print(f"{WHITE}│{RESET}  {CYAN}Followers:{WHITE} {followers:<12} {CYAN}Collected:{WHITE} {len(Uuid):<12}")
    print(f"{WHITE}└{'─'*78}┘{RESET}")
    
    # Menu options
    print(f"\n{YELLOW}📋 MAIN MENU{RESET}")
    print(f"{WHITE}┌{'─'*78}┐{RESET}")
    print(f"{WHITE}│{RESET}  {BLUE}01{RESET}  🐦 Dump Followers")
    print(f"{WHITE}│{RESET}  {BLUE}02{RESET}  👣 Dump Following")
    print(f"{WHITE}│{RESET}  {BLUE}03{RESET}  📂 Load from File")
    print(f"{WHITE}│{RESET}  {BLUE}04{RESET}  💾 Save Data")
    print(f"{WHITE}│{RESET}  {BLUE}05{RESET}  👁️ View Data")
    print(f"{WHITE}│{RESET}  {BLUE}06{RESET}  🗑️ Clear Data")
    print(f"{WHITE}│{RESET}  {BLUE}00{RESET}  🔄 Change Cookie")
    print(f"{WHITE}└{'─'*78}┘{RESET}")
    
    return cookie_dict, valid

def menu():
    """Main menu loop"""
    global Uuid
    
    cookie_dict, valid = show_menu()
    
    while True:
        choice = input(f"\n{RED}[{WHITE}▶{RED}] {BLUE}Select option :{YELLOW} ").strip()
        
        if choice in ['01', '1']:
            if not valid:
                print(f"{RED}✗ Invalid cookie! Please update your cookie.{RESET}")
                time.sleep(1)
                continue
            dump_users(cookie_dict, typess=True)
            
        elif choice in ['02', '2']:
            if not valid:
                print(f"{RED}✗ Invalid cookie! Please update your cookie.{RESET}")
                time.sleep(1)
                continue
            dump_users(cookie_dict, typess=False)
            
        elif choice in ['03', '3']:
            load_from_file()
            
        elif choice in ['04', '4']:
            save_menu()
            
        elif choice in ['05', '5']:
            view_data()
            input(f"\n{RED}[{WHITE}▶{RED}] {BLUE}Press Enter to continue...{RESET}")
            
        elif choice in ['06', '6']:
            clear_data()
            
        elif choice in ['00', '0']:
            if os.path.exists('data/cookie.txt'):
                os.remove('data/cookie.txt')
            print(f"{GREEN}✓ Cookie removed. Exiting...{RESET}")
            sys.exit(0)
            
        else:
            print(f"{RED}✗ Invalid option!{RESET}")
            time.sleep(0.5)
        
        # Refresh menu
        cookie_dict, valid = show_menu()

def dump_users(cookie_dict, typess):
    """Dump followers or following"""
    global Uuid
    
    print(f"\n{CYAN}Enter Instagram usernames (comma separated for multiple){RESET}")
    print(f"{YELLOW}Example: user1, user2, user3{RESET}")
    users_input = input(f"\n{RED}[{WHITE}▶{RED}] {BLUE}Username(s) :{YELLOW} ").strip()
    
    if not users_input:
        print(f"{RED}✗ No username entered!{RESET}")
        return
    
    usernames = [u.strip() for u in users_input.split(',') if u.strip()]
    
    mode = "followers" if typess else "following"
    print(f"\n{YELLOW}🔍 Fetching user IDs for {len(usernames)} users...{RESET}")
    
    user_ids = []
    for username in usernames:
        print(f"  {WHITE}→ {CYAN}{username}{RESET}")
        user_id = get_user_id(username, cookie_dict)
        if user_id:
            user_ids.append(user_id)
            print(f"    {GREEN}✓ ID: {user_id}{RESET}")
        else:
            print(f"    {RED}✗ Failed to get ID{RESET}")
        time.sleep(0.3)
    
    if not user_ids:
        print(f"{RED}✗ No valid user IDs found!{RESET}")
        return
    
    print(f"\n{YELLOW}📊 Starting dump for {len(user_ids)} users...{RESET}")
    print(f"{WHITE}Mode: {CYAN}{mode.capitalize()}{RESET}")
    print(f"{WHITE}Target: {CYAN}{', '.join(usernames)}{RESET}")
    print(f"{'-'*60}")
    
    # Dump for each user
    for i, user_id in enumerate(user_ids):
        print(f"\n{WHITE}[{YELLOW}{i+1}/{len(user_ids)}{WHITE}] Processing {CYAN}{usernames[i]}{RESET}")
        
        if typess:
            success = collect_followers(user_id, cookie_dict.get('cookie', ''))
        else:
            success = collect_following(user_id, cookie_dict.get('cookie', ''))
        
        if success:
            print(f"\n{GREEN}✓ Completed for {usernames[i]}. Total: {len(Uuid)} users{RESET}")
        else:
            print(f"\n{RED}✗ Failed for {usernames[i]}{RESET}")
        
        # Delay between users
        if i < len(user_ids) - 1:
            time.sleep(1)
    
    print(f"\n{'='*60}")
    print(f"{GREEN}✨ Dump complete! Total collected: {len(Uuid)} users{RESET}")
    input(f"\n{RED}[{WHITE}▶{RED}] {BLUE}Press Enter to continue...{RESET}")

def load_from_file():
    """Load user data from file"""
    global Uuid
    
    files = []
    if os.path.exists('output'):
        files = [f for f in os.listdir('output') if f.endswith('.txt')]
    
    if files:
        print(f"\n{CYAN}Available files:{RESET}")
        for i, f in enumerate(files, 1):
            print(f"  {i}. {f}")
        print(f"  {len(files)+1}. Enter custom path")
        choice = input(f"\n{RED}[{WHITE}▶{RED}] {BLUE}Select file :{YELLOW} ").strip()
        
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(files):
                filepath = os.path.join('output', files[idx])
            else:
                filepath = input(f"{RED}[{WHITE}▶{RED}] {BLUE}File path :{YELLOW} ").strip()
        except:
            filepath = input(f"{RED}[{WHITE}▶{RED}] {BLUE}File path :{YELLOW} ").strip()
    else:
        filepath = input(f"{RED}[{WHITE}▶{RED}] {BLUE}File path :{YELLOW} ").strip()
    
    if not os.path.exists(filepath):
        print(f"{RED}✗ File not found: {filepath}{RESET}")
        return
    
    try:
        count = 0
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    # Check if line has username|fullname format
                    if '|' in line:
                        Uuid.append(line)
                    else:
                        # Just username, add with empty fullname
                        Uuid.append(f"{line}|")
                    count += 1
        
        print(f"{GREEN}✓ Loaded {count} users from {filepath}{RESET}")
        
    except Exception as e:
        print(f"{RED}✗ Failed to load file: {e}{RESET}")
    
    time.sleep(1)

def save_menu():
    """Save data menu"""
    if not Uuid:
        print(f"{RED}✗ No data to save!{RESET}")
        return
    
    print(f"\n{YELLOW}💾 SAVE OPTIONS{RESET}")
    print(f"{WHITE}┌{'─'*78}┐{RESET}")
    print(f"{WHITE}│{RESET}  {BLUE}1{RESET}  💾 Save to /sdcard/dump.txt (Android)")
    print(f"{WHITE}│{RESET}  {BLUE}2{RESET}  💾 Save to custom file")
    print(f"{WHITE}│{RESET}  {BLUE}3{RESET}  👁️  View data first")
    print(f"{WHITE}└{'─'*78}┘{RESET}")
    
    choice = input(f"\n{RED}[{WHITE}▶{RED}] {BLUE}Select option :{YELLOW} ").strip()
    
    if choice in ['1']:
        if save_data_sdcard():
            print(f"{GREEN}✓ Data saved to /sdcard/dump.txt{RESET}")
        else:
            # Fallback to custom save
            filename = input(f"{RED}[{WHITE}▶{RED}] {BLUE}Enter filename :{YELLOW} ").strip()
            if filename:
                save_data_custom(filename)
    
    elif choice in ['2']:
        filename = input(f"{RED}[{WHITE}▶{RED}] {BLUE}Enter filename :{YELLOW} ").strip()
        if not filename:
            filename = f"dump_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        save_data_custom(filename)
    
    elif choice in ['3']:
        view_data()
        save_menu()
    
    else:
        print(f"{RED}✗ Invalid option!{RESET}")
    
    input(f"\n{RED}[{WHITE}▶{RED}] {BLUE}Press Enter to continue...{RESET}")

# ============ MAIN ============
if __name__ == "__main__":
    ensure_directories()
    
    try:
        menu()
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}⚠ Interrupted by user{RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{RED}✗ Fatal error: {e}{RESET}")
        sys.exit(1)
