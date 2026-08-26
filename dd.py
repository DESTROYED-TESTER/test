#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#================[IMPORT MODULE]================#
import unicodedata, urllib.parse, requests, random, sys, uuid, json, hmac, hashlib, time, re, base64, datetime, urllib.request, string, os
from urllib.parse import quote
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as bsp
from rich.console import Console
from rich.panel import Panel
from rich import print as cetak
import threading
from rich.columns import Columns
from rich.progress import Progress, TextColumn, SpinnerColumn
from rich.text import Text
import struct
import pytz
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_v1_5
import urllib.parse
from datetime import datetime
import queue
from collections import deque

# Global variables
Uid, Uuid = [], []
bkas = []
Ok, Cp, Loop = 0, 0, 0
xx = 0
SistemLog = "api.instagram.com"
stop_collection = False
collection_threads = []
username_queue = queue.Queue()
processed_users = set()
active_collectors = 0
collector_lock = threading.Lock()
data_lock = threading.Lock()
max_workers = 5
target_usernames = []

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
    'sec-fetch-site': 'same-origin',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'
}
ua = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 instagram 360.0.0.33.104 (iPhone16,2; iOS 18.2; en_US; en; scale=3.00; 1170x2532; 510000000)'
}
userinfo = 'https://i.instagram.com/api/v1/users/{id!s}/info/'

def Clear():
    try:
        os.system('clear')
    except:
        pass

def parse_cookie_string(cookie_str):
    """Parse cookie string into dictionary format"""
    cookies = {}
    # Remove whitespace
    cookie_str = cookie_str.strip()
    
    # Try to parse as key=value pairs separated by ; or ,
    parts = re.split(r'[;,]', cookie_str)
    for part in parts:
        part = part.strip()
        if '=' in part:
            key, value = part.split('=', 1)
            cookies[key.strip()] = value.strip()
    
    # If no key=value pairs found, try to extract from common formats
    if not cookies:
        # Try to extract sessionid
        session_match = re.search(r'sessionid[=:]\s*([^;\s,]+)', cookie_str)
        if session_match:
            cookies['sessionid'] = session_match.group(1)
        
        # Try to extract ds_user_id
        user_match = re.search(r'ds_user_id[=:]\s*(\d+)', cookie_str)
        if user_match:
            cookies['ds_user_id'] = user_match.group(1)
        
        # Try to extract csrftoken
        csrf_match = re.search(r'csrftoken[=:]\s*([^;\s,]+)', cookie_str)
        if csrf_match:
            cookies['csrftoken'] = csrf_match.group(1)
        
        # Try to extract mid
        mid_match = re.search(r'mid[=:]\s*([^;\s,]+)', cookie_str)
        if mid_match:
            cookies['mid'] = mid_match.group(1)
    
    return cookies

def format_cookie_string(cookies_dict):
    """Convert cookie dictionary back to string format"""
    if isinstance(cookies_dict, dict):
        return '; '.join([f"{k}={v}" for k, v in cookies_dict.items()])
    return str(cookies_dict)

def get_old_cookie_format():
    """Get cookie in old Instagram format (pre-2023)"""
    print(f"\n{YELLOW}📋 Old Cookie Format Instructions:{RESET}")
    print(f"{WHITE}1. Open Instagram in browser{RESET}")
    print(f"{WHITE}2. Open Developer Tools (F12){RESET}")
    print(f"{WHITE}3. Go to Application/Storage → Cookies{RESET}")
    print(f"{WHITE}4. Copy the following values:{RESET}")
    print(f"   {CYAN}- sessionid (required){RESET}")
    print(f"   {CYAN}- ds_user_id (required){RESET}")
    print(f"   {CYAN}- csrftoken (recommended){RESET}")
    print(f"   {CYAN}- mid (optional){RESET}")
    print(f"\n{YELLOW}Example format: sessionid=xxx; ds_user_id=xxx; csrftoken=xxx{RESET}")
    
    cookie_input = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Enter cookie (key=value pairs): {YELLOW}").strip()
    return cookie_input

def get_new_cookie_format():
    """Get cookie in new Instagram format (2023+)"""
    print(f"\n{YELLOW}📋 New Cookie Format Instructions:{RESET}")
    print(f"{WHITE}1. Login to Instagram in browser{RESET}")
    print(f"{WHITE}2. Open Developer Tools (F12){RESET}")
    print(f"{WHITE}3. Go to Application/Storage → Cookies{RESET}")
    print(f"{WHITE}4. Copy the entire cookie string{RESET}")
    print(f"\n{YELLOW}Example format: sessionid=xxx; ds_user_id=xxx; csrftoken=xxx; ...{RESET}")
    print(f"{WHITE}   Or paste the full cookie string from browser{RESET}")
    
    cookie_input = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Enter full cookie string: {YELLOW}").strip()
    return cookie_input

