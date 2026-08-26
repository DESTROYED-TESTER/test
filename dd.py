#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Instagram Data Dumper v4.0 - NON-STOP UNLIMITED DUMP
- Single username auto-capture
- Unlimited dump (never stops, runs in background)
- Ctrl+Z support for Termux background execution
- Auto-resume on restart
- Continuous pagination until completion
- Auto-save every 50 users
- Multiple account support
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
from rich.progress import Progress, TextColumn, SpinnerColumn, BarColumn, TimeElapsedColumn
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
import subprocess
import atexit

# Global variables
Uid, Uuid = [], []
bkas = []
Ok, Cp, Loop = 0, 0, 0
xx = 0
SistemLog = "api.instagram.com"
MAX_RETRIES = 5
REQUEST_DELAY = 1.5
DUMP_COUNT = 0
LAST_SAVE = 0
AUTO_SAVE_INTERVAL = 50  # Save every 50 users
RUNNING = True
CURRENT_USER = ""
TOTAL_FETCHED = 0
LAST_PAGE_CURSOR = ""
CHECKPOINT_FILE = 'data/checkpoint.pkl'
TARGET_FILE = 'data/targets.txt'
DUMP_MODE = ""  # 'followers' or 'following'
PID_FILE = 'data/dump.pid'
BACKGROUND_MODE = False

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

# ============ PROCESS MANAGEMENT ============
def write_pid():
    """Write PID to file for background process management"""
    try:
        with open(PID_FILE, 'w') as f:
            f.write(str(os.getpid()))
        return True
    except:
        return False

def remove_pid():
    """Remove PID file"""
    try:
        if os.path.exists(PID_FILE):
            os.remove(PID_FILE)
    except:
        pass

def is_running():
    """Check if dump process is already running"""
    try:
        if os.path.exists(PID_FILE):
            with open(PID_FILE, 'r') as f:
                pid = int(f.read().strip())
            # Check if process exists
            try:
                os.kill(pid, 0)
                return True
            except:
                remove_pid()
                return False
    except:
        return False
    return False

def check_background_status():
    """Check if dump is running in background"""
    if is_running():
        print(f"{YELLOW}⚠ Dump is already running in background!{RESET}")
        print(f"{WHITE}Use 'fg' to bring to foreground or 'kill %%' to stop{RESET}")
        return True
    return False

# ============ SIGNAL HANDLER ============
def signal_handler(sig, frame):
    global RUNNING
    if sig == signal.SIGTSTP:  # Ctrl+Z
        print(f"\n\n{YELLOW}⚠ Dump suspended to background. Use 'fg' to resume or 'bg' to continue in background{RESET}")
        print(f"{GREEN}✓ Progress saved! Total: {len(Uuid)} users{RESET}")
        save_checkpoint()
        save_to_sdcard()
        # Suspend process
        os.kill(os.getpid(), signal.SIGSTOP)
        return
    
    print(f"\n\n{YELLOW}⚠ Received interrupt signal. Saving progress...{RESET}")
    RUNNING = False
    save_checkpoint()
    save_to_sdcard()
    remove_pid()
    print(f"{GREEN}✓ Progress saved! Total: {len(Uuid)} users{RESET}")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTSTP, signal_handler)
atexit.register(remove_pid)

# ============ CHECKPOINT FUNCTIONS ============
def save_checkpoint():
    """Save current progress to checkpoint file"""
    try:
        checkpoint = {
            'Uuid': Uuid,
            'DUMP_COUNT': DUMP_COUNT,
            'CURRENT_USER': CURRENT_USER,
            'LAST_PAGE_CURSOR': LAST_PAGE_CURSOR,
            'TOTAL_FETCHED': TOTAL_FETCHED,
            'DUMP_MODE': DUMP_MODE,
            'timestamp': datetime.now().isoformat()
        }
        with open(CHECKPOINT_FILE, 'wb') as f:
            pickle.dump(checkpoint, f)
        return True
    except Exception as e:
        return False

