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
from rich.tree import Tree
import urllib.parse
from datetime import datetime

# Global variables
Uid, Uuid = [], []
bkas = []
Ok, Cp, Loop = 0, 0, 0
xx = 0
SistemLog = "api.instagram.com"
stop_collection = False
collection_thread = None
current_task = None
collection_running = False
page_loading = False
pagination_active = False

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
    'x-csrftoken': 'TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E',
    'sec-fetch-site': 'same-origin',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'
}

ua = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 instagram 360.0.0.33.104 (iPhone16,2; iOS 18.2; en_US; en; scale=3.00; 1170x2532; 510000000)'
}

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
        
        # Use a set to remove duplicates before saving
        unique_data = list(set(Uuid))
        if len(unique_data) < len(Uuid):
            print(f"{YELLOW}⚠ Found {len(Uuid) - len(unique_data)} duplicates, removing...{RESET}")
            Uuid[:] = unique_data
        
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
        
        # Remove duplicates
        unique_data = list(set(Uuid))
        if len(unique_data) < len(Uuid):
            Uuid[:] = unique_data
        
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

def collect_with_pagination(typess, user_id, cookie, after, max_pages=10):
    """Collect data with proper pagination handling - FIXED"""
    global Uuid, xx, page_loading, stop_collection, collection_running, pagination_active
    
    # Check if we should stop
    if stop_collection or not collection_running:
        return
    
    api = "https://www.instagram.com/graphql/query/"
    
    if typess:
        query_hash = "37479f2b8209594dde7facb0d904896a"
    else:
        query_hash = "58712303d941c6855d4e888c5f0cd22f"
    
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
        ptk = {
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 instagram 360.0.0.33.104",
            "accept": "application/json",
            "cookie": cookie,
            "x-ig-app-id": "1217981644879628"
        }
        
        session = requests.Session()
        session.max_redirects = 5
        
        req = session.get(api, params=params, headers=ptk, timeout=30)
        req.raise_for_status()
        req_json = req.json()
        
        # Check for errors
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
            print(f"\n{RED}This user has no visible data or is private")
            return
        
        edges = user_data[khm].get('edges', [])
        if not edges:
            print(f"\n{YELLOW}No data found for this user")
            return
        
        total_batch = len(edges)
        print(f"\r{GREEN}📥 Found {total_batch} items in this batch{' ' * 20}", end='', flush=True)
        
        # Process edges
        for xyz in edges:
            if stop_collection or not collection_running:
                break
            username = xyz['node'].get('username', '')
            full_name = xyz['node'].get('full_name', '')
            
            if username:
                xy = username + '|' + full_name
                if xy not in Uuid:
                    xx += 1
                    Uuid.append(xy)
                    print(f'\r{WHITE}📊 Collected: {RED}{len(Uuid)}{WHITE} users so far  ', end='', flush=True)
        
        # Check for next page
        page_info = user_data[khm].get('page_info', {})
        has_next = page_info.get('has_next_page', False)
        end_cursor = page_info.get('end_cursor', '')
        
        # Only load next page if there is one and we haven't exceeded max pages
        if has_next and end_cursor and not stop_collection and collection_running:
            print(f"\n{YELLOW}📄 Loading next page...{RESET}")
            page_loading = True
            pagination_active = True
            time.sleep(0.5)  # Small delay between pages
            
            # Recursive call for next page
            collect_with_pagination(typess, user_id, cookie, end_cursor, max_pages)
        else:
            if has_next and not end_cursor:
                print(f"\n{YELLOW}⚠️ No end cursor found, stopping pagination{RESET}")
            else:
                print(f"\n{GREEN}✅ Finished collecting all pages for this user{' ' * 20}{RESET}")
            page_loading = False
            pagination_active = False
                
    except requests.exceptions.Timeout:
        print(f"\n{RED}⏰ Timeout error - retrying...{RESET}")
        if not stop_collection and collection_running:
            time.sleep(2)
            collect_with_pagination(typess, user_id, cookie, after, max_pages)
    except requests.exceptions.TooManyRedirects:
        print(f"\n{RED}🔄 Too many redirects - check your cookies{RESET}")
        page_loading = False
        pagination_active = False
    except requests.exceptions.RequestException as e:
        print(f"\n{RED}🌐 Network error: {str(e)[:50]}{RESET}")
        page_loading = False
        pagination_active = False
    except json.JSONDecodeError as e:
        print(f"\n{RED}📄 Invalid JSON response: {str(e)[:50]}{RESET}")
        page_loading = False
        pagination_active = False
    except KeyError as e:
        print(f"\n{RED}🔑 Key error: {str(e)[:50]}{RESET}")
        page_loading = False
        pagination_active = False
    except Exception as e:
        print(f"\n{RED}❌ Unexpected error: {str(e)[:50]}{RESET}")
        page_loading = False
        pagination_active = False

