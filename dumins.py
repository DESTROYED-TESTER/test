#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

# ============ SAVE FUNCTIONS ============
def save_to_sdcard():
    """Save collected data to /sdcard/dump.txt with username|fullname format"""
    try:
        # Check if we have data to save
        if not Uuid:
            print(f"{RED}✗ No data to save!{RESET}")
            return False
        
        # Ensure /sdcard directory exists (for Termux)
        if not os.path.exists('/sdcard'):
            print(f"{YELLOW}⚠ /sdcard directory not found. Creating...{RESET}")
            try:
                os.makedirs('/sdcard', exist_ok=True)
            except:
                pass
        
        # Write data to file
        with open('/sdcard/dump.txt', 'w', encoding='utf-8') as f:
            for item in Uuid:
                f.write(item + '\n')
        
        print(f"\n{GREEN}✓ Successfully saved {len(Uuid)} users to /sdcard/dump.txt{RESET}")
        print(f"{WHITE}  Format: username|full_name{RESET}")
        
        # Show sample of saved data
        print(f"\n{YELLOW}Sample of saved data:{RESET}")
        for i, item in enumerate(Uuid[:3]):
            parts = item.split('|')
            print(f"  {i+1}. Username: {GREEN}{parts[0]}{RESET} | Name: {CYAN}{parts[1] if len(parts) > 1 else 'N/A'}{RESET}")
        if len(Uuid) > 3:
            print(f"  ... and {len(Uuid)-3} more")
        
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
        
        # Ensure data directory exists
        if not os.path.exists('data'):
            os.makedirs('data')
        
        # Write data to file
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
{CYAN}│ {CYAN}Author : {GREEN}sumon {CYAN}│{CYAN}  │ {WHITE}Version : {GREEN}2.0 {CYAN}│{CYAN}│ {WHITE}Status : {GREEN}Premium{CYAN}    │
{CYAN}╰──────────────────────╯{CYAN}╰───────────────╯{CYAN}╰─────────────────────────╯""")
    print(f"{GREEN}{WHITE}Username :{GREEN} {nama[:8]}\n{WHITE}Followers : {GREEN}{fol}")
    
    print(f"\n{RED}[ {YELLOW}Main Menu {RED}]\n\n{RED}[{WHITE}01{RED}] {CYAN} Dump followers\n{RED}[{WHITE}02{RED}] {CYAN} Dump following\n{RED}[{WHITE}03{RED}] {CYAN} Load from file\n{RED}[{WHITE}04{RED}] {CYAN} Manage saved data\n{RED}[{WHITE}00{RED}] {RED} Delete/Change Cookies")
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
            memek = requests.get('https://wwwww.instagram.com/data/shared_data/', cookies=cintil, timeout=10)
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
        print(f"{GREEN}Collected {len(Uuid)} users successfully!{RESET}")
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
    
    api = "https://wwwww.instagram.com/graphql/query/"
    
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
    # Create data directory if it doesn't exist
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