def validate_cookie_old_format(cookie_str):
    """Validate old format cookie (pre-2023)"""
    cookies = parse_cookie_string(cookie_str)
    
    # Check for required fields
    if 'sessionid' not in cookies:
        print(f"{RED}✗ Missing sessionid in cookie{RESET}")
        return False, cookies
    
    if 'ds_user_id' not in cookies:
        print(f"{RED}✗ Missing ds_user_id in cookie{RESET}")
        return False, cookies
    
    # Validate sessionid format (should be numbers)
    if not cookies['sessionid'].isdigit():
        print(f"{RED}✗ Session ID should be numeric{RESET}")
        return False, cookies
    
    # Validate ds_user_id format (should be numbers)
    if not cookies['ds_user_id'].isdigit():
        print(f"{RED}✗ User ID should be numeric{RESET}")
        return False, cookies
    
    return True, cookies

def validate_cookie_new_format(cookie_str):
    """Validate new format cookie (2023+)"""
    cookies = parse_cookie_string(cookie_str)
    
    # Check for required fields
    if 'sessionid' not in cookies:
        print(f"{RED}✗ Missing sessionid in cookie{RESET}")
        return False, cookies
    
    if 'ds_user_id' not in cookies:
        print(f"{RED}✗ Missing ds_user_id in cookie{RESET}")
        return False, cookies
    
    # Session ID can have various formats in new cookies
    session_value = cookies['sessionid']
    if len(session_value) < 10:
        print(f"{RED}✗ Session ID seems too short{RESET}")
        return False, cookies
    
    return True, cookies

def get_cookie_from_browser():
    """Attempt to get cookie from browser's shared data"""
    try:
        print(f"{YELLOW}Attempting to get cookie from browser...{RESET}")
        
        # Try to get from Instagram's shared data
        response = requests.get('https://www.instagram.com/data/shared_data/', timeout=10)
        if response.status_code == 200:
            data = response.json()
            if 'config' in data and 'csrf_token' in data['config']:
                csrf = data['config']['csrf_token']
                print(f"{GREEN}✓ Got csrftoken: {csrf}{RESET}")
                # We still need sessionid and ds_user_id
                print(f"{YELLOW}Please provide sessionid and ds_user_id manually{RESET}")
                
                sessionid = input(f"{WHITE}Enter sessionid: {YELLOW}").strip()
                user_id = input(f"{WHITE}Enter ds_user_id: {YELLOW}").strip()
                
                if sessionid and user_id:
                    cookie_str = f"sessionid={sessionid}; ds_user_id={user_id}; csrftoken={csrf}"
                    return cookie_str
    except Exception as e:
        pass
    
    return None

def get_cookie_from_file():
    """Try to load cookie from various files"""
    cookie_files = ['data/cookie.txt', 'data/OK.txt', 'cookie.txt']
    
    for file_path in cookie_files:
        try:
            if os.path.isfile(file_path):
                with open(file_path, 'r') as f:
                    content = f.read().strip()
                    if content:
                        # Parse the content
                        cookies = parse_cookie_string(content)
                        if 'sessionid' in cookies and 'ds_user_id' in cookies:
                            print(f"{GREEN}✓ Loaded cookie from {file_path}{RESET}")
                            return content
        except:
            pass
    
    return None

