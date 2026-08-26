#!/usr/bin/env python3
#================[MEGA DUMPER v6.0 - 100K+ COLLECTOR]================#
"""
ULTIMATE MEGA DUMPER - 1 LAKH+ COLLECTION SYSTEM
- Optimized for 100,000+ users
- Multi-threaded mega collection
- Batch processing
- Automatic pagination handling
- Smart duplicate management
"""

import requests
import json
import time
import re
import os
import sys
import threading
import queue
import random
import hashlib
import signal
import pickle
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Set, List, Dict, Optional, Tuple
from collections import defaultdict
import gc

# ============ COLOR CODES ============
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
RESET = '\033[0m'

# ============ CONFIGURATION ============
CONFIG = {
    'max_workers': 10,          # Thread workers for parallel processing
    'batch_size': 100,           # Users per API request
    'delay_between_requests': 0.3,  # Delay to avoid rate limiting
    'max_depth': 5,             # Chain depth
    'target_collection': 100000, # 1 LAKH target
    'auto_save_interval': 1000,  # Save every 1000 users
    'max_retries': 5,
    'timeout': 30,
    'output_file': '/sdcard/mega_dump.txt',
    'cookie_file': 'data/cookie.txt',
    'progress_file': 'data/progress.pkl'
}

# ============ GLOBAL VARIABLES ============
dumped_users = {}  # username -> full_name
processed_users = set()
user_queue = queue.Queue(maxsize=10000)
dump_counter = 0
stop_dumping = False
current_depth = 0
cookies = {}
session = requests.Session()
lock = threading.Lock()
progress_lock = threading.Lock()
total_collected = 0
rate_limit_hits = 0
start_time = None

# ============ SIGNAL HANDLING ============
def signal_handler(sig, frame):
    global stop_dumping
    print(f"\n{YELLOW}[!] Saving progress and stopping...{RESET}")
    stop_dumping = True
    save_progress()
    save_mega_dump()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# ============ PROGRESS MANAGEMENT ============
def save_progress():
    """Save current progress for resuming"""
    with progress_lock:
        try:
            os.makedirs('data', exist_ok=True)
            progress_data = {
                'dumped_users': dumped_users,
                'processed_users': list(processed_users),
                'dump_counter': dump_counter,
                'total_collected': total_collected,
                'timestamp': datetime.now().isoformat()
            }
            with open(CONFIG['progress_file'], 'wb') as f:
                pickle.dump(progress_data, f)
            print(f"\n{GREEN}[✓] Progress saved: {len(dumped_users)} users{RESET}")
        except Exception as e:
            print(f"{RED}[✗] Progress save error: {e}{RESET}")

def load_progress():
    """Load previous progress"""
    global dumped_users, processed_users, dump_counter, total_collected
    
    if os.path.exists(CONFIG['progress_file']):
        try:
            with open(CONFIG['progress_file'], 'rb') as f:
                progress_data = pickle.load(f)
                dumped_users = progress_data.get('dumped_users', {})
                processed_users = set(progress_data.get('processed_users', []))
                dump_counter = progress_data.get('dump_counter', 0)
                total_collected = progress_data.get('total_collected', 0)
                print(f"{GREEN}[✓] Loaded progress: {len(dumped_users)} users{RESET}")
                return True
        except Exception as e:
            print(f"{YELLOW}[!] Could not load progress: {e}{RESET}")
    return False

# ============ COOKIE MANAGEMENT ============
def load_cookies():
    """Load and validate cookies"""
    global cookies
    
    print(f"{CYAN}[*] Loading Instagram cookies...{RESET}")
    os.makedirs('data', exist_ok=True)
    os.makedirs('/sdcard', exist_ok=True)
    
    if os.path.exists(CONFIG['cookie_file']):
        with open(CONFIG['cookie_file'], 'r') as f:
            cookie_str = f.read().strip()
            cookies = {'cookie': cookie_str}
            
        if validate_cookies():
            print(f"{GREEN}[✓] Cookies loaded!{RESET}")
            return True
            
    print(f"{YELLOW}[!] Enter your Instagram cookie{RESET}")
    cookie_input = input(f"{CYAN}Cookie: {RESET}").strip()
    
    if not cookie_input:
        print(f"{RED}[✗] No cookie provided!{RESET}")
        return False
        
    cookies = {'cookie': cookie_input}
    with open(CONFIG['cookie_file'], 'w') as f:
        f.write(cookie_input)
        
    if validate_cookies():
        print(f"{GREEN}[✓] Cookie saved!{RESET}")
        return True
    else:
        print(f"{RED}[✗] Invalid cookie!{RESET}")
        return False

