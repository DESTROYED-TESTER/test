#================[IMPORT MODULE]================#
import unicodedata, urllib.parse, requests, random, sys, uuid, json, hmac, hashlib, time, re, base64, datetime, urllib.request, string, os
from urllib.parse import quote
from concurrent.futures import ThreadPoolExecutor, as_completed
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
max_workers = 5  # Number of concurrent collection threads
target_usernames = []  # Initial usernames to start with

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

def Clear():
    try:
        os.system('clear')
    except:
        pass

def test_cookies(coki):
    """Test if cookies are still valid"""
    try:
        uid_match = re.search('ds_user_id=(\\d+)', str(coki.get('cookie', '')))
        if uid_match:
            uid = uid_match.group(1)
            response = requests.get(
                f'https://i.instagram.com/api/v1/users/{uid}/info/',
                headers={'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15'},
                cookies=coki,
                timeout=10
            )
            if response.status_code == 200:
                data = response.json()
                if 'user' in data:
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
    
    return True

def Aset_Ig():
    """Setup Instagram cookies"""
    os.system('clear')
    coki = {}
    
    if os.path.isfile('data/cookie.txt'):
        cookie_str = open('data/cookie.txt', 'r').read().strip()
        if cookie_str:
            coki = {'cookie': cookie_str}
            if not validate_cookie_format(cookie_str):
                print(f"{RED}Cookie format is invalid, please re-enter.{RESET}")
                time.sleep(2)
                os.remove('data/cookie.txt')
                coki = {}
    
    if not coki:
        print(f"{RED}[{WHITE}+{RED}] {CYAN}Please enter your instagram account cookie.")
        cookie_input = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Cookie :{YELLOW} ").strip()
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
            headers={'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15'},
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

def get_user_id(username, cookies):
    """Get user ID from username"""
    try:
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
    except:
        pass
    
    # Fallback method
    try:
        session = requests.Session()
        session.max_redirects = 3
        response = session.get(f'https://www.instagram.com/{username}/', cookies=cookies, timeout=10)
        
        if response.status_code == 200:
            patterns = [
                r'"user_id":"(\d+)"',
                r'"profilePage_(\d+)"',
                r'"id":"(\d+)","username":"' + username + '"'
            ]
            
            for pattern in patterns:
                match = re.search(pattern, response.text)
                if match:
                    return match.group(1)
    except:
        pass
    
    return None

