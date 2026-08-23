#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instagram User ID Fetcher & Follower/Following Dumper
Fixed version with proper error handling
"""

import requests
import json
import re
import time
import os
import sys

# Color codes
RED = "\033[1;91m"
GREEN = "\033[1;92m"
YELLOW = "\033[1;93m"
BLUE = "\033[1;94m"
WHITE = "\033[1;97m"
CYAN = "\033[1;96m"
RESET = "\033[0m"

# Global variables
Uuid = []
xx = 0

def test_cookies(coki):
    """Test if cookies are still valid"""
    try:
        if isinstance(coki, dict) and 'cookie' in coki:
            cookie_str = coki['cookie']
        else:
            cookie_str = coki
            
        test_session = requests.Session()
        test_session.cookies.update({'cookie': cookie_str})
        response = test_session.get('https://www.instagram.com/', timeout=10)
        
        if 'login' not in response.text.lower():
            return True
        return False
    except:
        return False

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
    
    # Method 2: Try using the graphql API with proper query
    try:
        url = 'https://www.instagram.com/graphql/query/'
        params = {
            'query_hash': 'c9100bf9110dd6361671f113dd02e7d6',
            'variables': json.dumps({'username': username})
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15',
            'x-ig-app-id': '1217981644879628',
        }
        response = requests.get(url, params=params, headers=headers, cookies=cookies, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'user' in data['data']:
                user_id = data['data']['user'].get('id')
                if user_id:
                    return user_id
    except Exception as e:
        pass
    
    # Method 3: Try scraping the profile page
    try:
        session = requests.Session()
        session.max_redirects = 3
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15'
        }
        response = session.get(f'https://www.instagram.com/{username}/', headers=headers, cookies=cookies, timeout=10)
        
        if response.status_code == 200:
            # Try to find user_id in the page source
            patterns = [
                r'"user_id":"(\d+)"',
                r'"profilePage_(\d+)"',
                r'"id":"(\d+)","username":"' + username + '"',
                r'{"id":"(\d+)","username":"' + username + '"',
                r'"id":"(\d+)"[^}]*"username":"' + username + '"',
                r'"user_id":"(\d+)"',
                r'"userId":"(\d+)"',
            ]
            
            for pattern in patterns:
                match = re.search(pattern, response.text)
                if match:
                    return match.group(1)
                    
    except Exception as e:
        pass
    
    # Method 4: Try using the web profile info endpoint with different headers
    try:
        url = f'https://www.instagram.com/web/profile/info/{username}/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest'
        }
        response = requests.get(url, headers=headers, cookies=cookies, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if 'user' in data:
                user_id = data['user'].get('id')
                if user_id:
                    return user_id
    except Exception as e:
        pass
    
    return None

def dumps(cintil, typess):
    """Dump followers or following from Instagram accounts"""
    global xx, Uuid
    
    # Initialize Uuid if not exists
    if 'Uuid' not in globals():
        global Uuid
        Uuid = []
    
    xx = 0
    
    # Test cookies first
    if not test_cookies(cintil):
        print(f"{YELLOW}Warning: Your cookies may be invalid. Proceeding anyway...{RESET}")
        time.sleep(1)
    
    xyz = []
    
    # Ensure csrftoken is present
    if 'csrftoken' not in str(cintil):
        try:
            memek = requests.get('https://www.instagram.com/data/shared_data/', cookies=cintil, timeout=10)
            memek.raise_for_status()
            token = memek.json()['config']['csrf_token']
            if isinstance(cintil, dict):
                cintil['cookie'] += f';csrftoken={token};'
            else:
                cintil = f'{cintil};csrftoken={token};'
        except Exception as e:
            print(f"{RED}Error: Csrftoken not available, dump will not run: {e}{RESET}")
            return
    
    print(f"\n{CYAN}Enter Instagram usernames, use commas for mass dumping{RESET}")
    print(f"{YELLOW}Example: user1,user2,user3{RESET}")
    users_input = input(f"{WHITE}[{GREEN}?{WHITE}] Username: {GREEN}").strip()
    
    if not users_input:
        print(f"{RED}No username entered!{RESET}")
        return
    
    users = [u.strip() for u in users_input.split(',') if u.strip()]
    
    print(f"\n{YELLOW}Fetching user IDs...{RESET}")
    
    try:
        for y in users:
            print(f"{WHITE}Fetching user ID for: {CYAN}{y}{RESET}")
            
            user_id = get_user_id_methods(y, cintil)
            
            if user_id:
                if user_id not in xyz:
                    xyz.append(user_id)
                    print(f"{GREEN}✓ Found user ID: {user_id} for {y}{RESET}")
            else:
                print(f"{RED}✗ Could not find user ID for: {y}{RESET}")
                
            time.sleep(0.5)
                
    except Exception as e:
        print(f"{RED}Error getting user IDs: {e}{RESET}")
        return
    
    if not xyz:
        print(f"{RED}No valid user IDs found! Make sure the usernames are correct.{RESET}")
        time.sleep(2)
        return
    
    print(f"\n{GREEN}Found {len(xyz)} valid user IDs{RESET}")
    
    try:
        mode = 'followers' if typess else 'following'
        print(f"\n{YELLOW}Starting to dump {mode}...{RESET}")
        
        for kintil in xyz:
            print(f"\n{WHITE}Processing user ID: {CYAN}{kintil}{RESET}")
            if typess:
                Graphql(True, kintil, cintil, '')
            else:
                Graphql(False, kintil, cintil, '')
                
            time.sleep(1)
            
    except Exception as e:
        print(f"{RED}Error during dump: {e}{RESET}")
    
    print(f"\n{GREEN}Total users collected: {len(Uuid)}{RESET}")
    print("")
    
    if len(Uuid) > 0:
        print(f"{GREEN}Collected {len(Uuid)} users successfully!{RESET}")
        
        # Save results to file
        try:
            with open("dumped_users.txt", "w", encoding='utf-8') as f:
                for user in Uuid:
                    f.write(f"{user}\n")
            print(f"{GREEN}Results saved to: dumped_users.txt{RESET}")
        except:
            pass
            
        time.sleep(1)
    else:
        print(f"{RED}No users collected. Check if the target accounts are private or have no {mode}.{RESET}")
        time.sleep(2)

def Graphql(typess, userid, cokie, after):
    """GraphQL query to fetch followers/following"""
    global xx, Uuid
    
    # Initialize Uuid if not exists
    if 'Uuid' not in globals():
        global Uuid
        Uuid = []
    
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
        "first": 50,
        "after": after
    }
    
    params = {
        'query_hash': query_hash,
        'variables': json.dumps(variables)
    }
    
    try:
        # Prepare headers
        ptk = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 instagram 360.0.0.33.104",
            "Accept": "application/json",
            "x-ig-app-id": "1217981644879628"
        }
        
        # Handle cookies properly
        if isinstance(cokie, dict) and 'cookie' in cokie:
            cookies = {'cookie': cokie['cookie']}
        elif isinstance(cokie, dict):
            cookies = cokie
        else:
            cookies = {'cookie': cokie}
        
        session = requests.Session()
        session.max_redirects = 5
        
        req = session.get(api, params=params, headers=ptk, cookies=cookies, timeout=30)
        req.raise_for_status()
        req_json = req.json()
        
        # Check for errors
        if 'require_login' in req_json:
            print(f'\n{YELLOW}[!] Invalid Cookie - Need to login{RESET}')
            return
        
        if 'status' in req_json and req_json['status'] == 'fail':
            print(f'\n{RED}Request failed: {req_json.get("message", "Unknown error")}{RESET}')
            return
        
        # Determine the correct key based on typess
        khm = 'edge_followed_by' if typess else 'edge_follow'
        
        # Check if user exists in response
        if 'data' not in req_json or 'user' not in req_json['data'] or not req_json['data']['user']:
            print(f"\n{RED}User not found or private. Skipping...{RESET}")
            return
        
        user_data = req_json['data']['user']
        
        # Check if the user has the requested data
        if khm not in user_data:
            print(f"\n{RED}This user has no visible {khm.replace('edge_', '')} or is private{RESET}")
            return
        
        # Process the edges
        edges = user_data[khm].get('edges', [])
        if not edges:
            print(f"\n{YELLOW}No {khm.replace('edge_', '')} found for this user{RESET}")
            return
        
        print(f"\n{GREEN}Found {len(edges)} {khm.replace('edge_', '')} in this batch{RESET}")
        
        for xyz in edges:
            username = xyz['node'].get('username', '')
            full_name = xyz['node'].get('full_name', '')
            user_id = xyz['node'].get('id', '')
            
            if username:
                xy = f"{username}|{full_name}|{user_id}"
                if xy not in Uuid:
                    xx += 1
                    Uuid.append(xy)
                    print(f'\r{WHITE}Collecting {len(Uuid)} users                      ', end='', flush=True)
                    time.sleep(0.001)
        
        # Check for pagination
        page_info = user_data[khm].get('page_info', {})
        end = page_info.get('has_next_page', False)
        
        if end:
            after = page_info.get('end_cursor', '')
            if after:
                print(f"\n{YELLOW}Loading next page...{RESET}")
                time.sleep(0.5)
                Graphql(typess, userid, cokie, after)
                
    except requests.exceptions.Timeout:
        print(f"\n{RED}Timeout error while fetching followers{RESET}")
    except requests.exceptions.TooManyRedirects:
        print(f"\n{RED}Too many redirects - check your cookies{RESET}")
    except requests.exceptions.RequestException as e:
        print(f"\n{RED}Network error: {e}{RESET}")
    except json.JSONDecodeError as e:
        print(f"\n{RED}Invalid JSON response: {e}{RESET}")
    except KeyError as e:
        print(f"\n{RED}Key error: {e} - Check response structure{RESET}")
    except Exception as e:
        print(f"\n{RED}Unexpected error: {e}{RESET}")

def main():
    """Main function to run the dumper"""
    clear()
    
    print(f"{CYAN}{'='*56}{RESET}")
    print(f"{CYAN}     📱 INSTAGRAM FOLLOWER/FOLLOWING DUMPER 📱{RESET}")
    print(f"{CYAN}{'='*56}{RESET}")
    
    # Get cookie
    print(f"{YELLOW}Enter your Instagram cookie (should contain sessionid){RESET}")
    cookie_input = input(f"{WHITE}[{GREEN}?{WHITE}] Cookie: {GREEN}").strip()
    
    if not cookie_input:
        print(f"{RED}No cookie entered!{RESET}")
        return
    
    cookies = {'cookie': cookie_input}
    
    # Choose mode
    print(f"\n{WHITE}[{GREEN}1{WHITE}] Dump Followers{RESET}")
    print(f"{WHITE}[{GREEN}2{WHITE}] Dump Following{RESET}")
    choice = input(f"{WHITE}[{GREEN}?{WHITE}] Select: {GREEN}").strip()
    
    if choice == '1':
        dumps(cookies, True)  # True for followers
    elif choice == '2':
        dumps(cookies, False)  # False for following
    else:
        print(f"{RED}Invalid choice!{RESET}")

def clear():
    """Clear screen"""
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        print('\n' * 100)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{YELLOW}[!] Interrupted by user.{RESET}")
    except Exception as e:
        print(f"\n{RED}[!] Error: {e}{RESET}")
