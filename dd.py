#!/usr/bin/env python3
#================[IMPORT MODULE]================#
import unicodedata, urllib.parse, requests, random, sys, uuid, json, hmac, hashlib, time, re, base64, datetime, urllib.request, string, os
from urllib.parse import quote; from concurrent.futures import ThreadPoolExecutor; from bs4 import BeautifulSoup as bsp
from rich.console import Console; from rich.panel import Panel as Pan, Panel as nel, Panel as panel; from rich import print as cetak
import threading; from rich.columns import Columns; from rich.progress import Progress, TextColumn, SpinnerColumn
from rich.text import Text
from concurrent.futures import ThreadPoolExecutor, as_completed
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
from rich import print as Cetak; from rich.tree import Tree; from rich.panel import Panel
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
from queue import Queue
import signal

# Global variables
Uid, Uuid = [], []
bkas = []
Ok, Cp, Loop = 0, 0, 0
xx = 0
SistemLog = "api.instagram.com"
stop_dumping = False
dump_counter = 0
max_dump_limit = 999999999  # Unlimited by default

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

# Thread pool for parallel dumping
executor = ThreadPoolExecutor(max_workers=5)
user_queue = Queue()
processed_users = set()

# Signal handler for graceful stop
def signal_handler(sig, frame):
    global stop_dumping
    print(f"\n{YELLOW}Stopping dump gracefully...{RESET}")
    stop_dumping = True
    save_progress()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def Clear():
    try:
        os.system('clear')
    except:
        pass

def save_progress():
    """Save current progress to file"""
    try:
        with open('data/progress.txt', 'w') as f:
            json.dump({
                'total': len(Uuid),
                'timestamp': datetime.now().isoformat()
            }, f)
    except:
        pass

def load_progress():
    """Load previous progress"""
    try:
        if os.path.exists('data/progress.txt'):
            with open('data/progress.txt', 'r') as f:
                data = json.load(f)
                return data.get('total', 0)
    except:
        return 0
    return 0

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
                    return True
    except:
        pass
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
        print(f"{RED}[{WHITE}+{RED}] {CYAN}Please enter your instagram account cookie.{RESET}")
        cookie_input = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Cookie :{YELLOW} ").strip()
        
        if cookie_input.lower() == 'res':
            cookie_str = find_res()
            if not cookie_str:
                print(f"{RED}Failed to load backup cookie.{RESET}")
                cookie_input = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Cookie :{YELLOW} ").strip()
                coki = {'cookie': cookie_input}
            else:
                coki = {'cookie': cookie_str}
        else:
            coki = {'cookie': cookie_input}
        
        if not validate_cookie_format(coki['cookie']):
            print(f"{RED}Invalid cookie format!{RESET}")
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
        
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")
        os.system('rm -rf data/cookie.txt')
        time.sleep(2)
        return Aset_Ig()

# ============ ENHANCED SAVE FUNCTIONS ============
def save_to_sdcard_unlimited():
    """Save collected data to /sdcard/dump.txt without overwriting"""
    try:
        if not Uuid:
            print(f"{RED}✗ No data to save!{RESET}")
            return False
        
        # Check if file exists and get current content
        existing_data = set()
        if os.path.exists('/sdcard/dump.txt'):
            with open('/sdcard/dump.txt', 'r', encoding='utf-8') as f:
                existing_data = set(line.strip() for line in f if line.strip())
        
        # Get new data
        new_data = set(Uuid) - existing_data
        
        if not new_data:
            print(f"{YELLOW}No new data to add.{RESET}")
            return True
        
        # Append new data
        with open('/sdcard/dump.txt', 'a', encoding='utf-8') as f:
            for item in new_data:
                f.write(item + '\n')
        
        print(f"\n{GREEN}✓ Added {len(new_data)} new users to /sdcard/dump.txt{RESET}")
        print(f"{WHITE}  Total users in file: {len(existing_data) + len(new_data)}{RESET}")
        return True
        
    except Exception as e:
        print(f"{RED}✗ Failed to save file: {e}{RESET}")
        return False