def Aset_Ig():
    os.system('clear')
    print(f"{BLUE}═" * 80)
    print(f"{campur} 🍪 INSTAGRAM COOKIE SETUP {RESET}")
    print(f"{BLUE}═" * 80)
    
    # Try to load existing cookie
    existing_cookie = get_cookie_from_file()
    if existing_cookie:
        print(f"{YELLOW}Found existing cookie. Testing...{RESET}")
        cookies = parse_cookie_string(existing_cookie)
        
        # Try to test the cookie
        if test_cookies(cookies):
            print(f"{GREEN}✓ Existing cookie is valid!{RESET}")
            coki = {'cookie': format_cookie_string(cookies)}
            uid_match = re.search('ds_user_id=(\\d+)', coki['cookie'])
            if uid_match:
                uid = uid_match.group(1)
                try:
                    resp = requests.get(
                        f'https://i.instagram.com/api/v1/users/{uid}/info/',
                        headers=ua,
                        cookies=cookies,
                        timeout=10
                    )
                    if resp.status_code == 200:
                        user_data = resp.json().get('user', {})
                        username = user_data.get('username', 'Unknown')
                        full_name = user_data.get('full_name', 'Name Unknown')
                        follower_count = user_data.get('follower_count', 0)
                        print(f"{GREEN}✓ Logged in as: {username}{RESET}")
                        print(f"{WHITE}  Full Name: {CYAN}{full_name}{RESET}")
                        print(f"{WHITE}  Followers: {CYAN}{follower_count}{RESET}")
                        time.sleep(1)
                        return coki, full_name, follower_count
                except:
                    pass
        
        print(f"{YELLOW}Existing cookie is invalid. Please enter a new one.{RESET}")
        time.sleep(1)
    
    # Cookie format selection
    print(f"\n{RED}[ {YELLOW}Select Cookie Format {RED}]\n")
    print(f"{RED}[{WHITE}01{RED}] {CYAN} Old format (pre-2023) - Simple key=value pairs")
    print(f"{RED}[{WHITE}02{RED}] {CYAN} New format (2023+) - Full cookie string")
    print(f"{RED}[{WHITE}03{RED}] {CYAN} Try to get from browser")
    print(f"{RED}[{WHITE}04{RED}] {CYAN} Enter manually")
    print(f"{BLUE}═" * 80)
    
    choice = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Select option: {YELLOW}").strip()
    
    cookie_str = None
    
    if choice in ['01', '1']:
        # Old format
        cookie_str = get_old_cookie_format()
        if cookie_str:
            valid, cookies = validate_cookie_old_format(cookie_str)
            if not valid:
                print(f"{RED}Invalid cookie format. Please try again.{RESET}")
                time.sleep(2)
                return Aset_Ig()
            cookie_str = format_cookie_string(cookies)
            
    elif choice in ['02', '2']:
        # New format
        cookie_str = get_new_cookie_format()
        if cookie_str:
            valid, cookies = validate_cookie_new_format(cookie_str)
            if not valid:
                print(f"{RED}Invalid cookie format. Please try again.{RESET}")
                time.sleep(2)
                return Aset_Ig()
            cookie_str = format_cookie_string(cookies)
            
    elif choice in ['03', '3']:
        # Try browser
        cookie_str = get_cookie_from_browser()
        if not cookie_str:
            print(f"{RED}Failed to get cookie from browser.{RESET}")
            time.sleep(1)
            return Aset_Ig()
            
    elif choice in ['04', '4']:
        # Manual entry
        print(f"\n{YELLOW}Enter cookie manually (any format){RESET}")
        print(f"{WHITE}Examples:{RESET}")
        print(f"  {CYAN}sessionid=123456; ds_user_id=789012; csrftoken=abc123{RESET}")
        print(f"  {CYAN}or just: sessionid=123456; ds_user_id=789012{RESET}")
        cookie_str = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Cookie: {YELLOW}").strip()
        
        if cookie_str:
            cookies = parse_cookie_string(cookie_str)
            if 'sessionid' not in cookies or 'ds_user_id' not in cookies:
                print(f"{RED}Missing required fields (sessionid and ds_user_id){RESET}")
                print(f"{YELLOW}Please try again{RESET}")
                time.sleep(2)
                return Aset_Ig()
            cookie_str = format_cookie_string(cookies)
    else:
        print(f"{RED}Invalid option!{RESET}")
        time.sleep(1)
        return Aset_Ig()
    
    if not cookie_str:
        print(f"{RED}No cookie entered!{RESET}")
        time.sleep(1)
        return Aset_Ig()
    
    # Test the cookie
    cookies = parse_cookie_string(cookie_str)
    coki = {'cookie': cookie_str}
    
    print(f"\n{YELLOW}Testing cookie...{RESET}")
    
    if test_cookies(cookies):
        # Get user info
        uid_match = re.search('ds_user_id=(\\d+)', cookie_str)
        if uid_match:
            uid = uid_match.group(1)
            try:
                resp = requests.get(
                    f'https://i.instagram.com/api/v1/users/{uid}/info/',
                    headers=ua,
                    cookies=cookies,
                    timeout=10
                )
                if resp.status_code == 200:
                    user_data = resp.json().get('user', {})
                    username = user_data.get('username', 'Unknown')
                    full_name = user_data.get('full_name', 'Name Unknown')
                    follower_count = user_data.get('follower_count', 0)
                    
                    # Save cookie
                    if not os.path.exists('data'):
                        os.makedirs('data')
                    with open('data/cookie.txt', 'w') as f:
                        f.write(cookie_str)
                    
                    print(f"\n{GREEN}✓ Successfully logged in as: {username}{RESET}")
                    print(f"{WHITE}  Full Name: {CYAN}{full_name}{RESET}")
                    print(f"{WHITE}  Followers: {CYAN}{follower_count}{RESET}")
                    time.sleep(1)
                    return coki, full_name, follower_count
            except Exception as e:
                print(f"{RED}Error getting user info: {e}{RESET}")
    
    print(f"{RED}✗ Cookie verification failed! Please check your cookie.{RESET}")
    print(f"{YELLOW}Make sure:{RESET}")
    print(f"  • Cookie is from a valid Instagram session")
    print(f"  • You have sessionid and ds_user_id")
    print(f"  • The account is not banned or restricted")
    time.sleep(3)
    return Aset_Ig()

