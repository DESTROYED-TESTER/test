#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#================[IMPORT MODULE]================#
import unicodedata, urllib.parse, requests, random, sys, uuid, json, hmac, hashlib, time, re, base64, datetime, urllib.request, string, os
from urllib.parse import quote
from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup as bsp
from rich.console import Console
from rich.panel import Panel as Pan, Panel as nel, Panel as panel
from rich import print as cetak
import threading
from rich.columns import Columns
from rich.progress import Progress, TextColumn, SpinnerColumn
from rich.text import Text
from concurrent.futures import ThreadPoolExecutor
import threading
import struct
import base64
import string
import uuid
import json
import requests
import pytz
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_v1_5
from rich import print as Cetak
from rich.tree import Tree
from rich.panel import Panel
import urllib.parse
from urllib.parse import quote
import re
import os
import sys
import json
import random
import urllib.request
import hashlib
import time
import uuid
import requests
import base64
import datetime
from concurrent.futures import ThreadPoolExecutor
from rich.panel import Panel as panel
from rich import print as prints
from datetime import datetime
from collections import deque
import queue
import signal

# Global variables
Uid, Uuid = [], []
bkas = []
Ok, Cp, Loop = 0, 0, 0
xx = 0
SistemLog = "api.instagram.com"
is_running = True
dump_queue = deque()
processed_users = set()
total_collected = 0
active_threads = []

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

getuserid = 'https://i.instagram.com/api/v1/users/web_profile_info/?username={nama!s}'
HEADERS = {
    'Host': 'www.instagram.com',
    'x-ig-app-id': '1217981644879628',
    'x-ig-www-claim': 'hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03DgxmT',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 instagram 360.0.0.33.104 (iPhone16,2; iOS 18.2; en_US; en; scale=3.00; 1170x2532; 510000000)',
    'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest',
    'x-asbd-id': '129477',
    'x-csrftoken': 'TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E',
    'sec-fetch-site': 'same-origin',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'
}
ua = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 instagram 360.0.0.33.104 (iPhone16,2; iOS 18.2; en_US; en; scale=3.00; 1170x2532; 510000000)'
}
userinfo = 'https://i.instagram.com/api/v1/users/{id!s}/info/'

def signal_handler(sig, frame):
    global is_running
    print(f"\n\n{YELLOW}⚠ Stopping dump process... (Press Ctrl+C again to force exit){RESET}")
    is_running = False
    time.sleep(1)
    if len(Uuid) > 0:
        print(f"{GREEN}✓ Collected {len(Uuid)} users. Saving...{RESET}")
        save_to_sdcard()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def Clear():
    try:
        os.system('clear')
    except:
        pass

def find_res():
    cookie = None
    try:
        if os.path.isfile('data/OK.txt'):
            with open('data/OK.txt', 'r') as f:
                lines = f.read().splitlines()
                for line in lines:
                    if 'sessionid=' in line:
                        cookie = line.strip()
                        break
        if not cookie and os.path.isfile('data/cookie.txt'):
            with open('data/cookie.txt', 'r') as f:
                cookie = f.read().strip()
    except:
        pass
    return cookie

def test_cookies(coki):
    """Test if cookies are still valid using multiple methods"""
    
    # Method 1: Try to get user info using the API
    try:
        uid_match = re.search('ds_user_id=(\\d+)', str(coki.get('cookie', '')))
        if uid_match:
            uid = uid_match.group(1)
            response = requests.get(
                f'https://i.instagram.com/api/v1/users/{uid}/info/',
                headers=ua,
                cookies=coki,
                timeout=10
            )
            if response.status_code == 200:
                data = response.json()
                if 'user' in data and data['user'].get('username'):
                    print(f"{GREEN}✓ Cookies are valid!{RESET}")
                    print(f"{WHITE}  Username: {CYAN}{data['user'].get('username')}{RESET}")
                    print(f"{WHITE}  Full Name: {CYAN}{data['user'].get('full_name', 'N/A')}{RESET}")
                    print(f"{WHITE}  Followers: {CYAN}{data['user'].get('follower_count', 0)}{RESET}")
                    return True
    except Exception as e:
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
        elif response.status_code == 302 or response.status_code == 401:
            print(f"{RED}✗ Cookies may be expired!{RESET}")
            return False
    except Exception as e:
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
    
    session_match = re.search('sessionid=([^;]+)', cookie_str)
    if session_match:
        session_value = session_match.group(1)
        if not session_value or len(session_value) < 5:
            print(f"{RED}✗ Session ID appears invalid (too short){RESET}")
            return False
    
    user_match = re.search('ds_user_id=([^;]+)', cookie_str)
    if user_match:
        user_id = user_match.group(1)
        if not user_id.isdigit():
            print(f"{RED}✗ User ID appears invalid (not a number){RESET}")
            return False
    
    print(f"{GREEN}✓ Cookie format looks valid{RESET}")
    return True