def auto_save_periodic():
    """Auto-save data every 10 users"""
    global Uuid
    if len(Uuid) > 0 and len(Uuid) % 10 == 0:
        save_to_sdcard_unlimited()
        save_progress()

# ============ UNLIMITED DUMPING ENGINE ============
def Graphql_unlimited(typess, userid, cokie, after, max_pages=999999):
    """Unlimited dumping with infinite pagination"""
    global xx, Uuid, stop_dumping, dump_counter, max_dump_limit
    
    if stop_dumping:
        return
    
    api = "https://www.instagram.com/graphql/query/"
    
    if typess:
        query_hash = "37479f2b8209594dde7facb0d904896a"
    else:
        query_hash = "58712303d941c6855d4e888c5f0cd22f"
    
    variables = {
        "id": userid,
        "first": 100,  # Max results per request
        "after": after
    }
    
    params = {
        'query_hash': query_hash,
        'variables': json.dumps(variables)
    }
    
    try:
        ptk = {
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 instagram 360.0.0.33.104",
            "accept": "application/json",
            "cookie": cokie,
            "x-ig-app-id": "1217981644879628"
        }
        
        session = requests.Session()
        session.max_redirects = 5
        
        req = session.get(api, params=params, headers=ptk, timeout=30)
        req.raise_for_status()
        req_json = req.json()
        
        if 'require_login' in req_json:
            print(f'\n{WHITE}[{YELLOW}!{WHITE}] Invalid Cookie - Need to login')
            return
        
        if 'status' in req_json and req_json['status'] == 'fail':
            print(f'\n{RED}Request failed: {req_json.get("message", "Unknown error")}')
            return
        
        khm = 'edge_followed_by' if typess else 'edge_follow'
        
        if 'data' not in req_json or 'user' not in req_json['data'] or not req_json['data']['user']:
            print(f"\n{RED}User not found or private. Skipping...")
            return
        
        user_data = req_json['data']['user']
        
        if khm not in user_data:
            print(f"\n{RED}This user has no visible {khm.replace('edge_', '')} or is private")
            return
        
        edges = user_data[khm].get('edges', [])
        if not edges:
            print(f"\n{YELLOW}No {khm.replace('edge_', '')} found for this user")
            return
        
        # Process edges
        for xyz in edges:
            if stop_dumping:
                return
            
            username = xyz['node'].get('username', '')
            full_name = xyz['node'].get('full_name', '')
            
            if username:
                xy = username + '|' + full_name
                if xy not in Uuid:
                    xx += 1
                    dump_counter += 1
                    Uuid.append(xy)
                    
                    # Auto-save periodically
                    if dump_counter % 10 == 0:
                        save_to_sdcard_unlimited()
                    
                    print(f'\r{WHITE}Collected: {GREEN}{len(Uuid)}{WHITE} | Last: {CYAN}{username}{WHITE}                            ', end='', flush=True)
                    time.sleep(0.001)
        
        # Check for pagination - CONTINUE UNTIL NO MORE PAGES
        page_info = user_data[khm].get('page_info', {})
        end = page_info.get('has_next_page', False)
        
        if end and not stop_dumping:
            after = page_info.get('end_cursor', '')
            if after:
                print(f"\n{YELLOW}Loading next page... (Total: {len(Uuid)}){RESET}")
                time.sleep(0.5)  # Delay between pages
                Graphql_unlimited(typess, userid, cokie, after, max_pages)
        else:
            print(f"\n{GREEN}✓ Completed dumping {len(Uuid)} users!{RESET}")
                
    except requests.exceptions.Timeout:
        print(f"\n{RED}Timeout error - retrying...{RESET}")
        time.sleep(2)
        Graphql_unlimited(typess, userid, cokie, after, max_pages)
    except Exception as e:
        print(f"\n{RED}Error: {e} - Retrying...{RESET}")
        time.sleep(2)
        Graphql_unlimited(typess, userid, cokie, after, max_pages)