def test_cookies(cookies):
    """Test if cookies are still valid using multiple methods"""
    
    if isinstance(cookies, str):
        cookies = parse_cookie_string(cookies)
    
    # Method 1: Try to get user info using the API
    try:
        uid = cookies.get('ds_user_id')
        if uid:
            response = requests.get(
                f'https://i.instagram.com/api/v1/users/{uid}/info/',
                headers=ua,
                cookies=cookies,
                timeout=10
            )
            if response.status_code == 200:
                data = response.json()
                if 'user' in data and data['user'].get('username'):
                    return True
    except Exception as e:
        pass
    
    # Method 2: Try to access the login ajax endpoint
    try:
        test_session = requests.Session()
        test_session.max_redirects = 3
        response = test_session.get(
            'https://www.instagram.com/api/v1/web/accounts/login/ajax/',
            cookies=cookies,
            timeout=10,
            allow_redirects=False
        )
        
        if response.status_code == 200:
            return True
        elif response.status_code == 302 or response.status_code == 401:
            return False
    except Exception as e:
        pass
    
    # Method 3: Try to get the user's profile page
    try:
        test_session = requests.Session()
        test_session.max_redirects = 3
        response = test_session.get(
            'https://www.instagram.com/',
            cookies=cookies,
            timeout=10,
            allow_redirects=False
        )
        
        if response.status_code == 200:
            if 'login' not in response.text.lower():
                return True
    except Exception as e:
        pass
    
    return False

# ============ SAVE FUNCTIONS ============
def save_to_sdcard():
    """Save collected data to /sdcard/dump.txt"""
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
        return True
        
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
    
    print(f"\n{RED}[ {YELLOW}Main Menu {RED}]\n\n{RED}[{WHITE}01{RED}] {CYAN} Dump followers\n{RED}[{WHITE}02{RED}] {CYAN} Dump following\n{RED}[{WHITE}03{RED}] {CYAN} Load from file\n{RED}[{WHITE}04{RED}] {CYAN} Manage saved data\n{RED}[{WHITE}05{RED}] {CYAN} Chain Collection (Never Stop)\n{RED}[{WHITE}00{RED}] {RED} Delete/Change Cookies")
    print(f"{BLUE}═" * 80)
    x = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Please select a menu option :{YELLOW} ")

    if x in ['01', '1']:
        dumps(aset, True)
    elif x in ['02', '2']:
        dumps(aset, False)
    elif x in ['03', '3']:
        crackfile()
    elif x in ['04', '4']:
        MetodeType()
    elif x in ['05', '5']:
        chain_collection_menu()
    elif x in ['00', '0']:
        if os.path.exists('data/cookie.txt'):
            os.remove('data/cookie.txt')
        prints(f"{GREEN}Successfully deleted cookies")
        exit()
    else:
        print(f"{RED}Invalid option!")
        time.sleep(1)
        Menu()

def dumps(cintil, typess):
    global xx, Uuid
    xx = 0
    
    if not test_cookies(cintil):
        print(f"{YELLOW}Warning: Your cookies may be invalid. Proceeding anyway...")
        time.sleep(1)
    
    xyz = []
    if 'csrftoken' not in str(cintil):
        try:
            memek = requests.get('https://www.instagram.com/data/shared_data/', cookies=cintil, timeout=10)
            memek.raise_for_status()
            token = memek.json()['config']['csrf_token']
            cintil['cookie'] += ';csrftoken=%s;' % token
        except Exception as e:
            os.system('rm -rf data/cookie.txt')
            exit(f'\n{WHITE}[{YELLOW}!{WHITE}] Csrftoken not available, dump will not run: {e}')
    
    prints(panel(f"\n{CYAN}Enter instagram usernames, use commas for mass cracking\nExample: user1,user2,user3", style="Purple"))
    users_input = input(f"{RED}[{WHITE}+{RED}] {BLUE}Username :{YELLOW} ").strip()
    
    if not users_input:
        print(f"{RED}No username entered!")
        return Menu()
    
    users = [u.strip() for u in users_input.split(',') if u.strip()]
    
    print(f"\n{YELLOW}Fetching user IDs...")
    
    try:
        for y in users:
            print(f"{WHITE}Fetching user ID for: {CYAN}{y}")
            
            user_id = get_user_id_methods(y, cintil)
            
            if user_id:
                if user_id not in xyz:
                    xyz.append(user_id)
                    print(f"{GREEN}✓ Found user ID: {user_id} for {y}")
            else:
                print(f"{RED}✗ Could not find user ID for: {y}")
                
            time.sleep(0.5)
                
    except Exception as e:
        print(f"{RED}Error getting user IDs: {e}")
        return Menu()
    
    if not xyz:
        print(f"{RED}No valid user IDs found! Make sure the usernames are correct.")
        time.sleep(2)
        return Menu()
    
    print(f"\n{GREEN}Found {len(xyz)} valid user IDs")
    
    try:
        mode = 'followers' if typess else 'following'
        print(f"\n{YELLOW}Starting to dump {mode}...")
        
        for kintil in xyz:
            print(f"\n{WHITE}Processing user ID: {CYAN}{kintil}")
            if typess:
                Graphql(True, kintil, cintil['cookie'], '')
            else:
                Graphql(False, kintil, cintil['cookie'], '')
                
            time.sleep(1)
            
    except Exception as e:
        print(f"{RED}Error during dump: {e}")
    
    print(f"\n{GREEN}Total users collected: {len(Uuid)}")
    print("")
    
    if len(Uuid) > 0:
        print(f"{GREEN}Collected {len(Uuid)} users successfully!{RESET}")
        time.sleep(1)
        MetodeType()
    else:
        print(f"{RED}No users collected. Check if the target accounts are private or have no {mode}.")
        time.sleep(2)
        Menu()

