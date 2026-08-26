#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Instagram Data Dumper v3.0 - NON-STOP DUMP
- Auto-retry on failure
- Multi-target support with priority queue
- Continuous operation mode
- Auto-save every 100 users
- Resume from last checkpoint
- Rate limit handling with exponential backoff
"""

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
from rich.progress import Progress, TextColumn, SpinnerColumn, BarColumn
from rich.text import Text
import struct
import pytz
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_v1_5
from rich import print as Cetak
from rich.tree import Tree
import urllib.parse
from datetime import datetime
import concurrent.futures
from collections import deque
import signal
import pickle

# Global variables
Uid, Uuid = [], []
bkas = []
Ok, Cp, Loop = 0, 0, 0
xx = 0
SistemLog = "api.instagram.com"
MAX_RETRIES = 5
REQUEST_DELAY = 2.0  # Base delay between requests
DUMP_COUNT = 0
LAST_SAVE = 0
AUTO_SAVE_INTERVAL = 100  # Save every 100 users
RUNNING = True
TARGET_QUEUE = deque()
PROCESSED_TARGETS = set()
FAILED_TARGETS = deque()
CHECKPOINT_FILE = 'data/checkpoint.pkl'
TARGET_FILE = 'data/targets.txt'

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

# ============ SIGNAL HANDLER ============
def signal_handler(sig, frame):
    global RUNNING
    print(f"\n{YELLOW}Received interrupt signal. Saving checkpoint...{RESET}")
    RUNNING = False
    save_checkpoint()
    save_to_sdcard()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# ============ CHECKPOINT FUNCTIONS ============
def save_checkpoint():
    """Save current progress to checkpoint file"""
    try:
        checkpoint = {
            'Uuid': Uuid,
            'DUMP_COUNT': DUMP_COUNT,
            'PROCESSED_TARGETS': PROCESSED_TARGETS,
            'FAILED_TARGETS': FAILED_TARGETS,
            'timestamp': datetime.now().isoformat()
        }
        with open(CHECKPOINT_FILE, 'wb') as f:
            pickle.dump(checkpoint, f)
        print(f"{GREEN}✓ Checkpoint saved: {len(Uuid)} users{RESET}")
        return True
    except Exception as e:
        print(f"{RED}✗ Failed to save checkpoint: {e}{RESET}")
        return False

def load_checkpoint():
    """Load checkpoint if exists"""
    global Uuid, DUMP_COUNT, PROCESSED_TARGETS, FAILED_TARGETS
    try:
        if os.path.exists(CHECKPOINT_FILE):
            with open(CHECKPOINT_FILE, 'rb') as f:
                checkpoint = pickle.load(f)
            Uuid = checkpoint.get('Uuid', [])
            DUMP_COUNT = checkpoint.get('DUMP_COUNT', 0)
            PROCESSED_TARGETS = checkpoint.get('PROCESSED_TARGETS', set())
            FAILED_TARGETS = deque(checkpoint.get('FAILED_TARGETS', []))
            print(f"{GREEN}✓ Checkpoint loaded: {len(Uuid)} users{RESET}")
            return True
    except Exception as e:
        print(f"{RED}✗ Failed to load checkpoint: {e}{RESET}")
    return False

# ============ AUTO SAVE ============
def auto_save():
    """Auto-save if interval reached"""
    global LAST_SAVE, DUMP_COUNT
    if DUMP_COUNT - LAST_SAVE >= AUTO_SAVE_INTERVAL:
        save_checkpoint()
        save_to_sdcard()
        LAST_SAVE = DUMP_COUNT

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
            f.write("# Instagram Users Dump - Non-Stop Mode\n")
            f.write(f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"# Total: {len(Uuid)}\n")
            f.write("# Format: username|full_name\n")
            f.write("#" + "="*50 + "\n\n")
            
            for item in Uuid:
                f.write(item + '\n')
        
        print(f"\n{GREEN}✓ Auto-saved {len(Uuid)} users to /sdcard/dump.txt{RESET}")
        return True
        
    except Exception as e:
        print(f"{RED}✗ Failed to auto-save: {e}{RESET}")
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
            f.write(f"# Instagram Users Dump - Non-Stop Mode\n")
            f.write(f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"# Total: {len(Uuid)}\n")
            f.write("#" + "="*50 + "\n\n")
            for item in Uuid:
                f.write(item + '\n')
        
        print(f"\n{GREEN}✓ Saved {len(Uuid)} users to data/{filename}{RESET}")
        return True
        
    except Exception as e:
        print(f"{RED}✗ Failed to save: {e}{RESET}")
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

# ============ COOKIE FUNCTIONS ============
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
        print(f"{RED}[{WHITE}+{RED}] {CYAN}Please enter your instagram account cookie.")
        print(f"{YELLOW}Cookie should contain: sessionid, ds_user_id, csrftoken{RESET}")
        cookie_input = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Cookie :{YELLOW} ").strip()
        
        if cookie_input.lower() == 'res':
            cookie_str = find_res()
            if not cookie_str:
                print(f"{RED}Failed to load backup cookie, please enter manually.{RESET}")
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

# ============ GRAPHQL FUNCTIONS ============
def Graphql(typess, userid, cokie, after, target_username=""):
    """Fetch followers or following using GraphQL API with retry"""
    global xx, Uuid, DUMP_COUNT
    
    if 'xx' not in globals():
        global xx
        xx = 0
    
    api = "https://www.instagram.com/graphql/query/"
    
    if typess:
        query_hash = "37479f2b8209594dde7facb0d904896a"  # Followers
    else:
        query_hash = "58712303d941c6855d4e888c5f0cd22f"  # Following
    
    variables = {
        "id": userid,
        "first": 50,
        "after": after
    }
    
    params = {
        'query_hash': query_hash,
        'variables': json.dumps(variables)
    }
    
    for attempt in range(MAX_RETRIES):
        if not RUNNING:
            return
        
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
                if not RUNNING:
                    return
                
                username = xyz['node'].get('username', '')
                full_name = xyz['node'].get('full_name', '')
                
                if username:
                    xy = username + '|' + full_name
                    if xy not in Uuid:
                        xx += 1
                        DUMP_COUNT += 1
                        Uuid.append(xy)
                        print(f'\r{WHITE}Total Collected: {RED}{len(Uuid)}{WHITE} | Current: {CYAN}{username}{WHITE}                    ', end='', flush=True)
                        time.sleep(0.05)
                        
                        # Auto-save checkpoint
                        auto_save()
            
            page_info = user_data[khm].get('page_info', {})
            end = page_info.get('has_next_page', False)
            
            if end and RUNNING:
                after = page_info.get('end_cursor', '')
                if after:
                    print(f"\n{YELLOW}Loading next page...{RESET}")
                    time.sleep(REQUEST_DELAY)
                    Graphql(typess, userid, cokie, after, target_username)
            break
            
        except requests.exceptions.Timeout:
            print(f"\n{RED}Timeout error, attempt {attempt+1}/{MAX_RETRIES}")
            time.sleep(2 ** attempt)
        except requests.exceptions.TooManyRedirects:
            print(f"\n{RED}Too many redirects - check your cookies")
            break
        except requests.exceptions.RequestException as e:
            print(f"\n{RED}Network error, attempt {attempt+1}/{MAX_RETRIES}: {e}")
            time.sleep(2 ** attempt)
        except json.JSONDecodeError as e:
            print(f"\n{RED}Invalid JSON response, attempt {attempt+1}/{MAX_RETRIES}")
            time.sleep(2 ** attempt)
        except Exception as e:
            print(f"\n{RED}Unexpected error, attempt {attempt+1}/{MAX_RETRIES}: {e}")
            time.sleep(2 ** attempt)

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
    except Exception as e:
        pass
    
    # Method 2: GraphQL query
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
    
    # Method 3: Scrape page source
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
    except Exception as e:
        pass
    
    return None

# ============ NON-STOP DUMP FUNCTIONS ============
def load_targets_from_file():
    """Load targets from file"""
    targets = []
    try:
        if os.path.exists(TARGET_FILE):
            with open(TARGET_FILE, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        targets.append(line)
    except Exception as e:
        print(f"{RED}Error loading targets: {e}{RESET}")
    return targets

def save_targets_to_file(targets):
    """Save targets to file"""
    try:
        with open(TARGET_FILE, 'w') as f:
            f.write("# Instagram Targets - Non-Stop Dump\n")
            f.write(f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("#" + "="*50 + "\n\n")
            for target in targets:
                f.write(target + '\n')
        return True
    except Exception as e:
        print(f"{RED}Error saving targets: {e}{RESET}")
        return False

def add_targets_interactive():
    """Interactive target addition"""
    print(f"\n{CYAN}Enter instagram usernames to dump (comma separated)")
    print(f"Example: user1,user2,user3,user4")
    users_input = input(f"{RED}[{WHITE}+{RED}] {BLUE}Usernames :{YELLOW} ").strip()
    
    if not users_input:
        return []
    
    users = [u.strip() for u in users_input.split(',') if u.strip()]
    return users

def nonstop_dump_mode(cintil, typess):
    """Non-stop dumping mode with auto-retry and continuous operation"""
    global RUNNING, Uuid, DUMP_COUNT, TARGET_QUEUE, PROCESSED_TARGETS, FAILED_TARGETS
    
    print(f"\n{YELLOW}╔{'═'*78}╗{RESET}")
    print(f"{YELLOW}║{RESET} {GREEN}★ NON-STOP DUMP MODE ACTIVE ★{RESET} {' ' * 40}{YELLOW}║{RESET}")
    print(f"{YELLOW}╚{'═'*78}╝{RESET}")
    
    mode = 'followers' if typess else 'following'
    print(f"{WHITE}Mode: {CYAN}{mode.upper()}{RESET}")
    print(f"{WHITE}Press Ctrl+C to stop and save{RESET}")
    print(f"{WHITE}Auto-save every {AUTO_SAVE_INTERVAL} users{RESET}\n")
    
    # Load existing targets
    existing_targets = load_targets_from_file()
    if existing_targets:
        print(f"{GREEN}Loaded {len(existing_targets)} targets from file{RESET}")
        for target in existing_targets:
            if target not in PROCESSED_TARGETS:
                TARGET_QUEUE.append(target)
    
    # Load checkpoint
    load_checkpoint()
    
    # Main loop
    while RUNNING:
        # Check if we need more targets
        if len(TARGET_QUEUE) == 0:
            print(f"\n{YELLOW}No more targets in queue. Add new targets:{RESET}")
            new_targets = add_targets_interactive()
            if new_targets:
                for target in new_targets:
                    if target not in PROCESSED_TARGETS and target not in TARGET_QUEUE:
                        TARGET_QUEUE.append(target)
                save_targets_to_file(list(TARGET_QUEUE))
            else:
                print(f"{YELLOW}No targets added. Waiting 10 seconds...{RESET}")
                time.sleep(10)
                continue
        
        # Process next target
        if TARGET_QUEUE:
            target = TARGET_QUEUE.popleft()
            
            if target in PROCESSED_TARGETS:
                continue
            
            print(f"\n{WHITE}┌{'─'*78}┐{RESET}")
            print(f"{WHITE}│{RESET} {YELLOW}▶ Processing: {CYAN}{target}{RESET} {' ' * (60 - len(target))}{WHITE}│{RESET}")
            print(f"{WHITE}│{RESET} {WHITE}Total collected: {GREEN}{len(Uuid)}{RESET} {' ' * (56 - len(str(len(Uuid))))}{WHITE}│{RESET}")
            print(f"{WHITE}│{RESET} {WHITE}Queue remaining: {GREEN}{len(TARGET_QUEUE)}{RESET} {' ' * (56 - len(str(len(TARGET_QUEUE))))}{WHITE}│{RESET}")
            print(f"{WHITE}└{'─'*78}┘{RESET}")
            
            # Get user ID
            user_id = None
            for attempt in range(MAX_RETRIES):
                if not RUNNING:
                    break
                user_id = get_user_id_methods(target, cintil)
                if user_id:
                    break
                print(f"{RED}Attempt {attempt+1}/{MAX_RETRIES} failed for {target}{RESET}")
                time.sleep(2 ** attempt)
            
            if user_id:
                print(f"{GREEN}✓ Found user ID: {user_id}{RESET}")
                try:
                    Graphql(typess, user_id, cintil['cookie'], '', target)
                    PROCESSED_TARGETS.add(target)
                    print(f"\n{GREEN}✓ Completed: {target} ({len(Uuid)} total users){RESET}")
                except Exception as e:
                    print(f"{RED}✗ Error processing {target}: {e}{RESET}")
                    FAILED_TARGETS.append(target)
            else:
                print(f"{RED}✗ Could not find user ID for: {target}{RESET}")
                FAILED_TARGETS.append(target)
            
            # Save after each target
            save_checkpoint()
            save_to_sdcard()
            
            # Retry failed targets if any
            if FAILED_TARGETS and len(FAILED_TARGETS) > 0:
                print(f"\n{YELLOW}Retrying failed targets...{RESET}")
                failed_copy = list(FAILED_TARGETS)
                FAILED_TARGETS.clear()
                for ftarget in failed_copy:
                    if ftarget not in PROCESSED_TARGETS:
                        TARGET_QUEUE.append(ftarget)
            
            # Random delay between targets to avoid rate limiting
            delay = REQUEST_DELAY + random.uniform(0, 2)
            print(f"{WHITE}Waiting {delay:.1f}s before next target...{RESET}")
            time.sleep(delay)
    
    # Final save
    save_checkpoint()
    save_to_sdcard()
    print(f"\n{GREEN}✓ Non-stop dump completed! Total: {len(Uuid)} users{RESET}")

# ============ MAIN FUNCTIONS ============
def MetodeType():
    """Manage saved data options"""
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
            DUMP_COUNT = 0
            print(f"{GREEN}✓ Data cleared successfully!{RESET}")
        else:
            print(f"{YELLOW}Operation cancelled.{RESET}")
        time.sleep(1)
        MetodeType()
        
    elif choice in ['05', '5']:
        Menu()
        
    elif choice in ['00', '0']:
        print(f"{GREEN}Exiting...{RESET}")
        save_checkpoint()
        sys.exit(0)
        
    else:
        print(f"{RED}Invalid option!{RESET}")
        time.sleep(1)
        MetodeType()

def Menu():
    """Main menu"""
    os.system('clear')
    aset, nama, fol = Aset_Ig()
    print(f"{BLUE}═" * 80)
    print(f"""{campur} 
 _______  ______ _______ _______ _     _      _____  ______
 |       |_____/ |_____| |       |____/         |   |  ____
 |_____  |    \\_ |     | |_____  |    \\_      __|__ |_____|
                                          
