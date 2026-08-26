#!/usr/bin/env python3
#================[ULTIMATE CHAIN DUMPER v5.0]================#
"""
COMPLETE UNLIMITED DUMPING SYSTEM
- Capture usernames from any source
- Use captured usernames for unlimited dumping
- Chain dumping: Followers -> Following -> More Followers
- Infinite recursive dumping
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
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import quote
from typing import Set, List, Dict, Optional
import signal

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
    'max_workers': 5,
    'batch_size': 50,
    'delay_between_requests': 0.5,
    'max_depth': 99,  # How deep to chain dump
    'max_users_per_run': 10000,  # Max users per dump run
    'auto_save_interval': 100,  # Save every N users
    'output_file': '/sdcard/dump.txt',
    'cookie_file': 'data/cookie.txt'
}

# ============ GLOBAL VARIABLES ============
dumped_users = set()
processed_users = set()
user_queue = queue.Queue()
dump_counter = 0
stop_dumping = False
current_depth = 0
cookies = {}
session = requests.Session()

# ============ SIGNAL HANDLING ============
def signal_handler(sig, frame):
    global stop_dumping
    print(f"\n{YELLOW}[!] Stopping dump gracefully...{RESET}")
    stop_dumping = True
    save_dump()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# ============ COOKIE MANAGEMENT ============
def load_cookies():
    """Load and validate cookies"""
    global cookies
    
    print(f"{CYAN}[*] Loading Instagram cookies...{RESET}")
    
    # Create data directory
    os.makedirs('data', exist_ok=True)
    os.makedirs('/sdcard', exist_ok=True)
    
    if os.path.exists(CONFIG['cookie_file']):
        with open(CONFIG['cookie_file'], 'r') as f:
            cookie_str = f.read().strip()
            cookies = {'cookie': cookie_str}
            
        if validate_cookies():
            print(f"{GREEN}[✓] Cookies loaded successfully!{RESET}")
            return True
            
    print(f"{YELLOW}[!] Please enter your Instagram cookie{RESET}")
    cookie_input = input(f"{CYAN}Cookie: {RESET}").strip()
    
    if not cookie_input:
        print(f"{RED}[✗] No cookie provided!{RESET}")
        return False
        
    cookies = {'cookie': cookie_input}
    
    # Save cookie
    with open(CONFIG['cookie_file'], 'w') as f:
        f.write(cookie_input)
        
    if validate_cookies():
        print(f"{GREEN}[✓] Cookie saved and validated!{RESET}")
        return True
    else:
        print(f"{RED}[✗] Invalid cookie!{RESET}")
        return False

def validate_cookies():
    """Validate cookie by fetching user info"""
    try:
        # Extract user ID from cookie
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
                print(f"  Followers: {CYAN}{user.get('follower_count', 0)}{RESET}")
                print(f"  Following: {CYAN}{user.get('following_count', 0)}{RESET}")
                return True
    except:
        pass
    return False

# ============ USER ID RESOLUTION ============
def get_user_id(username: str) -> Optional[str]:
    """Get user ID from username with multiple methods"""
    
    # Method 1: Official API
    try:
        url = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={username}'
        response = session.get(
            url,
            headers={
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2) AppleWebKit/605.1.15',
                'x-ig-app-id': '1217981644879628'
            },
            cookies=cookies,
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('user', {}).get('id')
    except:
        pass
    
    # Method 2: GraphQL
    try:
        url = 'https://www.instagram.com/graphql/query/'
        params = {
            'query_hash': 'c9100bf9110dd6361671f113dd02e7d6',
            'variables': json.dumps({'username': username})
        }
        response = session.get(url, params=params, cookies=cookies, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('user', {}).get('id')
    except:
        pass
    
    # Method 3: Scrape
    try:
        response = session.get(
            f'https://www.instagram.com/{username}/',
            cookies=cookies,
            timeout=10
        )
        
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

# ============ DUMPING ENGINE ============
def dump_relationship(user_id: str, username: str, mode: str = 'followers', depth: int = 0) -> List[str]:
    """
    Dump followers or following with unlimited pagination
    Returns list of captured usernames
    """
    global dump_counter, current_depth, stop_dumping
    
    if stop_dumping:
        return []
    
    if depth > CONFIG['max_depth']:
        print(f"{YELLOW}[!] Max depth reached for {username}{RESET}")
        return []
    
    if len(dumped_users) >= CONFIG['max_users_per_run']:
        print(f"{YELLOW}[!] Max users per run reached!{RESET}")
        stop_dumping = True
        return []
    
    # Check if already processed
    user_key = f"{username}_{mode}_{depth}"
    if user_key in processed_users:
        return []
    processed_users.add(user_key)
    
    print(f"\n{CYAN}[*] Dumping {mode} for @{username} (Depth: {depth}){RESET}")
    print(f"{WHITE}   Current total: {len(dumped_users)} users{RESET}")
    
    api_url = "https://www.instagram.com/graphql/query/"
    after = ""
    page_count = 0
    collected_users = []
    
    # Query hash
    query_hash = "37479f2b8209594dde7facb0d904896a" if mode == 'followers' else "58712303d941c6855d4e888c5f0cd22f"
    edge_key = 'edge_followed_by' if mode == 'followers' else 'edge_follow'
    
    while not stop_dumping and len(dumped_users) < CONFIG['max_users_per_run']:
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
                timeout=30
            )
            
            if response.status_code == 429:
                print(f"{YELLOW}[!] Rate limited! Waiting 10 seconds...{RESET}")
                time.sleep(10)
                continue
                
            if response.status_code != 200:
                print(f"{RED}[✗] Error {response.status_code}{RESET}")
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
                
            # Process each user
            for edge in edges:
                if stop_dumping or len(dumped_users) >= CONFIG['max_users_per_run']:
                    break
                    
                node = edge.get('node', {})
                username_found = node.get('username', '')
                full_name = node.get('full_name', '')
                user_id_found = node.get('id', '')
                
                if username_found:
                    user_entry = f"{username_found}|{full_name}|{user_id_found}"
                    
                    if username_found not in dumped_users:
                        dumped_users.add(username_found)
                        collected_users.append(user_entry)
                        dump_counter += 1
                        
                        # Display progress
                        print(f'\r{GREEN}[+] {dump_counter}: {username_found} ({full_name}){RESET}{" " * 30}', end='')
                        
                        # Auto-save
                        if dump_counter % CONFIG['auto_save_interval'] == 0:
                            save_dump()
                            
            # Check for more pages
            page_info = user_data[edge_key].get('page_info', {})
            has_next = page_info.get('has_next_page', False)
            after = page_info.get('end_cursor', '')
            
            page_count += 1
            
            if not has_next or not after:
                break
                
            # Add delay between pages
            time.sleep(CONFIG['delay_between_requests'])
            
        except Exception as e:
            print(f"\n{RED}[✗] Error: {e}{RESET}")
            time.sleep(2)
            continue
    
    print(f"\n{GREEN}[✓] Collected {len(collected_users)} {mode} from @{username}{RESET}")
    return collected_users

# ============ CHAIN DUMPING ============
def chain_dump(initial_usernames: List[str], modes: List[str] = ['followers', 'following'], 
               max_depth: int = 3) -> None:
    """
    Chain dump: Collect users, then dump their followers/following recursively
    """
    global current_depth, stop_dumping
    
    current_depth = 0
    all_usernames = set(initial_usernames)
    processed_targets = set()
    
    print(f"\n{YELLOW}{'='*60}{RESET}")
    print(f"{GREEN}[*] Starting CHAIN DUMPING{RESET}")
    print(f"{WHITE}   Initial usernames: {len(initial_usernames)}{RESET}")
    print(f"{WHITE}   Max depth: {max_depth}{RESET}")
    print(f"{WHITE}   Modes: {', '.join(modes)}{RESET}")
    print(f"{YELLOW}{'='*60}{RESET}\n")
    
    for depth in range(max_depth):
        if stop_dumping:
            break
            
        current_depth = depth
        print(f"\n{BOLD}📍 DEPTH {depth + 1}{RESET}")
        print(f"{WHITE}   Processing {len(all_usernames)} users{RESET}\n")
        
        # Get user IDs for all usernames
        user_ids = {}
        for username in list(all_usernames):
            if username in processed_targets or stop_dumping:
                continue
                
            if len(dumped_users) >= CONFIG['max_users_per_run']:
                print(f"{YELLOW}[!] Max users reached!{RESET}")
                stop_dumping = True
                break
                
            user_id = get_user_id(username)
            if user_id:
                user_ids[username] = user_id
            processed_targets.add(username)
            
        if not user_ids:
            print(f"{YELLOW}[!] No valid user IDs found at depth {depth}{RESET}")
            break
            
        # Dump for each user
        new_users = set()
        for username, user_id in user_ids.items():
            if stop_dumping:
                break
                
            if len(dumped_users) >= CONFIG['max_users_per_run']:
                break
                
            for mode in modes:
                if stop_dumping:
                    break
                    
                collected = dump_relationship(user_id, username, mode, depth)
                for user_entry in collected:
                    # Extract username from entry
                    parts = user_entry.split('|')
                    if parts:
                        new_users.add(parts[0])
                        
                # Save after each user
                save_dump()
                
        # Prepare for next depth
        if new_users:
            all_usernames.update(new_users)
            print(f"\n{GREEN}[✓] Added {len(new_users)} new users for next depth{RESET}")
        else:
            print(f"{YELLOW}[!] No new users found, stopping chain{RESET}")
            break
            
        time.sleep(2)  # Delay between depths
        
    print(f"\n{GREEN}{'='*60}{RESET}")
    print(f"{GREEN}[✓] Chain dump completed!{RESET}")
    print(f"{WHITE}   Total users collected: {len(dumped_users)}{RESET}")
    print(f"{WHITE}   Total entries: {dump_counter}{RESET}")
    print(f"{GREEN}{'='*60}{RESET}")
    save_dump()

# ============ SAVE FUNCTIONS ============
def save_dump():
    """Save collected data to file"""
    global dumped_users, dump_counter
    
    if not dumped_users:
        return
        
    try:
        # Save to main output file
        with open(CONFIG['output_file'], 'w', encoding='utf-8') as f:
            for username in dumped_users:
                f.write(username + '\n')
                
        # Save backup with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_file = f"data/dump_backup_{timestamp}.txt"
        os.makedirs('data', exist_ok=True)
        
        with open(backup_file, 'w', encoding='utf-8') as f:
            for username in dumped_users:
                f.write(username + '\n')
                
        # Save stats
        stats_file = 'data/dump_stats.json'
        with open(stats_file, 'w') as f:
            json.dump({
                'total_users': len(dumped_users),
                'last_update': datetime.now().isoformat(),
                'dump_counter': dump_counter,
                'timestamp': int(time.time())
            }, f, indent=2)
            
    except Exception as e:
        print(f"{RED}[✗] Error saving: {e}{RESET}")

def load_dump():
    """Load previous dump data"""
    global dumped_users
    
    if os.path.exists(CONFIG['output_file']):
        try:
            with open(CONFIG['output_file'], 'r', encoding='utf-8') as f:
                for line in f:
                    username = line.strip()
                    if username:
                        dumped_users.add(username)
            print(f"{GREEN}[✓] Loaded {len(dumped_users)} users from previous dump{RESET}")
            return True
        except:
            pass
    return False

def view_dump():
    """View collected data"""
    if not dumped_users:
        print(f"{RED}[✗] No data collected yet!{RESET}")
        return
        
    print(f"\n{GREEN}{'='*60}{RESET}")
    print(f"{GREEN}Total Users: {len(dumped_users)}{RESET}")
    print(f"{YELLOW}{'='*60}{RESET}")
    
    # Show all users
    for i, username in enumerate(sorted(dumped_users), 1):
        print(f"{WHITE}{i:4}. {CYAN}{username}{RESET}")
    
    print(f"{YELLOW}{'='*60}{RESET}")

# ============ MENU SYSTEM ============
def main_menu():
    """Main interactive menu"""
    global stop_dumping, dumped_users, dump_counter
    
    while True:
        os.system('clear') if os.name == 'posix' else os.system('cls')
        
        print(f"""
{CYAN}╔═══════════════════════════════════════════════════════╗
║      ULTIMATE CHAIN DUMPER v5.0                    ║
║      UNLIMITED • INFINITE • DEEP DUMP              ║
╚═══════════════════════════════════════════════════════╝{RESET}