def Aset_Ig():
    os.system('clear')
    coki = {}
    
    if os.path.isfile('data/cookie.txt'):
        cookie_str = open('data/cookie.txt', 'r').read().strip()
        if cookie_str:
            coki = {'cookie': cookie_str}
            print(f"{YELLOW}Found existing cookie, testing...{RESET}")
            
            if not validate_cookie_format(cookie_str):
                print(f"{RED}Cookie format is invalid, please re-enter.{RESET}")
                time.sleep(2)
                os.remove('data/cookie.txt')
                coki = {}
    
    if not coki:
        print(f"{RED}[{WHITE}+{RED}] {CYAN}Please enter your instagram account cookie. Make sure to use a throwaway account!")
        print(f"{YELLOW}Cookie should contain: sessionid, ds_user_id, csrftoken{RESET}")
        cookie_input = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Cookie :{YELLOW} ").strip()
        
        if cookie_input.lower() == 'res':
            cookie_str = find_res()
            if not cookie_str:
                print(f"{RED}Failed to load backup cookie, please enter manually.")
                cookie_input = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Cookie :{YELLOW} ").strip()
                coki = {'cookie': cookie_input}
            else:
                coki = {'cookie': cookie_str}
        else:
            coki = {'cookie': cookie_input}
        
        if not validate_cookie_format(coki['cookie']):
            print(f"{RED}Invalid cookie format! Please check your input.{RESET}")
            time.sleep(3)
            return Aset_Ig()
    
    try:
        uid_match = re.search('ds_user_id=(\\d+)', str(coki['cookie']))
        if not uid_match:
            print(f"{RED}Could not find ds_user_id in cookie!{RESET}")
            time.sleep(2)
            return Aset_Ig()
        
        uid = uid_match.group(1)
        
        resp = requests.get(
            f'https://i.instagram.com/api/v1/users/{uid}/info/',
            headers=ua,
            cookies=coki,
            timeout=10
        )
        resp.raise_for_status()
        user_data = resp.json().get('user', {})
        
        if not user_data:
            print(f"{RED}Failed to get user data!{RESET}")
            time.sleep(2)
            return Aset_Ig()
        
        full_name = user_data.get('full_name', 'Name Unknown')
        follower_count = user_data.get('follower_count', 0)
        username = user_data.get('username', 'Unknown')
        
        open('data/cookie.txt', 'w').write(coki['cookie'])
        
        print(f"{GREEN}✓ Successfully logged in as: {username}{RESET}")
        print(f"{WHITE}  Full Name: {CYAN}{full_name}{RESET}")
        print(f"{WHITE}  Followers: {CYAN}{follower_count}{RESET}")
        time.sleep(1)
        
        return coki, full_name, follower_count
        
    except requests.exceptions.RequestException as e:
        print(f"{RED}Network error: {e}{RESET}")
        time.sleep(2)
        return Aset_Ig()
    except json.JSONDecodeError:
        print(f"{RED}Invalid response from server. Cookie may be expired.{RESET}")
        os.system('rm -rf data/cookie.txt')
        time.sleep(2)
        return Aset_Ig()
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")
        os.system('rm -rf data/cookie.txt')
        time.sleep(2)
        return Aset_Ig()