def validate_cookies():
    """Validate cookie by fetching user info"""
    try:
        uid_match = re.search('ds_user_id=(\\d+)', str(cookies.get('cookie', '')))
        if not uid_match:
            return False
            
        uid = uid_match.group(1)
        response = session.get(
            f'https://i.instagram.com/api/v1/users/{uid}/info/',
            headers={
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2) AppleWebKit/605.1.15',
                'x-ig-app-id': '1217981644879628'
            },
            cookies=cookies,
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            if 'user' in data:
                user = data['user']
                print(f"{GREEN}✓ Logged in as: {CYAN}{user.get('username')}{RESET}")
                print(f"  Followers: {CYAN}{user.get('follower_count', 0):,}{RESET}")
                print(f"  Following: {CYAN}{user.get('following_count', 0):,}{RESET}")
                return True
    except:
        pass
    return False

# ============ USER ID RESOLUTION ============
def get_user_id(username: str) -> Optional[str]:
    """Get user ID from username with multiple methods"""
    
    # Method 1: Official API
    for attempt in range(CONFIG['max_retries']):
        try:
            url = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={username}'
            response = session.get(
                url,
                headers={
                    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2) AppleWebKit/605.1.15',
                    'x-ig-app-id': '1217981644879628'
                },
                cookies=cookies,
                timeout=CONFIG['timeout']
            )
            
            if response.status_code == 200:
                data = response.json()
                user_id = data.get('data', {}).get('user', {}).get('id')
                if user_id:
                    return user_id
        except:
            pass
        time.sleep(0.5)
    
    # Method 2: GraphQL
    try:
        url = 'https://www.instagram.com/graphql/query/'
        params = {
            'query_hash': 'c9100bf9110dd6361671f113dd02e7d6',
            'variables': json.dumps({'username': username})
        }
        response = session.get(url, params=params, cookies=cookies, timeout=CONFIG['timeout'])
        
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('user', {}).get('id')
    except:
        pass
    
    return None