def collect_followers(user_id, cookies, after='', max_pages=10):
    """Collect followers from a user ID - optimized for speed"""
    global Uuid, xx
    
    api = "https://www.instagram.com/graphql/query/"
    query_hash = "37479f2b8209594dde7facb0d904896a"
    page_count = 0
    collected_count = 0
    
    while page_count < max_pages:
        variables = {
            "id": user_id,
            "first": 100,
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
                "cookie": cookies,
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
                            # Add to queue for processing
                            if username not in processed_users:
                                username_queue.put(username)
                                processed_users.add(username)
                            collected_count += 1
            
            # Check for next page
            page_info = user_data['edge_followed_by'].get('page_info', {})
            if page_info.get('has_next_page', False):
                after = page_info.get('end_cursor', '')
                page_count += 1
                time.sleep(0.1)  # Minimal delay
            else:
                break
                
        except Exception as e:
            print(f"\n{RED}Error collecting: {e}")
            break
    
    return collected_count

def collect_following(user_id, cookies, after='', max_pages=10):
    """Collect following from a user ID"""
    global Uuid, xx
    
    api = "https://www.instagram.com/graphql/query/"
    query_hash = "58712303d941c6855d4e888c5f0cd22f"
    page_count = 0
    collected_count = 0
    
    while page_count < max_pages:
        variables = {
            "id": user_id,
            "first": 100,
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
                "cookie": cookies,
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
            # Get username from queue (with timeout)
            username = username_queue.get(timeout=2)
        except queue.Empty:
            # Check if there are any active collectors and if queue is empty
            if username_queue.empty() and active_collectors <= 1:
                # Add some random seed usernames to keep going
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
                    print(f"{YELLOW}🔄 Added {len(random_usernames)} random usernames to queue from existing data{RESET}")
                    continue
            continue
        
        if username in processed_users:
            # Actually, we should process it anyway since we might want to collect from it
            pass
        
        # Get user ID
        user_id = get_user_id(username, cookies)
        if not user_id:
            with data_lock:
                if username in processed_users:
                    processed_users.remove(username)
            continue
        
        # Collect data from this user
        try:
            if mode == 'followers':
                collected = collect_followers(user_id, cookies['cookie'], max_pages=max_pages)
            else:
                collected = collect_following(user_id, cookies['cookie'], max_pages=max_pages)
            
            if collected > 0:
                print(f"{GREEN}📊 Collected {collected} users from @{username}{RESET}")
            
        except Exception as e:
            print(f"{RED}Error processing @{username}: {e}{RESET}")
    
    with collector_lock:
        active_collectors -= 1
    
    print(f"{YELLOW}⏹️ Collector worker stopped{RESET}")

def start_chain_collection(cookies, initial_usernames, mode='followers', max_workers=5, max_pages=5):
    """Start the chain collection system"""
    global stop_collection, active_collectors, processed_users, target_usernames
    
    stop_collection = False
    active_collectors = 0
    processed_users = set()
    target_usernames = initial_usernames.copy()
    
    # Clear queue and add initial usernames
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
    print(f"{WHITE}🔄 Chain: Yes (auto-discover new users){RESET}")
    print(f"{BLUE}═" * 80)
    
    # Start worker threads
    workers = []
    for i in range(max_workers):
        worker = threading.Thread(
            target=collector_worker, 
            args=(cookies, mode, max_pages),
            daemon=True
        )
        worker.start()
        workers.append(worker)
        time.sleep(0.2)  # Stagger start
    
    return workers

def display_stats():
    """Display current collection stats"""
    print(f"\n{BLUE}═" * 80)
    print(f"{YELLOW}📊 COLLECTION STATS{RESET}")
    print(f"{BLUE}═" * 80)
    print(f"{WHITE}Total users collected: {GREEN}{len(Uuid)}{RESET}")
    print(f"{WHITE}Queue size: {GREEN}{username_queue.qsize()}{RESET}")
    print(f"{WHITE}Active workers: {GREEN}{active_collectors}{RESET}")
    print(f"{WHITE}Processed users: {GREEN}{len(processed_users)}{RESET}")
    
    # Show some sample usernames from the queue
    sample_usernames = []
    temp_queue = []
    
    try:
        for _ in range(min(5, username_queue.qsize())):
            item = username_queue.get_nowait()
            if item:
                sample_usernames.append(item)
                temp_queue.append(item)
        for item in temp_queue:
            username_queue.put(item)
    except:
        pass
    
    if sample_usernames:
        print(f"{WHITE}Next in queue: {GREEN}{', '.join(sample_usernames)}{RESET}")
    
    print(f"{BLUE}═" * 80)
    return len(Uuid)

def save_data_to_file(filename="collected_data.txt"):
    """Save collected data to file"""
    try:
        with data_lock:
            with open(filename, 'w', encoding='utf-8') as f:
                for item in Uuid:
                    f.write(item + '\n')
        print(f"{GREEN}✅ Data saved to {filename} ({len(Uuid)} users){RESET}")
        return True
    except Exception as e:
        print(f"{RED}Error saving data: {e}{RESET}")
        return False

def load_data_from_file(filename):
    """Load data from file and add to queue"""
    global Uuid
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
        
        added = 0
        with data_lock:
            for line in lines:
                if line and line not in Uuid:
                    Uuid.append(line)
                    username = line.split('|')[0]
                    if username not in processed_users:
                        username_queue.put(username)
                        processed_users.add(username)
                    added += 1
        
        print(f"{GREEN}✅ Loaded {added} users from {filename}{RESET}")
        return added
    except Exception as e:
        print(f"{RED}Error loading data: {e}{RESET}")
        return 0

def stop_collection_system():
    """Stop all collection threads"""
    global stop_collection
    print(f"\n{YELLOW}⏹️ Stopping collection system...{RESET}")
    stop_collection = True
    
    # Wait for workers to finish
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
            display_stats()
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
        print(f"{RED}[{WHITE}00{RED}] {RED} Exit")
        print(f"{BLUE}═" * 80)
        
        choice = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Select option :{YELLOW} ").strip()
        
        if choice in ['01', '1']:
            if not cookies:
                cookies, _, _ = Aset_Ig()
            
            initial_usernames = ['instagram', 'facebook', 'tiktok', 'youtube']
            
            if is_running:
                print(f"{YELLOW}Collection is already running!{RESET}")
                time.sleep(1)
                continue
            
            # Get mode preference
            mode_input = input(f"{WHITE}Collect (f)ollowers or (following)? [f/following]: {YELLOW}").strip().lower()
            mode = 'followers' if mode_input in ['f', 'followers', ''] else 'following'
            
            workers = start_chain_collection(
                cookies, 
                initial_usernames, 
                mode=mode, 
                max_workers=max_workers,
                max_pages=5
            )
            is_running = True
            print(f"{GREEN}✅ Collection started! Press any key to continue{RESET}")
            input()
            
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
            
            # Get mode preference
            mode_input = input(f"{WHITE}Collect (f)ollowers or (following)? [f/following]: {YELLOW}").strip().lower()
            mode = 'followers' if mode_input in ['f', 'followers', ''] else 'following'
            
            workers = start_chain_collection(
                cookies, 
                initial_usernames, 
                mode=mode, 
                max_workers=max_workers,
                max_pages=5
            )
            is_running = True
            print(f"{GREEN}✅ Collection started with custom usernames!{RESET}")
            input()
            
        elif choice in ['03', '3']:
            if is_running:
                print(f"{RED}Cannot change mode while running. Stop collection first.{RESET}")
                time.sleep(1)
                continue
            
            mode_input = input(f"{WHITE}Set default mode (f)ollowers or (following): {YELLOW}").strip().lower()
            mode = 'followers' if mode_input in ['f', 'followers', ''] else 'following'
            # Save mode preference
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
                display_stats()
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
            
            save_data_to_file(filename)
            input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Press Enter to continue...{RESET}")
            
        elif choice in ['07', '7']:
            filename = input(f"{WHITE}Enter filename to load: {YELLOW}").strip()
            if not filename:
                print(f"{RED}No filename entered!{RESET}")
                time.sleep(1)
                continue
            
            if not os.path.exists(filename):
                print(f"{RED}File not found: {filename}{RESET}")
                time.sleep(1)
                continue
            
            loaded = load_data_from_file(filename)
            if loaded > 0 and not is_running:
                # Start collecting from loaded data
                if cookies:
                    mode_input = input(f"{WHITE}Start collecting from loaded data? (y/n): {YELLOW}").strip().lower()
                    if mode_input == 'y':
                        mode_choice = input(f"{WHITE}Collect (f)ollowers or (following)? [f/following]: {YELLOW}").strip().lower()
                        mode = 'followers' if mode_choice in ['f', 'followers', ''] else 'following'
                        workers = start_chain_collection(
                            cookies, 
                            [],  # Empty initial - will use queue from loaded data
                            mode=mode, 
                            max_workers=max_workers,
                            max_pages=5
                        )
                        is_running = True
                        print(f"{GREEN}✅ Collection started from loaded data!{RESET}")
            
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
                # Also clear queue
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
            print(f"{GREEN}Exiting...{RESET}")
            sys.exit(0)
            
        else:
            print(f"{RED}Invalid option!{RESET}")
            time.sleep(1)

# Main execution
if __name__ == "__main__":
    # Create data directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')
    
    try:
        chain_collection_menu()
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Exiting...{RESET}")
        if 'stop_collection' in globals():
            stop_collection = True
        sys.exit(0)
    except Exception as e:
        print(f"\n{RED}An error occurred: {e}{RESET}")
        sys.exit(1)