{YELLOW}📊 STATISTICS:{RESET}
  Total Users: {GREEN}{len(dumped_users)}{RESET}
  Last Dump Count: {GREEN}{dump_counter}{RESET}
  
{RED}[1] {CYAN}Single User Dump
{RED}[2] {CYAN}Multiple Users Dump
{RED}[3] {CYAN}Chain Dump (Auto-Expand)
{RED}[4] {CYAN}Deep Chain Dump (Max Depth)
{RED}[5] {CYAN}Load From File & Dump
{RED}[6] {CYAN}View Collected Data
{RED}[7] {CYAN}Save Data Now
{RED}[8] {CYAN}Clear Data
{RED}[9] {CYAN}Change Settings
{RED}[0] {RED}Exit
""")
        
        choice = input(f"{CYAN}Select option: {RESET}").strip()
        
        if choice in ['1', '01']:
            username = input(f"{CYAN}Enter username: {RESET}").strip()
            if username:
                mode = input(f"{CYAN}Mode (followers/following/both): {RESET}").strip().lower()
                modes = ['followers', 'following'] if mode == 'both' else [mode]
                user_id = get_user_id(username)
                if user_id:
                    stop_dumping = False
                    for m in modes:
                        if not stop_dumping:
                            dump_relationship(user_id, username, m, 0)
                    save_dump()
                    input(f"\n{GREEN}Press Enter to continue...{RESET}")
                else:
                    print(f"{RED}[✗] User not found!{RESET}")
                    time.sleep(2)
                    
        elif choice in ['2', '02']:
            usernames_input = input(f"{CYAN}Enter usernames (comma separated): {RESET}").strip()
            if usernames_input:
                usernames = [u.strip() for u in usernames_input.split(',') if u.strip()]
                mode = input(f"{CYAN}Mode (followers/following/both): {RESET}").strip().lower()
                modes = ['followers', 'following'] if mode == 'both' else [mode]
                
                stop_dumping = False
                for username in usernames:
                    if stop_dumping:
                        break
                    user_id = get_user_id(username)
                    if user_id:
                        for m in modes:
                            if stop_dumping:
                                break
                            dump_relationship(user_id, username, m, 0)
                    else:
                        print(f"{RED}[✗] User not found: {username}{RESET}")
                    time.sleep(1)
                save_dump()
                input(f"\n{GREEN}Press Enter to continue...{RESET}")
                
        elif choice in ['3', '03']:
            usernames_input = input(f"{CYAN}Enter starting usernames (comma separated): {RESET}").strip()
            if usernames_input:
                usernames = [u.strip() for u in usernames_input.split(',') if u.strip()]
                depth = 2
                try:
                    depth = int(input(f"{CYAN}Chain depth (1-10): {RESET}").strip() or "2")
                    depth = max(1, min(10, depth))
                except:
                    depth = 2
                    
                stop_dumping = False
                chain_dump(usernames, ['followers'], depth)
                input(f"\n{GREEN}Press Enter to continue...{RESET}")
                
        elif choice in ['4', '04']:
            usernames_input = input(f"{CYAN}Enter starting usernames: {RESET}").strip()
            if usernames_input:
                usernames = [u.strip() for u in usernames_input.split(',') if u.strip()]
                stop_dumping = False
                chain_dump(usernames, ['followers', 'following'], CONFIG['max_depth'])
                input(f"\n{GREEN}Press Enter to continue...{RESET}")
                
        elif choice in ['5', '05']:
            filename = input(f"{CYAN}Enter filename: {RESET}").strip()
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    usernames = [line.strip() for line in f if line.strip()]
                print(f"{GREEN}[✓] Loaded {len(usernames)} usernames{RESET}")
                
                mode = input(f"{CYAN}Mode (followers/following/both): {RESET}").strip().lower()
                modes = ['followers', 'following'] if mode == 'both' else [mode]
                
                stop_dumping = False
                for username in usernames:
                    if stop_dumping:
                        break
                    user_id = get_user_id(username)
                    if user_id:
                        for m in modes:
                            if stop_dumping:
                                break
                            dump_relationship(user_id, username, m, 0)
                    time.sleep(0.5)
                save_dump()
                input(f"\n{GREEN}Press Enter to continue...{RESET}")
            else:
                print(f"{RED}[✗] File not found!{RESET}")
                time.sleep(2)
                
        elif choice in ['6', '06']:
            view_dump()
            input(f"\n{GREEN}Press Enter to continue...{RESET}")
            
        elif choice in ['7', '07']:
            save_dump()
            print(f"{GREEN}[✓] Data saved!{RESET}")
            time.sleep(1)
            
        elif choice in ['8', '08']:
            confirm = input(f"{RED}Clear all data? (y/n): {RESET}").strip().lower()
            if confirm == 'y':
                dumped_users.clear()
                dump_counter = 0
                print(f"{GREEN}[✓] Data cleared!{RESET}")
            time.sleep(1)
            
        elif choice in ['9', '09']:
            settings_menu()
            
        elif choice in ['0', '00']:
            save_dump()
            print(f"{GREEN}Goodbye!{RESET}")
            sys.exit(0)
            
        else:
            print(f"{RED}Invalid option!{RESET}")
            time.sleep(1)

def settings_menu():
    """Settings configuration"""
    global CONFIG
    
    os.system('clear') if os.name == 'posix' else os.system('cls')
    
    print(f"""
{CYAN}╔═══════════════════════════════════╗
║          SETTINGS                  ║
╚═══════════════════════════════════╝{RESET}