def load_checkpoint():
    """Load checkpoint if exists"""
    global Uuid, DUMP_COUNT, CURRENT_USER, LAST_PAGE_CURSOR, TOTAL_FETCHED, DUMP_MODE
    try:
        if os.path.exists(CHECKPOINT_FILE):
            with open(CHECKPOINT_FILE, 'rb') as f:
                checkpoint = pickle.load(f)
            Uuid = checkpoint.get('Uuid', [])
            DUMP_COUNT = checkpoint.get('DUMP_COUNT', 0)
            CURRENT_USER = checkpoint.get('CURRENT_USER', '')
            LAST_PAGE_CURSOR = checkpoint.get('LAST_PAGE_CURSOR', '')
            TOTAL_FETCHED = checkpoint.get('TOTAL_FETCHED', 0)
            DUMP_MODE = checkpoint.get('DUMP_MODE', '')
            return True
    except Exception as e:
        pass
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
            return False
        
        if not os.path.exists('/sdcard'):
            try:
                os.makedirs('/sdcard', exist_ok=True)
            except:
                pass
        
        with open('/sdcard/dump.txt', 'w', encoding='utf-8') as f:
            f.write("# Instagram Users Dump - Non-Stop Unlimited\n")
            f.write(f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"# Total: {len(Uuid)}\n")
            f.write(f"# Target: {CURRENT_USER}\n")
            f.write(f"# Mode: {DUMP_MODE}\n")
            f.write("# Format: username|full_name\n")
            f.write("#" + "="*50 + "\n\n")
            
            for item in Uuid:
                f.write(item + '\n')
        
        return True
        
    except Exception as e:
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
            f.write(f"# Instagram Users Dump - Non-Stop Unlimited\n")
            f.write(f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"# Total: {len(Uuid)}\n")
            f.write(f"# Target: {CURRENT_USER}\n")
            f.write(f"# Mode: {DUMP_MODE}\n")
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
    if CURRENT_USER:
        print(f"{WHITE}Target User: {CYAN}{CURRENT_USER}{RESET}")
    if DUMP_MODE:
        print(f"{WHITE}Mode: {CYAN}{DUMP_MODE}{RESET}")
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
    """Test if cookies are still valid"""
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
                    return True
    except Exception as e:
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
def Graphql(typess, userid, cokie, after=""):
    """Fetch followers or following using GraphQL API with unlimited pagination"""
    global xx, Uuid, DUMP_COUNT, TOTAL_FETCHED, LAST_PAGE_CURSOR, RUNNING, CURRENT_USER, DUMP_MODE
    
    if 'xx' not in globals():
        global xx
        xx = 0
    
    api = "https://www.instagram.com/graphql/query/"
    
    if typess:
        query_hash = "37479f2b8209594dde7facb0d904896a"  # Followers
        mode = "followers"
    else:
        query_hash = "58712303d941c6855d4e888c5f0cd22f"  # Following
        mode = "following"
    
    DUMP_MODE = mode
    
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
                RUNNING = False
                return
            
            if 'status' in req_json and req_json['status'] == 'fail':
                print(f'\n{RED}Request failed: {req_json.get("message", "Unknown error")}')
                time.sleep(5)
                continue
            
            khm = 'edge_followed_by' if typess else 'edge_follow'
            
            if 'data' not in req_json or 'user' not in req_json['data'] or not req_json['data']['user']:
                print(f"\n{RED}User not found or private. Skipping...")
                RUNNING = False
                return
            
            user_data = req_json['data']['user']
            
            if khm not in user_data:
                print(f"\n{RED}This user has no visible {mode} or is private")
                RUNNING = False
                return
            
            total_count = user_data[khm].get('count', 0)
            if total_count > 0 and TOTAL_FETCHED == 0:
                print(f"\n{GREEN}Total {mode}: {total_count}{RESET}")
                print(f"{WHITE}Starting non-stop dump... Press Ctrl+Z to background{RESET}\n")
            
            edges = user_data[khm].get('edges', [])
            if not edges:
                print(f"\n{YELLOW}No more {mode} found - Dump Complete!{RESET}")
                print(f"{GREEN}✓ Total collected: {len(Uuid)} users{RESET}")
                RUNNING = False
                save_checkpoint()
                save_to_sdcard()
                return
            
            # Process edges
            for xyz in edges:
                if not RUNNING:
                    return
                
                username = xyz['node'].get('username', '')
                full_name = xyz['node'].get('full_name', '')
                is_verified = xyz['node'].get('is_verified', False)
                is_private = xyz['node'].get('is_private', False)
                
                if username:
                    name_with_badge = full_name + (' ✓' if is_verified else '') + (' 🔒' if is_private else '')
                    xy = username + '|' + name_with_badge
                    
                    if xy not in Uuid:
                        xx += 1
                        DUMP_COUNT += 1
                        TOTAL_FETCHED += 1
                        Uuid.append(xy)
                        
                        # Display progress
                        print(f'\r{WHITE}📥 {CYAN}{username:<20}{WHITE} | Total: {GREEN}{len(Uuid):>6}{WHITE} | {YELLOW}{mode}{WHITE} | Rate: {GREEN}{TOTAL_FETCHED}{WHITE}                    ', end='', flush=True)
                        
                        # Auto-save checkpoint
                        if len(Uuid) % AUTO_SAVE_INTERVAL == 0:
                            save_checkpoint()
                            save_to_sdcard()
                            print(f"\n{GREEN}✓ Auto-saved {len(Uuid)} users{RESET}")
            
            # Check for next page
            page_info = user_data[khm].get('page_info', {})
            end = page_info.get('has_next_page', False)
            
            if end and RUNNING:
                after = page_info.get('end_cursor', '')
                if after:
                    LAST_PAGE_CURSOR = after
                    print(f"\n{YELLOW}⟳ Loading next page... (Collected: {len(Uuid)}){RESET}")
                    time.sleep(REQUEST_DELAY + random.uniform(0, 0.5))
                    Graphql(typess, userid, cokie, after)
            else:
                print(f"\n\n{GREEN}✓ Dump Complete! Total {mode} collected: {len(Uuid)}{RESET}")
                save_checkpoint()
                save_to_sdcard()
                RUNNING = False
                remove_pid()
            break
            
        except requests.exceptions.Timeout:
            print(f"\n{RED}⚠ Timeout, attempt {attempt+1}/{MAX_RETRIES}")
            time.sleep(2 ** attempt)
        except requests.exceptions.TooManyRedirects:
            print(f"\n{RED}⚠ Too many redirects - check cookies")
            break
        except requests.exceptions.RequestException as e:
            print(f"\n{RED}⚠ Network error, attempt {attempt+1}/{MAX_RETRIES}")
            time.sleep(2 ** attempt)
        except json.JSONDecodeError:
            print(f"\n{RED}⚠ Invalid JSON, attempt {attempt+1}/{MAX_RETRIES}")
            time.sleep(2 ** attempt)
        except Exception as e:
            print(f"\n{RED}⚠ Error, attempt {attempt+1}/{MAX_RETRIES}: {e}")
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