# ============ SAVE FUNCTIONS ============
def save_to_sdcard():
    """Save collected data to /sdcard/dump.txt with username|fullname format"""
    try:
        if not Uuid:
            print(f"{RED}✗ No data to save!{RESET}")
            return False
        
        if not os.path.exists('/sdcard'):
            print(f"{YELLOW}⚠ /sdcard directory not found. Creating...{RESET}")
            try:
                os.makedirs('/sdcard', exist_ok=True)
            except:
                pass
        
        with open('/sdcard/dump.txt', 'w', encoding='utf-8') as f:
            for item in Uuid:
                f.write(item + '\n')
        
        print(f"\n{GREEN}✓ Successfully saved {len(Uuid)} users to /sdcard/dump.txt{RESET}")
        print(f"{WHITE}  Format: username|full_name{RESET}")
        
        return True
        
    except PermissionError:
        print(f"{RED}✗ Permission denied! Try running with storage permission.{RESET}")
        print(f"{YELLOW}  In Termux, run: termux-setup-storage{RESET}")
        return False
    except Exception as e:
        print(f"{RED}✗ Failed to save file: {e}{RESET}")
        return False

def save_to_custom(filename):
    """Save collected data to a custom file"""
    try:
        if not Uuid:
            print(f"{RED}✗ No data to save!{RESET}")
            return False
        
        if not os.path.exists('data'):
            os.makedirs('data')
        
        with open(f'data/{filename}', 'w', encoding='utf-8') as f:
            for item in Uuid:
                f.write(item + '\n')
        
        print(f"\n{GREEN}✓ Successfully saved {len(Uuid)} users to data/{filename}{RESET}")
        print(f"{WHITE}  Format: username|full_name{RESET}")
        return True
        
    except Exception as e:
        print(f"{RED}✗ Failed to save file: {e}{RESET}")
        return False

def view_data():
    """Display all collected data"""
    if not Uuid:
        print(f"\n{RED}No data to display!{RESET}")
        return
    
    print(f"\n{YELLOW}{'='*60}{RESET}")
    print(f"{GREEN}Total Users: {len(Uuid)}{RESET}")
    print(f"{YELLOW}{'='*60}{RESET}")
    
    for i, item in enumerate(Uuid, 1):
        parts = item.split('|')
        username = parts[0] if parts else 'Unknown'
        fullname = parts[1] if len(parts) > 1 else 'N/A'
        print(f"{WHITE}{i:4}. {RESET}{GREEN}{username:<20}{RESET} | {CYAN}{fullname}{RESET}")
    
    print(f"{YELLOW}{'='*60}{RESET}")

# ============ UNLIMITED DUMP SYSTEM ============
def get_user_id_unlimited(username, cookies):
    """Get user ID with multiple methods for unlimited dumping"""
    methods = [
        # Method 1: Web Profile API
        lambda: get_user_id_web_profile(username, cookies),
        # Method 2: GraphQL API
        lambda: get_user_id_graphql(username, cookies),
        # Method 3: Scrape from page
        lambda: get_user_id_scrape(username, cookies)
    ]
    
    for method in methods:
        try:
            result = method()
            if result:
                return result
        except:
            continue
    return None

def get_user_id_web_profile(username, cookies):
    url = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={username}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15',
        'x-ig-app-id': '1217981644879628',
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers, cookies=cookies, timeout=10)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'user' in data['data']:
            return data['data']['user'].get('id')
    return None

def get_user_id_graphql(username, cookies):
    url = 'https://www.instagram.com/graphql/query/'
    params = {
        'query_hash': 'c9100bf9110dd6361671f113dd02e7d6',
        'variables': json.dumps({'username': username})
    }
    response = requests.get(url, params=params, cookies=cookies, timeout=10)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'user' in data['data']:
            return data['data']['user'].get('id')
    return None

def get_user_id_scrape(username, cookies):
    session = requests.Session()
    session.max_redirects = 3
    response = session.get(f'https://www.instagram.com/{username}/', cookies=cookies, timeout=10)
    if response.status_code == 200:
        patterns = [
            r'"user_id":"(\d+)"',
            r'"profilePage_(\d+)"',
            r'"id":"(\d+)","username":"' + username + '"',
            r'{"id":"(\d+)","username":"' + username + '"'
        ]
        for pattern in patterns:
            match = re.search(pattern, response.text)
            if match:
                return match.group(1)
    return None