Current Settings:
  Max Workers: {GREEN}{CONFIG['max_workers']}{RESET}
  Batch Size: {GREEN}{CONFIG['batch_size']}{RESET}
  Delay: {GREEN}{CONFIG['delay_between_requests']}s{RESET}
  Max Depth: {GREEN}{CONFIG['max_depth']}{RESET}
  Max Users Per Run: {GREEN}{CONFIG['max_users_per_run']}{RESET}
  Auto-Save Interval: {GREEN}{CONFIG['auto_save_interval']}{RESET}
  
{RED}[1] {CYAN}Change Max Workers
{RED}[2] {CYAN}Change Batch Size  
{RED}[3] {CYAN}Change Delay
{RED}[4] {CYAN}Change Max Depth
{RED}[5] {CYAN}Change Max Users
{RED}[6] {CYAN}Change Auto-Save Interval
{RED}[0] {CYAN}Back to Main Menu
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
            value = int(input(f"{CYAN}Max Depth (1-50): {RESET}"))
            CONFIG['max_depth'] = max(1, min(50, value))
            print(f"{GREEN}[✓] Updated!{RESET}")
        except:
            print(f"{RED}[✗] Invalid input{RESET}")
            
    elif choice == '5':
        try:
            value = int(input(f"{CYAN}Max Users (100-1000000): {RESET}"))
            CONFIG['max_users_per_run'] = max(100, min(1000000, value))
            print(f"{GREEN}[✓] Updated!{RESET}")
        except:
            print(f"{RED}[✗] Invalid input{RESET}")
            
    elif choice == '6':
        try:
            value = int(input(f"{CYAN}Auto-Save Interval (10-1000): {RESET}"))
            CONFIG['auto_save_interval'] = max(10, min(1000, value))
            print(f"{GREEN}[✓] Updated!{RESET}")
        except:
            print(f"{RED}[✗] Invalid input{RESET}")
            
    elif choice == '0':
        return
        
    time.sleep(1)
    settings_menu()

# ============ MAIN ============
def main():
    """Main entry point"""
    print(f"""
{CYAN}╔═══════════════════════════════════════════════════════╗
║                                                       ║
║     ULTIMATE CHAIN DUMPER v5.0                       ║
║     {BOLD}DUMP • CAPTURE • REPEAT • UNLIMITED{BOLD}         ║
║                                                       ║
║     - Capture usernames from any source              ║
║     - Unlimited recursive dumping                    ║
║     - Chain dump followers & following              ║
║     - Auto-expand your user database                 ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝{RESET}
    """)
    
    # Load cookies
    if not load_cookies():
        print(f"{RED}[✗] Authentication failed! Exiting...{RESET}")
        sys.exit(1)
        
    # Load previous dump
    load_dump()
    
    # Start menu
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{YELLOW}[!] Interrupted by user{RESET}")
        save_dump()
        sys.exit(0)

if __name__ == "__main__":
    main()