# ============ MEGA DUMP ENGINE ============
def mega_dump_relationship(user_id: str, username: str, mode: str = 'followers', 
                           target: int = CONFIG['target_collection']) -> int:
    """
    MEGA DUMP - Optimized for collecting 100K+ users
    Returns number of users collected
    """
    global dump_counter, total_collected, stop_dumping, rate_limit_hits
    
    if stop_dumping:
        return 0
    
    if len(dumped_users) >= target:
        print(f"{GREEN}[✓] Target {target:,} users reached!{RESET}")
        stop_dumping = True
        return 0
    
    # Check if already processed
    user_key = f"{username}_{mode}"
    if user_key in processed_users:
        return 0
    processed_users.add(user_key)
    
    print(f"\n{CYAN}[*] MEGA DUMPING {mode.upper()} for @{username}{RESET}")
    print(f"{WHITE}   Current: {len(dumped_users):,} / {target:,} users{RESET}")
    print(f"{WHITE}   Rate limit hits: {rate_limit_hits}{RESET}")
    
    api_url = "https://www.instagram.com/graphql/query/"
    after = ""
    page_count = 0
    batch_count = 0
    
    # Query hash
    query_hash = "37479f2b8209594dde7facb0d904896a" if mode == 'followers' else "58712303d941c6855d4e888c5f0cd22f"
    edge_key = 'edge_followed_by' if mode == 'followers' else 'edge_follow'
    
    while not stop_dumping and len(dumped_users) < target:
        variables = {
            "id": user_id,
            "first": CONFIG['batch_size'],
            "after": after
        }
        
        params = {
            'query_hash': query_hash,
            'variables': json.dumps(variables)
        }
        
        try:
            response = session.get(
                api_url,
                params=params,
                headers={
                    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2) AppleWebKit/605.1.15',
                    'Accept': 'application/json',
                    'x-ig-app-id': '1217981644879628'
                },
                cookies=cookies,
                timeout=CONFIG['timeout']
            )
            
            if response.status_code == 429:
                rate_limit_hits += 1
                wait_time = min(30, rate_limit_hits * 2)
                print(f"\n{YELLOW}[!] Rate limited! Waiting {wait_time}s...{RESET}")
                time.sleep(wait_time)
                continue
                
            if response.status_code != 200:
                print(f"\n{RED}[✗] Error {response.status_code}{RESET}")
                time.sleep(2)
                continue
                
            data = response.json()
            
            if 'data' not in data or 'user' not in data['data']:
                break
                
            user_data = data['data']['user']
            
            if edge_key not in user_data:
                break
                
            edges = user_data[edge_key].get('edges', [])
            
            if not edges:
                break
                
            # Process this batch
            new_users = []
            for edge in edges:
                if stop_dumping or len(dumped_users) >= target:
                    break
                    
                node = edge.get('node', {})
                username_found = node.get('username', '')
                full_name = node.get('full_name', '')
                
                if username_found and username_found not in dumped_users:
                    new_users.append((username_found, full_name))
            
            # Add users to dictionary
            with lock:
                for username_found, full_name in new_users:
                    if username_found not in dumped_users:
                        dumped_users[username_found] = full_name
                        total_collected += 1
                        dump_counter += 1
            
            batch_count += len(new_users)
            
            # Display progress
            elapsed = time.time() - start_time if start_time else 0
            rate = total_collected / elapsed if elapsed > 0 else 0
            progress_pct = (len(dumped_users) / target) * 100
            
            print(f'\r{GREEN}[+] {total_collected:,} users ({progress_pct:.1f}%) '
                  f'{WHITE}| Batch: {batch_count} '
                  f'{CYAN}| Rate: {rate:.1f}/s{RESET}', end='')
            
            # Auto-save
            if dump_counter % CONFIG['auto_save_interval'] == 0:
                print(f"\n{YELLOW}[!] Auto-saving...{RESET}")
                save_progress()
                save_mega_dump()
            
            # Check for more pages
            page_info = user_data[edge_key].get('page_info', {})
            has_next = page_info.get('has_next_page', False)
            after = page_info.get('end_cursor', '')
            
            page_count += 1
            
            if not has_next or not after:
                break
                
            # Smart delay between pages
            time.sleep(CONFIG['delay_between_requests'])
            
            # Memory management
            if page_count % 10 == 0:
                gc.collect()
            
        except Exception as e:
            print(f"\n{RED}[✗] Error: {e}{RESET}")
            time.sleep(2)
            continue
    
    print(f"\n{GREEN}[✓] Collected {total_collected:,} users from @{username}{RESET}")
    return total_collected

# ============ MULTI-THREADED MEGA DUMP ============
class MegaDumper:
    def __init__(self):
        self.workers = []
        self.user_queue = queue.Queue()
        self.results = []
        self.running = True
        
    def worker(self, mode: str = 'followers'):
        """Worker thread for processing users"""
        while self.running and not stop_dumping:
            try:
                username, user_id = self.user_queue.get(timeout=5)
                if user_id:
                    mega_dump_relationship(user_id, username, mode, CONFIG['target_collection'])
                self.user_queue.task_done()
            except queue.Empty:
                continue
            except Exception as e:
                print(f"{RED}[✗] Worker error: {e}{RESET}")
                
    def start_workers(self, usernames: List[str], mode: str = 'followers', num_workers: int = 5):
        """Start worker threads for parallel processing"""
        global start_time
        start_time = time.time()
        
        # Queue all users
        for username in usernames:
            user_id = get_user_id(username)
            if user_id:
                self.user_queue.put((username, user_id))
                print(f"{GREEN}[✓] Queued: {username} ({user_id}){RESET}")
            else:
                print(f"{RED}[✗] Invalid: {username}{RESET}")
            time.sleep(0.3)
        
        if self.user_queue.empty():
            print(f"{RED}[✗] No valid users to process!{RESET}")
            return
        
        print(f"\n{GREEN}[*] Starting {num_workers} workers for {mode}...{RESET}")
        print(f"{WHITE}   Target: {CONFIG['target_collection']:,} users{RESET}\n")
        
        # Start workers
        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            futures = []
            for _ in range(num_workers):
                future = executor.submit(self.worker, mode)
                futures.append(future)
            
            # Wait for completion or stop
            while not stop_dumping and not self.user_queue.empty():
                time.sleep(1)
                
            self.running = False
            for future in futures:
                future.cancel()
                
        # Final save
        save_progress()
        save_mega_dump()