def collect_from_user(user_id, cookies, typess, max_users=None):
    """Collect users from a single target with pagination support"""
    global is_running, total_collected, Uuid
    
    if not is_running:
        return
    
    collected = 0
    after = ""
    mode = "followers" if typess else "following"
    
    while is_running and (max_users is None or collected < max_users):
        try:
            result = graphql_batch(user_id, cookies, typess, after)
            if not result:
                break
                
            users, after, has_next = result
            
            # Process collected users
            for user in users:
                if user and user not in processed_users:
                    processed_users.add(user)
                    Uuid.append(user)
                    total_collected += 1
                    collected += 1
                    
                    # Update progress every 10 users
                    if total_collected % 10 == 0:
                        print(f"\r{GREEN}✓ Total collected: {total_collected} users from {len(dump_queue)} targets{RESET}", end="", flush=True)
            
            if not has_next or not after:
                break
                
            # Add delay between pagination requests
            time.sleep(0.5)
            
        except Exception as e:
            print(f"\n{RED}Error collecting from user {user_id}: {e}{RESET}")
            break

def graphql_batch(user_id, cookies, typess, after):
    """Fetch a batch of followers/following"""
    api = "https://www.instagram.com/graphql/query/"
    
    if typess:
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
    
    ptk = {
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15",
        "accept": "application/json",
        "cookie": cookies,
        "x-ig-app-id": "1217981644879628"
    }
    
    session = requests.Session()
    session.max_redirects = 5
    
    req = session.get(api, params=params, headers=ptk, timeout=30)
    req.raise_for_status()
    req_json = req.json()
    
    if 'require_login' in req_json:
        print(f'\n{RED}Invalid Cookie - Need to login{RESET}')
        return None
    
    if 'status' in req_json and req_json['status'] == 'fail':
        print(f'\n{RED}Request failed: {req_json.get("message", "Unknown error")}{RESET}')
        return None
    
    khm = 'edge_followed_by' if typess else 'edge_follow'
    
    if 'data' not in req_json or 'user' not in req_json['data'] or not req_json['data']['user']:
        return None
    
    user_data = req_json['data']['user']
    
    if khm not in user_data:
        return None
    
    edges = user_data[khm].get('edges', [])
    if not edges:
        return None
    
    users = []
    for xyz in edges:
        username = xyz['node'].get('username', '')
        full_name = xyz['node'].get('full_name', '')
        if username:
            users.append(f"{username}|{full_name}")
    
    page_info = user_data[khm].get('page_info', {})
    has_next = page_info.get('has_next_page', False)
    next_cursor = page_info.get('end_cursor', '') if has_next else None
    
    return users, next_cursor, has_next

def unlimited_dump(cookies, typess):
    """Main unlimited dump function with queue system"""
    global is_running, dump_queue, processed_users, total_collected, active_threads
    
    # Reset state
    is_running = True
    processed_users = set()
    total_collected = 0
    active_threads = []
    
    print(f"\n{CYAN}╔══════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║{WHITE}         UNLIMITED INSTAGRAM DUMP SYSTEM v2.0                {CYAN}║{RESET}")
    print(f"{CYAN}╚══════════════════════════════════════════════════════════════╝{RESET}")
    print(f"\n{YELLOW}Instructions:{RESET}")
    print(f"  {GREEN}•{WHITE} Enter usernames (separated by commas) to start collecting{RESET}")
    print(f"  {GREEN}•{WHITE} The system will automatically follow and collect from each user{RESET}")
    print(f"  {GREEN}•{WHITE} It will continue until you press {RED}Ctrl+C{RESET}")
    print(f"  {GREEN}•{WHITE} New usernames found will be added to the queue automatically{RESET}")
    print(f"  {GREEN}•{WHITE} Results will be saved to {CYAN}/sdcard/dump.txt{RESET}\n")
    
    # Get initial usernames
    users_input = input(f"{RED}[{WHITE}+{RED}] {BLUE}Enter usernames (comma separated) :{YELLOW} ").strip()
    
    if not users_input:
        print(f"{RED}No username entered!{RESET}")
        return
    
    initial_users = [u.strip() for u in users_input.split(',') if u.strip()]
    
    # Get user IDs and add to queue
    print(f"\n{YELLOW}Processing initial usernames...{RESET}")
    for username in initial_users:
        user_id = get_user_id_unlimited(username, cookies)
        if user_id:
            if user_id not in processed_users:
                dump_queue.append((user_id, username))
                processed_users.add(user_id)
                print(f"{GREEN}✓ Added: {username} (ID: {user_id}){RESET}")
        else:
            print(f"{RED}✗ Could not find: {username}{RESET}")
        time.sleep(0.5)
    
    if not dump_queue:
        print(f"{RED}No valid users found to process!{RESET}")
        return
    
    # Start unlimited processing
    print(f"\n{GREEN}Starting unlimited dump... Press Ctrl+C to stop{RESET}")
    print(f"{YELLOW}Targets in queue: {len(dump_queue)}{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\n")
    
    # Use ThreadPoolExecutor for concurrent processing
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = []
        
        while is_running and dump_queue:
            # Process targets from queue
            while dump_queue and len(futures) < 3:
                user_id, username = dump_queue.popleft()
                future = executor.submit(process_target, user_id, username, cookies, typess)
                futures.append(future)
            
            # Check completed futures
            for future in as_completed(futures):
                if not is_running:
                    break
                futures.remove(future)
                # New users might have been added to queue
                
            # Small delay to prevent CPU overload
            time.sleep(0.1)
        
        # Cancel remaining futures if stopping
        for future in futures:
            future.cancel()
    
    # Final save
    if Uuid:
        print(f"\n{GREEN}✓ Dump complete! Total collected: {len(Uuid)} users{RESET}")
        save_to_sdcard()