def Graphql(typess, userid, cokie, after):
    global xx, Uuid
    
    if 'xx' not in globals():
        global xx
        xx = 0
    
    api = "https://www.instagram.com/graphql/query/"
    
    if typess:
        query_hash = "37479f2b8209594dde7facb0d904896a"
    else:
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
        
        print(f"\n{GREEN}Found {len(edges)} {khm.replace('edge_', '')} in this batch")
        
        for xyz in edges:
            username = xyz['node'].get('username', '')
            full_name = xyz['node'].get('full_name', '')
            
            if username:
                xy = username + '|' + full_name
                if xy not in Uuid:
                    xx += 1
                    Uuid.append(xy)
                    print(f'\r{WHITE}Collecting Uid {RED}{len(Uuid)}{WHITE}                            ', end='', flush=True)
                    time.sleep(0.001)
        
        page_info = user_data[khm].get('page_info', {})
        end = page_info.get('has_next_page', False)
        
        if end:
            after = page_info.get('end_cursor', '')
            if after:
                print(f"\n{YELLOW}Loading next page...")
                time.sleep(0.5)
                Graphql(typess, userid, cokie, after)
                
    except requests.exceptions.Timeout:
        print(f"\n{RED}Timeout error while fetching {khm.replace('edge_', '')}")
    except requests.exceptions.TooManyRedirects:
        print(f"\n{RED}Too many redirects - check your cookies")
    except requests.exceptions.RequestException as e:
        print(f"\n{RED}Network error: {e}")
    except json.JSONDecodeError as e:
        print(f"\n{RED}Invalid JSON response: {e}")
    except KeyError as e:
        print(f"\n{RED}Key error: {e} - Check response structure")
    except Exception as e:
        print(f"\n{RED}Unexpected error: {e}")

def get_user_id_methods(username, cookies):
    """Try multiple methods to get user ID"""
    
    # Method 1: Try using the official API
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
    except Exception as e:
        pass
    
    # Method 2: Try using the graphql API
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
    except Exception as e:
        pass
    
    # Method 3: Try scraping with limited redirects
    try:
        session = requests.Session()
        session.max_redirects = 3
        response = session.get(f'https://www.instagram.com/{username}/', cookies=cookies, timeout=10)
        
        if response.status_code == 200:
            patterns = [
                r'"user_id":"(\d+)"',
                r'"profilePage_(\d+)"',
                r'"id":"(\d+)","username":"' + username + '"',
                r'{"id":"(\d+)","username":"' + username + '"',
                r'"id":"(\d+)"[^}]*"username":"' + username + '"'
            ]
            
            for pattern in patterns:
                match = re.search(pattern, response.text)
                if match:
                    return match.group(1)
                    
    except Exception as e:
        pass
    
    return None

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

# ============ CHAIN COLLECTION SYSTEM ============
def collect_followers(user_id, cookies, after='', max_pages=5):
    """Collect followers from a user ID"""
    global Uuid, xx, username_queue, processed_users
    
    api = "https://www.instagram.com/graphql/query/"
    query_hash = "37479f2b8209594dde7facb0d904896a"
    page_count = 0
    collected_count = 0
    
    if isinstance(cookies, dict):
        cookie_str = format_cookie_string(cookies)
    else:
        cookie_str = cookies
    
    while page_count < max_pages:
        variables = {
            "id": user_id,
            "first": 50,
            "after": after
        }
        
        params = {
            'query_hash': query_hash,
            'variables': json.dumps(variables)
        }
        
        try:
            headers = {
                "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15",
                "accept": "application/json",
                "cookie": cookie_str,
                "x-ig-app-id": "1217981644879628"
            }
            
            session = requests.Session()
            session.max_redirects = 5
            req = session.get(api, params=params, headers=headers, timeout=15)
            req.raise_for_status()
            req_json = req.json()
            
            if 'require_login' in req_json:
                print(f'\n{WHITE}[{YELLOW}!{WHITE}] Invalid Cookie - Need to login')
                return False
            
            if 'data' not in req_json or 'user' not in req_json['data']:
                break
            
            user_data = req_json['data']['user']
            if not user_data:
                break
                
            if 'edge_followed_by' not in user_data:
                break
            
            edges = user_data['edge_followed_by'].get('edges', [])
            
            with data_lock:
                for xyz in edges:
                    username = xyz['node'].get('username', '')
                    full_name = xyz['node'].get('full_name', '')
                    
                    if username:
                        xy = username + '|' + full_name
                        if xy not in Uuid:
                            xx += 1
                            Uuid.append(xy)
                            if username not in processed_users:
                                username_queue.put(username)
                                processed_users.add(username)
                            collected_count += 1
            
            page_info = user_data['edge_followed_by'].get('page_info', {})
            if page_info.get('has_next_page', False):
                after = page_info.get('end_cursor', '')
                page_count += 1
                time.sleep(0.1)
            else:
                break
                
        except Exception as e:
            print(f"\n{RED}Error collecting: {e}")
            break
    
    return collected_count