def multi_user_dump(cintil, typess):
    """Dump multiple users with thread pooling"""
    global stop_dumping
    
    print(f"\n{CYAN}Enter usernames (comma separated) for unlimited dumping{RESET}")
    print(f"{YELLOW}Example: user1,user2,user3,user4{RESET}")
    users_input = input(f"{RED}[{WHITE}+{RED}] {BLUE}Usernames :{YELLOW} ").strip()
    
    if not users_input:
        print(f"{RED}No username entered!{RESET}")
        return Menu()
    
    users = [u.strip() for u in users_input.split(',') if u.strip()]
    
    # Get user IDs
    user_ids = []
    print(f"\n{YELLOW}Fetching user IDs...{RESET}")
    
    for username in users:
        if stop_dumping:
            break
        user_id = get_user_id_methods(username, cintil)
        if user_id:
            user_ids.append(user_id)
            print(f"{GREEN}✓ {username} -> ID: {user_id}{RESET}")
        else:
            print(f"{RED}✗ Could not find ID for {username}{RESET}")
        time.sleep(0.5)
    
    if not user_ids:
        print(f"{RED}No valid user IDs found!{RESET}")
        time.sleep(2)
        return Menu()
    
    mode = 'followers' if typess else 'following'
    print(f"\n{GREEN}Starting UNLIMITED {mode.upper()} dump for {len(user_ids)} users{RESET}")
    print(f"{YELLOW}Press Ctrl+C to stop at any time{RESET}\n")
    
    # Dump each user
    for user_id in user_ids:
        if stop_dumping:
            break
        print(f"\n{WHITE}Processing user ID: {CYAN}{user_id}{RESET}")
        Graphql_unlimited(typess, user_id, cintil['cookie'], '')
        time.sleep(1)
    
    print(f"\n{GREEN}Total users collected: {len(Uuid)}{RESET}")
    
    if len(Uuid) > 0:
        save_to_sdcard_unlimited()
        print(f"\n{YELLOW}Data saved to /sdcard/dump.txt{RESET}")
        time.sleep(1)
    
    MetodeType()

# ============ BATCH DUMP FROM FILE ============
def batch_dump_from_file(cintil, typess):
    """Dump users from a file containing usernames"""
    global stop_dumping
    
    try:
        filename = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Enter file name with usernames: {YELLOW}").strip()
        
        if not os.path.exists(filename):
            print(f"{RED}File not found!{RESET}")
            return Menu()
        
        with open(filename, 'r') as f:
            users = [line.strip() for line in f if line.strip()]
        
        if not users:
            print(f"{RED}No usernames found in file!{RESET}")
            return Menu()
        
        print(f"{GREEN}Loaded {len(users)} usernames from file{RESET}")
        
        # Get user IDs
        user_ids = []
        print(f"\n{YELLOW}Fetching user IDs...{RESET}")
        
        for username in users:
            if stop_dumping:
                break
            user_id = get_user_id_methods(username, cintil)
            if user_id:
                user_ids.append(user_id)
                print(f"{GREEN}✓ {username} -> ID: {user_id}{RESET}")
            else:
                print(f"{RED}✗ Could not find ID for {username}{RESET}")
            time.sleep(0.3)
        
        if not user_ids:
            print(f"{RED}No valid user IDs found!{RESET}")
            time.sleep(2)
            return Menu()
        
        mode = 'followers' if typess else 'following'
        print(f"\n{GREEN}Starting BATCH UNLIMITED {mode.upper()} dump for {len(user_ids)} users{RESET}")
        print(f"{YELLOW}Press Ctrl+C to stop at any time{RESET}\n")
        
        # Dump each user
        for user_id in user_ids:
            if stop_dumping:
                break
            print(f"\n{WHITE}Processing user ID: {CYAN}{user_id}{RESET}")
            Graphql_unlimited(typess, user_id, cintil['cookie'], '')
            time.sleep(1)
        
        print(f"\n{GREEN}Total users collected: {len(Uuid)}{RESET}")
        
        if len(Uuid) > 0:
            save_to_sdcard_unlimited()
            print(f"\n{YELLOW}Data saved to /sdcard/dump.txt{RESET}")
            time.sleep(1)
        
        MetodeType()
        
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")
        time.sleep(2)
        Menu()