def process_target(user_id, username, cookies, typess):
    """Process a single target user"""
    global dump_queue, processed_users
    
    if not is_running:
        return
    
    try:
        # Check if user is already processed or in queue
        if user_id in processed_users:
            return
        
        processed_users.add(user_id)
        
        # Collect users from this target
        collect_from_user(user_id, cookies, typess, max_users=None)
        
        # Random delay to avoid rate limiting
        time.sleep(random.uniform(1, 3))
        
    except Exception as e:
        print(f"\n{RED}Error processing user {username}: {e}{RESET}")

def process_new_users_from_batch(new_users, cookies):
    """Process newly found usernames and add to queue"""
    global dump_queue, processed_users
    
    if not new_users or not is_running:
        return
    
    for username in new_users:
        if not username or username in processed_users:
            continue
            
        try:
            user_id = get_user_id_unlimited(username, cookies)
            if user_id and user_id not in processed_users:
                processed_users.add(user_id)
                dump_queue.append((user_id, username))
                print(f"\n{GREEN}➕ New target added: {username} (ID: {user_id}){RESET}")
                time.sleep(0.3)
        except:
            continue

# ============ METODE TYPE ============
def MetodeType():
    global Uuid
    if not Uuid:
        print(f"\n{RED}No users collected! Please run a dump first.{RESET}")
        time.sleep(2)
        Menu()
        return
    
    os.system('clear')
    print(f"{BLUE}═" * 80)
    print(f"{GREEN}Total collected users: {len(Uuid)}{RESET}")
    
    print(f"\n{RED}[ {YELLOW}Save & Manage Options {RED}]\n")
    print(f"{RED}[{WHITE}01{RED}] {CYAN} Save to /sdcard/dump.txt")
    print(f"{RED}[{WHITE}02{RED}] {CYAN} Save to custom file (data/ folder)")
    print(f"{RED}[{WHITE}03{RED}] {CYAN} View all collected data")
    print(f"{RED}[{WHITE}04{RED}] {CYAN} Clear collected data")
    print(f"{RED}[{WHITE}05{RED}] {CYAN} Return to main menu")
    print(f"{RED}[{WHITE}00{RED}] {RED} Exit")
    print(f"{BLUE}═" * 80)
    
    choice = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Select option :{YELLOW} ").strip()
    
    if choice in ['01', '1']:
        if save_to_sdcard():
            input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Press Enter to continue...{RESET}")
        MetodeType()
        
    elif choice in ['02', '2']:
        filename = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Enter filename (e.g., output.txt) :{YELLOW} ").strip()
        if not filename:
            filename = f"dump_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        if not filename.endswith('.txt'):
            filename += '.txt'
        if save_to_custom(filename):
            input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Press Enter to continue...{RESET}")
        MetodeType()
        
    elif choice in ['03', '3']:
        view_data()
        input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Press Enter to continue...{RESET}")
        MetodeType()
        
    elif choice in ['04', '4']:
        confirm = input(f"\n{RED}[{WHITE}+{RED}] {RED}Are you sure you want to clear all collected data? (y/n): {YELLOW}").strip().lower()
        if confirm == 'y':
            Uuid = []
            print(f"{GREEN}✓ Data cleared successfully!{RESET}")
        else:
            print(f"{YELLOW}Operation cancelled.{RESET}")
        time.sleep(1)
        MetodeType()
        
    elif choice in ['05', '5']:
        Menu()
        
    elif choice in ['00', '0']:
        print(f"{GREEN}Exiting...{RESET}")
        sys.exit(0)
        
    else:
        print(f"{RED}Invalid option!{RESET}")
        time.sleep(1)
        MetodeType()