def continuous_collection(cintil, user_ids, typess, delay=2):
    """UNLIMITED Continuous data collection without stopping"""
    global stop_collection, current_task, collection_running, Uuid, page_loading, pagination_active
    
    print(f"\n{CYAN}🚀 STARTING UNLIMITED CONTINUOUS COLLECTION{RESET}")
    print(f"{YELLOW}📌 Press Ctrl+C or type 'stop' to stop collection{RESET}")
    print(f"{YELLOW}⏱️  Delay: {delay} seconds between requests{RESET}")
    print(f"{GREEN}🔄 This will run FOREVER until you stop it!{RESET}\n")
    
    collected_count = 0
    error_count = 0
    current_task = "collection"
    collection_running = True
    total_loops = 0
    page_loading = False
    pagination_active = False
    
    # Create a separate thread for user input
    def check_stop():
        global stop_collection, collection_running
        while collection_running and not stop_collection:
            try:
                cmd = sys.stdin.readline().strip().lower()
                if cmd == 'stop':
                    stop_collection = True
                    collection_running = False
                    print(f"\n{YELLOW}🛑 Stop command received. Stopping collection...{RESET}")
                    break
            except:
                break
    
    # Start input thread
    input_thread = threading.Thread(target=check_stop, daemon=True)
    input_thread.start()
    
    try:
        while not stop_collection and collection_running:
            total_loops += 1
            print(f"\n{BLUE}{'='*60}{RESET}")
            print(f"{CYAN}🔄 COLLECTION LOOP #{total_loops}{RESET}")
            print(f"{WHITE}📊 Total users collected: {GREEN}{len(Uuid)}{RESET}")
            print(f"{BLUE}{'='*60}{RESET}")
            
            for idx, user_id in enumerate(user_ids, 1):
                if stop_collection or not collection_running:
                    break
                
                # Clear previous line
                sys.stdout.write('\033[K')
                
                try:
                    print(f"\n{WHITE}[{CYAN}{datetime.now().strftime('%H:%M:%S')}{WHITE}] {YELLOW}🎯 Processing #{idx}/{len(user_ids)}: {user_id}{RESET}")
                    
                    # Get initial data
                    previous_count = len(Uuid)
                    
                    # Reset pagination flags
                    page_loading = False
                    pagination_active = False
                    
                    # Collect data with pagination
                    collect_with_pagination(typess, user_id, cintil['cookie'], '')
                    
                    # Wait for pagination to complete if it's still active
                    wait_count = 0
                    while pagination_active and wait_count < 30:  # Max 30 seconds wait
                        if stop_collection or not collection_running:
                            break
                        time.sleep(0.5)
                        wait_count += 1
                    
                    # Check if new data was collected
                    new_data = len(Uuid) - previous_count
                    if new_data > 0:
                        collected_count += new_data
                        print(f"\r{GREEN}✅ Collected {new_data} new users (Total: {len(Uuid)}){' ' * 20}{RESET}")
                        error_count = 0
                    else:
                        print(f"\r{YELLOW}⚠️  No new data collected for this user{' ' * 20}{RESET}")
                        error_count += 1
                    
                    # Check for errors
                    if error_count > 3:
                        print(f"\r{RED}❌ Multiple errors occurred. Re-authenticating...{' ' * 20}{RESET}")
                        try:
                            cintil, _, _ = Aset_Ig()
                            error_count = 0
                        except:
                            pass
                    
                    # Countdown with animation
                    for i in range(delay, 0, -1):
                        if stop_collection or not collection_running:
                            break
                        print(f"\r{WHITE}⏳ Waiting {i}s until next request...{' ' * 30}", end='', flush=True)
                        time.sleep(1)
                    
                    # Clear the waiting message
                    print('\r' + ' ' * 60 + '\r', end='', flush=True)
                    
                except KeyboardInterrupt:
                    print(f"\n{YELLOW}🛑 Collection interrupted by user{RESET}")
                    stop_collection = True
                    collection_running = False
                    break
                except Exception as e:
                    print(f"\r{RED}❌ Error: {str(e)[:50]}{' ' * 20}{RESET}")
                    error_count += 1
                    print(f"\r{WHITE}⏳ Waiting {delay*2}s before retry...{' ' * 30}", end='', flush=True)
                    time.sleep(delay * 2)
                    print('\r' + ' ' * 60 + '\r', end='', flush=True)
            
            # Auto-save after each full cycle
            if len(Uuid) > 0 and collection_running:
                print(f"\n{YELLOW}💾 Auto-saving {len(Uuid)} users...{RESET}")
                save_to_sdcard()
                print(f"{GREEN}✅ Auto-save completed!{RESET}")
    
    except KeyboardInterrupt:
        print(f"\n{YELLOW}🛑 Collection interrupted by user{RESET}")
    
    finally:
        stop_collection = True
        collection_running = False
        current_task = None
        page_loading = False
        pagination_active = False
        
    print(f"\n{GREEN}{'='*60}{RESET}")
    print(f"{GREEN}🎉 COLLECTION COMPLETED!{RESET}")
    print(f"{WHITE}📊 Total users collected: {CYAN}{len(Uuid)}{RESET}")
    print(f"{WHITE}🔄 Total loops completed: {CYAN}{total_loops}{RESET}")
    print(f"{WHITE}📈 New users collected: {CYAN}{collected_count}{RESET}")
    print(f"{GREEN}{'='*60}{RESET}")

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