# ============ UNLIMITED DUMP FUNCTIONS ============
def unlimited_dump_mode(cintil, typess):
    """Unlimited dump with single username input and auto-capture"""
    global RUNNING, Uuid, DUMP_COUNT, CURRENT_USER, TOTAL_FETCHED, LAST_PAGE_CURSOR, BACKGROUND_MODE
    
    Clear()
    print(f"{BLUE}═" * 80)
    print(f"{campur}★ NON-STOP UNLIMITED DUMP MODE ★{RESET}")
    print(f"{BLUE}═" * 80)
    
    # Check if already running
    if is_running():
        print(f"{YELLOW}⚠ Dump is already running in background!{RESET}")
        print(f"{WHITE}Options:{RESET}")
        print(f"  {CYAN}1. 'fg' - Bring to foreground{RESET}")
        print(f"  {CYAN}2. 'kill %%' - Stop background process{RESET}")
        print(f"  {CYAN}3. 'bg' - Continue in background{RESET}")
        input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Press Enter to continue...{RESET}")
        Menu()
        return
    
    # Check for existing session
    if load_checkpoint() and Uuid:
        print(f"\n{YELLOW}⚠ Found existing checkpoint with {len(Uuid)} users{RESET}")
        print(f"{WHITE}Target: {CYAN}{CURRENT_USER}{RESET}")
        print(f"{WHITE}Mode: {CYAN}{DUMP_MODE}{RESET}")
        resume = input(f"{WHITE}Resume from checkpoint? (y/n): {YELLOW}").strip().lower()
        if resume == 'y' and CURRENT_USER:
            print(f"{GREEN}✓ Resuming dump for: {CURRENT_USER}{RESET}")
            print(f"{WHITE}Continuing from page: {LAST_PAGE_CURSOR if LAST_PAGE_CURSOR else 'start'}{RESET}")
            time.sleep(1)
            
            # Ensure csrftoken exists
            if 'csrftoken' not in str(cintil):
                try:
                    memek = requests.get('https://www.instagram.com/data/shared_data/', cookies=cintil, timeout=10)
                    memek.raise_for_status()
                    token = memek.json()['config']['csrf_token']
                    cintil['cookie'] += ';csrftoken=%s;' % token
                except Exception as e:
                    print(f'\n{WHITE}[{YELLOW}!{WHITE}] Csrftoken not available: {e}')
                    return
            
            # Get user ID for resume
            user_id = get_user_id_methods(CURRENT_USER, cintil)
            if user_id:
                write_pid()
                Graphql(typess, user_id, cintil['cookie'], LAST_PAGE_CURSOR)
            return
    
    # Get username
    print(f"\n{CYAN}Enter Instagram username to dump (auto-capture all followers/following){RESET}")
    print(f"{YELLOW}Example: cristiano{RESET}")
    username = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Username :{YELLOW} ").strip()
    
    if not username:
        print(f"{RED}No username entered!{RESET}")
        time.sleep(1)
        return
    
    CURRENT_USER = username
    TOTAL_FETCHED = 0
    LAST_PAGE_CURSOR = ""
    RUNNING = True
    
    # Ask for background mode
    bg_mode = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Run in background? (y/n) [Ctrl+Z to suspend]: {YELLOW}").strip().lower()
    BACKGROUND_MODE = bg_mode == 'y'
    
    # Ensure csrftoken exists
    if 'csrftoken' not in str(cintil):
        try:
            memek = requests.get('https://www.instagram.com/data/shared_data/', cookies=cintil, timeout=10)
            memek.raise_for_status()
            token = memek.json()['config']['csrf_token']
            cintil['cookie'] += ';csrftoken=%s;' % token
        except Exception as e:
            os.system('rm -rf data/cookie.txt')
            print(f'\n{WHITE}[{YELLOW}!{WHITE}] Csrftoken not available: {e}')
            return
    
    # Get user ID with retry
    print(f"\n{YELLOW}Fetching user ID for: {CYAN}{username}{RESET}")
    user_id = None
    for attempt in range(MAX_RETRIES):
        user_id = get_user_id_methods(username, cintil)
        if user_id:
            break
        print(f"{RED}Attempt {attempt+1}/{MAX_RETRIES} failed. Retrying...{RESET}")
        time.sleep(2 ** attempt)
    
    if not user_id:
        print(f"{RED}✗ Could not find user ID for: {username}{RESET}")
        print(f"{YELLOW}Make sure the username is correct and the account is public.{RESET}")
        time.sleep(2)
        return
    
    print(f"{GREEN}✓ Found user ID: {user_id}{RESET}")
    mode = 'followers' if typess else 'following'
    print(f"\n{WHITE}Starting non-stop {mode} dump...{RESET}")
    print(f"{YELLOW}Commands:{RESET}")
    print(f"  {CYAN}Ctrl+C{RESET} - Stop and save")
    print(f"  {CYAN}Ctrl+Z{RESET} - Suspend to background (use 'fg' to resume)")
    print(f"{WHITE}Auto-saves every {AUTO_SAVE_INTERVAL} users{RESET}\n")
    
    if BACKGROUND_MODE:
        print(f"{GREEN}✓ Running in background mode{RESET}")
        write_pid()
    
    # Start the unlimited dump
    Graphql(typess, user_id, cintil['cookie'], '')
    
    # Final save
    save_checkpoint()
    save_to_sdcard()
    remove_pid()
    
    print(f"\n{GREEN}✓ Dump completed! Total: {len(Uuid)} users{RESET}")
    if len(Uuid) > 0:
        print(f"{WHITE}Saved to: {CYAN}/sdcard/dump.txt{RESET}")
    time.sleep(2)

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
    if CURRENT_USER:
        print(f"{WHITE}Target: {CYAN}{CURRENT_USER}{RESET}")
    
    print(f"\n{RED}[ {YELLOW}Save & Manage Options {RED}]\n")
    print(f"{RED}[{WHITE}01{RED}] {CYAN} Save to /sdcard/dump.txt")
    print(f"{RED}[{WHITE}02{RED}] {CYAN} Save to custom file (data/ folder)")
    print(f"{RED}[{WHITE}03{RED}] {CYAN} View all collected data")
    print(f"{RED}[{WHITE}04{RED}] {CYAN} Clear collected data")
    print(f"{RED}[{WHITE}05{RED}] {CYAN} Return to main menu")
    print(f"{RED}[{WHITE}06{RED}] {CYAN} Check background status")
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
            TOTAL_FETCHED = 0
            if os.path.exists(CHECKPOINT_FILE):
                os.remove(CHECKPOINT_FILE)
            print(f"{GREEN}✓ Data cleared successfully!{RESET}")
        else:
            print(f"{YELLOW}Operation cancelled.{RESET}")
        time.sleep(1)
        MetodeType()
        
    elif choice in ['05', '5']:
        Menu()
        
    elif choice in ['06', '6']:
        if is_running():
            print(f"{GREEN}✓ Dump is running in background (PID: {open(PID_FILE).read().strip()}){RESET}")
        else:
            print(f"{YELLOW}No background dump running{RESET}")
        input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Press Enter to continue...{RESET}")
        MetodeType()
        
    elif choice in ['00', '0']:
        print(f"{GREEN}Exiting...{RESET}")
        save_checkpoint()
        remove_pid()
        sys.exit(0)
        
    else:
        print(f"{RED}Invalid option!{RESET}")
        time.sleep(1)
        MetodeType()