{CYAN}╭──────────────────────╮{CYAN}╭───────────────╮{CYAN}╭─────────────────────────╮
{CYAN}│ {CYAN}Author : {GREEN}sumon {CYAN}│{CYAN}  │ {WHITE}Version : {GREEN}3.0 {CYAN}│{CYAN}│ {WHITE}Status : {GREEN}Non-Stop{CYAN}    │
{CYAN}╰──────────────────────╯{CYAN}╰───────────────╯{CYAN}╰─────────────────────────╯""")
    print(f"{GREEN}{WHITE}Username :{GREEN} {nama[:8]}\n{WHITE}Followers : {GREEN}{fol}")
    print(f"{WHITE}Total Collected: {GREEN}{len(Uuid)} users{RESET}")
    
    print(f"\n{RED}[ {YELLOW}Main Menu {RED}]\n")
    print(f"{RED}[{WHITE}01{RED}] {CYAN} Dump followers (Non-Stop)")
    print(f"{RED}[{WHITE}02{RED}] {CYAN} Dump following (Non-Stop)")
    print(f"{RED}[{WHITE}03{RED}] {CYAN} Load from file")
    print(f"{RED}[{WHITE}04{RED}] {CYAN} Manage saved data")
    print(f"{RED}[{WHITE}05{RED}] {CYAN} Resume from checkpoint")
    print(f"{RED}[{WHITE}00{RED}] {RED} Delete/Change Cookies")
    print(f"{BLUE}═" * 80)
    x = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Please select a menu option :{YELLOW} ")

    if x in ['01', '1']:
        nonstop_dump_mode(aset, True)
    elif x in ['02', '2']:
        nonstop_dump_mode(aset, False)
    elif x in ['03', '3']:
        crackfile()
    elif x in ['04', '4']:
        MetodeType()
    elif x in ['05', '5']:
        if load_checkpoint():
            print(f"{GREEN}✓ Resume from checkpoint: {len(Uuid)} users{RESET}")
            time.sleep(2)
            Menu()
        else:
            print(f"{RED}No checkpoint found!{RESET}")
            time.sleep(2)
            Menu()
    elif x in ['00', '0']:
        if os.path.exists('data/cookie.txt'):
            os.remove('data/cookie.txt')
        if os.path.exists(CHECKPOINT_FILE):
            os.remove(CHECKPOINT_FILE)
        prints(f"{GREEN}Successfully deleted cookies and checkpoint")
        exit()
    else:
        print(f"{RED}Invalid option!")
        time.sleep(1)
        Menu()

def crackfile():
    """Load data from a file"""
    try:
        nu = input(f"{PURPLE}[{WHITE}+{PURPLE}] {WHITE}Enter Your File Name: {PURPLE}")
        if not os.path.isfile(nu):
            print(f"{PURPLE}[{RED}+{PURPLE}] {RED}File Not Found.")
            return Menu()
        
        with open(nu, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
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

# ============ MAIN EXECUTION ============
if __name__ == "__main__":
    # Create data directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')
    
    try:
        Menu()
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Exiting... Saving checkpoint...{RESET}")
        save_checkpoint()
        save_to_sdcard()
        sys.exit(0)
    except Exception as e:
        print(f"\n{RED}An error occurred: {e}{RESET}")
        save_checkpoint()
        sys.exit(1)