def collect_following(user_id, cookies, after='', max_pages=5):
    """Collect following from a user ID"""
    global Uuid, xx, username_queue, processed_users
    
    api = "https://www.instagram.com/graphql/query/"
    query_hash = "58712303d941c6855d4e888c5f0cd22f"
    page_count = 0
    collected_count = 0
    
    if isinstance(cookies, dict):
        cookie_str = format_cookie_string(cookies)
    else:
        cookie_str = cookies
    
    while page_count < max_pages:
        variables = {
            "id": user_id,
            "first": 50,
            "after": after
        }
        
        params = {
            'query_hash': query_hash,
            'variables': json.dumps(variables)
        }
        
        try:
            headers = {
                "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15",
                "accept": "application/json",
                "cookie": cookie_str,
                "x-ig-app-id": "1217981644879628"
            }
            
            session = requests.Session()
            session.max_redirects = 5
            req = session.get(api, params=params, headers=headers, timeout=15)
            req.raise_for_status()
            req_json = req.json()
            
            if 'require_login' in req_json:
                print(f'\n{WHITE}[{YELLOW}!{WHITE}] Invalid Cookie - Need to login')
                return False
            
            if 'data' not in req_json or 'user' not in req_json['data']:
                break
            
            user_data = req_json['data']['user']
            if not user_data:
                break
                
            if 'edge_follow' not in user_data:
                break
            
            edges = user_data['edge_follow'].get('edges', [])
            
            with data_lock:
                for xyz in edges:
                    username = xyz['node'].get('username', '')
                    full_name = xyz['node'].get('full_name', '')
                    
                    if username:
                        xy = username + '|' + full_name
                        if xy not in Uuid:
                            xx += 1
                            Uuid.append(xy)
                            if username not in processed_users:
                                username_queue.put(username)
                                processed_users.add(username)
                            collected_count += 1
            
            page_info = user_data['edge_follow'].get('page_info', {})
            if page_info.get('has_next_page', False):
                after = page_info.get('end_cursor', '')
                page_count += 1
                time.sleep(0.1)
            else:
                break
                
        except Exception as e:
            print(f"\n{RED}Error collecting: {e}")
            break
    
    return collected_count

def collector_worker(cookies, mode='followers', max_pages=3):
    """Worker thread that continuously processes usernames from queue"""
    global active_collectors, stop_collection
    
    with collector_lock:
        active_collectors += 1
    
    print(f"{GREEN}✅ Collector worker started. Mode: {mode}{RESET}")
    
    while not stop_collection:
        try:
            username = username_queue.get(timeout=2)
        except queue.Empty:
            if username_queue.empty() and active_collectors <= 1:
                if Uuid:
                    random_usernames = []
                    with data_lock:
                        for i in range(min(10, len(Uuid))):
                            user_data = Uuid[random.randint(0, len(Uuid)-1)]
                            username_part = user_data.split('|')[0]
                            if username_part not in processed_users:
                                random_usernames.append(username_part)
                                processed_users.add(username_part)
                    
                    for uname in random_usernames:
                        username_queue.put(uname)
                    print(f"{YELLOW}🔄 Added {len(random_usernames)} random usernames to queue{RESET}")
                    continue
            continue
        
        user_id = get_user_id_methods(username, cookies)
        if not user_id:
            with data_lock:
                if username in processed_users:
                    processed_users.remove(username)
            continue
        
        try:
            if mode == 'followers':
                collected = collect_followers(user_id, cookies, max_pages=max_pages)
            else:
                collected = collect_following(user_id, cookies, max_pages=max_pages)
            
            if collected > 0:
                print(f"{GREEN}📊 Collected {collected} users from @{username}{RESET}")
            
        except Exception as e:
            print(f"{RED}Error processing @{username}: {e}{RESET}")
    
    with collector_lock:
        active_collectors -= 1
    
    print(f"{YELLOW}⏹️ Collector worker stopped{RESET}")

def start_chain_collection(cookies, initial_usernames, mode='followers', max_workers=5, max_pages=5):
    """Start the chain collection system"""
    global stop_collection, active_collectors, processed_users
    
    stop_collection = False
    active_collectors = 0
    processed_users = set()
    
    while not username_queue.empty():
        try:
            username_queue.get_nowait()
        except:
            break
    
    for username in initial_usernames:
        if username not in processed_users:
            username_queue.put(username)
            processed_users.add(username)
    
    print(f"\n{GREEN}🚀 Starting chain collection system...{RESET}")
    print(f"{WHITE}📝 Initial usernames: {', '.join(initial_usernames)}{RESET}")
    print(f"{WHITE}🔧 Mode: {mode.upper()}{RESET}")
    print(f"{WHITE}👥 Workers: {max_workers}{RESET}")
    print(f"{WHITE}📄 Pages per user: {max_pages}{RESET}")
    print(f"{BLUE}═" * 80)
    
    workers = []
    for i in range(max_workers):
        worker = threading.Thread(
            target=collector_worker, 
            args=(cookies, mode, max_pages),
            daemon=True
        )
        worker.start()
        workers.append(worker)
        time.sleep(0.2)
    
    return workers