def Menu():
    """Main menu"""
    os.system('clear')
    aset, nama, fol = Aset_Ig()
    
    # Check background status
    bg_status = ""
    if is_running():
        bg_status = f" {GREEN}[Running in BG]{RESET}"
    
    print(f"{BLUE}═" * 80)
    print(f"""{campur} 
 _______  ______ _______ _______ _     _      _____  ______
 |       |_____/ |_____| |       |____/         |   |  ____
 |_____  |    \\_ |     | |_____  |    \\_      __|__ |_____|
                                          
{CYAN}╭──────────────────────╮{CYAN}╭───────────────╮{CYAN}╭─────────────────────────────╮
{CYAN}│ {CYAN}Author : {GREEN}sumon {CYAN}│{CYAN}  │ {WHITE}Version : {GREEN}4.0 {CYAN}│{CYAN}│ {WHITE}Mode : {GREEN}Non-Stop Unlimited{CYAN}  │
{CYAN}╰──────────────────────╯{CYAN}╰───────────────╯{CYAN}╰─────────────────────────────╯""")
    print(f"{GREEN}{WHITE}Username :{GREEN} {nama[:8]}\n{WHITE}Followers : {GREEN}{fol}")
    print(f"{WHITE}Total Collected: {GREEN}{len(Uuid)} users{RESET}{bg_status}")
    
    print(f"\n{RED}[ {YELLOW}Main Menu {RED}]\n")
    print(f"{RED}[{WHITE}01{RED}] {CYAN} Dump Followers (Non-Stop Unlimited)")
    print(f"{RED}[{WHITE}02{RED}] {CYAN} Dump Following (Non-Stop Unlimited)")
    print(f"{RED}[{WHITE}03{RED}] {CYAN} Load from file")
    print(f"{RED}[{WHITE}04{RED}] {CYAN} Manage saved data")
    print(f"{RED}[{WHITE}05{RED}] {CYAN} Resume from checkpoint")
    print(f"{RED}[{WHITE}06{RED}] {CYAN} Check/Manage background process")
    print(f"{RED}[{WHITE}00{RED}] {RED} Delete/Change Cookies")
    print(f"{BLUE}═" * 80)
    x = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Please select a menu option :{YELLOW} ")

    if x in ['01', '1']:
        unlimited_dump_mode(aset, True)
    elif x in ['02', '2']:
        unlimited_dump_mode(aset, False)
    elif x in ['03', '3']:
        crackfile()
    elif x in ['04', '4']:
        MetodeType()
    elif x in ['05', '5']:
        if load_checkpoint():
            print(f"{GREEN}✓ Resume from checkpoint: {len(Uuid)} users{RESET}")
            print(f"{WHITE}Target: {CYAN}{CURRENT_USER}{RESET}")
            print(f"{WHITE}Mode: {CYAN}{DUMP_MODE}{RESET}")
            time.sleep(2)
            Menu()
        else:
            print(f"{RED}No checkpoint found!{RESET}")
            time.sleep(2)
            Menu()
    elif x in ['06', '6']:
        if is_running():
            pid = open(PID_FILE).read().strip()
            print(f"\n{GREEN}✓ Dump is running in background (PID: {pid}){RESET}")
            print(f"\n{WHITE}Commands:{RESET}")
            print(f"  {CYAN}fg{RESET} - Bring to foreground")
            print(f"  {CYAN}kill {pid}{RESET} - Stop the process")
            print(f"  {CYAN}kill -STOP {pid}{RESET} - Pause process")
            print(f"  {CYAN}kill -CONT {pid}{RESET} - Resume process")
        else:
            print(f"\n{YELLOW}No background dump running{RESET}")
        input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Press Enter to continue...{RESET}")
        Menu()
    elif x in ['00', '0']:
        if os.path.exists('data/cookie.txt'):
            os.remove('data/cookie.txt')
        if os.path.exists(CHECKPOINT_FILE):
            os.remove(CHECKPOINT_FILE)
        remove_pid()
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
    
    # Check if running as background
    if len(sys.argv) > 1 and sys.argv[1] == '--background':
        print(f"{GREEN}✓ Running in background mode...{RESET}")
        write_pid()
    
    try:
        Menu()
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Exiting... Saving checkpoint...{RESET}")
        save_checkpoint()
        save_to_sdcard()
        remove_pid()
        print(f"{GREEN}✓ Progress saved! Total: {len(Uuid)} users{RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{RED}An error occurred: {e}{RESET}")
        save_checkpoint()
        remove_pid()
        sys.exit(1)