# ============ SAVE FUNCTIONS ============
def save_mega_dump():
    """Save mega dump with 100K+ users efficiently"""
    global dumped_users
    
    if not dumped_users:
        return
        
    try:
        # Save to main file
        output_file = CONFIG['output_file']
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        # Write in chunks to handle large files
        chunk_size = 10000
        dumped_items = list(dumped_users.items())
        
        with open(output_file, 'w', encoding='utf-8') as f:
            for i in range(0, len(dumped_items), chunk_size):
                chunk = dumped_items[i:i+chunk_size]
                for username, full_name in chunk:
                    f.write(f"{username}|{full_name}\n")
        
        # Save backup with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_file = f"data/mega_dump_{timestamp}.txt"
        
        with open(backup_file, 'w', encoding='utf-8') as f:
            for username, full_name in dumped_items:
                f.write(f"{username}|{full_name}\n")
        
        # Save stats
        stats_file = 'data/mega_stats.json'
        with open(stats_file, 'w') as f:
            json.dump({
                'total_users': len(dumped_users),
                'last_update': datetime.now().isoformat(),
                'dump_counter': dump_counter,
                'rate_limit_hits': rate_limit_hits,
                'timestamp': int(time.time())
            }, f, indent=2)
            
        print(f"\n{GREEN}[✓] Saved {len(dumped_users):,} users to {output_file}{RESET}")
        
    except Exception as e:
        print(f"{RED}[✗] Save error: {e}{RESET}")

def load_mega_dump():
    """Load existing mega dump"""
    global dumped_users
    
    if os.path.exists(CONFIG['output_file']):
        try:
            with open(CONFIG['output_file'], 'r', encoding='utf-8') as f:
                for line in f:
                    if '|' in line:
                        parts = line.strip().split('|', 1)
                        if len(parts) == 2:
                            dumped_users[parts[0]] = parts[1]
            print(f"{GREEN}[✓] Loaded {len(dumped_users):,} users from file{RESET}")
            return True
        except Exception as e:
            print(f"{YELLOW}[!] Could not load: {e}{RESET}")
    return False