def get_user_id_methods(username, cookies):
    """Try multiple methods to get user ID"""
    
    # Method 1: Official API
    try:
        url = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={username}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 instagram 360.0.0.33.104',
            'x-ig-app-id': '1217981644879628',
            'Accept': 'application/json'
        }
        response = requests.get(url, headers=headers, cookies=cookies, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'user' in data['data']:
                user_id = data['data']['user'].get('id')
                if user_id:
                    return user_id
    except:
        pass
    
    # Method 2: GraphQL
    try:
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
    except:
        pass
    
    # Method 3: Scraping
    try:
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
    except:
        pass
    
    return None

# ============ METODE TYPE ENHANCED ============
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
    print(f"{YELLOW}Last 5 users:{RESET}")
    for i, item in enumerate(Uuid[-5:], 1):
        parts = item.split('|')
        print(f"  {i}. {GREEN}{parts[0]}{RESET} | {CYAN}{parts[1] if len(parts) > 1 else 'N/A'}{RESET}")
    
    print(f"\n{RED}[ {YELLOW}Save & Manage Options {RED}]\n")
    print(f"{RED}[{WHITE}01{RED}] {CYAN} Save to /sdcard/dump.txt (Append)")
    print(f"{RED}[{WHITE}02{RED}] {CYAN} Save to custom file")
    print(f"{RED}[{WHITE}03{RED}] {CYAN} View all collected data")
    print(f"{RED}[{WHITE}04{RED}] {CYAN} Clear collected data")
    print(f"{RED}[{WHITE}05{RED}] {CYAN} Return to main menu")
    print(f"{RED}[{WHITE}00{RED}] {RED} Exit")
    print(f"{BLUE}═" * 80)
    
    choice = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Select option :{YELLOW} ").strip()
    
    if choice in ['01', '1']:
        save_to_sdcard_unlimited()
        input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Press Enter to continue...{RESET}")
        MetodeType()
        
    elif choice in ['02', '2']:
        filename = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Enter filename: {YELLOW}").strip()
        if not filename:
            filename = f"dump_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        if not filename.endswith('.txt'):
            filename += '.txt'
        
        with open(filename, 'w', encoding='utf-8') as f:
            for item in Uuid:
                f.write(item + '\n')
        print(f"{GREEN}✓ Saved to {filename}{RESET}")
        input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Press Enter to continue...{RESET}")
        MetodeType()
        
    elif choice in ['03', '3']:
        view_data()
        input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Press Enter to continue...{RESET}")
        MetodeType()
        
    elif choice in ['04', '4']:
        confirm = input(f"\n{RED}Clear all data? (y/n): {YELLOW}").strip().lower()
        if confirm == 'y':
            Uuid = []
            print(f"{GREEN}✓ Data cleared!{RESET}")
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

def Menu():
    os.system('clear')
    aset, nama, fol = Aset_Ig()
    print(f"{BLUE}═" * 80)
    print(f"""{campur} 
 ⚡ UNLIMITED INSTAGRAM DUMPER v3.0 ⚡
 {CYAN}╭─────────────────────────────────────────────────────────────╮
 {CYAN}│ {WHITE}Author  : {GREEN}sumon                                   {CYAN}│
 {CYAN}│ {WHITE}Version : {GREEN}3.0 - Unlimited Dumping                {CYAN}│
 {CYAN}│ {WHITE}Status  : {GREEN}● Active - NON-STOP                   {CYAN}│
 {CYAN}╰─────────────────────────────────────────────────────────────╯""")
    print(f"{GREEN}Username : {WHITE}{nama[:12]}{RESET}")
    print(f"{GREEN}Followers: {WHITE}{fol}{RESET}")
    
    print(f"\n{RED}[ {YELLOW}UNLIMITED DUMP MENU {RED}]\n")
    print(f"{RED}[{WHITE}01{RED}] {CYAN} Dump Followers (UNLIMITED)")
    print(f"{RED}[{WHITE}02{RED}] {CYAN} Dump Following (UNLIMITED)")
    print(f"{RED}[{WHITE}03{RED}] {CYAN} Batch Dump from File")
    print(f"{RED}[{WHITE}04{RED}] {CYAN} Manage Saved Data")
    print(f"{RED}[{WHITE}05{RED}] {CYAN} Auto-Dump Top Users")
    print(f"{RED}[{WHITE}00{RED}] {RED} Delete/Change Cookies")
    print(f"{BLUE}═" * 80)
    
    x = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Select option :{YELLOW} ")

    if x in ['01', '1']:
        multi_user_dump(aset, True)
    elif x in ['02', '2']:
        multi_user_dump(aset, False)
    elif x in ['03', '3']:
        batch_dump_from_file(aset, True)
    elif x in ['04', '4']:
        MetodeType()
    elif x in ['05', '5']:
        auto_dump_top_users(aset)
    elif x in ['00', '0']:
        if os.path.exists('data/cookie.txt'):
            os.remove('data/cookie.txt')
        prints(f"{GREEN}Cookies deleted")
        exit()
    else:
        print(f"{RED}Invalid option!{RESET}")
        time.sleep(1)
        Menu()

def auto_dump_top_users(cintil):
    """Auto-dump followers of popular accounts"""
    print(f"\n{CYAN}AUTO-DUMP MODE: Will dump followers of multiple accounts{RESET}")
    
    popular_accounts = input(f"{RED}[{WHITE}+{RED}] {BLUE}Enter usernames (comma separated): {YELLOW}").strip()
    
    if not popular_accounts:
        print(f"{RED}No usernames entered!{RESET}")
        return Menu()
    
    users = [u.strip() for u in popular_accounts.split(',') if u.strip()]
    
    # Get user IDs
    user_ids = []
    print(f"\n{YELLOW}Fetching user IDs...{RESET}")
    
    for username in users:
        user_id = get_user_id_methods(username, cintil)
        if user_id:
            user_ids.append(user_id)
            print(f"{GREEN}✓ {username} -> ID: {user_id}{RESET}")
        else:
            print(f"{RED}✗ Could not find ID for {username}{RESET}")
        time.sleep(0.5)
    
    if not user_ids:
        print(f"{RED}No valid user IDs found!{RESET}")
        time.sleep(2)
        return Menu()
    
    print(f"\n{GREEN}Starting AUTO-DUMP for {len(user_ids)} accounts...{RESET}")
    print(f"{YELLOW}Press Ctrl+C to stop at any time{RESET}\n")
    
    # Dump followers for each account
    for user_id in user_ids:
        print(f"\n{WHITE}{'='*60}{RESET}")
        print(f"{CYAN}Dumping followers for user ID: {user_id}{RESET}")
        print(f"{WHITE}{'='*60}{RESET}")
        Graphql_unlimited(True, user_id, cintil['cookie'], '')
        time.sleep(2)
    
    print(f"\n{GREEN}Total users collected: {len(Uuid)}{RESET}")
    
    if len(Uuid) > 0:
        save_to_sdcard_unlimited()
        print(f"\n{YELLOW}Data saved to /sdcard/dump.txt{RESET}")
        time.sleep(1)
    
    MetodeType()

# ============ MAIN EXECUTION ============
if __name__ == "__main__":
    if not os.path.exists('data'):
        os.makedirs('data')
    
    print(f"""
    {CYAN}╔═══════════════════════════════════════════╗
    ║    UNLIMITED INSTAGRAM DUMPER v3.0      ║
    ║    NON-STOP - INFINITE DUMPING          ║
    ║    Press CTRL+C to stop anytime         ║
    ╚═══════════════════════════════════════════╝{RESET}
    """)
    time.sleep(1)
    
    try:
        Menu()
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}⚠ Dumping stopped by user{RESET}")
        save_to_sdcard_unlimited()
        print(f"{GREEN}✓ Data saved to /sdcard/dump.txt{RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{RED}Error: {e}{RESET}")
        sys.exit(1)