def stop_collection_system():
    """Stop all collection threads"""
    global stop_collection
    print(f"\n{YELLOW}⏹️ Stopping collection system...{RESET}")
    stop_collection = True
    
    timeout = 10
    while active_collectors > 0 and timeout > 0:
        time.sleep(1)
        timeout -= 1
    
    print(f"{GREEN}✅ Collection system stopped{RESET}")
    return len(Uuid)

def chain_collection_menu():
    """Main menu for chain collection"""
    global stop_collection, max_workers
    
    workers = []
    is_running = False
    cookies, _, _ = Aset_Ig()
    
    while True:
        os.system('clear')
        print(f"{BLUE}═" * 80)
        print(f"{campur} 🚀 CHAIN DATA COLLECTION SYSTEM - NEVER STOP{RESET}")
        print(f"{BLUE}═" * 80)
        
        if is_running:
            print(f"{WHITE}📊 Currently RUNNING{RESET}")
            print(f"{WHITE}Total users: {GREEN}{len(Uuid)}{RESET}")
            print(f"{WHITE}Queue size: {GREEN}{username_queue.qsize()}{RESET}")
            print(f"{WHITE}Active workers: {GREEN}{active_collectors}{RESET}")
        else:
            print(f"{WHITE}📊 Currently NOT collecting{RESET}")
            print(f"{WHITE}Users in database: {GREEN}{len(Uuid)}{RESET}")
        
        print(f"\n{RED}[ {YELLOW}Chain Collection Menu {RED}]\n")
        print(f"{RED}[{WHITE}01{RED}] {CYAN} Start chain collection (never stops)")
        print(f"{RED}[{WHITE}02{RED}] {CYAN} Start with custom initial usernames")
        print(f"{RED}[{WHITE}03{RED}] {CYAN} Change collection mode (followers/following)")
        print(f"{RED}[{WHITE}04{RED}] {CYAN} Change worker count (currently: {max_workers})")
        print(f"{RED}[{WHITE}05{RED}] {CYAN} Show current stats")
        print(f"{RED}[{WHITE}06{RED}] {CYAN} Save collected data")
        print(f"{RED}[{WHITE}07{RED}] {CYAN} Load data from file")
        print(f"{RED}[{WHITE}08{RED}] {RED} Stop collection (if running)")
        print(f"{RED}[{WHITE}09{RED}] {CYAN} View collected users")
        print(f"{RED}[{WHITE}10{RED}] {CYAN} Clear all data")
        print(f"{RED}[{WHITE}00{RED}] {RED} Return to main menu")
        print(f"{BLUE}═" * 80)
        
        choice = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Select option :{YELLOW} ").strip()
        
        if choice in ['01', '1']:
            if not cookies:
                cookies, _, _ = Aset_Ig()
            
            initial_usernames = ['instagram', 'facebook', 'tiktok', 'youtube', 'twitter', 'snapchat']
            
            if is_running:
                print(f"{YELLOW}Collection is already running!{RESET}")
                time.sleep(1)
                continue
            
            workers = start_chain_collection(
                cookies, 
                initial_usernames, 
                mode='followers', 
                max_workers=max_workers,
                max_pages=5
            )
            is_running = True
            print(f"{GREEN}✅ Collection started!{RESET}")
            input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Press Enter to continue...{RESET}")
            
        elif choice in ['02', '2']:
            if not cookies:
                cookies, _, _ = Aset_Ig()
            
            usernames_input = input(f"{WHITE}Enter initial usernames (comma separated): {YELLOW}").strip()
            initial_usernames = [u.strip() for u in usernames_input.split(',') if u.strip()]
            
            if not initial_usernames:
                print(f"{RED}No usernames entered!{RESET}")
                time.sleep(1)
                continue
            
            if is_running:
                print(f"{YELLOW}Stopping current collection...{RESET}")
                stop_collection_system()
                is_running = False
            
            workers = start_chain_collection(
                cookies, 
                initial_usernames, 
                mode='followers', 
                max_workers=max_workers,
                max_pages=5
            )
            is_running = True
            print(f"{GREEN}✅ Collection started with custom usernames!{RESET}")
            input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Press Enter to continue...{RESET}")
            
        elif choice in ['03', '3']:
            if is_running:
                print(f"{RED}Cannot change mode while running. Stop collection first.{RESET}")
                time.sleep(1)
                continue
            
            mode_input = input(f"{WHITE}Set default mode (f)ollowers or (following): {YELLOW}").strip().lower()
            mode = 'followers' if mode_input in ['f', 'followers', ''] else 'following'
            print(f"{GREEN}✅ Mode set to: {mode}{RESET}")
            time.sleep(1)
            
        elif choice in ['04', '4']:
            try:
                new_workers = int(input(f"{WHITE}Enter number of workers (1-20): {YELLOW}").strip())
                if 1 <= new_workers <= 20:
                    max_workers = new_workers
                    print(f"{GREEN}✅ Worker count updated to: {max_workers}{RESET}")
                    
                    if is_running:
                        print(f"{YELLOW}⚠️ Workers will be updated on next start{RESET}")
                else:
                    print(f"{RED}Please enter a number between 1 and 20{RESET}")
            except:
                print(f"{RED}Invalid input!{RESET}")
            time.sleep(1)
            
        elif choice in ['05', '5']:
            if is_running:
                print(f"\n{BLUE}═" * 80)
                print(f"{YELLOW}📊 CURRENT STATS{RESET}")
                print(f"{BLUE}═" * 80)
                print(f"{WHITE}Total users: {GREEN}{len(Uuid)}{RESET}")
                print(f"{WHITE}Queue size: {GREEN}{username_queue.qsize()}{RESET}")
                print(f"{WHITE}Active workers: {GREEN}{active_collectors}{RESET}")
                print(f"{WHITE}Processed users: {GREEN}{len(processed_users)}{RESET}")
                print(f"{BLUE}═" * 80)
            else:
                print(f"{WHITE}Total collected: {GREEN}{len(Uuid)}{RESET}")
            input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Press Enter to continue...{RESET}")
            
        elif choice in ['06', '6']:
            if len(Uuid) == 0:
                print(f"{RED}No data to save!{RESET}")
                time.sleep(1)
                continue
            
            filename = input(f"{WHITE}Enter filename (default: collected_data.txt): {YELLOW}").strip()
            if not filename:
                filename = "collected_data.txt"
            if not filename.endswith('.txt'):
                filename += '.txt'
            
            save_to_custom(filename)
            input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Press Enter to continue...{RESET}")
            
        elif choice in ['07', '7']:
            filename = input(f"{WHITE}Enter filename to load: {YELLOW}").strip()
            if not filename:
                print(f"{RED}No filename entered!{RESET}")
                time.sleep(1)
                continue
            
            if not os.path.exists(filename) and not os.path.exists(f'data/{filename}'):
                print(f"{RED}File not found: {filename}{RESET}")
                time.sleep(1)
                continue
            
            try:
                if os.path.exists(filename):
                    with open(filename, 'r') as f:
                        lines = f.read().splitlines()
                else:
                    with open(f'data/{filename}', 'r') as f:
                        lines = f.read().splitlines()
                
                with data_lock:
                    for line in lines:
                        if line and line not in Uuid:
                            Uuid.append(line)
                            username = line.split('|')[0]
                            if username not in processed_users:
                                username_queue.put(username)
                                processed_users.add(username)
                
                print(f"{GREEN}✅ Loaded {len(lines)} users from file{RESET}")
            except Exception as e:
                print(f"{RED}Error loading file: {e}{RESET}")
            
            input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Press Enter to continue...{RESET}")
            
        elif choice in ['08', '8']:
            if is_running:
                total = stop_collection_system()
                is_running = False
                print(f"{WHITE}Total collected: {GREEN}{total}{RESET}")
            else:
                print(f"{YELLOW}Collection is not running{RESET}")
            time.sleep(1)
            
        elif choice in ['09', '9']:
            if len(Uuid) == 0:
                print(f"{RED}No users collected yet!{RESET}")
                time.sleep(1)
                continue
            
            print(f"\n{YELLOW}RECENTLY COLLECTED USERS:{RESET}")
            with data_lock:
                show_count = min(20, len(Uuid))
                for i in range(-show_count, 0):
                    user_data = Uuid[i]
                    parts = user_data.split('|')
                    username = parts[0]
                    fullname = parts[1] if len(parts) > 1 else 'N/A'
                    print(f"  {WHITE}{i+show_count+1:3}. {GREEN}{username:<20}{RESET} | {CYAN}{fullname}{RESET}")
            
            if len(Uuid) > 20:
                print(f"\n{YELLOW}... and {len(Uuid)-20} more users{RESET}")
            
            print(f"\n{WHITE}Total users: {GREEN}{len(Uuid)}{RESET}")
            input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Press Enter to continue...{RESET}")
            
        elif choice in ['10', '10']:
            confirm = input(f"{RED}Are you sure you want to clear all collected data? (y/n): {YELLOW}").strip().lower()
            if confirm == 'y':
                with data_lock:
                    Uuid.clear()
                    processed_users.clear()
                while not username_queue.empty():
                    try:
                        username_queue.get_nowait()
                    except:
                        break
                print(f"{GREEN}✅ All data cleared!{RESET}")
            time.sleep(1)
            
        elif choice in ['00', '0']:
            if is_running:
                stop_collection_system()
            Menu()
            return
            
        else:
            print(f"{RED}Invalid option!{RESET}")
            time.sleep(1)

# Main execution
if __name__ == "__main__":
    if not os.path.exists('data'):
        os.makedirs('data')
    
    try:
        Menu()
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Exiting...{RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{RED}An error occurred: {e}{RESET}")
        sys.exit(1)