def view_mega_dump():
    """View mega dump statistics and sample"""
    if not dumped_users:
        print(f"{RED}[✗] No data collected!{RESET}")
        return
    
    print(f"\n{GREEN}{'='*70}{RESET}")
    print(f"{BOLD}{GREEN}📊 MEGA DUMP STATISTICS{RESET}")
    print(f"{GREEN}{'='*70}{RESET}")
    print(f"{WHITE}Total Users: {CYAN}{len(dumped_users):,}{RESET}")
    print(f"{WHITE}Dump Count: {CYAN}{dump_counter:,}{RESET}")
    print(f"{WHITE}Rate Limit Hits: {CYAN}{rate_limit_hits}{RESET}")
    
    if start_time:
        elapsed = time.time() - start_time
        hours = int(elapsed // 3600)
        minutes = int((elapsed % 3600) // 60)
        print(f"{WHITE}Elapsed Time: {CYAN}{hours}h {minutes}m{RESET}")
        if elapsed > 0:
            rate = len(dumped_users) / elapsed
            print(f"{WHITE}Collection Rate: {CYAN}{rate:.1f} users/sec{RESET}")
    
    print(f"\n{YELLOW}Sample Users (First 10):{RESET}")
    print(f"{YELLOW}{'─'*70}{RESET}")
    for i, (username, full_name) in enumerate(list(dumped_users.items())[:10], 1):
        print(f"{WHITE}{i:3}. {GREEN}{username:<20} {CYAN}{full_name}{RESET}")
    
    if len(dumped_users) > 10:
        print(f"{WHITE}... and {len(dumped_users)-10:,} more users{RESET}")
    
    print(f"{GREEN}{'='*70}{RESET}")

# ============ MEGA COLLECTION MODES ============
def mega_chain_dump(usernames: List[str], mode: str = 'followers', depth: int = 3):
    """Chain dump for 100K+ collection"""
    global stop_dumping, current_depth
    
    current_depth = 0
    all_usernames = set(usernames)
    
    print(f"\n{YELLOW}{'='*70}{RESET}")
    print(f"{GREEN}[*] STARTING MEGA CHAIN DUMP{RESET}")
    print(f"{WHITE}   Initial users: {len(usernames)}{RESET}")
    print(f"{WHITE}   Mode: {mode}{RESET}")
    print(f"{WHITE}   Depth: {depth}{RESET}")
    print(f"{WHITE}   Target: {CONFIG['target_collection']:,} users{RESET}")
    print(f"{YELLOW}{'='*70}{RESET}\n")
    
    for depth_level in range(depth):
        if stop_dumping or len(dumped_users) >= CONFIG['target_collection']:
            break
            
        current_depth = depth_level
        print(f"\n{BOLD}📍 DEPTH {depth_level + 1}{RESET}")
        print(f"{WHITE}   Users to process: {len(all_usernames)}{RESET}")
        
        # Get user IDs
        user_ids = {}
        for username in list(all_usernames)[:50]:  # Process top 50 per depth
            if stop_dumping:
                break
            if username not in processed_users:
                user_id = get_user_id(username)
                if user_id:
                    user_ids[username] = user_id
                    processed_users.add(username)
                time.sleep(0.3)
        
        if not user_ids:
            print(f"{YELLOW}[!] No valid users at depth {depth_level}{RESET}")
            break
            
        # Process users
        dumper = MegaDumper()
        user_list = list(user_ids.keys())
        dumper.start_workers(user_list, mode, min(CONFIG['max_workers'], len(user_list)))
        
        # Collect new users for next depth
        new_users = set(dumped_users.keys()) - all_usernames
        if new_users:
            all_usernames.update(new_users)
            print(f"\n{GREEN}[✓] Added {len(new_users):,} new users for next depth{RESET}")
        else:
            print(f"{YELLOW}[!] No new users found, stopping chain{RESET}")
            break
            
        # Save after each depth
        save_progress()
        save_mega_dump()
        time.sleep(2)
    
    print(f"\n{GREEN}{'='*70}{RESET}")
    print(f"{GREEN}[✓] MEGA CHAIN DUMP COMPLETED{RESET}")
    print(f"{WHITE}   Total users: {len(dumped_users):,}{RESET}")
    print(f"{GREEN}{'='*70}{RESET}")
    save_progress()
    save_mega_dump()

# ============ MENU SYSTEM ============
def main_menu():
    """Main interactive menu"""
    global stop_dumping, dumped_users, dump_counter, total_collected, rate_limit_hits
    
    while True:
        os.system('clear') if os.name == 'posix' else os.system('cls')
        
        print(f"""
{CYAN}╔══════════════════════════════════════════════════════════╗
║           MEGA DUMPER v6.0 - 100K+ COLLECTOR            ║
║                                                          ║
║    {BOLD}🚀 COLLECT 1 LAKH+ INSTAGRAM USERS{RESET}{CYAN}            ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝{RESET}

{YELLOW}📊 STATISTICS:{RESET}
  Total Users: {GREEN}{len(dumped_users):,}{RESET} / {CYAN}{CONFIG['target_collection']:,}{RESET}
  Progress: {GREEN}{(len(dumped_users)/CONFIG['target_collection']*100):.1f}%{RESET}
  Dump Counter: {GREEN}{dump_counter:,}{RESET}
  Rate Limit Hits: {GREEN}{rate_limit_hits}{RESET}
  
{RED}[1] {CYAN}MEGA DUMP Followers (100K)
{RED}[2] {CYAN}MEGA DUMP Following (100K)
{RED}[3] {CYAN}MEGA CHAIN DUMP - Auto Expand
{RED}[4] {CYAN}Load & Dump from File
{RED}[5] {CYAN}View Collected Data
{RED}[6] {CYAN}Save & Export Data
{RED}[7] {CYAN}Clear Data
{RED}[8] {CYAN}Change Target (Default: 100K)
{RED}[9] {CYAN}Settings
{RED}[0] {RED}Exit
""")
        
        choice = input(f"{CYAN}Select option: {RESET}").strip()
        
        if choice in ['1', '01']:
            usernames = input(f"{CYAN}Enter username(s) comma separated: {RESET}").strip()
            if usernames:
                user_list = [u.strip() for u in usernames.split(',') if u.strip()]
                if user_list:
                    stop_dumping = False
                    dumper = MegaDumper()
                    dumper.start_workers(user_list, 'followers', CONFIG['max_workers'])
                    input(f"\n{GREEN}Press Enter to continue...{RESET}")
                    
        elif choice in ['2', '02']:
            usernames = input(f"{CYAN}Enter username(s) comma separated: {RESET}").strip()
            if usernames:
                user_list = [u.strip() for u in usernames.split(',') if u.strip()]
                if user_list:
                    stop_dumping = False
                    dumper = MegaDumper()
                    dumper.start_workers(user_list, 'following', CONFIG['max_workers'])
                    input(f"\n{GREEN}Press Enter to continue...{RESET}")
                    
        elif choice in ['3', '03']:
            usernames = input(f"{CYAN}Enter starting username(s): {RESET}").strip()
            if usernames:
                user_list = [u.strip() for u in usernames.split(',') if u.strip()]
                mode = input(f"{CYAN}Mode (followers/following): {RESET}").strip().lower() or 'followers'
                depth = int(input(f"{CYAN}Chain depth (1-5): {RESET}").strip() or '3')
                depth = max(1, min(5, depth))
                stop_dumping = False
                mega_chain_dump(user_list, mode, depth)
                input(f"\n{GREEN}Press Enter to continue...{RESET}")
                
        elif choice in ['4', '04']:
            filename = input(f"{CYAN}Enter filename: {RESET}").strip()
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    usernames = [line.strip() for line in f if line.strip()]
                print(f"{GREEN}[✓] Loaded {len(usernames)} usernames{RESET}")
                mode = input(f"{CYAN}Mode (followers/following): {RESET}").strip().lower() or 'followers'
                stop_dumping = False
                dumper = MegaDumper()
                dumper.start_workers(usernames, mode, CONFIG['max_workers'])
                input(f"\n{GREEN}Press Enter to continue...{RESET}")
            else:
                print(f"{RED}[✗] File not found!{RESET}")
                time.sleep(2)
                
        elif choice in ['5', '05']:
            view_mega_dump()
            input(f"\n{GREEN}Press Enter to continue...{RESET}")
            
        elif choice in ['6', '06']:
            save_mega_dump()
            save_progress()
            print(f"{GREEN}[✓] Data saved!{RESET}")
            time.sleep(1)
            
        elif choice in ['7', '07']:
            confirm = input(f"{RED}Clear all {len(dumped_users):,} users? (y/n): {RESET}").strip().lower()
            if confirm == 'y':
                dumped_users.clear()
                processed_users.clear()
                dump_counter = 0
                total_collected = 0
                rate_limit_hits = 0
                print(f"{GREEN}[✓] Data cleared!{RESET}")
            time.sleep(1)
            
        elif choice in ['8', '08']:
            try:
                target = int(input(f"{CYAN}New target (10,000 - 1,000,000): {RESET}").strip())
                CONFIG['target_collection'] = max(10000, min(1000000, target))
                print(f"{GREEN}[✓] Target set to {CONFIG['target_collection']:,}{RESET}")
            except:
                print(f"{RED}[✗] Invalid input{RESET}")
            time.sleep(1)
            
        elif choice in ['9', '09']:
            settings_menu()
            
        elif choice in ['0', '00']:
            save_mega_dump()
            save_progress()
            print(f"{GREEN}Goodbye! Total: {len(dumped_users):,} users{RESET}")
            sys.exit(0)
            
        else:
            print(f"{RED}Invalid option!{RESET}")
            time.sleep(1)

def settings_menu():
    """Settings configuration"""
    global CONFIG
    
    os.system('clear') if os.name == 'posix' else os.system('cls')
    
    print(f"""
{CYAN}╔═══════════════════════════════════════════╗
║              SETTINGS                       ║
╚═══════════════════════════════════════════╝{RESET}

Current Settings:
  Max Workers: {GREEN}{CONFIG['max_workers']}{RESET}
  Batch Size: {GREEN}{CONFIG['batch_size']}{RESET}
  Delay: {GREEN}{CONFIG['delay_between_requests']}s{RESET}
  Target Collection: {GREEN}{CONFIG['target_collection']:,}{RESET}
  Auto-Save Interval: {GREEN}{CONFIG['auto_save_interval']:,}{RESET}
  Max Depth: {GREEN}{CONFIG['max_depth']}{RESET}
  
{RED}[1] {CYAN}Change Max Workers (1-20)
{RED}[2] {CYAN}Change Batch Size (10-200)
{RED}[3] {CYAN}Change Delay (0.1-5.0)
{RED}[4] {CYAN}Change Auto-Save Interval
{RED}[5] {CYAN}Reset Settings
{RED}[0] {CYAN}Back
""")
    
    choice = input(f"{CYAN}Select option: {RESET}").strip()
    
    if choice == '1':
        try:
            value = int(input(f"{CYAN}Max Workers (1-20): {RESET}"))
            CONFIG['max_workers'] = max(1, min(20, value))
            print(f"{GREEN}[✓] Updated!{RESET}")
        except:
            print(f"{RED}[✗] Invalid input{RESET}")
    elif choice == '2':
        try:
            value = int(input(f"{CYAN}Batch Size (10-200): {RESET}"))
            CONFIG['batch_size'] = max(10, min(200, value))
            print(f"{GREEN}[✓] Updated!{RESET}")
        except:
            print(f"{RED}[✗] Invalid input{RESET}")
    elif choice == '3':
        try:
            value = float(input(f"{CYAN}Delay (0.1-5.0): {RESET}"))
            CONFIG['delay_between_requests'] = max(0.1, min(5.0, value))
            print(f"{GREEN}[✓] Updated!{RESET}")
        except:
            print(f"{RED}[✗] Invalid input{RESET}")
    elif choice == '4':
        try:
            value = int(input(f"{CYAN}Auto-Save Interval (100-10000): {RESET}"))
            CONFIG['auto_save_interval'] = max(100, min(10000, value))
            print(f"{GREEN}[✓] Updated!{RESET}")
        except:
            print(f"{RED}[✗] Invalid input{RESET}")
    elif choice == '5':
        CONFIG.update({
            'max_workers': 10,
            'batch_size': 100,
            'delay_between_requests': 0.3,
            'target_collection': 100000,
            'auto_save_interval': 1000,
            'max_depth': 5
        })
        print(f"{GREEN}[✓] Settings reset!{RESET}")
    elif choice == '0':
        return
        
    time.sleep(1)
    settings_menu()

# ============ MAIN ============
def main():
    """Main entry point"""
    print(f"""
{CYAN}╔══════════════════════════════════════════════════════════╗
║                                                          ║
║     🚀 MEGA DUMPER v6.0 - 100K+ COLLECTOR              ║
║                                                          ║
║     {BOLD}COLLECT 1 LAKH+ INSTAGRAM USERS{BOLD}                 ║
║                                                          ║
║     - Optimized for 100,000+ users                     ║
║     - Multi-threaded mega collection                   ║
║     - Auto-resume from progress                        ║
║     - Smart rate limiting management                   ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝{RESET}
    """)
    
    # Load cookies
    if not load_cookies():
        print(f"{RED}[✗] Authentication failed!{RESET}")
        sys.exit(1)
        
    # Load previous progress
    load_progress()
    load_mega_dump()
    
    print(f"\n{GREEN}[✓] Ready to collect {CONFIG['target_collection']:,} users{RESET}")
    print(f"{WHITE}   Current: {len(dumped_users):,} users{RESET}")
    print(f"{WHITE}   Remaining: {CONFIG['target_collection'] - len(dumped_users):,} users{RESET}\n")
    
    # Start menu
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{YELLOW}[!] Interrupted by user{RESET}")
        save_progress()
        save_mega_dump()
        print(f"{GREEN}[✓] Saved {len(dumped_users):,} users{RESET}")
        sys.exit(0)

if __name__ == "__main__":
    main()