def dumps(cintil, typess):
    global xx, Uuid, stop_collection, collection_thread, collection_running, page_loading, pagination_active
    
    xx = 0
    stop_collection = False
    collection_running = False
    page_loading = False
    pagination_active = False
    
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
            exit(f'\n{WHITE}[{YELLOW}!{WHITE}] Csrftoken not available: {e}')
    
    print(f"\n{CYAN}🚀 UNLIMITED CONTINUOUS COLLECTION MODE{RESET}")
    print(f"{YELLOW}📌 This mode will run FOREVER collecting data{RESET}")
    print(f"{GREEN}🔄 The collection will cycle through users infinitely{RESET}")
    print(f"{YELLOW}⌨️  Type 'stop' at any time to stop collection{RESET}\n")
    
    print(f"{CYAN}Enter instagram usernames for continuous collection (use commas for multiple){RESET}")
    print(f"{WHITE}Example: user1,user2,user3{RESET}")
    users_input = input(f"{RED}[{WHITE}+{RED}] {BLUE}Usernames :{YELLOW} ").strip()
    
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
    
    print(f"\n{GREEN}Found {len(xyz)} valid user IDs{RESET}")
    
    # Ask for delay between requests
    print(f"\n{CYAN}Set delay between requests (in seconds, default: 2){RESET}")
    print(f"{WHITE}Lower delay = faster collection, but higher risk of rate limiting{RESET}")
    delay_input = input(f"{RED}[{WHITE}+{RED}] {BLUE}Delay (seconds) :{YELLOW} ").strip()
    try:
        delay = int(delay_input) if delay_input else 2
        if delay < 1:
            delay = 1
    except:
        delay = 2
    
    mode = 'followers' if typess else 'following'
    print(f"\n{YELLOW}🚀 Starting UNLIMITED continuous collection of {mode}...{RESET}")
    print(f"{GREEN}🔄 Collection will run until you type 'stop' or press Ctrl+C{RESET}")
    print(f"{CYAN}📊 Data will be auto-saved after each full cycle{RESET}\n")
    
    # Start continuous collection
    continuous_collection(cintil, xyz, typess, delay)
    
    # After collection stops, show results
    print(f"\n{GREEN}{'='*60}{RESET}")
    print(f"{GREEN}🎉 COLLECTION SUMMARY{RESET}")
    print(f"{WHITE}📊 Total users collected: {CYAN}{len(Uuid)}{RESET}")
    print(f"{WHITE}📂 Collection mode: {CYAN}{'Followers' if typess else 'Following'}{RESET}")
    print(f"{GREEN}{'='*60}{RESET}")
    
    if len(Uuid) > 0:
        print(f"\n{YELLOW}📋 Sample of collected data:{RESET}")
        for i, item in enumerate(Uuid[:5]):
            parts = item.split('|')
            print(f"  {i+1}. Username: {GREEN}{parts[0]}{RESET} | Name: {CYAN}{parts[1] if len(parts) > 1 else 'N/A'}{RESET}")
        if len(Uuid) > 5:
            print(f"  ... and {len(Uuid)-5} more")
    
    # Final auto-save
    print(f"\n{YELLOW}💾 Final auto-saving collected data...{RESET}")
    save_to_sdcard()
    
    print(f"\n{GREEN}✅ All data has been saved!{RESET}")
    time.sleep(2)
    MetodeType()

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
    global stop_collection, collection_running
    os.system('clear')
    aset, nama, fol = Aset_Ig()
    print(f"{BLUE}═" * 80)
    print(f"""{campur} 
 _______  ______ _______ _______ _     _      _____  ______
 |       |_____/ |_____| |       |____/         |   |  ____
 |_____  |    \\_ |     | |_____  |    \\_      __|__ |_____|
                                          
{CYAN}╭──────────────────────────────╮{CYAN}╭──────────────────────────────╮
{CYAN}│ {CYAN}Author : {GREEN}sumon {CYAN}                 │{CYAN}│ {WHITE}Version : {GREEN}2.0 {CYAN}             │
{CYAN}│ {WHITE}Status : {GREEN}Premium{CYAN}               │{CYAN}│ {WHITE}UNLIMITED Collection: {GREEN}ON{CYAN} │
{CYAN}╰──────────────────────────────╯{CYAN}╰──────────────────────────────╯""")
    print(f"{GREEN}{WHITE}Username :{GREEN} {nama[:8]}\n{WHITE}Followers : {GREEN}{fol}")
    
    print(f"\n{RED}[ {YELLOW}Main Menu {RED}]\n")
    print(f"{RED}[{WHITE}01{RED}] {CYAN} 🚀 UNLIMITED Collection (Followers)")
    print(f"{RED}[{WHITE}02{RED}] {CYAN} 🚀 UNLIMITED Collection (Following)")
    print(f"{RED}[{WHITE}03{RED}] {CYAN} 📂 Load from file")
    print(f"{RED}[{WHITE}04{RED}] {CYAN} 💾 Manage saved data")
    print(f"{RED}[{WHITE}00{RED}] {RED} 🔄 Delete/Change Cookies")
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
    elif x in ['00', '0']:
        if os.path.exists('data/cookie.txt'):
            os.remove('data/cookie.txt')
        prints(f"{GREEN}Successfully deleted cookies")
        exit()
    else:
        print(f"{RED}Invalid option!")
        time.sleep(1)
        Menu()

# Main execution
if __name__ == "__main__":
    # Create data directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')
    
    try:
        Menu()
    except KeyboardInterrupt:
        stop_collection = True
        collection_running = False
        print(f"\n\n{YELLOW}Stopping collection...{RESET}")
        time.sleep(1)
        print(f"{GREEN}Exiting...{RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{RED}An error occurred: {e}{RESET}")
        sys.exit(1)