def Menu():
    os.system('clear')
    aset, nama, fol = Aset_Ig()
    print(f"{BLUE}═" * 80)
    print(f"""{campur} 
 _______  ______ _______ _______ _     _      _____  ______
 |       |_____/ |_____| |       |____/         |   |  ____
 |_____  |    \\_ |     | |_____  |    \\_      __|__ |_____|
                                          
{CYAN}╭──────────────────────╮{CYAN}╭───────────────╮{CYAN}╭─────────────────────────╮
{CYAN}│ {CYAN}Author : {GREEN}sumon {CYAN}│{CYAN}  │ {WHITE}Version : {GREEN}3.0 {CYAN}│{CYAN}│ {WHITE}Status : {GREEN}Premium{CYAN}    │
{CYAN}╰──────────────────────╯{CYAN}╰───────────────╯{CYAN}╰─────────────────────────╯""")
    print(f"{GREEN}{WHITE}Username :{GREEN} {nama[:8]}\n{WHITE}Followers : {GREEN}{fol}")
    
    print(f"\n{RED}[ {YELLOW}Main Menu {RED}]\n")
    print(f"{RED}[{WHITE}01{RED}] {CYAN} UNLIMITED FOLLOWERS DUMP (Auto Discovery)")
    print(f"{RED}[{WHITE}02{RED}] {CYAN} UNLIMITED FOLLOWING DUMP (Auto Discovery)")
    print(f"{RED}[{WHITE}03{RED}] {CYAN} Load from file")
    print(f"{RED}[{WHITE}04{RED}] {CYAN} Manage saved data")
    print(f"{RED}[{WHITE}00{RED}] {RED} Delete/Change Cookies")
    print(f"{BLUE}═" * 80)
    x = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Please select a menu option :{YELLOW} ")

    if x in ['01', '1']:
        unlimited_dump(aset, True)
        input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Press Enter to return to menu...{RESET}")
        Menu()
    elif x in ['02', '2']:
        unlimited_dump(aset, False)
        input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Press Enter to return to menu...{RESET}")
        Menu()
    elif x in ['03', '3']:
        crackfile()
    elif x in ['04', '4']:
        MetodeType()
    elif x in ['00', '0']:
        if os.path.exists('data/cookie.txt'):
            os.remove('data/cookie.txt')
        prints(f"{GREEN}Successfully deleted cookies")
        exit()
    else:
        print(f"{RED}Invalid option!")
        time.sleep(1)
        Menu()

def crackfile():
    try:
        nu = input(f"{PURPLE}[{WHITE}+{PURPLE}] {WHITE}Enter Your File Name: {PURPLE}")
        if not os.path.isfile(nu):
            print(f"{PURPLE}[{RED}+{PURPLE}] {RED}File Not Found.")
            return Menu()
            
        with open(nu, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    Uuid.append(line)
        print(f"{PURPLE}[{WHITE}+{PURPLE}] {WHITE}Total IDs : {len(Uuid)}")
        if len(Uuid) > 0:
            MetodeType()
        else:
            print(f"{RED}No valid IDs found in file!")
            return Menu()
    except Exception as e:
        print(f"{PURPLE}[{RED}+{PURPLE}] {RED}Error: {e}")
        return Menu()

# Main execution
if __name__ == "__main__":
    if not os.path.exists('data'):
        os.makedirs('data')
    
    try:
        Menu()
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Exiting...{RESET}")
        if Uuid:
            save_to_sdcard()
        sys.exit(0)
    except Exception as e:
        print(f"\n{RED}An error occurred: {e}{RESET}")
        sys.exit(1)
